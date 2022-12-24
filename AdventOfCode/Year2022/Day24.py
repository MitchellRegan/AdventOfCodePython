#https://adventofcode.com/2022/day/24
#https://adventofcode.com/2022/day/24#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = os.path.join(inFileDir, "InputTestFiles/d24_test.txt")
#inFile = os.path.join(inFileDir, "InputRealFiles/d24_real.txt")

def getInput():
    map = []
    #Dict to store all of the storms found. The key is an int for the ID, and the value is [row, col, direction]
    stormID = 0
    storms = {}

    with open(inFile, 'r') as f:
        row = 0
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            for col in range(0, len(line)):
                if line[col] == '>':
                    storms[stormID] = [row, col, 'R']
                    stormID += 1
                elif line[col] == 'V':
                    storms[stormID] = [row, col, 'D']
                    stormID += 1
                elif line[col] == '<':
                    storms[stormID] = [row, col, 'L']
                    stormID += 1
                elif line[col] == '^':
                    storms[stormID] = [row, col, 'U']
                    stormID += 1

            row += 1
            map.append(line)

    start = (0, 1)
    exit = (len(map)-1, len(map[0])-2)
    return [map, start, exit, storms]


def solution1():
    map, start, exit, storms = getInput()
    print("Start:", start, "End:", exit)
    for row in map:
        print(row)
    for s in storms.keys():
        print(s, ":", storms[s])
    return


def solution2():
    return


print("Year 2022, Day 24 solution part 1:", solution1())
print("Year 2022, Day 24 solution part 2:", solution2())