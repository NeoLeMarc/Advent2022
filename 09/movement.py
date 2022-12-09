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

lastDirection = "" 


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

def isTouching(headpos, tailpos):
    if headpos == tailpos:
        return True
    elif headpos[0] == tailpos[0] and abs(headpos[1] - tailpos[1]) == 1 or \
         headpos[1] == tailpos[1] and abs(headpos[0] - tailpos[0]) == 1:
         return True
    else:
         return False

def oneStepDistance(headpos, tailpos):
    if abs(headpos[1] - tailpos[1]) == 1 and abs(headpos[0] - tailpos[0]) == 1: 
         return True
    else:
        return False
 
def twoStepDistance(headpos, tailpos):
    if abs(headpos[1] - tailpos[1]) <= 1 and abs(headpos[0] - tailpos[0]) == 2 or \
       abs(headpos[1] - tailpos[1]) == 2 and abs(headpos[0] - tailpos[0]) <= 1:
         return True
    else:
        print("Debug: %s - %s" % (abs(headpos[0] - tailpos[0]), abs(headpos[1] - tailpos[1])))
        return False

def sameColumnOrRow(headpos, tailpos):
    if headpos[0] == tailpos[0] or headpos[1] == tailpos[1]:
        return True
    else:
        return False

# If the head is ever two steps directly up, down, left or right from tail
# then tail must move on step in that direction
# Otherwise, if head and tail aren't touching and aren't in the same
# row or column, the tail always moves one step diagonally to keep up
def moveTail(headpos, tailpos):
    if isTouching(headpos, tailpos):
        print("Touching")
    elif oneStepDistance(headpos, tailpos):
        #moveTailOneStep(lastDirection)
        print("One step distance - do nothing")
    else:
    #elif twoStepDistance(headpos, tailpos):
        print("Two step distance")
        if sameColumnOrRow(headpos, tailpos):
            print("Same column or row")
            moveTailOneStep(lastDirection)
        else:
            moveTailDiagonal()
#    else:
#        raise Exception("Can not handle distance")

def moveTailDiagonal():
    print("move Diagonally")
    if headpos[0] > tailpos[0]:
        tailpos[0] += 1
    else:
        tailpos[0] -= 1

    if headpos[1] > tailpos[1]:
        tailpos[1] += 1
    else:
        tailpos[1] -= 1

    # Update headpos history
    visitedTail.append(tuple(tailpos))

def moveTailUp():
    global tailpos 
    tailpos[1] += 1 

def moveTailDown():
    global tailpos 
    tailpos[1] -= 1

def moveTailLeft():
    global tailpos 
    tailpos[0] -= 1

def moveTailRight():
    global tailpos 
    tailpos[0] += 1

def moveTailOneStep(direction):
    move = None
    if direction == 'L':
        move = moveTailLeft

    elif direction == 'R':
        move = moveTailRight

    elif direction == 'U':
        move = moveTailUp

    elif direction == 'D':
        move = moveTailDown

    else:
        raise Exception("Unknown direction")

    move()
    visitedTail.append(tuple(tailpos))

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
        draw(headpos, tailpos)
        moveTail(headpos, tailpos)
        visitedHead.append(tuple(headpos))

with open(sys.argv[1], 'r') as infile:
    for line in infile.readlines():
        print(line)
        line = line.strip()
        direction, count = line.split(" ")
        lastDirection = direction
        handleMovement(direction, int(count))
        draw(headpos, tailpos)
        print("**********")
    #print(visitedHead)

