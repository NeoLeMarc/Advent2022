import sys
from pprint import pprint
print("recursion limit: %i" % sys.getrecursionlimit())
sys.setrecursionlimit(5000)

topCrates = []

class Crate(object):
    
    def __init__(self, pos, value, previousCrate, nextCrate):
        if not value.isalpha():
            value = None
        self.value = value
        self.nextCrate = None
        self.previousCrate = None
        self.pos = pos

    def append(self, value):
        if self.nextCrate != None:
            self.nextCrate.append(value)
            #print("crate: traversing")
        else:
            self.nextCrate = Crate(self.pos, value, self, None)
            #print("crate: appending")

    def move(self, target, count = 0):
        print("Moving %i to %i" % (self.pos, target))
        oldpos = self.pos

        # Skip empty grates
        if self.value == None:
            print("Empty container found")
            if self.nextCrate != None:
                self.nextCrate.move(target, count)
            else:
                return
        else:

            moveContainer = self
            for i in range(1, count):
                print(moveContainer.value)
                print(i)

                ## Skip empty containers:
                while moveContainer.value == None:
                    print("Skipping empty container")
                    moveContainer = moveContainer.nextCrate
                    moveContainer.pos = target

                if moveContainer.nextCrate != None:
                    moveContainer = moveContainer.nextCrate
                    moveContainer.pos = target
                else:
                    print("no more containers")

            print(moveContainer.value)

            # Unlink from next container 
            if moveContainer.nextCrate != None:
                moveContainer.nextCrate.previousCrate = None

            # Link next container to top of list
            if moveContainer.nextCrate == None:
                topCrates[self.pos] = None
            else:
                topCrates[self.pos] = moveContainer.nextCrate 

            # Now link the target top crate as next container
            moveContainer.nextCrate = topCrates[target]

            # Noe let us be the top container of the target
            topCrates[target] = self

            # Set pos to new pos
            self.pos = target 

            # And create the back link
            if moveContainer.nextCrate != None:
                moveContainer.previousCrate = self

        # fix top list
        if not topCrates[oldpos]:
            topCrates[oldpos] = Crate(oldpos, "", None, None)

    def getValues(self):
        values = ""
        if self.value:
            values += self.value
        if self.nextCrate != None:
            #print(self.nextCrate)
            values += self.nextCrate.getValues()
        return values

def printCrates():
    i = 1
    for topCrate in topCrates:
        print("%i: %s" % (i, topCrate.getValues()))
        i += 1

with open("input.txt", "r") as infile:
    lines = infile.readlines()

    # Start with top crates
    line = ""
    for i in range(0, 9):
        value = lines[0][i*4+1]
        if value != " ":
            line += value 
        else:
            line += "*" 

        topCrates.append(Crate(i, value, None, None))
    print(line) 

    # Now parse the following crates
    for y in range(1, 8):
        line = ""
        for i in range(0,9):
            value = lines[y][i*4+1]
            if value != " ":
                line += value 
            else:
                line += "*" 
            topCrates[i].append(value)

        print(line)
    printCrates()

    # Now parse instructions
    for line in lines[10:]:
        l = line.strip().split(" ")
        _, count, _, source, _, target = l
        count = int(count)
        source = int(source)
        target = int(target)
        print(line)
        print("%i %s -> %s" % (i, source, target))
        print(topCrates[source-1].value)
        if topCrates[source-1] != None:
            topCrates[source-1].move(target-1, count)
        else:
            print("Warning: Trying to move empty")

        printCrates()
line = ""
for c in topCrates:
    if c and c.value != None:
        line += c.value
    else:
        print("*")
print(line)
