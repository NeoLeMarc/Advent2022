#!/usr/bin/env python3
import sys, copy
lines = ""
ways = []
paths = []
minpath = 0

def walker(path, prefix, curletter, curpos, direction):
    path = copy.copy(path)
    #print("\nwalker(%s, %s, %s, %s, %s)" % (str(path), prefix, curletter, str(curpos), str(direction)))
    global ways
    global paths
    global minpath
    if minpath > 0 and len(path) + 1 >= minpath:
        print("Already found shorter path, exiting")
        return False
    newpos = (curpos[0] + direction[0], curpos[1] + direction[1])
 
    #print("Path: %s" % path)
    #print("Prefix: %s" % prefix)
    #print("Curletter: %s" % curletter)
    #print("Curpos: %s" % str(curpos))
    #print("Newpos: %s" % str(newpos))
    #print("Direction: %s" % str(direction))


    if newpos[0] < 0 or newpos[0] >= len(lines):
    #    print("Outside grid")
        return False #  Outside of grid
    elif newpos[1] < 0 or newpos[1]  >= len(lines[0]):
    #    print("Outside grid")
        return False # Outside of grid


    newletter = lines[newpos[0]][newpos[1]] 
    #print("Newletter: %s" % newletter)

    if newpos in path:
     #   print("Moving backwards")
        return False # Moving to already visited path

    path.append(newpos)

    if newletter == 'E':
        # possible way found
        prefix += newletter
        paths.append(path)
        ways.append(prefix)
        print("End found")
        if minpath == 0 or len(path) <= minpath:
            print("Minpath: %i" % minpath)
            minpath = len(path)
        return True 

    elif newletter == 'S' or newletter >= curletter and abs(ord(newletter) - ord(curletter)) <= 1:
    #    print(prefix)
    #    print("Found higher letter")
        prefix += newletter 
        curletter = newletter

        # Move in all possible directions
        if walker(path, prefix, curletter, newpos, (0, 1)) or \
                walker(path, prefix, curletter, newpos, (0, -1)) or \
                walker(path, prefix, curletter, newpos, (1, 0)) or \
                walker(path, prefix, curletter, newpos, (-1, 0)):
                    return True
        else:
            return False
    else:
        # Path ends here
     #   print("End of path")
        return False

with open(sys.argv[1], "r") as infile:
    lines = infile.read().splitlines()

print("Start")
walker([(0,0)], 'S', 'a', (0, 0), (1,0))
walker([(0,0)], 'S', 'a', (0, 0), (0,1))
print(ways)

for way in ways:
    print(len(way) + 1)

print(paths)
