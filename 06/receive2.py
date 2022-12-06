#!/usr/local/bin/python

with open('input.txt', 'r') as infile:
    line = infile.readline()


for i in range(0, len(line) + 1):
    print(i)
    print(line[i:i+14])
    if len(list(dict.fromkeys(list(line[i:i+14])))) == 14:
        print(i+1)
        break
