#!/usr/bin/env
import sys

with open(sys.argv[1], 'r') as infile:
    lines = infile.read().splitlines()

positions = []
maxX = 0
minX = 999999999999

zoomlevel = int(sys.argv[2])
zMinX = int(sys.argv[3])
zMaxX = int(sys.argv[4])
zMinY = int(sys.argv[5])
zMaxY = int(sys.argv[6])

def manhattanDistance(a, b):
    d = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return d

for line in lines:
    l = line.split(' ')
    sensorpos_x = int(int(l[2][2:-1]) / zoomlevel)
    sensorpos_y = int(int(l[3][2:-1]) / zoomlevel)

    beaconpos_x = int(int(l[8][2:-1]) / zoomlevel)
    beaconpos_y = int(int(l[9][2:]) / zoomlevel)

    distance = manhattanDistance((sensorpos_x, sensorpos_y), (beaconpos_x, beaconpos_y)) 

    p = ((sensorpos_x, sensorpos_y), (beaconpos_x, beaconpos_y))
    positions.append((p, distance))

    if sensorpos_x > maxX:
        maxX = sensorpos_x

    if beaconpos_x + distance > maxX:
        maxX = beaconpos_x + distance

    if sensorpos_x - distance < minX - distance:
        minX = sensorpos_x - (distance - 1)

    if beaconpos_x < minX:
        minX = beaconpos_x

targetY = int(zMinY/zoomlevel)

for lookY in range(int(zMinY/zoomlevel), targetY):
    freepositions = [1 for x in range(minX, maxX + 1)]
    #print("minX: %i -  maxX: %i" % (minX, maxX))
    for pos in positions:
        p, d0 = pos
        #print("Comparing to %s with d0 = %i" % (str(p[0]), d0))

        for x in range(zMinX, zMaxX + 1):
            d = manhattanDistance(p[0], (x, lookY))
            if d <= d0:
                #print("Removing: %s (%i < %i)" % (str((x, lookY)), d, d0))
                #print((x, lookY))
                freepositions[x - minX] = 0

        if sum(freepositions) == 0:
            print("Found")
            print("Break")
            raise Exception("Found at Y: %i" % lookY * zoomlevel)
            break
    
    numfree = len(freepositions) - sum(freepositions)
    if numfree > 0:
        print(numfree)

    print("Done with %i of %i" % (lookY, targetY))
