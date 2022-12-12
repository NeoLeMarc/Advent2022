#!/usr/bin/env python3
import sys, copy
sys.setrecursionlimit(5000)
lines = ""
ways = []
paths = []
minpath = 0
deadends = []
visited = []

def printMap():
    global lines

    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    ## Draw a map
    for i in range(0, len(lines)):
        out = ""
        for j in range(0, len(lines[0])):
            if (i, j) in visited:
                out += bcolors.OKGREEN + lines[i][j] + bcolors.ENDC
            else:
                out += bcolors.FAIL + lines[i][j] + bcolors.ENDC
        print(out) 

def printDebug(path, prefix, curletter, curpos, newpos, direction):
    print("Path: %s" % path)
    print("Prefix: %s" % prefix)
    print("Curletter: %s" % curletter)
    print("Curpos: %s" % str(curpos))
    print("Newpos: %s" % str(newpos))
    print("Direction: %s" % str(direction))


def walker(path, prefix, curletter, curpos, direction):
    global visited
    if curpos not in visited:
        visited.append(curpos)
    global deadends
    if curpos in deadends:
        print("Hit a deadend, exiting")
        print("\nwalker(%s, %s, %s, %s, %s)" % (str(path), prefix, curletter, str(curpos), str(direction)))
        return False
    path = copy.copy(path)
    global ways
    global paths
    global minpath
    if minpath > 0 and len(path) + 1 >= minpath:
        print("Already found shorter path, exiting")
        return False
    newpos = (curpos[0] + direction[0], curpos[1] + direction[1])
 

    if newpos[0] < 0 or newpos[0] >= len(lines):
        print("Outside grid")
        return False #  Outside of grid
    elif newpos[1] < 0 or newpos[1]  >= len(lines[0]):
        print("Outside grid")
        return False # Outside of grid


    newletter = lines[newpos[0]][newpos[1]] 
    #print("Newletter: %s" % newletter)

    if newpos in path:
        #print("Moving backwards")
        return False # Moving to already visited path

    path.append(newpos)

    if newletter == 'S':
        # possible way found
        prefix += newletter
        paths.append(path)
        ways.append(prefix)
        print("End found")
        if minpath == 0 or len(path) <= minpath:
            print("Minpath: %i" % minpath)
            minpath = len(path)
        return True 

    elif (curletter == 'E' and newletter == 'z') or newletter <= curletter and abs(ord(newletter) - ord(curletter)) <= 1 or newletter < curletter:
        print(prefix)
        #print("Found higher letter")
        prefix += newletter 
        curletter = newletter

        # Greedy optimization: if we find a lower letter, continue on that avenue
        newpos_x = max(min(newpos[0], len(lines) - 1), 0)
        newpos_y = max(min(newpos[0], len(lines[0]) - 1), 0)

        res = False
        if lines[max(newpos_x - 1, 0)][newpos_y] < curletter:
            print("Go down")
            res = walker(path, prefix, curletter, newpos, (-1, 0))
        elif lines[min(newpos_x + 1, len(lines) - 1)][newpos_y] < curletter:
            print("Go up")
            res = walker(path, prefix, curletter, newpos, (1, 0))
        elif lines[newpos_x][max(newpos_y - 1, 0)] < curletter:
            print("Go left")
            res = walker(path, prefix, curletter, newpos, (0, -1))
        elif lines[newpos_x][min(newpos_y + 1, len(lines[0]))] < curletter:
            print("Go right")
            res = walker(path, prefix, curletter, newpos, (0, 1))

        if res:
            # Shortcut found
            return True
        else:
            print("No shortcut")


        # Move in all possible directions
        if walker(path, prefix, curletter, newpos, (0, -1)) or \
                walker(path, prefix, curletter, newpos, (-1, 0)) or \
                walker(path, prefix, curletter, newpos, (0, 1)) or \
                walker(path, prefix, curletter, newpos, (1, 0)):
                    return True
        else:
            # Hit a deadend
            print("Found deadend")
            printDebug(path, prefix, curletter, curpos, newpos, direction)
            deadends.append(newpos)
            return False
    else:
        # Path ends here
        print("End of path")
        printDebug(path, prefix, curletter, curpos, newpos, direction)
        return False

with open(sys.argv[1], "r") as infile:
    lines = infile.read().splitlines()

print("Start")

startpos = (int(sys.argv[2]), int(sys.argv[3]))
print(startpos)
print(lines[startpos[0]][startpos[1]])
print("Minpath try: %i" % minpath)
newpos = startpos

walker([startpos], 'E', 'E', newpos, (1,0))
walker([startpos], 'E', 'E', newpos, (0,1))
walker([startpos], 'E', 'E', newpos, (-1,0))
walker([startpos], 'E', 'E', newpos, (0,-1))
print(ways)

for way in ways:
    print(len(way))

printMap()
print(paths)
pathlen = [len(i) for i in paths]
print(min(pathlen))
print(ways)
