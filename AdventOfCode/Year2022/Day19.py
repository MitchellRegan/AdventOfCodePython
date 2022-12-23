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


def recursiveGeodeCount(costs, resources=[0,0,0,0], bots=[1,0,0,0], turns=24):
    '''Recursive method to find the maximum number of geodes that can be made for a given set of instructions.
    - costs: Dictionary containing the construction costs for each bot.
    - resources: List of ints representing the number of resources currently posessed. In order they are: Ore, Clay, Obsidian, Geodes.
    - bots: List of ints representing the number of bots currently posessed. In order they are: Ore, Clay, Obsidian, Geode.
    - turns: The number of turns left to produce geodes
    Returns: Int for the number of geodes created when "turns" reaches 0.
    '''
    #First check if we're out of turns. If so, we return the number of geodes that have been created
    if turns == 0:
        return resources[3]

    #Int to track the largest number of geodes created from any recursive calls
    mostGeodes = 0

    #If we can make an ore bot, we try that
    if resources[0] >= costs["oreRobotCost"]:
        newResources = [x for x in resources]
        newResources[0] -= costs["oreRobotCost"]

        newResources[0] += bots[0]
        newResources[1] += bots[1]
        newResources[2] += bots[2]
        newResources[3] += bots[3]

        newBots = [x for x in bots]
        newBots[0] += 1
        numGeode = recursiveGeodeCount(costs, newResources, newBots, turns-1)
        if numGeode > mostGeodes:
            mostGeodes = numGeode

    #If we can make a clay bot, we try that
    if resources[0] >= costs["clayRobotCost"]:
        newResources = [x for x in resources]
        newResources[0] -= costs["clayRobotCost"]

        newResources[0] += bots[0]
        newResources[1] += bots[1]
        newResources[2] += bots[2]
        newResources[3] += bots[3]

        newBots = [x for x in bots]
        newBots[1] += 1
        numGeode = recursiveGeodeCount(costs, newResources, newBots, turns-1)
        if numGeode > mostGeodes:
            mostGeodes = numGeode

    #If we can make an obsidian bot, we try that
    if resources[0] >= costs["obsRobotOreCost"] and resources[1] >= costs["obsRobotClayCost"]:
        newResources = [x for x in resources]
        newResources[0] -= costs["obsRobotOreCost"]
        newResources[1] -= costs["obsRobotClayCost"]

        newResources[0] += bots[0]
        newResources[1] += bots[1]
        newResources[2] += bots[2]
        newResources[3] += bots[3]

        newBots = [x for x in bots]
        newBots[2] += 1
        numGeode = recursiveGeodeCount(costs, newResources, newBots, turns-1)
        if numGeode > mostGeodes:
            mostGeodes = numGeode

    #If we can make a geode bot, we try that
    if resources[0] >= costs["geoRobotOreCost"] and resources[2] >= costs["geoRobotObsCost"]:
        newResources = [x for x in resources]
        newResources[0] -= costs["geoRobotOreCost"]
        newResources[2] -= costs["geoRobotObsCost"]

        newResources[0] += bots[0]
        newResources[1] += bots[1]
        newResources[2] += bots[2]
        newResources[3] += bots[3]

        newBots = [x for x in bots]
        newBots[3] += 1
        numGeode = recursiveGeodeCount(costs, newResources, newBots, turns-1)
        if numGeode > mostGeodes:
            mostGeodes = numGeode

    #Now we try doing nothing and see if that generates more resources
    newResources = [x for x in resources]
    newResources[0] += bots[0]
    newResources[1] += bots[1]
    newResources[2] += bots[2]
    newResources[3] += bots[3]
    newBots = [x for x in bots]

    numGeode = recursiveGeodeCount(costs, newResources, newBots, turns-1)
    if numGeode > mostGeodes:
        mostGeodes = numGeode

    return mostGeodes


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
        geodes = recursiveGeodeCount(ins[k])
        print("Instruction", k, "geodes:", geodes)

    return


def solution2():
    return


print("Year 2022, Day 19 solution part 1:", solution1())
print("Year 2022, Day 19 solution part 2:", solution2())