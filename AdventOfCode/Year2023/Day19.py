#https://adventofcode.com/2023/day/19
#https://adventofcode.com/2023/day/19#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 1:
    inFile = os.path.join(inFileDir, "InputTestFiles/d19_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d19_real.txt")


def getInput():
    rules = {}
    parts = []

    with open(inFile, 'r') as f:
        lineIsRules = True

        for line in f:
            if line == '\n':
                lineIsRules = False
            else:
                line = line.replace('\n', '')[:-1]
                if lineIsRules:
                    name = line.split('{')[0]
                    r = line.split('{')[1].split(',')
                    rules[name] = r
                else:
                    line = line[1:].replace("x=", '').replace("m=", '').replace("a=", '').replace("s=", '').split(',')
                    parts.append([int(line[0]), int(line[1]), int(line[2]), int(line[3])])

    return rules, parts


def solution1():
    rules, parts = getInput()

    total = 0
    for part in parts:
        x,m,a,s = part

        currRule = 'in'
        while True:
            #If the current rule name is 'A' for 'accepted', we add the xmas values to the total
            if currRule == 'A':
                total += x + m + a + s
                break
            #If the current rule name is 'R' for 'rejected', we stop all processes
            elif currRule == 'R':
                break

            #Otherwise we parse through the instructions for the current rule
            for ruleStr in rules[currRule]:
                #If the current rule instruction is one character or it's just a new rule name, we switch to that rule
                if len(ruleStr) == 1 or ruleStr in rules.keys():
                    currRule = ruleStr
                    break

                val = None
                if ruleStr[0] == 'x': val = x
                elif ruleStr[0] == 'm': val = m
                elif ruleStr[0] == 'a': val = a
                elif ruleStr[0] == 's': val = s

                comp = int(ruleStr[2:].split(':')[0])
                nextRule = ruleStr[2:].split(':')[1]
                
                if '<' in ruleStr and val < comp:
                    currRule = nextRule
                    break
                elif '>' in ruleStr and val > comp:
                    currRule = nextRule
                    break

    return total


def solution2():
    rules, parts = getInput()
    
    xRange = [1,4000]
    mRange = [1,4000]
    aRange = [1,4000]
    sRange = [1,4000]

    q = ['in']
    seen = []
    pathMap = {}
    while len(q) > 0:
        head = q.pop(0)
        for ins in rules[head]:
            #Not caring about 
            if ins == 'A' or ins == 'R':
                continue
            nextNode = None

            if ins in rules.keys():
                if ins not in q and ins not in seen:
                    q.append(ins)
                nextNode


    return 


print("Year 2023, Day 19 solution part 1:", solution1())
print("Year 2023, Day 19 solution part 2:", solution2())