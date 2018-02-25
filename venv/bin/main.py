# !/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class Pair(object):
    def __init__(self, cs, fr):
        self.cs = cs
        self.fr = fr
        self.value = [cs, fr]
        self.right = 0
        self.wrong = 0


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

    def remove_newlines(self):
        for i in self.initial_pairs:
            if "\n" in i.cs:
                i.cs = i.cs[:-1]
            if "\n" in i.fr:
                i.fr = i.fr[:-1]

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


    def shuffle(self):
        random.shuffle(self.initial_pairs)

    def save(self, filename):
        f = open(filename, "w+")
        cs = self.cs()
        fr = self.fr()
        for i in range(len(cs)):
            f.write(str(cs[i] + "|" + fr[i]) + "\n")

    def retrieve(self, filename):
        self.initial_pairs = []
        try:
            f = open(filename, "r")
        except FileNotFoundError:
            return
        pairs = []
        line = f.readline()
        while line != "":
            n = line.split("|")
            try:
                pairs.append(Pair(n[0], n[1]))
            except IndexError:
                return pairs
            line = f.readline()
        self.add(pairs)

def retrieve(lis):
    def without_newline(string):
        if "\n" in string:
            string = string[:-1]
        return string
    if isinstance(lis, list):
        ret = []
        for item in lis:
            f = open(item, "r")
            lines = []
            line = f.readline()
            while line != "":
                lines.append(without_newline(line))
                line = f.readline()
            ret.append(lines)
        return ret

    elif isinstance(lis, str):
        f = open(lis, "r")
        lines = []
        line = f.readline()
        while line != "":
            lines.append(without_newline(line))
            line = f.readline()
        return lines


def save_list(lis, filename):
    f = open(filename, "w+")
    for i in lis:
        f.write(str(i) + "\n")
    f.close()


def make_data(soubor):
    slovnik = {}
    file = open(soubor, "r")
    #main loop
    line = file.readline()
    while line != "":
        data = line.split("|")
        slovnik[data[0]] = data[1]
        line = file.readline()
    file.close()
    #removes newline in the end
    for i in slovnik.keys():
        slovnik[i] = slovnik[i][:-1]
    file.close()
    return slovnik


def dict_to_pair(dic):
    ret = []
    for key in dic.keys():
        ret.append(Pair(key, dic[key]))
    return ret


def str_to_list(string):
    string = string.strip("[")
    string = string.strip("]")
    string = string.split(", ")
    return string


def list_to_PairList(lis, data):
    temp = []
    for word in lis:
        temp.append(data.search(word))
    return PairList(initial_pairs=temp)


def without_newline(string):
    if "\n" in string:
        string = string[:-1]
    return string


##main asking loop
data = PairList(initial_pairs=dict_to_pair(make_data("slovicka_ascii.txt")))
word1 = PairList()
word2 = PairList()
word3 = PairList()
main = retrieve("main.txt")
word3.retrieve("word3.txt")
word1.retrieve("word1.txt")
word2.retrieve("word2.txt")

if not word1 == PairList():
    word1.add(data.initial_pairs)

if not main:
    random.shuffle(word1.initial_pairs)
    main = word1.cs()[0:25]

save_list(main, "main.txt")
word1.save("word1.txt")
word2.save("word2.txt")
word3.save("word3.txt")
