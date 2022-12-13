#!/usr/bin/env python
import sys
inp = []

YES = -1
NO = 1
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
        return compareList(a, b)
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
         # if *exactly* one value is an integer, convert the integer to a list, then retry
         print("Mixed types, converting b to list")
         b = [b]
         return compareValue(a, b)
    elif type(b) == type([]) and type(a) == type(int()):
        # if *exactly* one value is an integer, convert the integer to a list, then retry
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

def compareList(a, b):
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
    elif len(a) > 0 and len(b) <= 0:
        return  NO
    elif len(b) > 0 and len(a) <= 0:
        return YES 
    else:
        # that does not seem right
        print("going to next element")
        return CONTINUE

inlist = [[[2]],[[6]]]
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
        inlist.append(a)
        inlist.append(b)
        in1 = infile.readline()
        in2 = infile.readline()

print(inlist)
from functools import cmp_to_key
slist = sorted(inlist, key=cmp_to_key(compareList))
for i in range(0, len(slist)):
    value = slist[i]
    print(value)
    if value in ([[6]], [[2]]):
        print("*** Delimiter found at %i: %s" % (i, slist[i]))
#i = 1 
#tsum = 0
#for pair in inp:
#    print("Pair (%i): %s" % (i, str(pair)))
#    print("A = %s" % pair[0])
#    print("B = %s" % pair[1])
#    print("**") 
#    value = compareList(pair[0], pair[1])
#    print("-----------------------")
##
#    if value == YES:
#        tsum += i
#        print("Incrementing tsum, is now: %i" % tsum)
#    elif value == NO:
#        print("Not incrementing")
#    else:
#        raise Exception("Unexpected return")
#    sys.stdout.flush()
#    i += 1
#    print("********************************************************")
#print("Tsum is: %i" % tsum)
