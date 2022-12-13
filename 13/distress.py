#!/usr/bin/env python
import sys
inp = []

YES = 1
NO = -1
CONTINUE = 0

def compareInt(a, b):
    if a < b:
        return YES
    if a > b:
        return NO
    else: 
        return CONTINUE 

def compareValue(a, b):
    print(a, b)

    # if both values are integers, the lower interger should come first
    if type(a) == type(int()) and type(b) == type(int()):
        res = compareInt(a, b)
        if res == YES:
            print("a < b")
            return YES
        elif  res == NO:
            print("b > a")
            return NO
        else:
            print("CONTINUE")
            return CONTINUE
    elif type(a) == type([]) and type(b) == type([]):
        # if both values are lists:
        if len(a) < len(b):
            # if left is shorter, inputs are in right order
            return YES
        elif len(b) > len(a):
            # if right is shorter, inputs re not in right order
            return NO
        else:
            # continue checking the next part of the input
            return CONTINUE
    elif len(a) > 1 and len(b) > 1:
        print("Not implemented")
        raise Exception("Not implemented")
    else:
        print("Not implemented")
        print(type(a))
        print(type(b))
        raise Exception("Not implemented")

def compareList(pair):
    a, b = pair

    i = 0
    if len(a) > 0 and len(b) > 0:
        value = CONTINUE
        while value == CONTINUE:
            value = compareValue(a[i], b[i])
            if value == CONTINUE:
                print("Got CONTINUE")
                i += 1
            else:
                print("Value is: %i" % value)
                return value
    else:
        raise Exception("Got empty list")

with open(sys.argv[1], 'r') as infile:
    in1 = infile.readline()
    in2 = infile.readline()

    while in1:
        ini1 = 'a = ' + in1
        ini2 = 'b = ' + in2
        infile.readline()
        if not ini1:
            break
        exec(ini1)
        exec(ini2)
        inp.append((a, b))
        in1 = infile.readline()
        in2 = infile.readline()

for pair in inp:
    print("Pair: %s" % str(pair))
    value = compareList(pair)
    print("-----------------------")
    sys.stdout.flush()
