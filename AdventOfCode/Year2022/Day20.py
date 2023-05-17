#https://adventofcode.com/2022/day/20
#https://adventofcode.com/2022/day/20#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d20_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d20_real.txt")


def getInput():
    '''Function to get the puzzle input from our input file.
    Return 1: List of ordered pairs for the initial sequence of values.
    '''
    numList = []

    with open(inFile, 'r') as f:
        index = 0
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            #Storing each value as well as it's original index in the list
            val = int(line)
            numList.append((val, index))
            index += 1

    return numList


def solution1():
    numList = getInput()
    #print("\tStarting Order:", numList)

    #Looping through each initial index of numbers to move
    for startIndex in range(0, len(numList)):
        #Finding the current index of the value that was initially at the starting index
        currIndex = 0
        for c in range(0, len(numList)):
            if numList[c][1] == startIndex:
                currIndex = c
                break

        #Finding the new index by adding the number value to the current index
        newIndex = currIndex
        if numList[currIndex][0] < 0 and currIndex + numList[currIndex][0] <= 0:
            newIndex += (numList[currIndex][0] - 1)
        elif numList[currIndex][0] > 0 and currIndex + numList[currIndex][0] >= len(numList) - 1:
            newIndex += (numList[currIndex][0] + 1) % len(numList)
        else:
            newIndex += numList[currIndex][0] % len(numList)

        newIndex = newIndex % len(numList)
        #print(numList[currIndex][0], "\tMoving from index", currIndex, "to", newIndex)

        if newIndex != currIndex:
            val = numList.pop(currIndex)
            numList.insert(newIndex, val)

    #outputStr = ""
    #for x in numList:
    #    outputStr = outputStr + str(x[0]) + ", "
    #print(outputStr)
    #print()

    #Finding the index where value 0 is
    offset = 0
    for x in range(0, len(numList)):
        if numList[x][0] == 0:
            offset = x
    #print("Zero found at index", offset)
    val1000 = numList[(1000+offset) % len(numList)][0]
    val2000 = numList[(2000+offset) % len(numList)][0]
    val3000 = numList[(3000+offset) % len(numList)][0]
    #print("1000th val:", val1000, "2000th val:", val2000, "3000th val:", val3000)
    return val1000 + val2000 + val3000


def solution2():
    return


print("Year 2022, Day 20 solution part 1:", solution1())
print("Year 2022, Day 20 solution part 2:", solution2())