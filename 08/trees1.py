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
        if int(lines[i][j]) > maxseen:
            maxseen = int(lines[i][j])
            visible.append((i, j)) 
            cvisible += 1
    print(cvisible)

print("------")
# Top to bottom
cvisible = 0
for j in range(0, len(lines[i])):
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
for j in range(len(lines[i]) -1, -1, -1):
    maxseen = 0
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
print(visible)
print(len(visible))
