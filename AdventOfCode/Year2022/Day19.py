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


class BuildState:
    '''A class for how many resources, robots, and remaining minutes for a given state.
    '''
    def __init__(self, instruction_, copyState_=None):
        '''Constructor for this build state.
        - copyState_: Reference to another BuildState class to make a shallow copy.
        '''
        #If there wasn't a valid state given to copy, we make a brand new state
        if copyState_  == None or not isinstance(copyState_, BuildState):
            self.instruction = instruction_
            self.resources = [0, 0, 0, 0]
            self.bots = [1, 0, 0, 0]
            self.time = 24
        #If we were given a build state, we make a shallow copy of its bots, resources, and time
        else:
            self.instruction = instruction_
            self.resources = [x for x in copyState_.resources]
            self.bots = [x for x in copyState_.bots]
            self.time = 0 + copyState_.time


    def generateResources(self):
        '''Method to have each existing bot add to our resource list.
        '''
        self.resources[0] += self.bots[0]
        self.resources[1] += self.bots[1]
        self.resources[2] += self.bots[2]
        self.resources[3] += self.bots[3]
        self.time -= 1


    def canBuildBot(self, bot_=None):
        '''Mehod to check if this state can build any of the available bots: None, "ore", "clay", "obsidian", "geode"
        '''
        if bot_ not in [None, "ore", "clay", "obsidian", "geode"]:
            return False

        if bot_ == "ore":
            return self.resources[0] >= self.instruction["oreRobotCost"]
        elif bot_ == "clay":
            return self.resources[0] >= self.instruction["clayRobotCost"]
        elif bot_ == "obsidian":
            return self.resources[0] >= self.instruction["obsRobotOreCost"] and self.resources[1] >= self.instruction["obsRobotClayCost"]
        elif bot_ == "geode":
            return self.resources[0] >= self.instruction["geoRobotOreCost"] and self.resources[2] >= self.instruction["geoRobotObsCost"]
        else:
            return True


    def buildBot(self, bot_=None):
        '''Mehod to build any of the available bots: None, "ore", "clay", "obsidian", "geode"
        '''
        if bot_ not in [None, "ore", "clay", "obsidian", "geode"]:
            return False

        #Updating the number of resources available
        self.generateResources()

        if bot_ == "ore":
            self.resources[0] -= self.instruction["oreRobotCost"]
        elif bot_ == "clay":
            self.resources[0] -= self.instruction["clayRobotCost"]
        elif bot_ == "obsidian":
            self.resources[0] -= self.instruction["obsRobotOreCost"]
            self.resources[1] -= self.instruction["obsRobotClayCost"]
        elif bot_ == "geode":
            self.resources[0] -= self.instruction["geoRobotOreCost"]
            self.resources[2] -= self.instruction["geoRobotObsCost"]


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


