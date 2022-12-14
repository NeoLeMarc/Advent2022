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
    spath = line.split(" -> ")
    path = []
    for p in spath:
        y, x = p.split(',')
        x = int(x)
        y = int(y)

        if x < min_x:
            min_x = x - 1

        if x > max_x:
            max_x = x + 1

        if y < min_y:
            min_y = y - 1

        if y > max_y:
            max_y = y + 1 
        pathElement = (x, y)
        path.append(pathElement)
    paths.append(path)

#print("%s %s / %s %s" % (min_x, max_x, min_y, max_y))

cave = []

# Iinitialize cave
def initializeCave(cave):
    for x in range(0, max_x + 2):
        cave.append([])
        for y in range(0, max_y + 2):
            cave[x].append('.')

initializeCave(cave)

for path in paths:
    prevpoint = None
    for point in path:
        print(point)
        ## needs improvement
        if prevpoint:
            for x in range(min(prevpoint[0], point[0]), max(prevpoint[0], point[0]) + 1):
                for y in range(min(prevpoint[1], point[1]), max(prevpoint[1], point[1]) + 1):
                    print(x, y)
                    cave[x][y] = '#'
        prevpoint = point
        print("-------------")

print("%i - %i" % (min_x, max_x))
print("%i - %i" % (min_y, max_y))
def printCave(cave):
    for x in range(min_x - 10, max_x + 10):
        line = ""
        for y in range(min_y - 20, max_y + 20):
            if x > 0 and len(cave) > x:
                if y > 0 and len(cave[x]) > y:
                    line += cave[x][y]
        print(line)

printCave(cave)
