#https://adventofcode.com/2022/day/20
#https://adventofcode.com/2022/day/20#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d20_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d20_real.txt")


def getInput():
    nums = []

    with open(inFile, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            nums.append(int(line))

    return nums


def solution1():
    og = getInput()
    nums = getInput()

    for i in range(0, len(og)):
        startIndex = nums.index(og[i])
        newIndex = nums[startIndex] + startIndex

        if newIndex < 0:
            newIndex -= 1
            while newIndex < 0:
                newIndex += (len(og))

        if newIndex >= len(og):
            while newIndex >= len(og):
                newIndex -= len(og)

        #newIndex = newIndex % len(og)

        if newIndex == 0:
            nums.pop(startIndex)
            #nums.append(og[i])
            nums.insert(0, og[i])
        elif newIndex == len(og)-1:
            nums.pop(startIndex)
            #nums.insert(0, og[i])
            nums.append(og[i])
        elif startIndex < newIndex:
            nums.pop(startIndex)
            nums.insert(newIndex, og[i])
        elif startIndex > newIndex:
            nums.pop(startIndex)
            nums.insert(newIndex+1, og[i])

    n1000 = (1000 % len(og)) + nums.index(0)
    if n1000 >= len(og):
        n1000 -= len(og)
    n2000 = (2000 % len(og)) + nums.index(0)
    if n2000 >= len(og):
        n2000 -= len(og)
    n3000 = (3000 % len(og)) + nums.index(0)
    if n3000 >= len(og):
        n3000 -= len(og)

    print("1000th:", nums[n1000], "2000th:", nums[n2000], "3000th:", nums[n3000])
    #not -7625
    #not -18805
    #not 11148
    #not 8925
    return nums[n1000] + nums[n2000] + nums[n3000]


def solution2():
    return


print("Year 2022, Day 20 solution part 1:", solution1())
print("Year 2022, Day 20 solution part 2:", solution2())