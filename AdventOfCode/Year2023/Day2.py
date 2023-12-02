#https://adventofcode.com/2023/day/2
#https://adventofcode.com/2023/day/2#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if False:
    inFile = os.path.join(inFileDir, "InputTestFiles/d2_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d2_real.txt")


def solution1():
    cubes = {"red":12, "green":13, "blue":14}
    sum = 0
    with open(inFile, 'r') as f:
        lineNum = 1
        for line in f:
            line = line.split(": ")[1]
            pulls = line.split("; ")
            validLine = True
            for p in pulls:
                p = p.replace(",", "")
                p = p.replace("\n", "")
                p = p.split(" ")

                for i in range(1, len(p), 2):
                    if cubes[p[i]] < int(p[i-1]):
                        validLine = False
                        break
            
            if validLine:
                sum += lineNum
            lineNum += 1

    return sum


def solution2():
    cubes = {"red":12, "green":13, "blue":14}
    sum = 0
    with open(inFile, 'r') as f:
        lineNum = 1
        for line in f:
            line = line.split(": ")[1]
            line = line.replace(",", "")
            line = line.replace(";", "")
            line = line.replace("\n", "")
            line = line.split(" ")
            
            red = -1
            green = -1
            blue = -1

            for i in range(1, len(line), 2):
                if line[i] == "red":
                    if red < int(line[i-1]):
                        red = int(line[i-1])
                elif line[i] == "green":
                    if green < int(line[i-1]):
                        green = int(line[i-1])
                if line[i] == "blue":
                    if blue < int(line[i-1]):
                        blue = int(line[i-1])
                        
            power = red * blue * green
            sum += power
            lineNum += 1

    return sum


print("Year 2023, Day 2 solution part 1:", solution1())
print("Year 2023, Day 2 solution part 2:", solution2())