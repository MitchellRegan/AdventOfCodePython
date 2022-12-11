#https://adventofcode.com/2022/day/11
#https://adventofcode.com/2022/day/11#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d11_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d11_real.txt")

def solution1():
    sum = 0

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:

    return sum


def solution2():

    return 0


print("Year 2022, Day 11 solution part 1:", solution1())
print("Year 2022, Day 11 solution part 2:", solution2())