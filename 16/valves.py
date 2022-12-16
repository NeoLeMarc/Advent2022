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

def calculateValue(seen, adjacent, timeLeft):
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
            value = valves[adj][0] * timeLeft
            ret.append((adj, value, timeLeft))
            ret.extend(calculateValue(seen, valves[adj][1], timeLeft - 1))
    return ret

while timeLeft > 0:
    mostValuableValue = 0
    mostValuableKey = curpos 
    ret = calculateValue([curpos], valves[curpos][1], timeLeft)
    print(ret)

    # get most valuable block
    for r in ret:
        if r[1] > mostValuableValue:
            mostValuableValue = r[1]
            mostValuableKey = r[0]

    print(mostValuableKey)
    print(mostValuableValue)
    break
