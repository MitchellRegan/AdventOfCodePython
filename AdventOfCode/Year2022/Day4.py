#https://adventofcode.com/2022/day/4
#https://adventofcode.com/2022/day/4#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d4_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d4_real.txt")

def solution1():
    sumTotal = 0
    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            groups = line.split(',')

            elf1 = groups[0].split('-')
            elf1[0] = int(elf1[0])
            elf1[1] = int(elf1[1])
            elf2 = groups[1].split('-')
            elf2[0] = int(elf2[0])
            elf2[1] = int(elf2[1])

            if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
                sumTotal += 1
            elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
                sumTotal += 1

    return sumTotal


def solution2():
    sumTotal = 0
    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            groups = line.split(',')

            elf1 = groups[0].split('-')
            min1 = int(elf1[0])
            max1 = int(elf1[1])
            elf2 = groups[1].split('-')
            min2 = int(elf2[0])
            max2 = int(elf2[1])

            if min1 <= min2 and min2 <= max1:
                sumTotal += 1
            elif min2 <= min1 and min1 <= max2:
                sumTotal += 1
            elif min1 <= max2 and max2 <= max1:
                sumTotal += 1
            elif min2 <= max1 and max1 <= max2:
                sumTotal += 1
            elif min1 <= min2 and max2 <= max1:
                sumTotal += 1
            elif min2 <= min1 and max1 <= max2:
                sumTotal += 1

    return sumTotal


print("Year 2022, Day 4 solution part 1:", solution1())
print("Year 2022, Day 4 solution part 2:", solution2())
