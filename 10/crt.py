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

def isVisible(pixelpos, spritemiddle):
    if abs(pixelpos - spritemiddle) <= 1:
        return True
    else:
        return False

sum = 0
line = ""
for i in range(0, len(cycles)):
    pos = i%40
    if pos == 0:
        print(line)
        line = ""

    if isVisible(pos, x):
        line += "#"
    else:
        line += "-"

    x += cycles[i]
print(line)
