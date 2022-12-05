topCrates = []

class Crate(object):
    
    def __init__(self, pos, value, previousCrate, nextCrate):
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

    def move(self, target):
        # Link to top of target
        if self.nextCrate != None:
            self.nextCrate.previousCrate = None
        topCrates[self.pos] = self.nextCrate
        self.nextCrate = topCrates[target]
        topCrates[target] = self
        if self.nextCrate != None:
            self.nextCrate.previousCrate = self

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

    # Now parse instructions
    for line in lines[10:]:
        l = line.strip().split(" ")
        _, count, _, source, _, target = l
        count = int(count)
        source = int(source)
        target = int(target)
        print(line)
        for i in range(0, count):
            print(i)
            if topCrates[source-1] != None:
                topCrates[source-1].move(target-1)

line = ""
for c in topCrates:
    if c and c.value != None:
        line += c.value
    else:
        print("*")
print(line)
