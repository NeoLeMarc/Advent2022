
class Crate(object):
    
    def __init__(self, value, previousCrate, nextCrate):
        self.value = value
        self.nextCrate = None
        self.previousCrate = None

    def append(self, value):
        if self.nextCrate != None:
            self.append(value)
            print("crate: traversing")
        else:
            self.nextCrate = Crate(value, self, None)
            print("crate: appending")

topCrates = []

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

        topCrates.append(Crate(value, None, None))
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
