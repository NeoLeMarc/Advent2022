#!/usr/bin/env python3

# laod and parse list
maxsum1 = 0
maxsum2 = 0
maxsum3 = 0
with open("input.txt", "r") as infile:
    elfsum = 0

    for line in infile.readlines():
        line = line.strip()
        if not line.isnumeric():
            if elfsum > maxsum1:
                maxsum3 = maxsum2
                maxsum2 = maxsum1
                maxsum1 = elfsum
            elfsum = 0
            print("-----")
        else:
            elfsum += int(line)
            print(elfsum)

print("Maximum sum: %i" % (maxsum1 + maxsum2 + maxsum3))
