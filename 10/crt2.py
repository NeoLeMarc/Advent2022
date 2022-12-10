#!/usr/bin/env python3
import sys

ip = 0
cycles = []
x = 1 

def parseCommand(line):
    if line[0] == 'noop':
        cycles.append(0)
    elif line[0] == 'addx':
        cycles.append(0)
        cycles.append(int(line[1]))
    else:
        raise Exception('unknown command ' + str(line))

with open(sys.argv[1], 'r') as infile:
    for line in infile:
        line = line.strip()
        parseCommand(line.split())

print(cycles)

sum = 0
for i in range(0, len(cycles)):
    if i+1 in (20, 60, 100, 140, 180, 220):
        sum += (i+1)*x
        print("%i : %i : %i" % (i+1, x, (i+1)*x))

    x += cycles[i]
print(sum)

