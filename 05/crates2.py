import sys
from pprint import pprint
print("recursion limit: %i" % sys.getrecursionlimit())
sys.setrecursionlimit(40)

topCrates = []

class Crate(object):
    
    def __init__(self, pos, value, previousCrate, nextCrate):
        if not value.isalpha():
            value = None
        if value == None and previousCrate != None:
            raise Exception("Non-top empty container")
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
        
        # Remove empty containers
        if self.value == None:
            print("Removing empty container")
            if self.previousCrate == None:
                # Top crate
                self.nextCrate.previousCrate = None
                topCrates[self.pos] = self.nextCrate
            else:
                self.nextCrate.previousCrate = self.previousCrate

    def move(self, target, count):
        if count > 1:
            # Move other containers first to perserve order
            # Warning: topCrates is borken until move is finished
            if self.nextCrate:
                self.nextCrate.move(target, count - 1)
            else:
                return
        if count < 0:
            return

        print("%s: Moving %i to %i count %i (%s)" % (self.value, self.pos, target, count, self))
        oldpos = self.pos

        print("!!!!!!! DEBUG !!!!!!")
        print("Start:")
        print(self)
        pprint(self.__dict__)
        pprint(topCrates)


        # Unlink from next and previous container 
        if self.nextCrate != None:
            self.nextCrate.previousCrate = self.previousCrate 

        if self.previousCrate:
            self.previousCrate.nextCrate = self.nextCrate

        else:
            # Link next container to top of list - but only if we were the top container
            topCrates[oldpos] = self.nextCrate
        
        # Now we are at the top
        self.previousCrate = None

        # Now link the target top crate as next container
        print("Target: " + str(target))
        oldnext = self.nextCrate
        oldnext.nextCrate = self.nextCrate # Maybe bufix
        self.nextCrate = topCrates[target]

        # Noe let us be the top container of the target
        topCrates[target] = self

        # Set pos to new pos
        self.pos = target 

        # And create the back link
        if self.nextCrate != None:
            self.nextCrate.previousCrate = self

        # fix top list
        if not topCrates[oldpos]:
            topCrates[oldpos] = Crate(oldpos, "", None, None)

        print("End:")
        print(self)
        pprint(self.__dict__)
        print("Old next:")
        if oldnext != None:
            pprint(oldnext.__dict__)
        else:
            print("None")
        pprint(topCrates)

    def getValues(self, seen):
        #if self.previousCrate == None:
        #    print("------>")
        #    pprint(self.__dict__)
        #print("get values: %s" % str(seen))
        #if len(seen) == 0:
        #    print("Begin debug")
        #    pprint(topCrates)
        #    print(self)
        #    pprint(self.__dict__)

        if self in seen:
            print("Circle information")
            print(seen)
            pprint(topCrates)
            print("Culprit:")
            print(seen[-1])
            pprint(seen[-1].__dict__)
            print("Affected:")
            print(self)
            pprint(self.__dict__)
            sys.stdout.flush()
            raise Exception("Error: circle found")

        seen.append(self)

        values = ""
        if self.value:
            values += self.value
            if self.value == None:
                values += "*"
        if self.nextCrate != None:
            #print(self.nextCrate)
            values += self.nextCrate.getValues(seen)
        #print("<-------")
        return values

def printCrates():
    i = 1
    for topCrate in topCrates:
        print("%i: %s" % (i, topCrate.getValues([])))
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
                topCrates[i].append(value)
            else:
                line += "*" 

        print(line)
    printCrates()

    # Now parse instructions
    for line in lines[10:]:
        print("--------------------------")
        l = line.strip().split(" ")
        _, count, _, source, _, target = l
        count = int(count)
        source = int(source)
        target = int(target)
        print(line)

        print("%s -> %s" % (source, target))
        print(topCrates[source-1].value)
        if topCrates[source-1] != None:
            topCrates[source-1].move(target-1, count)
        else:
            print("Warning: Trying to move empty")
        printCrates()
        pprint(topCrates)


line = ""
for c in topCrates:
    if c and c.value != None:
        line += c.value
    else:
        print("*")
print(line)
