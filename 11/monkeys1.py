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
        elif self.operation[0] == '*':
            new *= increment 
        else:
            raise Exception("Unknown operation")

        print("Operation: %s : %s : %s" % (str(self.operation), item, new))
        return new

    def doTest(self, item):
        self.inspectcount += 1
        new = int(item / self.test)
        print("Test: %i -> %i " % (item, new))
        if new % self.test:
            return new, True
        else:
            return new, False

    def handleItem(self, item):
        new = self.doOperation(item)
        new, testresult = self.doTest(new)

        if testresult:
            monkeys[self.truemonkey].throw(new)
        else:
            monkeys[self.falsemonkey].throw(new)

    def throw(self, item):
        print("! Monkey %i receiving item: %s" % (self.number, item))
        self.items.append(item)

    def execute(self):
        print("Run Monkey %i" % self.number)
        while self.items:
            item = self.items.pop()
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

for i in range(0, 20):
    for monkey in monkeys:
        monkey.printState()
        monkey.execute()
        print("****")

for monkey in monkeys:
    print("%i - %s" % (monkey.number, str(monkey.inspectcount)))
