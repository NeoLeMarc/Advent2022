#!/usr/bin/env python3

def isContained(a, b):
    if int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1]):
        return True
    else:
        return False

def doesOverlap(elf1, elf2):
    elf1A = elf1.split("-")
    elf2A = elf2.split("-")

    if isContained(elf1A, elf2A) or isContained(elf2A, elf1A):
        return True
    else:
        return False


overlaps = 0

with open("input.txt", "r") as infile:
    for line in infile.readlines():
        elf1, elf2 = line.split(",")
        print(line)
        if doesOverlap(elf1, elf2):
            overlaps += 1
            print("Overlaps")

print(overlaps)
