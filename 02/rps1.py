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

pts = 0
with open("input.txt", "r") as infile:
    for line in infile.readlines():
        t, y = line.strip().split(' ')
        print(line)
        print(points(y))
        print(winpoints(t, y))
        pts += points(y) + winpoints(t, y)
        print ("==")

print(pts)
