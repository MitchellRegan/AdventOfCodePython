#https://adventofcode.com/2022/day/10
#https://adventofcode.com/2022/day/10#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d10_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d10_real.txt")

def solution1():
    instructions = []
    sum = 0
    x = 1
    neededCycles = [20,60,100,140,180,220]

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            if line[0:4] == "noop":
                instructions.append(0)
            elif line[0:4] == 'addx':
                val = line[5:]
                if val[-1] == '\n':
                    val = val[:-1]
                instructions.append(0)
                instructions.append(int(val))

    for i in range(0, len(instructions)):
        if (i+1) in neededCycles:
            sum += (i+1) * x
            #print(" - - Needed cycle", (i+1), " X=",x," Adding", ((i+1)*x))
        x += instructions[i]

    return sum


def solution2():
    x = 1
    instructions = []

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            if line[0:4] == "noop":
                instructions.append(0)
            elif line[0:4] == 'addx':
                val = line[5:]
                if val[-1] == '\n':
                    val = val[:-1]
                instructions.append(0)
                instructions.append(int(val))

    outputLine = ""
    for i in range(0, len(instructions)):
        #print("I:", i, "X:", x)
        compVal = i % 40

        if abs(x-compVal) < 2:
            outputLine += '#'
        else:
            outputLine += ' '
            
        x += instructions[i]

        if (i+1) % 40 == 0:
            print(outputLine)
            outputLine = ""
    print("")
    return "These characters ^^^"


print("Year 2022, Day 10 solution part 1:", solution1())
print("Year 2022, Day 10 solution part 2:", solution2())