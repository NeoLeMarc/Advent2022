#!/usr/bin/env python
import sys

monkeys = []

class Monkey:

    def __init__(self, number, starting_items, operation, test, truemonkey, falsemonkey):
        self.number = number
        self.items = [int(i) for i in starting_items]
        self.operation = operation
        self.test = int(test)
        self.truemonkey = int(truemonkey) - 1
        self.falsemonkey = int(falsemonkey) - 1
        self.initems = []
        self.printState()

    def printState(self):
        print("New monkey %i" % self.number)
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

        if self.operation[0] == '+':
            new += increment
        elif self.operation[0] == '*':
            new *= operation
        else:
            raise Exception("Unknown operation")

        return new

    def doTest(self, item):
        if item % self.test:
            return True
        else:
            return False

    def handleItem(self, item):
        new = self.doOperation(item)

        if self.doTest(item):
            monkeys[truemonkey].throw(item)
        else:
            monkey[falsemonkey].throw(item)

    def throw(self, item):
        self.initems.append(item)

    def execute(self):
        for item in self.items:
            self.handleItem(item)
        self.items = self.initems
        self.initems = []


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
