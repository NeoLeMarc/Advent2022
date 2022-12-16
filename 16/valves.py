#!/usr/bin/env python
import sys

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

def calculateValue(seen, adjacent, timeLeft, openValves):
    print(adjacent)
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
            if adj not in openValves: 
                value = valves[adj][0] * timeLeft
                ret.append((adj, value, timeLeft))
                ret.extend(calculateValue(seen, valves[adj][1], timeLeft - 1, openValves))
    return ret

totalValue = 0
currentIncrement = 0
openValves = []

while timeLeft > 0:
    mostValuableValue = 0
    mostValuableKey = curpos 
    mostValuableTimeLeft = 0
    ret = calculateValue([curpos], valves[curpos][1], timeLeft - 1, openValves)
    print("--------------------------")
    print(ret)
    print("Currently open valves: %s" % str(openValves))
    print("Current increment: %i" % currentIncrement)
    print("Time left: %i" % timeLeft)

    # get most valuable block
    for r in ret:
        if r[1] > mostValuableValue:
            mostValuableValue = r[1]
            mostValuableKey = r[0]
            mostValuableTimeLeft = r[2]

    print(mostValuableKey)
    print(mostValuableValue)
    print(timeLeft)

    # Go down the most valuable path
    currentIncrement += valves[mostValuableKey][0] 
    curpos = mostValuableKey
    openValves.append(curpos)

    # Increment for the time it takes to move to new position:
    for i in range(timeLeft - 1, mostValuableTimeLeft, -1):
        totalValue += currentIncrement


    timeLeft = mostValuableTimeLeft
    totalValue += currentIncrement
print("No time left")
print(totalValue)
