#https://adventofcode.com/2022/day/3
#https://adventofcode.com/2022/day/3#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d3_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d3_real.txt")

def solution1():
    sumTotal = 0

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            #Split the line in half
            left = line[:len(line)//2]
            right = line[len(line)//2:]

            #Find the char that's identical in both
            for c in left:
                if c in right:
                    #add the char's value to the sum total
                    val = ord(c)
                    if val >= 65 and val <= 90: #upper case
                        val -= 38
                    elif val >= 97 and val <= 122: #lower case
                        val -= 96

                    sumTotal += val
                    break
    return sumTotal


def solution2():
    sumTotal = 0
    currentGroup = []

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            #Grouping together every 3 lines
            currentGroup.append(line)

            #once there are 3 lines in the group, we look for a common char
            if len(currentGroup) == 3:
                for c in currentGroup[0]:
                    if c in currentGroup[1] and c in currentGroup[2]:
                        #Finding the value for the char
                        val = ord(c)
                        if val >= 65 and val <= 90: #upper case, values 27-52
                            val -= 38
                        elif val >= 97 and val <= 122: #lower case, values 1-26
                            val -= 96
                        sumTotal += val
                        break
                #Clearing the group to make room for the next one
                currentGroup = []

    return sumTotal


print("Year 2022, Day 3 solution part 1:", solution1())
print("Year 2022, Day 3 solution part 2:", solution2())
