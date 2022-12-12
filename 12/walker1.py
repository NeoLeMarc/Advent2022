#!/usr/bin/env python3
import sys, copy
sys.setrecursionlimit(5000)
lines = ""
ways = []
paths = []
minpath = 1400 
deadends = []
visited = []
showcount = 0 

def printMap(path):
    print("Path End: %s" % str(path[-1]))
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
            if (i, j) == path[-1]:
                #out += bcolors.FAIL + lines[i][j] + bcolors.ENDC
                out += bcolors.BOLD + "!" + bcolors.ENDC
            elif (i, j) in path:
                out += bcolors.OKGREEN + lines[i][j] + bcolors.ENDC
            elif (i, j) in visited:
                out += bcolors.OKBLUE + lines[i][j] + bcolors.ENDC
            else:
                out += bcolors.FAIL + lines[i][j] + bcolors.ENDC
        print(out) 

def printDebug(path, prefix, curletter, curpos, newpos, direction):
    return
    print("Path: %s" % path)
    print("Prefix: %s" % prefix)
    print("Curletter: %s" % curletter)
    print("Curpos: %s" % str(curpos))
    print("Newpos: %s" % str(newpos))
    print("Direction: %s" % str(direction))


def walker(path, prefix, curletter, curpos, direction, greedy, foundpath = []):
    if len(foundpath) > 0 and curpos not in foundpath:
        # Heading down a wrong path
        return False

    global visited
    if curpos not in visited:
        visited.append(curpos)
    global deadends
    if curpos in deadends and greedy > -1:
        #print("Hit a deadend, exiting")
        #print("\nwalker(%s, %s, %s, %s, %s)" % (str(path), prefix, curletter, str(curpos), str(direction)))
        return False
    path = copy.copy(path)
    global ways
    global paths
    global minpath
    if minpath > 0 and len(path) + 1 >= minpath:
        #print("Already found shorter path, exiting")
        return False
    newpos = (curpos[0] + direction[0], curpos[1] + direction[1])
 

    if newpos[0] < 0 or newpos[0] >= len(lines):
        #print("Outside grid")
        return False #  Outside of grid
    elif newpos[1] < 0 or newpos[1]  >= len(lines[0]):
        #print("Outside grid")
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
        #print("End found")
        if minpath == 0 or len(path) <= minpath:
            foundpath = ways[-1]
            print("Minpath: %i" % minpath)
            minpath = len(path)
            print(prefix)
            print("Minpath: %i" % minpath)
            print("Prefix len %i" % len(path))
            print("Greedy %i" % greedy)
            print("Ways found: %i" % len(ways))
            if len(ways):
                print("Waylength: %i" % len(ways[-1]))
            print("Len foundpath: %i" % len(foundpath))
 
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
        printMap(path)
 
        return True 

    elif (curletter == 'E' and newletter == 'z') or abs(ord(newletter) - ord(curletter)) <= 1 or curletter != 'E' and (ord(newletter) > ord(curletter)):
        #print(prefix)
        #print("Found higher letter")
        prefix += newletter 
        curletter = newletter

        # Greedy optimization: if we find a lower letter, continue on that avenue
        newpos_x = max(min(newpos[0], len(lines) - 1), 0)
        newpos_y = max(min(newpos[0], len(lines[0]) - 1), 0)

        res = False
        if len(foundpath):
            if (newpos_x -1, newpos_y) in foundpath:
                res = walker(path, prefix, curletter, newpos, (-1, 0), greedy, foundpath)
            if (newpos_x , newpos_y -1) in foundpath:
                res = walker(path, prefix, curletter, newpos, (0, -1), greedy, foundpath)
            if (newpos_x + 1 , newpos_y) in foundpath:
                res = walker(path, prefix, curletter, newpos, (1, 0), greedy, foundpath)
            if (newpos_x , newpos_y + 1) in foundpath:
                res = walker(path, prefix, curletter, newpos, (0, 1), greedy, foundpath)



        if greedy > 0:
            if lines[max(newpos_x - 1, 0)][newpos_y] < curletter:
                res = walker(path, prefix, curletter, newpos, (-1, 0), greedy, foundpath)
            elif lines[min(newpos_x + 1, len(lines) - 1)][newpos_y] < curletter:
                res = walker(path, prefix, curletter, newpos, (1, 0), greedy, foundpath)
            elif lines[newpos_x][max(newpos_y - 1, 0)] < curletter:
                res = walker(path, prefix, curletter, newpos, (0, -1), greedy, foundpath)
            elif lines[newpos_x][min(newpos_y + 1, len(lines[0]))] < curletter:
                res = walker(path, prefix, curletter, newpos, (0, 1), greedy, foundpath)

        if res and greedy:
            # Shortcut found
            return True
        else:
            pass
            #print("No shortcut")


        # Move in all possible directions
        if walker(path, prefix, curletter, newpos, (0, -1), greedy, foundpath) or \
                walker(path, prefix, curletter, newpos, (-1, 0), greedy, foundpath) or \
                walker(path, prefix, curletter, newpos, (0, 1), greedy, foundpath) or \
                walker(path, prefix, curletter, newpos, (1, 0), greedy, foundpath):
                    return True
        else:
            # Hit a deadend
            #print("Found deadend")
            #printDebug(path, prefix, curletter, curpos, newpos, direction)
            deadends.append(newpos)
            return False
    else:
        # Path ends here
        #print("End of path")
        global showcount
        showcount += 1 
        showcount = showcount % 10000
        if showcount == 1:
            print("****************************")
            print(prefix)
            print("Minpath: %i" % minpath)
            print("Prefix len %i" % len(path))
            print("Greedy %i" % greedy)
            print("Ways found: %i" % len(ways))
            if len(ways):
                print("Waylength: %i" % len(ways[-1]))
            print("Len foundpath: %i" % len(foundpath))
            printMap(path)
        #printDebug(path, prefix, curletter, curpos, newpos, direction)
        return False

