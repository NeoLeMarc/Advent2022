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

for i in range(0, len(cycles)):
    x += cycles[i]
    print("%i : %i : %i" % (i+1, x, 20*x))
