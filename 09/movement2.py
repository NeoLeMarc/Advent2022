#!/usr/bin/env python
import sys

minX = 0
minY = 0
maxX = 0
maxY = 0

visitedHeadA = [[]]
visitedTailA = [[] for i in range(0, 9)]

headposA = [[0,0]]
tailposA = [[0,0] for i in range(0, 9)]

lastDirection = "" 


def draw(headposA, tailposA):
    for y in range(minY, maxY + 1):
        line = ""
        for x in range(minX, maxX + 1):
            tpos = (x, maxY- y)
            if tpos == tuple(headposA[0]):
                #print("found")
                line += "H" 
            elif list(tpos) in tailposA:
                line += str(tailposA.index(list(tpos)) + 1) 
            else:
                line += "."
        print(line)

def drawVisited(visited):
    for y in range(minY - 5, maxY + 5):
        line = ""
        for x in range(minX - 5, maxX + 5):
            tpos = (x, maxY-5-y)
            if tuple(tpos) in visited:
                line += "#" 
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
def moveTail(position, headpos, tailpos):
    if isTouching(headpos, tailpos):
        #print("Touching")
        pass
    elif oneStepDistance(headpos, tailpos):
        #moveTailOneStep(lastDirection)
        #print("One step distance - do nothing")
        pass
    else:
    #elif twoStepDistance(headpos, tailpos):
        #print("Two step distance")
        if sameColumnOrRow(headpos, tailpos):
            #print("Same column or row")
            #moveTailOneStep(position, lastDirection, tailpos)
            catchUp(position, headpos, tailpos)
        else:
            moveTailDiagonal(position, headpos, tailpos)
#    else:
#        raise Exception("Can not handle distance")

def moveTailDiagonal(position, headpos, tailpos):
    global lastDirection
    #print("move Diagonally")
    if headpos[0] > tailpos[0]:
        tailpos[0] += 1
    else:
        tailpos[0] -= 1

    if headpos[1] > tailpos[1]:
        tailpos[1] += 1
    else:
        tailpos[1] -= 1

    # Update headpos history
    lastDirection = 'X'
    visitedTailA[position].append(tuple(tailpos))

def moveTailUp(tailpos):
    global maxY
    tailpos[1] += 1 

    if tailpos[1] > maxY:
        maxY = tailpos[1]

def moveTailDown(tailpos):
    global minY
    tailpos[1] -= 1

    if tailpos[1] < minY:
        minY = tailpos[1]

def moveTailLeft(tailpos):
    global minX
    tailpos[0] -= 1

    if tailpos[0] < minX:
        minX = tailpos[0]

def moveTailRight(tailpos):
    global maxX
    tailpos[0] += 1

    if tailpos[0] > maxX:
        maxX = tailpos[0]


def moveTailOneStep(position, direction, tailpos):
    move = None
    if direction == 'L':
        move = moveTailLeft

    elif direction == 'R':
        move = moveTailRight

    elif direction == 'U':
        move = moveTailUp

    elif direction == 'D':
        move = moveTailDown

    elif direction == 'X':
        ## warning, last element moved diagonally
        raise Exception("Moved diagonally")

    else:
        raise Exception("Unknown direction")

    move(tailpos)
    visitedTailA[position].append(tuple(tailpos))
    lastDirection = direction

def catchUp(position, headpos, tailpos):
    # Need to catch up with head
    distanceX = headpos[0] - tailpos[0]
    distanceY = headpos[1] - tailpos[1]

    if distanceX == 2:
        ## head is in rightdirection
        moveTailRight(tailpos)
    elif distanceX == -2:
        moveTailLeft(tailpos)
    elif distanceY == 2:
        moveTailUp(tailpos)
    elif distanceY == -2:
        moveTailDown(tailpos)
    else:
        raise Exception("Can not catch up with head")

def moveUp(headpos):
    global maxY
    headpos[1] += 1 
    if headpos[1] > maxY:
        maxY = headpos[1]

def moveDown(headpos):
    global minY
    headpos[1] -= 1

    if headpos[1] < minY:
        minY = headpos[1]

def moveLeft(headpos):
    global minX
    headpos[0] -= 1

    if headpos[0] < minX:
        minX = headpos[0]

def moveRight(headpos):
    global maxX
    headpos[0] += 1

    if headpos[0] > maxX:
        maxX = headpos[0]


def handleMovement(direction, count, headposA, tailposA):
    move = None
    if direction == 'L':
        move = moveLeft

    elif direction == 'R':
        move = moveRight

    elif direction == 'U':
        move = moveUp

    elif direction == 'D':
        move = moveDown

    elif direction == 'X':
        ## warning, last element moved diagonally
        raise Exception("Moved diagonally")

    else:
        raise Exception("Unknown direction")

    for i in range(0, count):
        print(i)
        move(headposA[0])
        print("Headmove: ")
        draw(headposA, tailposA)

        print("First tail:")
        moveTail(0, headposA[0], tailposA[0])
        draw(headposA, tailposA)

        for j in range(1, 9):
            moveTail(j, tailposA[j-1], tailposA[j])

        print("Longtail: ")
        draw(headposA, tailposA)

        visitedHeadA[0].append(tuple(headposA[0]))
        #print("-----------")

with open(sys.argv[1], 'r') as infile:
    for line in infile.readlines():
        print(line)
        line = line.strip()
        direction, count = line.split(" ")
        lastDirection = direction
        handleMovement(direction, int(count), headposA, tailposA)
        print("Result: ")
        print(headposA[0])
        print("Min:( %i, %i) - Max: (%i, %i)" % (minX, minY, maxX, maxY))
        draw(headposA, tailposA)
        print("**********")
    #print(visitedHead)

#print(visitedTailA)
visited = list(dict.fromkeys(visitedTailA[-1]))
print(visited)
print(len(list(dict.fromkeys(visitedTailA[-1]))))
drawVisited(visited)
