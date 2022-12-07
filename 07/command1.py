#!/usr/bin/env python3
from pprint import pprint


dirstructure = {"/" : {'files' : {}, 'dirs' : {}} }
curdir = dirstructure["/"] 
path = [curdir]
dirsum = []
smallsum = 0

def handleCd(l):
    global curdir
    global path
    global dirstructure

    if l[2] == "/":
        curdir = dirstructure['/']

    if l[2] == "..":
        curdir = path.pop()

    else:
        directory = l[2]
        if directory not in curdir['dirs']:
            curdir['dirs'][directory] = {'files' : {}, 'dirs' : {}}
        curdir = curdir['dirs'][directory]
        path.append(curdir)

#    pprint(l)
#    pprint(path)
#    pprint(curdir)
#    pprint(dirstructure)
    print("-------")

def handleDir(l):
    print("handleDir()")
    # Found a directory
    global curdir
    global path
    global dirstructure

    directory = l[1]

    if directory not in curdir['dirs']:
        curdir['dirs'][directory] = {'files' : {}, 'dirs' : {}}
    
#    pprint(l)
#    pprint(curdir)
    print("xxxxxxxxxxx")

def handleFile(l):
    print("handleFile(%s)" % str(l))
    global curdir
    filename = l[1]
    size = l[0]

    curdir["files"][filename] = size
#    pprint(curdir)
    print("!!!!!!!!!!!")

def handleCommand(l):
    if l[1] == 'ls':
        print('LS')
    elif l[1] == 'cd':
        handleCd(l)
        #print('CD')
    elif l[0] == 'dir':
        handleDir(l)
    elif l[0].isnumeric():
        handleFile(l)
    else:
        print(l)
        raise Exception("Unknown command %s" % str(l))

def getDirSize(pathstring, p):
    global smallsum
    global dirsum
    print(p)
    size = 0
    for filename in p['files']:
        size += int(p['files'][filename])

    for dirname in p['dirs']:
        size += getDirSize(pathstring + dirname + "/", p['dirs'][dirname])

    dirsum.append((pathstring, size))

    if size <= 100000:
        smallsum += size
    return size

with open("input.txt", "r") as infile:
    for line in infile.readlines():
       print(line.strip())
       l = line.strip().split(" ")
       handleCommand(l)



pprint(dirstructure)
print(getDirSize("/", dirstructure['/']))
print(dirsum)
print("smallsum: %i" % smallsum)
