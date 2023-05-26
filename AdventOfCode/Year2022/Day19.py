#https://adventofcode.com/2022/day/19
#https://adventofcode.com/2022/day/19#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = os.path.join(inFileDir, "InputTestFiles/d19_test.txt")
#inFile = os.path.join(inFileDir, "InputRealFiles/d19_real.txt")


def getInput():
    ins = {}
    with open(inFile, 'r') as f:
        for line in f:
            i = line.split(' ')
            curDict = {}
            idNum = int(i[1][:-1])
            curDict["oreRobotCost"] = int(i[6])
            curDict["clayRobotCost"] = int(i[12])
            curDict["obsRobotOreCost"] = int(i[18])
            curDict["obsRobotClayCost"] = int(i[21])
            curDict["geoRobotOreCost"] = int(i[27])
            curDict["geoRobotObsCost"] = int(i[30])
        
            ins[idNum] = curDict
    return ins


def getInstructionScore(ins, debug=False):
    #Currently-owned resources
    ore = [0] * 25
    clay = [0] * 25
    obsidian = [0] * 25
    geode = [0] * 25
    
    #List of ordered pairs for each robot and what minute they were created at
    oreBot = [1] * 25
    clayBot = [0] * 25
    obsidianBot = [0] * 25
    geodeBot = [0] * 25

    #Creating a projection of each resource we'll have over the 24 min
    if debug:
        print("%8s %13s  %13s  %13s  %13s" %("Time", "Ore/Bots", "Clay/Bots", "Obsidian/Bots", "Geodes/Bots"))
    for i in range(1, 25):
        #If an ore bot was built, we have to subtract the required ore resources for crafting
        if oreBot[i] > oreBot[i-1]:
            ore[i] = ore[i-1] + oreBot[i-1]
            ore[i] -= ins["oreRobotCost"]
        else:
            ore[i] = ore[i-1] + oreBot[i]

        #If a clay bot was built, we have to subtract the required ore resources for crafting
        if clayBot[i] > clayBot[i-1]:
            clay[i] = clay[i-1] + clayBot[i-1]
            ore[i] -= ins["clayRobotCost"]
        else:
            clay[i] = clay[i-1] + clayBot[i]

        #If an obsidian bot was built, we have to subtract the required ore and clay resources for crafting
        if obsidianBot[i] > obsidianBot[i-1]:
            obsidian[i] = obsidian[i-1] + obsidianBot[i-1]
            ore[i] -= ins["obsRobotOreCost"]
            clay[i] -= ins["obsRobotClayCost"]
        else:
            obsidian[i] = obsidian[i-1] + obsidianBot[i]

        #If a geode bot was built, we have to subtract the required ore and obsidian resources for crafting
        if geodeBot[i] > geodeBot[i-1]:
            geode[i] = geode[i-1] + geodeBot[i-1]
            ore[i] -= ins["geoRobotOreCost"]
            obsidian[i] -= ins["geoRobotObsCost"]
        else:
            geode[i] = geode[i-1] + geodeBot[i]
        
        if debug:
            print("%8s %5d : %-5d  %5d : %-5d  %5d : %-5d  %5d : %-5d" %("t="+str(i), ore[i], oreBot[i], clay[i], clayBot[i], obsidian[i], obsidianBot[i], geode[i], geodeBot[i]))

    print()


def solution1():
    instructions = getInput()

    for k in instructions.keys():
        #geodes = recursiveGeodeCount(ins[k])
        #print("Instruction", k, "geodes:", geodes)
        print(k, ":", instructions[k])
        getInstructionScore(instructions[k])

    return


def solution2():
    return


print("Year 2022, Day 19 solution part 1:", solution1())
print("Year 2022, Day 19 solution part 2:", solution2())