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
        print("Delegating to compare lists")
        return compareList((a, b))
        # if both values are lists:
        #if len(a) < len(b):
        #    # if left is shorter, inputs are in right order
        #    return YES
        #elif len(b) > len(a):
        #    # if right is shorter, inputs re not in right order
        #    return NO
        #else:
        #    # continue
        #    print("CONTINUE 1")
        #    return CONTINUE
    elif type(a) == type([]) and type(b) == type(int()):
         # if exactly one value is an integer, convert the integer to a list, then retry
         print("Mixed types, converting b to list")
         b = [b]
         return compareValue(a, b)
    elif type(b) == type([]) and type(a) == type(int()):
        # if exactly one value is an integer, convert the integer to a list, then retry
        print("Mixed types, converting a to list")
        a = [a]
        return compareValue(a, b)
    elif len(a) > 1 and len(b) > 1:
        print("Not implemented")
        raise Exception("Not implemented")
    else:
        print("Not implemented")
        print(type(a))
        print(type(b))
        sys.stdout.flush()
        raise Exception("Not implemented")

def compareList(pair):
    a, b = pair

    i = 0
    if len(a) > 0 and len(b) > 0:
        value = CONTINUE
        while value == CONTINUE:
            try:
                a[i]
            except(IndexError):
                try:
                    b[i]
                    print("A ran out of items")
                    return YES 
                except(IndexError):
                    print("Both ran out of items")
                    return CONTINUE

            try:
                b[i]
            except(IndexError):
                print("B ran out of items")
                return NO

            value = compareValue(a[i], b[i])
            if value == CONTINUE:
                print("Got CONTINUE")
                i += 1
            else:
                print("Value is: %i" % value)
                return value
    else:
        if len(a) > len(b):
            print("b is empty")
            return NO 
        else:
            print("a is empty")
            return YES 

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

i = 0 
tsum = 0
for pair in inp:
    print("Pair (%i): %s" % (i, str(pair)))
    value = compareList(pair)
    print(value)
    print("-----------------------")

    if value == YES:
        tsum += i
        print("Incrementing tsum, is now: %i" % tsum)
    sys.stdout.flush()
    i += 1
print("Tsum is: %i" % tsum)
