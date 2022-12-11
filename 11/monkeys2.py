#!/usr/bin/env python
import sys

monkeys = []

class Monkey:

    def __init__(self, number, starting_items, operation, test, truemonkey, falsemonkey):
        self.number = number
        self.items = [int(i) for i in starting_items]
        self.operation = operation
        self.test = int(test)
        self.truemonkey = int(truemonkey) 
        self.falsemonkey = int(falsemonkey) 
        self.printState()
        self.inspectcount = 0

    def printState(self):
        print("Monkeystate %i" % self.number)
        print("Items: %s" % str(self.items))
        print("Operation: %s" % str(self.operation))
        print("Test: %i" % self.test)
        print("Truemonkey: %i" % self.truemonkey)
        print("Falsemonkey: %i" % self.falsemonkey)
        print("----------------------------")

    def doOperation(self, item):
        if self.operation[1] == 'old':
            increment = item
        else:
            increment = int(self.operation[1])

        new = item
        if self.operation[0] == '+':
            new += increment
            print("   Worry level increases by %i to %i." % (increment, new))
        elif self.operation[0] == '*':
            new *= increment 
            print("   Worry is multiplied by %i to %i." % (increment, new))
        else:
            raise Exception("Unknown operation")

#        print("Operation: %s : %s : %s" % (str(self.operation), item, new))
        return new

    def doTest(self, item):
        self.inspectcount += 1
        new = item 
#        new = int(item / 3)
#        print("   Monkey gets bored with item. Worry level is divided by 3 to %i." % new)
        if new % self.test == 0:
            print("   Current worry level %i is divisible by %i." % (new, self.test))
            return new, True
        else:
            print("   Current worry level %i is not divisible by %i." % (new, self.test))
            return new, False

    def handleItem(self, item):
        new = self.doOperation(item)
        new, testresult = self.doTest(new)

        if testresult:
            print("    Item with worry level %i is thrown to monkey %i" % (new, self.truemonkey))
            monkeys[self.truemonkey].throw(item)
        else:
            print("    Item with worry level %i is thrown to monkey %i" % (new, self.falsemonkey))
            monkeys[self.falsemonkey].throw(item)

    def throw(self, item):
#        print("! Monkey %i receiving item: %s" % (self.number, item))
        self.items.append(item)

    def getItems(self):
        return self.items

    def execute(self):
#        print("Run Monkey %i" % self.number)
        print("Monkey %i:" % self.number)
        self.items.reverse()
        while self.items:
            item = self.items.pop()
            print(" Monkey inspects an item with a worry level of %i." % item)
            self.handleItem(item)


with open(sys.argv[1], 'r') as file:
    line = file.readline()
    while line:
        print(line)
        monkeyNumber = int(line.strip().split(' ')[1][:-1])

        itemsstr = file.readline().strip().split(':')[1].split(',')
        operation = file.readline().strip().split(' ')[-2:]
        test = file.readline().split(' ')[-1]
        truemonkey = file.readline().split(' ')[-1]
        falsemonkey = file.readline().split(' ')[-1]

        monkeys.append(Monkey(monkeyNumber, itemsstr, operation, test, truemonkey, falsemonkey))
        file.readline()
        line = file.readline()

for i in range(0, 20): # 10000):
    print("\nRound: %i" % i)
    for monkey in monkeys:
        monkey.execute()

    for monkey in monkeys:
        print("Monkey %i: " % monkeys.index(monkey) + str(monkey.getItems()))

for monkey in monkeys:
    print(monkey.inspectcount)

inspectcount = [i.inspectcount for i in monkeys]
inspectcount.sort()
print(inspectcount.pop() * inspectcount.pop())
