#!/usr/bin/env python3

def getPriority(i):
    p = ord(i.upper()) - ord('A') + 1
    if i.isupper():
        p += 26
    return p

def getCount(substr):
    ret = {}
    for c in substr:
        if c not in ret:
            ret[c] = 0
        ret[c] += 1
    return ret

def getCommon(a, b, z):
    for c in a:
        if c in b and c in z:
            return c

priosum = 0

with open('input.txt', 'r') as infile:
    while True:
        elf1 = infile.readline().strip()
        elf2 = infile.readline().strip()
        elf3 = infile.readline().strip()

        if not elf1:
            break

        countA = getCount(elf1) 
        countB = getCount(elf2)
        countC = getCount(elf3)

        print("%s : %s -%s - %s" % (elf1 + elf2 + elf3, str(countA), str(countB), str(countC)))
        print("Common: %s" % getCommon(countA, countB, countC))
        common = getCommon(countA, countB, countC)

        print("Priority: %i" % getPriority(common))
        
        priosum += getPriority(common)
        print(priosum)
        print("-------")

print("Sum: ")
print(priosum)
