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
cache = {}

def stringify(seen, adjacent, timeLeft, steps, curpos, nextStep):
    return str(seen) + "-" + str(adjacent) + "-" + str(timeLeft) + "-" + str(steps) + "-" + str(curpos) + "-" + str(nextStep)

def calculateValue(seen, adjacent, timeLeft, steps, curpos, nextStep, trackback):
    global openValves
    global cache

    # dynamic programming
    if stringify(seen, adjacent, timeLeft, steps, curpos, nextStep) in cache:
        #print("Cache hit!")
        if steps <= 2:
            print(stringify(seen, adjacent, timeLeft, steps, curpos, nextStep))
            print(cache[stringify(seen, adjacent, timeLeft, steps, curpos, nextStep)])
        return cache[stringify(seen, adjacent, timeLeft, steps, curpos, nextStep)]
                                                                                                                    

    #print(adjacent)
    if timeLeft == 0:
        #print("No time left")
        # No time
        return []
    else:
        pass
#        print(timeLeft)

    ret = [] # valvename, value, timeLeft if going there
    stop = False
    value = 0
    for adj in adjacent:
        if nextStep == None:
            nextStepS = adj 
            print(adj)
        else:
            nextStepS = nextStep
 
        if adj not in seen:
            # open this valve only if it is not already open
            seen.append(adj)
            #print("Adding: %s" % adj)
            if adj not in openValves and timeLeft > 0: 
                value = valves[adj][0] * timeLeft # opening a valve takes one minute
            else:
                value = 0

        downstreamValues = calculateValue(copy.copy(seen), copy.copy(valves[adj][1]), timeLeft - 1, steps + 1, curpos, nextStepS, trackback + "->" + adj)
        ret.append((adj, value + sum([i[1] for i in downstreamValues]), (timeLeft - 1), nextStepS, trackback))
        #ret.extend(calculateValue(seen, copy.copy(valves[adj][1]), timeLeft - 1, steps + 1, curpos, nextStepS))

    cache[stringify(seen, adjacent, timeLeft, steps, curpos, nextStep)] = ret
    if steps <= 3:
        print("Trackback: %s - %s" % (trackback, str(ret)))
    return ret

totalValue = 0
currentIncrement = 0
openValves = []

while timeLeft > 1:
    # open valve 
    print("Current position: %s" % curpos)
    print("Value at current position: %i" % valves[curpos][0] )
    if curpos not in openValves and valves[curpos][0] > 0:
        currentIncrement += valves[curpos][0] 
        # opening valve
        openValves.append(curpos)

        print("** Minute: %i" % (30 - timeLeft + 1))
        print("opening valve %s" % (curpos))
        print("Currently open valves: %s" % str(openValves))
        print("TimeLeft: %i" % timeLeft)
        print("Current increment: %i" % currentIncrement)
        totalValue += currentIncrement
        print("Total value: %i" % totalValue)
        timeLeft -= 1
 
    mostValuableValue = -1 
    mostValuableKey = curpos 
    mostValuableTimeLeft = 0
    ret = calculateValue([curpos], copy.copy(valves[curpos][1]), timeLeft - 1, 1, curpos, None, curpos)
    print(ret)
    print("--------------------------")
    print("Currently open valves: %s" % str(openValves))
    print("Current increment: %i" % currentIncrement)
    print("Time left: %i" % timeLeft)

    # get most valuable block
    # pick any path at first to not get stuck
    ##mostValuableValue = ret[0][1]
    ##mostValuableKey = ret[0][0]
    ##mostValuableTimeLeft = ret[0][2]
    print(ret)
    for r in ret:
        if r[1] > mostValuableValue:
            mostValuableValue = r[1]
            mostValuableKey = r[0]
            mostValuableTimeLeft = r[2]
            nextStep = r[3]
            #if mostValuableKey in openValves:
            #    raise Exception("Seen valve twice: %s" % mostValuableKey)

    print(mostValuableKey)
    print(mostValuableValue)
    print(nextStep)
    print(timeLeft)

    # Increment for the time it takes to move to new position:
    # opening valve takes one minute
    # take the next step:
    print("** Minute: %i" % (30 - timeLeft + 1))

    if nextStep == curpos:
        print("Waling directly from %s -> %s" % (curpos, mostValuableKey))
        curpos = mostValuableKey
    else:
        print("Walking from %s -> %s over %s **" % (curpos, mostValuableKey, nextStep))
        curpos = nextStep
    print("Currently open valves: %s" % str(openValves))
    print("TimeLeft: %i" % timeLeft)
    print("Current increment: %i" % currentIncrement)
    totalValue += currentIncrement
    print("Total value: %i" % totalValue)
    timeLeft -= 1
    
    
    print("Time left: %i" % timeLeft)
    print("---------------------------")
print("No time left - exiting")
print(totalValue)
