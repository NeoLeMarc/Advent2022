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

def getCommon(a, b):
    for c in a:
        if c in b:
            return c

priosum = 0

with open('input.txt', 'r') as infile:
    for line in infile.readlines():
        line = line.strip()

        if len(line) % 2 != 0:
            print("Warning: uneven line detected")
            print(line)

        compartmentA = line[:int(len(line)/2)]
        compartmentB = line[int(len(line)/2):]

        countA = getCount(compartmentA) 
        countB = getCount(compartmentB)

        print("%s : %s -%s" % (line, str(countA), str(countB)))
        print("Common: %s" % getCommon(countA, countB))
        common = getCommon(countA, countB)

        print("Priority: %i" % getPriority(common))
        
        priosum += getPriority(common)
        print(priosum)
        print("-------")

print("Sum: ")
print(priosum)
