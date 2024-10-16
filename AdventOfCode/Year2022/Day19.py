#https://adventofcode.com/2022/day/19
#https://adventofcode.com/2022/day/19#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = os.path.join(inFileDir, "InputTestFiles/d19_test.txt")
#inFile = os.path.join(inFileDir, "InputRealFiles/d19_real.txt")


def getInput():
    inpt = []
    
    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            bpNum = int(line[1][:-1])
            oreBotOreCost = int(line[6])
            clayBotOreCost = int(line[12])
            obsBotOreCost = int(line[18])
            obsBotClayCost = int(line[21])
            geoBotOreCost = int(line[27])
            geoBotObsCost = int(line[30])
            inpt.append((bpNum, oreBotOreCost, clayBotOreCost, obsBotOreCost, obsBotClayCost, geoBotOreCost, geoBotObsCost))
            
    return inpt

        
def solution1():
    inpt = getInput()
    bpNum, oreBotOreCost, clayBotOreCost, obsBotOreCost, obsBotClayCost, geoBotOreCost, geoBotObsCost = [0,0,0,0,0,0,0]
    #timeTilMostGeodes = [None, None]#time stamp when the reccord amount of geodes were found, and the record amount of geodes found
    #bestGeoTime = (24,0)
    #print("Best Geo Time START:", bestGeoTime)
    bestGeo, bestTime = [0, 0]
    print("Best Geo", bestGeo, "Best Time:", bestTime, "    START")

    def getMostGeodes(t:int, ore:int, clay:int, obs:int, geo:int, oreBot:int, clayBot:int, obsBot:int, geoBot:int)->int:
        '''Recursive function that finds the largest number of geodes that can be found with the starting bot state and time.'''
        newT = t-1
        newOre = ore + oreBot
        newClay = clay + clayBot
        newObs = obs + obsBot
        newGeo = geo + geoBot
        #print("Time:", newT, "  ore:", (newOre, oreBot), "  clay:", (newClay, clayBot), "  obs:", (newObs, obsBot), "  geo:", (newGeo, geoBot))
        
        #Recursion break
        if newT == 0:
            return geo
        
        #Checking for early-exits from recursion
        nonlocal bestGeo
        nonlocal bestTime
        #print("Best Geo", bestGeo, "Best Time:", bestTime, "    RECURSIVE")
        if newGeo > bestGeo and newT >= bestTime:
            #print("\tUpdating Best Geo:", newGeo, "    Best Time:", newT)
            bestGeo = newGeo
            bestTime = newT
        elif newT < bestTime-2 and newGeo < bestGeo:
            #print("Not efficient enough. Best Geo:", bestGeo, "  Best Time:", bestTime)
            return newGeo

        best = newGeo
        #Building a geode bot if possible
        if newOre >= geoBotOreCost and newObs >= geoBotObsCost:
            #print("======== GeoBot Ore Cost:", geoBotOreCost, "    Obsidian Cost:", geoBotObsCost)
            best = max(best, getMostGeodes(newT, newOre-geoBotOreCost, newClay, newObs-geoBotObsCost, newGeo, oreBot+0, clayBot+0, obsBot+0, geoBot+1))
        #Building an obsidian bot if possible
        if newOre >= obsBotOreCost and newClay >= obsBotClayCost:
            best = max(best, getMostGeodes(newT, newOre-obsBotOreCost, newClay-obsBotClayCost, newObs, newGeo, oreBot+0, clayBot+0, obsBot+1, geoBot+0))
        #Building a clay bot if possible
        if newOre >= clayBotOreCost:
            best = max(best, getMostGeodes(newT, newOre-clayBotOreCost, newClay, newObs, newGeo, oreBot+0, clayBot+1, obsBot+0, geoBot+0))
        #Building an ore bot if possible
        if newOre >= oreBotOreCost:
            best = max(best, getMostGeodes(newT, newOre-oreBotOreCost, newClay, newObs, newGeo, oreBot+1, clayBot+0, obsBot+0, geoBot+0))
        #Skipping any building this update
        best = max(best, getMostGeodes(newT, newOre, newClay, newObs, newGeo, oreBot+0, clayBot+0, obsBot+0, geoBot+0))
        return best
            
    ans = 0
    for line in inpt:
        print(line)
        #line = [x for x in line]
        #line.append(0)
        #line.append(0)
        #bpNum, oreBotOreCost, clayBotOreCost, obsBotOreCost, obsBotClayCost, geoBotOreCost, geoBotObsCost, bestTime, bestGeo = line
        bpNum, oreBotOreCost, clayBotOreCost, obsBotOreCost, obsBotClayCost, geoBotOreCost, geoBotObsCost = line
        bestGeo, bestTime = [0, 0]
        print("Best Geo", bestGeo, "Best Time:", bestTime, "    LOOP")
        numGeode = getMostGeodes(24, 0, 0, 0, 0, 1, 0, 0, 0)
        ans += numGeode * bpNum
        print("Blueprint", bpNum, "max geodes =", numGeode)
    return ans


def solution2():
    return


print("Year 2022, Day 19 solution part 1:", solution1())
print("Year 2022, Day 19 solution part 2:", solution2())