#https://adventofcode.com/2023/day/5
#https://adventofcode.com/2023/day/5#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d5_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d5_real.txt")


def getInput():
    input = {}
    seeds = []

    with open(inFile, 'r') as f:
        lineNum = 0
        conversionKey = None
        ranges = []

        for line in f:
            if lineNum == 0:
                line = line.split(' ')[1:]
                seeds = [int(x) for x in line]
            elif lineNum == 1:
                conversionKey = None
            #saving the conversion key after all ranges are found
            elif line == '\n':
                input[conversionKey] = ranges
                conversionKey = None
                ranges = []
            #getting conversion key
            elif not line[0].isdigit():
                line = line.split(' ')[0].split('-')
                conversionKey = (line[0], line[2])
            #getting range values
            else:
                line = line.split(' ')
                ranges.append((int(line[0]), int(line[1]), int(line[2])))

            lineNum += 1

        if conversionKey is not None:
            input[conversionKey] = ranges

    return input, seeds


def solution1():
    input, seeds = getInput()
    order = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    lowestLocNum = None

    #iterating through each seed alone
    for seed in seeds:
        #print("Seed", seed)
        locNum = seed

        #iterating through the order of steps
        for step in range(0, len(order)-1):
            #print("Seed", seed, "order:", order[step], "to", order[step+1])
            conversionKey = (order[step], order[step+1])

            #Iterating through the range values for this step
            for r in input[conversionKey]:
                #print('\tRange:', r)
                #print("\t", order[step], "range is", r[1], "-", r[1]+r[2]-1)
                #print("\t", order[step+1], "range is", r[0], "-", r[0]+r[2]-1)

                if locNum >= r[1] and locNum <= r[1]+r[2]-1:
                    newNum = r[0] + (locNum - r[1])
                    #print("\t\t", order[step], locNum, "=", order[step+1], newNum)
                    locNum = newNum
                    break

            #If no matching ranges found, the location number doesn't change
            
        #Getting the smallest location number available
        if lowestLocNum is None or locNum < lowestLocNum:
            lowestLocNum = locNum

    return lowestLocNum


def solution2():
    input, seeds = getInput()
    order = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    lowestLocNum = None

    #Converting the individual seed values into ranges
    newSeeds = []
    for i in range(0, len(seeds), 2):
        newSeeds.append((seeds[i], seeds[i]+seeds[i+1]-1))


    for sr in newSeeds:
        index = sr[0]
        #Jumping indexes based on a percentage of the difference between the seed range start and end
        jump = int((sr[1] - sr[0]) * 0.01)
        if jump == 0:
            jump = 1

        #Keeping track of the previous iteration's location number
        #Use this to check if our end values are increasing or decreasing
        prevIndex = None
        prevLocNum = None
        tempJump = jump

        #Looping until our seed index goes out of the current seed range
        while index <= sr[1]:
            locNum = index

            #iterating through the order of steps
            for step in range(0, len(order)-1):
                conversionKey = (order[step], order[step+1])

                #Iterating through the range values for this step
                for r in input[conversionKey]:
                    if locNum >= r[1] and locNum <= r[1]+r[2]-1:
                        newNum = r[0] + (locNum - r[1])
                        #print("\t\t", order[step], locNum, "=", order[step+1], newNum)
                        locNum = newNum
                        break
                #If no matching ranges found, the location number doesn't change
                
            #If this is the first iteration of this seed range, we need to set the starting values
            if lowestLocNum is None or prevIndex is None:
                prevLocNum = locNum
                prevIndex = index
                index += jump
            #If the location value increased linearly with the jump increase in seed index, we can keep jumping forward
            elif locNum - prevLocNum == tempJump or index == prevIndex+1:
                prevLocNum = locNum
                prevIndex = index

                #If our index is currently at the max, we force a break
                if index == sr[1]:
                    index += tempJump
                #If our index is below the max range, we jump forward up to the max
                else:
                    index += tempJump
                    if index > sr[1]:
                        index = sr[1]

                if tempJump != jump:
                    tempJump = jump
            #If the location number's value didn't increase linearly with the jump, we
            #roll the current index back to the halfway point from the last time it did increase linearly
            else:
                #Rolling the current index back to a minimum of prevIndex+1
                placeholder = index
                index = prevIndex + (index - prevIndex)//2
                if index <= prevIndex:
                    index = prevIndex + 1

                tempJump = index - prevIndex
                    
            #Getting the smallest location number available
            if lowestLocNum is None or locNum < lowestLocNum:
                lowestLocNum = locNum

    return lowestLocNum


print("Year 2023, Day 5 solution part 1:", solution1())
print("Year 2023, Day 5 solution part 2:", solution2())