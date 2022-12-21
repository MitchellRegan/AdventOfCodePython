#https://adventofcode.com/2022/day/21
#https://adventofcode.com/2022/day/21#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d21_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d21_real.txt")

#Memo to store the int values of already seen monkey names
memo = {}
memo2 = {}
monkeys = {}

def getInput():
    with open(inFile, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            line = line.split(' ')

            name = line[0][:-1]
            command = None
            if len(line) == 2:
                command = int(line[1])
                memo[name] = command
            else:
                command = line[1:]

            monkeys[name] = command
    return


def getMonkeyValue_v2(name):
    #If the value for this monkey is an int, we return that value
    if type(monkeys[name]) == int:
        #If it isn't the human, we store it in the memo
        if name != "humn":
            memo2[name] = monkeys[name]
        return monkeys[name]

    #Getting the first monkey value
    m1 = 0
    if monkeys[name][0] in memo2.keys():
        m1 = memo2[monkeys[name][0]]
    else:
        m1 = getMonkeyValue_v2(monkeys[name][0])

    #Getting the second monkey value
    m2 = 0
    if monkeys[name][2] in memo2.keys():
        m2 = memo2[monkeys[name][2]]
    else:
        m2 = getMonkeyValue_v2(monkeys[name][2])

    #Performing the required operator on the two values
    op = monkeys[name][1]
    if op == '+':
        if monkeys[name][0] in memo2.keys() and monkeys[name][2] in memo2.keys():
            memo2[name] = m1 + m2
        return m1 + m2
    elif op == '-':
        if monkeys[name][0] in memo2.keys() and monkeys[name][2] in memo2.keys():
            memo2[name] = m1 - m2
        return m1 - m2
    elif op == '*':
        if monkeys[name][0] in memo2.keys() and monkeys[name][2] in memo2.keys():
            memo2[name] = m1 * m2
        return m1 * m2
    elif op == '/':
        if monkeys[name][0] in memo2.keys() and monkeys[name][2] in memo2.keys():
            memo2[name] = m1 // m2
        return m1 // m2
    #Root is the only one that returns a bool to check if the values are equal
    elif op == '=':
        return m1 - m2

    #Otherwise return None to cause an error
    return None


def solution1(name):
    #Checking if the monkey's name already has a defined int value attached to it
    if name in memo.keys():
        return memo[name]

    #If not, we need to calculate it using the monkeys given in its command
    m1 = solution1(monkeys[name][0])
    m2 = solution1(monkeys[name][2])
    op = monkeys[name][1]

    if op == '+':
        return m1 + m2
    elif op == '-':
        return m1 - m2
    elif op == '*':
        return m1 * m2
    elif op == '/':
        return m1 // m2

    #Otherwise return None to cause an error
    return None


def solution2():
    monkeys["root"][1] = '='
    curVal = 1
    preVal = 1
    i = 1
    j = None

    while True:
        monkeys["humn"] = i

        preVal = curVal
        curVal = getMonkeyValue_v2("root")

        if curVal == 0:
            return i
        if preVal > 0 and curVal > 0:
            j = i
            i = 2 * i
        elif preVal < 0 and curVal < 0:
            j = i
            i = i // 2
        elif (preVal < 0 and curVal > 0) or (preVal > 0 and curVal < 0):
            placeholder = i
            i = (abs(i-j) // 2) + min(i,j)
            j = placeholder


getInput()
print("Year 2022, Day 21 solution part 1:", solution1("root"))
print("Year 2022, Day 21 solution part 2:", solution2())