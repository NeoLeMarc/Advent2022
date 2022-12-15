#!/usr/bin/env
import sys

with open(sys.argv[1], 'r') as infile:
    lines = infile.read().splitlines()

for line in lines:
    l = line.split(' ')
    print(l)
    sensorpos_x = int(l[2][2:-1])
    sensorpos_y = int(l[3][2:-1])

    beaconpos_x = l[8][2:-1]
    beaconpos_y = l[9][2:]
