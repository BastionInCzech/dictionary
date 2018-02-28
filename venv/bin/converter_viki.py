# !/usr/bin/env python
# -*- coding: utf-8 -*
def convert_viki(file):
    i = open(file + ".txt", "r")
    o = open(file + "_ascii.txt", "w+")
    line = i.readline()
    while line != "":
        line = line.split(".")
        line = [line[0], line[-1]]
        for ii in line:
            if ii[-1] == " ":
                line[line.index(ii)] = ii[:-1]
        for ii in line:
            if ii[0] == " ":
                line[line.index(ii)] = ii[1:]
        o.write(line[0].lower() + "|" + line[-1].lower())
        line = i.readline()
    i.close()
    o.close()
convert_viki("slovicka")
