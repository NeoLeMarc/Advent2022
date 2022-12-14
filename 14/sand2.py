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
            min_x = x - 40

        if x > max_x:
            max_x = x 

        if y < min_y:
            min_y = y 

        if y > max_y:
            max_y = y + 1400 
        pathElement = (x, y)
        path.append(pathElement)
    paths.append(path)

#print("%s %s / %s %s" % (min_x, max_x, min_y, max_y))

cave = []

# Iinitialize cave
def initializeCave(cave):
    for x in range(0, max_x + 2):
        cave.append([])
        for y in range(0, max_y + 10):
            cave[x].append('.')
    ## Add floor at bottom
    cave.append([])
    cave.append([])

    for y in range(0, max_y + 10):
        cave[max_x + 2].append('#')
     
initializeCave(cave)

## Add rock structure
for path in paths:
    prevpoint = None
    for point in path:
        #print(point)
        ## needs improvement
        if prevpoint:
            for x in range(min(prevpoint[0], point[0]), max(prevpoint[0], point[0]) + 1):
                for y in range(min(prevpoint[1], point[1]), max(prevpoint[1], point[1]) + 1):
                    #print(x, y)
                    cave[x][y] = '#'
        prevpoint = point
        #print("-------------")


## Add source of sand
sandSource = (0, 500)
cave[sandSource[0]][sandSource[1]] = '+'

#print("%i - %i" % (min_x, max_x))
#print("%i - %i" % (min_y, max_y))
def printCave(cave):
    for x in range(0, max_x + 5):
        line = "%i " % x
        for y in range(min_y - 5, max_y + 5):
            if x >= 0 and len(cave) > x:
                if y >= 0 and len(cave[x]) > y:
                    line += cave[x][y]
        print(line)

printCave(cave)

import copy
sandCave = copy.copy(cave)

sandPos = None
sandCornNr = 0 

# Sand moves down, than one step down and to the left and then one step down and to the right
def checkAbyss(sandCave):
    if not sandPos:
        return False
    elif sandPos[0] >= max_x or sandPos[1] >= max_y:
        import sys
        sandCave[sandPos[0]][sandPos[1]] = "X"
        printCave(sandCave)
        sys.stdout.flush()
        raise Exception("Hit abyss after adding %i corns of sand" % sandCornNr)
    else:
        return False

def sandIsResting(cave):
    global sandPos
    if sandPos == None:
        return True
    else:
        return False 

def moveDown(cave):
    global sandPos
    cave[sandPos[0]][sandPos[1]] = '.'
    cave[sandPos[0] + 1][sandPos[1]] = 'o'
    sandPos = (sandPos[0] + 1, sandPos[1])
 
def moveDownLeft(cave):
    global sandPos
    cave[sandPos[0]][sandPos[1]] = '.'
    cave[sandPos[0] + 1][sandPos[1] - 1] = 'o'
    sandPos = (sandPos[0] + 1, sandPos[1] - 1)

def moveDownRight(cave):
    global sandPos
    cave[sandPos[0]][sandPos[1]] = '.'
    cave[sandPos[0] + 1][sandPos[1] + 1] = 'o'
    sandPos = (sandPos[0] + 1, sandPos[1] + 1)

def moveSand(cave):
    global sandPos
    # Sand moves down:
    #print((sandPos[0], sandPos[1]))
    if cave[sandPos[0] + 1][sandPos[1]] not in ('#', 'o'):
        moveDown(cave)
    elif cave[sandPos[0] + 1][sandPos[1] - 1] not in ('#', 'o'):
        moveDownLeft(cave)
    elif cave[sandPos[0] + 1][sandPos[1] + 1] not in ('#', 'o'):
        moveDownRight(cave)
    else:
        # sand is resting
        sandPos = None

def addSand(cave):
    global sandPos
    global sandCornNr
    if cave[sandSource[0] + 1][sandSource[1]] != '.' and cave[sandSource[0] + 1][sandSource[1] - 1] != '.' and cave[sandSource[0] + 1][sandSource[1] + 1] != '.' :
        printCave(sandCave)
        sys.stdout.flush()
        raise Exception("Overflow after adding %i corns of sand" % sandCornNr)
    else:
        cave[sandSource[0]][sandSource[1]]  = 'o'
        sandPos = (sandSource[0], sandSource[1])
        sandCornNr += 1

def updateSand(cave):
    #print(sandPos)
    if sandIsResting(cave):
        addSand(cave)
    else:
        moveSand(cave)

drawCount = 0
import os
while True:
    #print("---------------")
    updateSand(sandCave)
    drawCount = (drawCount + 1) % 10000
    if drawCount == 1:
        os.system("clear")
        printCave(sandCave)
        import time
        #time.sleep(0.1)
    #checkAbyss(sandCave)