#Value used in recursiveScore to keep track of the earliest minute that a geode bot (index 0) or obsidian bot (index 1) are made.
#States that can't build these bots by this time will early exit
bestBotTimes = [0,0,0]
def recursiveScore(instruction_, resources_=[0,0,0,0], bots_=[1,0,0,0], time_=24):
    '''Recursive function to find the largest amount of geodes that can be generated from the given instruction set.
    - instruction_: dictionary for the building costs of each robot.
    - resources_: list for the number of resources currently available. Index 0 = ore, 1 = clay, 2 = obsidian, 3 = geodes.
    - bots_: list for the number of bots that have been built. Index 0 = ore bots, 1 = clay bots, 2 = obsidian bots, 3 = geode bots.
    - time_: the current number of minutes that are remaining. Once it hits zero, the amount of geode resources available are returned.
    - returns: The number of geode resources available once 24 minutes have passed.
    '''
    #print("Time:", time_, "Resources:", resources_, "Bots:", bots_)
    #Making sure to reset the fastest geode time to 24min
    if time_ == 24:
        bestBotTimes[0] = 0
        bestBotTimes[1] = 0
        bestBotTimes[2] = 0
        print(bestBotTimes)

    #If the current time is less than the current best geode time and we don't have a geode bot yet, we exit
    if (time_ < bestBotTimes[0] and bots_[3] == 0) or (time_ < bestBotTimes[1] and bots_[2] == 0) or (time_ < bestBotTimes[2] and bots_[1] == 0):
        return resources_[3]
    #Once the recursion is out of time, we return the number of geodes that are currently available
    if time_ == 0:
        return resources_[3]

    #Tracking the max number of geodes found from any recursions
    maxGeodes = 0

    #If we can make a geode bot, we try that for the next recursion
    if instruction_["geoRobotOreCost"] <= resources_[0] and instruction_["geoRobotObsCost"] <= resources_[2]:
        newResources = [x for x in resources_]
        newBots = [x for x in bots_]
        #Removing the ore and obsidian used to create the new bot
        newResources[0] -= instruction_["geoRobotOreCost"]
        newResources[2] -= instruction_["geoRobotObsCost"]
        #Updating the resources to include newly generated ones from the existing bots (before the new one is made)
        newResources[0] += newBots[0]
        newResources[1] += newBots[1]
        newResources[2] += newBots[2]
        newResources[3] += newBots[3]
        #Adding the new geode bot to our roster
        newBots[3] += 1
        #Keeping track of the timestamp if this geode bot is made earlier than any other state
        if newBots[3] == 1 and time_ > bestBotTimes[0]:
            bestBotTimes[0] = time_
        #Passing this new state down to the next recursion level
        numGeodes = recursiveScore(instruction_, newResources, newBots, time_-1)
        if numGeodes > maxGeodes:
            maxGeodes = numGeodes
    #If we can make an obsidian bot, we try that for the next recursion
    if instruction_["obsRobotOreCost"] <= resources_[0] and instruction_["obsRobotClayCost"] <= resources_[1]:
        newResources = [x for x in resources_]
        newBots = [x for x in bots_]
        #Removing the ore and clay used to create the new bot
        newResources[0] -= instruction_["obsRobotOreCost"]
        newResources[1] -= instruction_["obsRobotClayCost"]
        #Updating the resources to include newly generated ones from the existing bots (before the new one is made)
        newResources[0] += newBots[0]
        newResources[1] += newBots[1]
        newResources[2] += newBots[2]
        newResources[3] += newBots[3]
        #Adding the new obsidian bot to our roster
        newBots[2] += 1
        #Keeping track of the timestamp if this obsidian bot is made earlier than any other state
        if newBots[2] == 1 and time_ > bestBotTimes[1]:
            bestBotTimes[1] = time_
        #Passing this new state down to the next recursion level
        numGeodes = recursiveScore(instruction_, newResources, newBots, time_-1)
        if numGeodes > maxGeodes:
            maxGeodes = numGeodes
    #If we can make a clay bot, we try that for the next recursion
    if instruction_["clayRobotCost"] <= resources_[0]:
        newResources = [x for x in resources_]
        newBots = [x for x in bots_]
        #Removing the ore used to create the new bot
        newResources[0] -= instruction_["clayRobotCost"]
        #Updating the resources to include newly generated ones from the existing bots (before the new one is made)
        newResources[0] += newBots[0]
        newResources[1] += newBots[1]
        newResources[2] += newBots[2]
        newResources[3] += newBots[3]
        #Adding the new clay bot to our roster
        newBots[1] += 1
        #Keeping track of the timestamp if this obsidian bot is made earlier than any other state
        if newBots[1] == 1 and time_ > bestBotTimes[2]:
            bestBotTimes[2] = time_
        #Passing this new state down to the next recursion level
        numGeodes = recursiveScore(instruction_, newResources, newBots, time_-1)
        if numGeodes > maxGeodes:
            maxGeodes = numGeodes
    #If we can make an ore bot, we try that for the next recursion
    if instruction_["oreRobotCost"] <= resources_[0]:
        newResources = [x for x in resources_]
        newBots = [x for x in bots_]
        #Removing the ore used to create the new bot
        newResources[0] -= instruction_["oreRobotCost"]
        #Updating the resources to include newly generated ones from the existing bots (before the new one is made)
        newResources[0] += newBots[0]
        newResources[1] += newBots[1]
        newResources[2] += newBots[2]
        newResources[3] += newBots[3]
        #Adding the new ore bot to our roster
        newBots[0] += 1
        #Passing this new state down to the next recursion level
        numGeodes = recursiveScore(instruction_, newResources, newBots, time_-1)
        if numGeodes > maxGeodes:
            maxGeodes = numGeodes
    #Now we do a recursion where no bots are built
    if True:
        newResources = [x for x in resources_]
        newBots = [x for x in bots_]
        #Updating the resources to include newly generated ones from the existing bots (before the new one is made)
        newResources[0] += newBots[0]
        newResources[1] += newBots[1]
        newResources[2] += newBots[2]
        newResources[3] += newBots[3]
        #Passing this new state down to the next recursion level
        numGeodes = recursiveScore(instruction_, newResources, newBots, time_-1)
        if numGeodes > maxGeodes:
            maxGeodes = numGeodes

    #Returning the largest number of geodes found from any recursion
    #print(maxGeodes)
    return maxGeodes


def solution1():
    instructions = getInput()
    totalScore = 0
    for k in instructions.keys():
        #geodes = recursiveGeodeCount(ins[k])
        #print("Instruction", k, "geodes:", geodes)
        print(k, ":", instructions[k])
        score = recursiveScore(instructions[k])
        print("\tScore:", score)
        print("\t\tFastest Geode Time:", 24-bestBotTimes[0])
        print("\t\tFastest Obsidian Time:", 24-bestBotTimes[1])
        print("\t\tFastest Clay Time:", 24-bestBotTimes[2])
        totalScore += score * k
        #totalScore += getInstructionScore(instructions[k]) * k

    return totalScore


def solution2():
    return


print("Year 2022, Day 19 solution part 1:", solution1())
print("Year 2022, Day 19 solution part 2:", solution2())