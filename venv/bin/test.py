import random


class Pair(object):
    def __init__(self, cs, fr):
        self.cs = cs
        self.fr = fr
        self.value = [cs, fr]


class PairList(object):
    def __init__(self, initial_pairs=[]):
        self.initial_pairs = initial_pairs

    def add(self, addition):
        if isinstance(addition, list):
            for ii in addition:
                self.initial_pairs.append(ii)
        if isinstance(addition, Pair):
            self.initial_pairs.append(addition)

    def cs(self):
        ret = []
        n = 0
        for pair in self.initial_pairs:
            ret.append(pair.cs)
        return ret

    def fr(self):
        ret = []
        n = 0
        for pair in self.initial_pairs:
            ret.append(pair.fr)
        return ret

    def dic(self):
        ret = {}
        for pair in self.initial_pairs:
            ret[pair.cs] = pair.fr
        return ret

    def search(self, term):
        if term in self.cs():
            index = self.cs().index(term)
            return self.initial_pairs[index]
        elif term in self.fr():
            index = self.fr().index(term)
            return self.initial_pairs[index]
        else:
            print("Invalid Search")

    def remove(self, id):
        cs = self.cs()
        fr = self.fr()
        if isinstance(id, str):
            for item in range(len(cs)):
                if cs[item] == id:
                    self.initial_pairs.pop(item)
            for item in range(len(cs)):
                if fr[item] == id:
                    self.initial_pairs.pop(item)

        if isinstance(id, Pair):
            self.initial_pairs.pop(self.cs().index(Pair.cs))

        if isinstance(id, int):
            pass

    def shuffle(self):
        random.shuffle(self.initial_pairs)

    def save(self, filename):
        f = open(filename, "w+")
        cs = self.cs()
        fr = self.fr()
        for i in range(len(cs)):
            f.write(str(cs[i] + "|" + fr[i]))

    def retrieve(self, filename):
        f = open(filename, "r")
        pairs = []
        while line != "":
            n = f.readline().split("|")
            pairs.append(n[0], n[1])
        self.add(pairs)


# sth = Pair("a", "b")
# print(isinstance(sth, Pair))
# data = True
# if not data == False:
#     print("1")
# if not data:
#     print("2")
# if data:
#     print(3)

# x = [Pair("ahoj", "joha"), Pair("some", "emos"), Pair("tau", "uat")]
# test = PairList(initial_pairs=x)
# print(test.dic())
# test.remove("ahoj")
# test.
# print(test.dic())

# x = Pair("ahoj", "joha")
# x.cs = "cau"
# print(x.cs)

# x = "string"
# if "\n" in x:
#     x = x[:-1]
# print(x)
# class test(object):
#     def __init__(self, number):
#         self.number = number
#
# one = test()
print("3 + 5")
print(3 + 5)
print(eval("3 + 5"))
