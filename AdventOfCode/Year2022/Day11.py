#https://adventofcode.com/2022/day/11
#https://adventofcode.com/2022/day/11#part2

import math
import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d11_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d11_real.txt")


def getMonkeys():
    #Behavior of each monkey
    monkeys = {}

    lineVal = 0
    monkeyNum = -1
    items = []
    operation = []
    div = 0
    trueCond = -1
    falseCond = -1
    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            if lineVal == 0: #monkey number
                monkeyNum = int(line[6:-2])
            elif lineVal == 1: #starting items
                items = line[18:-1]
                items = items.split(", ")
                for i in range(0, len(items)):
                    items[i] = int(items[i])
            elif lineVal == 2: #operation
                o = line[13:-1]
                operation = o.split(' ')
                operation = operation[2:]
            elif lineVal == 3: #divisor
                div = int(line[21:-1])
            elif lineVal == 4: #True condition
                trueCond = int(line[29:-1])
            elif lineVal == 5: #false condition
                falseCond = int(line[30:-1])

                #save monkey values
                monkey = {
                    "items": items,
                    "operation": operation,
                    "divisor": div,
                    "true": trueCond,
                    "false": falseCond
                    }
                monkeys[monkeyNum] = monkey
            else:#blank line. reset
                lineVal = -1
            lineVal += 1

    return monkeys


def solution1():
    #Behavior of each monkey
    monkeys = getMonkeys()
    #The number of times each monkey has seen an item
    itemsSeen = [0] * len(monkeys.keys())


    for r in range(0, 20):
        for m in range(0, len(monkeys.keys())):
            for j in range(0, len(monkeys[m]["items"])):
                #Increasing the counter for how many items this monkey has seen
                itemsSeen[m] += 1

                #Int value for the "worry" level of the current item
                worry = monkeys[m]["items"][0]

                #First value in the operation
                opVal1 = monkeys[m]["operation"][0]
                if opVal1 == "old":
                    opVal1 = worry
                else:
                    opVal1 = int(opVal1)

                #second value in the operation
                opVal2 = monkeys[m]["operation"][2]
                if opVal2 == "old":
                    opVal2 = worry
                else:
                    opVal2 = int(opVal2)

                #Operation to perform
                opSymb = monkeys[m]["operation"][1]
                result = 0

                if opSymb == '+':
                    result = opVal1 + opVal2
                elif opSymb == '-':
                    result = opVal1 - opVal2
                elif opSymb == '*':
                    result = opVal1 * opVal2
                elif opSymb == '/':
                    result = opVal1 / opVal2

                #print("Result after operation:", result)
                result = result // 3
                #print("Result after dividing by 3:", result)

                #Passing the item to a new monkey
                #print("Is evenly divisible by", monkeys[m]["divisor"])
                if result % monkeys[m]["divisor"] == 0:
                    #print("TRUE: Pass to monkey", monkeys[m]["true"])
                    passTo = monkeys[m]["true"]
                    monkeys[passTo]["items"].append(result)
                else:
                    #print("FALSE: Pass to monkey", monkeys[m]["false"])
                    passTo = monkeys[m]["false"]
                    monkeys[passTo]["items"].append(result)

                #Removing the item from this monkey's item list
                monkeys[m]["items"].pop(0)


    itemsSeen.sort(reverse=True)
    return itemsSeen[0] * itemsSeen[1]


def solution2():
    #Behavior of each monkey
    monkeys = getMonkeys()
    #The number of times each monkey has seen an item
    itemsSeen = [0] * len(monkeys.keys())

    #Getting the product of all monkey divisors to put a cap on the largest value that can be seen
    bigDiv = 1
    for m in monkeys.keys():
        bigDiv *= monkeys[m]["divisor"]

    for r in range(0, 10000):
        for m in range(0, len(monkeys.keys())):
            for j in range(0, len(monkeys[m]["items"])):
                #Increasing the counter for how many items this monkey has seen
                itemsSeen[m] += 1

                #Int value for the "worry" level of the current item
                worry = monkeys[m]["items"][0]

                #First value in the operation
                opVal1 = monkeys[m]["operation"][0]
                if opVal1 == "old":
                    opVal1 = worry
                else:
                    opVal1 = int(opVal1)

                #second value in the operation
                opVal2 = monkeys[m]["operation"][2]
                if opVal2 == "old":
                    opVal2 = worry
                else:
                    opVal2 = int(opVal2)

                #Operation to perform
                opSymb = monkeys[m]["operation"][1]
                result = 0

                if opSymb == '+':
                    result = opVal1 + opVal2
                elif opSymb == '-':
                    result = opVal1 - opVal2
                elif opSymb == '*':
                    result = opVal1 * opVal2
                elif opSymb == '/':
                    result = opVal1 / opVal2

                # Preventing the result from getting larger than the product of all monkey divisors
                result = result % bigDiv

                #Passing the item to a new monkey
                #print("Is evenly divisible by", monkeys[m]["divisor"])
                if result % monkeys[m]["divisor"] == 0:
                    #print("TRUE: Pass to monkey", monkeys[m]["true"])
                    passTo = monkeys[m]["true"]
                    monkeys[passTo]["items"].append(result)
                else:
                    #print("FALSE: Pass to monkey", monkeys[m]["false"])
                    passTo = monkeys[m]["false"]
                    monkeys[passTo]["items"].append(result)

                #Removing the item from this monkey's item list
                monkeys[m]["items"].pop(0)

    itemsSeen.sort(reverse=True)
    return itemsSeen[0] * itemsSeen[1]


print("Year 2022, Day 11 solution part 1:", solution1())
print("Year 2022, Day 11 solution part 2:", solution2())