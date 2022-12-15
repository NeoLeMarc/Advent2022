#!/usr/bin/env
import sys

with open(sys.argv[1], 'r') as infile:
    lines = infile.read().splitlines()

positions = []
maxX = 0
minX = 999999999999

zoomlevel = int(sys.argv[2])
zMinX = int(int(sys.argv[3])/zoomlevel)
zMaxX = int(int(sys.argv[4])/zoomlevel)
zMinY = int(int(sys.argv[5])/zoomlevel)
zMaxY = int(int(sys.argv[6])/zoomlevel)

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

targetY = int(zMaxY)

print("X: %i - %i" % (zMinX, zMaxX))
print("Y: %i - %i" % (zMinY, zMaxY))
print("Target: %i" % targetY)

print("From %i to %i" % (int(zMinY), targetY))

for lookY in range(int(zMinY), targetY):
    freepositions = [0 for x in range(int(zMinX), int(zMaxX) + 1)]
    #print("minX: %i -  maxX: %i" % (minX, maxX))
    for pos in positions:
        removals = 0
        p, d0 = pos
        #print("Comparing to %s with d0 = %i" % (str(p[0]), d0))

        for x in range(int(zMinX), int(zMaxX) + 1):
            d = manhattanDistance(p[0], (x, lookY))
            if d <= d0 - 1:
                pass
                #removals += 1
                #print("Removing: %s (%i < %i)" % (str((x, lookY)), d, d0))
                #print(d0)
                #print((x, lookY))
            else:
                # is invisible
                freepositions[x - zMinX] += 1 
                if freepositions[x - zMinX] == len(positions): 
                    # it's invisible to all beacons
                    print("Hit at (%i, %i)" % ((x + zMinX) * zoomlevel, lookY * zoomlevel))
                    raise Exception("Found at lookY: %i" % (lookY * zoomlevel))
                pass
                #print("%i > %i" % (d, d0))

    #    if sum(freepositions) > 0:
    #        print("Found")
    #        print("Break")
    #        ## Find xPos:
    #        #print(freepositions)
    #        for x in range(0, len(freepositions)):
    #            if freepositions[x] > 0:
    #                print("Hit at (%i, %i)" % ((x + zMinX) * zoomlevel, lookY * zoomlevel))
    #        raise Exception("Found at lookY: %i" % (lookY * zoomlevel))
    #        import time 
    #        time.sleep(1)
    #        break
    
    numfree = len(freepositions) - sum(freepositions)
    if numfree > 0:
        print("Position %s: %i" % (str(pos), numfree))

    print("Done with %i of %i" % (lookY, targetY))
