#!/usr/bin/env python3

# laod and parse list
maxsum = 0
with open("input.txt", "r") as infile:
    elfsum = 0

    for line in infile.readlines():
        line = line.strip()
        if not line.isnumeric():
            if elfsum > maxsum:
                maxsum = elfsum
            elfsum = 0
            print("-----")
        else:
            elfsum += int(line)
            print(elfsum)

print("Maximum sum: %i" % maxsum)
