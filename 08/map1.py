import sys
filename = sys.argv[1]

with open(filename, "r") as infile:
    lines = infile.read().splitlines()


visible = []
# Left to right
for i in range(0, len(lines)):
    maxseen = -1 
    cvisible = 0
    for j in range(0, len(lines[i])):
        print("l: %s (m: %i)" % (lines[i][j], maxseen))
        if int(lines[i][j]) > maxseen:
            maxseen = int(lines[i][j])
            visible.append((i, j)) 
            cvisible += 1
    print(cvisible)


print("------")
# Right to left
for i in range(0, len(lines)):
    maxseen = -1
    cvisible = 0
    for j in range(len(lines[i]) -1, -1, -1):
        print("l: %s (m: %i)" % (lines[i][j], maxseen))
        if int(lines[i][j]) > maxseen:
            maxseen = int(lines[i][j])
            visible.append((i, j)) 
            cvisible += 1
    print(cvisible)

print("------")
# Top to bottom
cvisible = 0
for j in range(0, len(lines[0])):
    maxseen = -1 
    cvisible = 0
    for i in range(0, len(lines)):
        print("l: %s (m: %i)" % (lines[i][j], maxseen))
        if int(lines[i][j]) > maxseen:
            maxseen = int(lines[i][j])
            visible.append((i, j)) 
            cvisible += 1
    print(cvisible)


print("------")
# Bottom to top
cvisible = 0
for j in range(0, len(lines[0])):
    maxseen = -1 
    cvisible = 0
    for i in range(len(lines) -1, -1, -1):
        print("l: %s (m: %i)" % (lines[i][j], maxseen))
        #print("(%i, %i)" % (i, j))
        if int(lines[i][j]) > maxseen:
            maxseen = int(lines[i][j])
            visible.append((i, j)) 
            cvisible += 1
    print(cvisible)

visible = list(set(visible))
list.sort(visible)
print(visible)
print(len(visible))

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
    for j in range(0, len(lines)):
        if (i, j) in visible:
            out += str(lines[i][j])
        else:
            out += bcolors.FAIL + lines[i][j] + bcolors.ENDC
    print(out)

