#!/usr/bin/env python
import sys
import copy

with open(sys.argv[1], 'r') as file:
    lines = file.read().splitlines()

timeLeft = 30
position = 'AA'
valves = {} # Position -> Flow rate, adjacent 

for line in lines:
    sline = line.split(' ')
    position = sline[1]
    rate = int(sline[4].split("=")[1][:-1])
    sadjacent = sline[9:]
    adjacent = []
    for adj in sadjacent:
        adjacent.append(adj.split(',')[0])
    #print(adjacent)
    valves[position] = (rate, adjacent)

#print(valves)
curpos = 'AA'

def calculateValue(seen, adjacent, timeLeft):
    global openValves
    #print(adjacent)
    if timeLeft == 0:
        print("No time left")
        # No time
        return []

    ret = [] # valvename, value, timeLeft if going there
    stop = False
    for adj in adjacent:
        if adj in seen:
            stop = True
            # Moving full circle
            print("Circle")
        else:
            seen.append(adj)
            print("Adding: %s" % adj)
            if adj not in openValves: 
                value = valves[adj][0] * timeLeft
            else:
                value = 0
            ret.append((adj, value, timeLeft))
            #ret.extend(calculateValue(seen, copy.copy(valves[adj][1]), timeLeft - 1))
    return ret

totalValue = 0
currentIncrement = 0
openValves = []

while timeLeft > 1:
    mostValuableValue = -1 
    mostValuableKey = curpos 
    mostValuableTimeLeft = 0
    ret = calculateValue([curpos], copy.copy(valves[curpos][1]), timeLeft - 1)
    print(ret)
    print("--------------------------")
    print("Currently open valves: %s" % str(openValves))
    print("Current increment: %i" % currentIncrement)
    print("Time left: %i" % timeLeft)

    # get most valuable block
    # pick any path at first to not get stuck
    mostValuableValue = ret[0][1]
    mostValuableKey = ret[0][0]
    mostValuableTimeLeft = ret[0][2]

    for r in ret:
        if r[1] > mostValuableValue:
            mostValuableValue = r[1]
            mostValuableKey = r[0]
            mostValuableTimeLeft = r[2]
            if mostValuableKey in openValves:
                raise Exception("Seen valve twice: %s" % mostValuableKey)

    print(mostValuableKey)
    print(mostValuableValue)
    print(timeLeft)

    # Go down the most valuable path
    currentIncrement += valves[mostValuableKey][0] 
    if mostValuableValue > 0:
        openValves.append(curpos)

    # Increment for the time it takes to move to new position:
    # opening valve takes one minute
    for i in range(timeLeft, mostValuableTimeLeft, -1):
        timeLeft -= 1
        print("** Walking from %s -> %s **" % (curpos, mostValuableKey))
        print("Currently open valves: %s" % str(openValves))
        print("TimeLeft: %i" % timeLeft)
        print("Current increment: %i" % currentIncrement)
        totalValue += currentIncrement
        print("Total value: %i" % totalValue)

    curpos = mostValuableKey
    # Just one more round
    timeLeft -= 1
    #timeLeft = mostValuableTimeLeft
    print("Time left: %i" % timeLeft)
    print("---------------------------")
print("No time left - exiting")
print(totalValue)
