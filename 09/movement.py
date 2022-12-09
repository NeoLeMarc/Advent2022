#!/usr/bin/env python
import sys

minX = 0
minY = 0
maxX = 0
maxY = 0

visitedHead = []
visitedTail = []

headpos = [0,0]
tailpos = [0,0]


def draw(headpos, tailpos):
    for y in range(minY, maxY + 1):
        line = ""
        for x in range(minX, maxX + 1):
            tpos = (x, y)
            if tpos == tuple(headpos):
                #print("found")
                line += "H" 
            elif tpos == tuple(tailpos):
                line += "T"
            else:
                line += "."
        print(line)

def moveUp():
    global maxY
    global headpos
    headpos[1] += 1 
    if headpos[1] > maxY:
        maxY = headpos[1]

def moveDown():
    global minY
    global headpos
    headpos[1] -= 1

    if headpos[1] < minY:
        minY = headpos[1]

def moveLeft():
    global minX
    global headpos
    headpos[0] -= 1

    if headpos[0] < minX:
        minX = headpos[0]

def moveRight():
    global maxX
    global headpos
    headpos[0] += 1

    if headpos[0] > maxX:
        maxX = headpos[0]


def handleMovement(direction, count):
    global visitedHead
    global headpos

    move = None
    if direction == 'L':
        move = moveLeft

    elif direction == 'R':
        move = moveRight

    elif direction == 'U':
        move = moveUp

    elif direction == 'D':
        move = moveDown

    else:
        raise Exception("Unknown direction")

    for i in range(0, count):
        move()
        visitedHead.append(tuple(headpos))

with open(sys.argv[1], 'r') as infile:
    for line in infile.readlines():
        print(line)
        line = line.strip()
        direction, count = line.split(" ")
        handleMovement(direction, int(count))
        draw(headpos, tailpos)
        print("**********")
    #print(visitedHead)

