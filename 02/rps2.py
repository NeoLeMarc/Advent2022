ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

def isrock(i):
    if i in ('A', 'X'):
        return True
    else:
        return False

def ispaper(i):
    if i in ('B', 'Y'):
        return True
    else: 
        return False

def isscissors(i):
    if i in ('C', 'Y'):
        return True
    else:
        return False


outcome = {'X' : 'lose',
           'Y' : 'draw',
           'Z' : 'win'}

def points(ins):
    return ord(ins) - ord('W')

def winpoints(t, y):
    if t == 'A':
        if y == 'X':
            # Draw
            return 3
        if y == 'Y':
            # Win
            return 6
        else: 
            # Lose
            return 0
    elif t == 'B':
        if y == 'X':
            return 0
        if y == 'Y':
            return 3
        else: 
            return 6
    else: 
        if y == 'X':
            return 6
        if y == 'Y':
            return 0
        else:
            return 3

def getStrategy(t, o):
    # x: lose
    # y: draw
    # z: win
    if outcome[o] == 'lose':
        # need to lose
        if isrock(t):
            # Rock -> Scissors
            return SCISSORS 
        elif isscissors(t):
            # Scissors -> Paper
            return PAPER 
        else:
            # Paper -> Rock
            return  ROCK

    if outcome[o] == 'draw':
        # need a draw
        if isscissors(t):
            return SCISSORS 
        elif isrock(t):
            return ROCK 
        else:
            return PAPER

    else:
        # need to win
        if isrock(t):
            return PAPER 
        elif isscissors(t):
            return ROCK
        else:
            return SCISSORS


pts = 0
with open("input.txt", "r") as infile:
    for line in infile.readlines():
        t, g = line.strip().split(' ')
        y = getStrategy(t, g)
        print(line)
        print(y)
        print(points(y))
        print(winpoints(t, y))
        pts += points(y) + winpoints(t, y)
        print ("==")

print(pts)
