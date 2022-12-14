#!/usr/bin/env python
import sys

lines = []

with open(sys.argv[1], 'r') as file:
    lines = file.read().splitlines()

min_x = 9999 
max_x = 0 
min_y = 9999
max_y = 0

paths = []
for line in lines:
    path = line.split(" -> ")
    paths.append(path)

    for p in path:
        x, y = p.split(',')
        x = int(x)
        y = int(y)

        if x < min_x:
            min_x = x

        if x > max_x:
            max_x = x

        if y < min_y:
            min_y = y

        if y > max_y:
            max_y = x

print("%s %s / %s %s" % (min_x, max_x, min_y, max_y))

cave = []

# Iinitialize cave
def printCave(cave):
    for x in range(0, max_x + 1):
        for y in range(0, max_y + 1):
            cave[x][y] = '.'

for path in paths:
    prevpoint = None
    for point in path:
        if prevpoint:
            for x in range(prevpoint[0], point[0] + 1):
                for y in range(prevpoint[1], point[1] + 1):
                    cave[x][y] = '#'
        prevpoint = path

def printCave(cave):
    for x in range(min_x, max_x + 1):
        line = ""
        for y in range(min_y, max_y + 1):
            line += cave[x][y]
        print(line)

printCave(cave)
