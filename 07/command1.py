#!/usr/bin/env python3
from pprint import pprint


dirstructure = {"/" : {'files' : {}, 'dirs' : {}, 'name' : '/'} }
curdir = dirstructure["/"] 
path = [curdir]
strpath = ['/']
dirsum = []
smallsum = 0
seendirs = []

def handleCd(l):
    global curdir
    global path
    global dirstructure
    global strpath

    if l[2] == "/":
        print("CD /")
        curdir = dirstructure['/']
        path = [curdir]
        strpath = ['/']
        print(" %s" % str(path))
        print("Curdir:")
        print(" %s" % str(curdir))

    elif l[2] == "..":
        print("CD ..")
        path.pop()
        strpath.pop()
        curdir = path[-1]
        print(" %s" % str(path))
        print("Curdir:")
        print(" %s" % str(curdir))

    else:
        directory = l[2]
        curdir = curdir['dirs'][directory]
        path.append(curdir)
        strpath.append(directory)
        print(" %s" % str(path))
        print("Curdir:")
        print(" %s" % str(curdir))


    print(strpath)

    #pprint(l)
    #pprint(path)
#    pprint(curdir)
#    pprint(dirstructure)
#    print("-------")

def handleDir(l):
    #print("handleDir(%s)" % str(l))
    # Found a directory
    global curdir
    global path
    global dirstructure

    directory = l[1]

    if directory in seendirs and directory == "hrtvrp":
        raise Exception("Duplicate dir: %s" % directory)

    seendirs.append(directory)

    if directory not in curdir['dirs']:
        curdir['dirs'][directory] = {'files' : {}, 'dirs' : {}, 'name' : directory}

#    pprint(l)
#    pprint(curdir)
#    print("xxxxxxxxxxx")

def handleFile(l):
    #print("handleFile(%s)" % str(l))
    global curdir
    filename = l[1]
    size = l[0]

    print(path)
    curdir["files"][filename] = size
#    pprint(curdir)
#    print("!!!!!!!!!!!")

def handleCommand(l):
    if l[1] == 'ls':
        print('LS')
        pass
    elif l[1] == 'cd':
        handleCd(l)
        #print('CD')
    elif l[0] == 'dir':
        handleDir(l)
    elif l[0].isnumeric():
        print(str(strpath))
        handleFile(l)
    else:
        print(l)
        raise Exception("Unknown command %s" % str(l))

def getDirSize(pathstring, p):
    #print("getDirSize(%s)" % (str(pathstring)))
    global smallsum
    global dirsum
    #print(pathstring)
    size = 0
    for filename in p['files']:
        size += int(p['files'][filename])

    for dirname in p['dirs']:
        #print(dirname)
        size += getDirSize(pathstring + dirname + "/", p['dirs'][dirname])

    dirsum.append((pathstring, size))
    #print("getDirSize(%s): %i" % (str(pathstring), size))

    if size <= 100000:
        smallsum += size
    #print(smallsum)
    return size

with open("input.txt", "r") as infile:
    for line in infile.readlines():
        print(line.strip())
        l = line.strip().split(" ")
        handleCommand(l)



#pprint(dirstructure)
print(getDirSize("/", dirstructure['/']))
print(dirsum)
print("smallsum: %i" % smallsum)

##
sum = 0
for s in dirsum:
    if int(s[1]) <= 100000:
        print(s[0])
        sum += int(s[1])
print(sum)
