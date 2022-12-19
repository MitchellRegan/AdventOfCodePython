#https://adventofcode.com/2022/day/19
#https://adventofcode.com/2022/day/19#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = os.path.join(inFileDir, "InputTestFiles/d19_test.txt")
#inFile = os.path.join(inFileDir, "InputRealFiles/d19_real.txt")


def getInstructionScore(ins):
    #Currently-owned resources
    ore = 0
    clay = 0
    obsidian = 0
    geodes = 0
    
    #Currently-owned bots
    oreBots = 1
    clayBots = 0
    obsBots = 0
    geodeBots = 0
    
    #Can only do 24 iterations to get max geodes
    for i in range(0, 24):
        #List to store the bot to make
        makeBot = [0,0,0,0]
        #Prioritize making a geode bot first
        if ore >= ins["geoRobotOreCost"] and obsidian >= ins["geoRobotObsCost"]:
            ore -= ins["geoRobotOreCost"]
            obsidian -= ins["geoRobotObsCost"]
            makeBot[3] = 1
        #Next prioritize making an obsidian bot
        elif ore >= ins["obsRobotOreCost"] and clay >= ins["obsRobotClayCost"]:
            ore -= ins["obsRobotOreCost"]
            clay -= ins["obsRobotClayCost"]
            makeBot[2] = 1
        #After that prioritize making clay bots
        elif ore >= ins["clayRobotCost"]:
            ore -= ins["clayRobotCost"]
            makeBot[1] = 1
        #Finally make more ore bots
        elif ore >= ins["oreRobotCost"]:
            ore -= ins["oreRobotCost"]
            makeBot[0] = 1
            
        #Increase our resource amounts gathered from bots
        ore += oreBots
        clay += clayBots
        obsidian += obsBots
        geodes += geodeBots
        
        #Increase our number of bots
        oreBots += makeBot[0]
        clayBots += makeBot[1]
        obsBots += makeBot[2]
        geodeBots += makeBot[3]
        
    print("Ore Bots:", oreBots, "Clay Bots:", clayBots, "Obsidian Bots:", obsBots, "Geode Bots:", geodeBots)
    return geodes


def solution1():
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
        
    for k in ins.keys():
        geodes = getInstructionScore(ins[k])
        print("Instruction", k, "score:", geodes)

    return


def solution2():
    return


print("Year 2022, Day 19 solution part 1:", solution1())
print("Year 2022, Day 19 solution part 2:", solution2())