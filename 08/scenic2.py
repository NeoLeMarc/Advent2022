import sys
filename = sys.argv[1]

with open(filename, "r") as infile:
    lines = infile.read().splitlines()


def calculateScenicScore(x, y):
    visible = []
    cvisible = 0
    # Left to right
    maxseen = -1 
    cvisible = 0
    for j in range(y, len(lines[0])):
        print("l: %s (m: %i)" % (lines[x][j], maxseen))
        if int(lines[x][j]) > maxseen:
            maxseen = int(lines[x][j])
            visible.append((x, j)) 
            cvisible += 1
    scenicA = cvisible

    print("------")
    # Right to left
    maxseen = -1
    cvisible = 0
    for j in range(y - 1, -1, -1):
        print("l: %s (m: %i)" % (lines[x][j], maxseen))
        if int(lines[x][j]) > maxseen:
            maxseen = int(lines[x][j])
            visible.append((x, j)) 
            cvisible += 1
    print(cvisible)
    scenicB = cvisible

    print("------")
    # Top to bottom
    cvisible = 0
    maxseen = -1 
    cvisible = 0
    for i in range(x + 1, len(lines)):
        print("l: %s (m: %i)" % (lines[i][y], maxseen))
        if int(lines[i][y]) > maxseen:
            maxseen = int(lines[i][y])
            visible.append((i, y)) 
            cvisible += 1
    print(cvisible)
    scenicC = cvisible


    print("------")
    # Bottom to top
    cvisible = 0
    maxseen = -1
    for i in range(x - 1, -1, -1):
        print("l: %s (m: %i)" % (lines[i][y], maxseen))
        #print("(%i, %i)" % (i, j))
        if int(lines[i][y]) > maxseen:
            maxseen = int(lines[i][y])
            visible.append((i, y)) 
            cvisible += 1
    print(cvisible)
    scenicD = cvisible

    visible = list(set(visible))
    list.sort(visible)
    print(visible)

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
            if (i, j) == (x, y):
                out += bcolors.BOLD + lines[i][j] + bcolors.ENDC
            if (i, j) in visible:
                out += bcolors.OKGREEN + lines[i][j] + bcolors.ENDC
            else:
                out += bcolors.FAIL + lines[i][j] + bcolors.ENDC
        print(out)

    print(len(visible))
    return scenicA + scenicB + scenicC + scenicD


calculateScenicScore(2, 2)