with open(sys.argv[1], "r") as infile:
    lines = infile.read().splitlines()

print("Start")

startpos = (int(sys.argv[2]), int(sys.argv[3]))
print(startpos)
print(lines[startpos[0]][startpos[1]])
print("Minpath try: %i" % minpath)
newpos = startpos

# Start greedy
walker([startpos], 'E', 'E', newpos, (0,1), 1)
#walker([startpos], 'E', 'E', newpos, (1,0), 1)
#walker([startpos], 'E', 'E', newpos, (-1,0), 1)
#walker([startpos], 'E', 'E', newpos, (0,-1), 1)
print(ways)

# Thorough
minpath = 1400 
for i in range(1400, 1):
    print("Presearch %i" % i)
    deadends = []
    foundpath = paths[-1]
    walker([startpos], 'E', 'E', newpos, (0,1), 0, foundpath)
    #walker([startpos], 'E', 'E', newpos, (1,0), 0, foundpath)
    #walker([startpos], 'E', 'E', newpos, (-1,0), 0, foundpath)
    #walker([startpos], 'E', 'E', newpos, (0,-1), 0, foundpath)
    print(ways)

    foundpath = paths[-1]
    if len(foundpath) < minpath:
        minpath = len(foundpath)
    else:
        minpath -= 1

    #walker([startpos], 'E', 'E', newpos, (0,1), -1, foundpath)
    #walker([startpos], 'E', 'E', newpos, (1,0), -1, foundpath)
    #walker([startpos], 'E', 'E', newpos, (-1,0), -1, foundpath)
    #walker([startpos], 'E', 'E', newpos, (0,-1), -1, foundpath)
    print(i)
    print(ways)
    print("----------------------------------------------------------")

print("Next phase")
foundpath = paths[-1]
minpath = len(foundpath) 
for i in range(min(minpath, 790), 40, -1):
    print("Presearch %i" % i)
    foundpath = paths[-1]
    walker([startpos], 'E', 'E', newpos, (0,1), 0, foundpath)
    #walker([startpos], 'E', 'E', newpos, (1,0), 0, foundpath)
    #walker([startpos], 'E', 'E', newpos, (-1,0), 0, foundpath)
    #walker([startpos], 'E', 'E', newpos, (0,-1), 0, foundpath)
    #print(ways)

    foundpath = paths[-1]
    if len(foundpath) < minpath:
        minpath = len(foundpath)
    else:
        minpath -= 1

import time
print("Waiting until starting thorough approach")
print(len(foundpath))

print("Now dijkstra")

print(paths)
pathlen = [len(i) for i in paths]
print(min(pathlen))
print(ways)
printMap(foundpath)
edges = {} 


def getEdge(node, distance, inpath, target):
    retedges = []
    if target in inpath:
        retedges.append((node, distance, target))
    return retedges

def getEdges(node, distance, inpath):
    x, y = node
    retedges = []

    for n in [(x -1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
        retedges.extend(getEdge(node, distance, inpath, n))

    return retedges

def searchpath(inpath):
    distance = 0

    for node in inpath:
        distance += 1
        for edge in getEdges(node, distance, inpath):
            target = edge[2]
            if target not in edges:
                edges[target] = []
            edges[target].append(edge)

searchpath(foundpath)

opath = []
print(edges)
found = False
print(sys.argv)
tpos = (int(sys.argv[4]), int(sys.argv[5]))
print("Tpos: %s" % str(tpos))
candidateedges = edges[tpos]
minl = 9999
seen = []
while not found:
    mine = None
    print(candidateedges)
    for candidate in candidateedges:
        print(candidate)
        if candidate[0] == startpos:
            print("Found!")
            found = True
            break
        elif candidate[1] < minl and candidate not in seen:
            print("Found candidate")
            mine = candidate
            seen.append(mine) 
            print(mine)
            minl = mine[1]
            opath.append(mine[0])
            print("---------")
    if mine == None:
        if not found:
            raise Exception("Dead End")
    else:
        candidateedges = edges[mine[0]]
    print(candidate)
print(opath)
printMap(opath)
print(len(opath))
sys.stdout.flush()
print("The End!")
