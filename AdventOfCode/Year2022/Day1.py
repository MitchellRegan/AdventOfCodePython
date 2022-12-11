#https://adventofcode.com/2022/day/1
#https://adventofcode.com/2022/day/1#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d1_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d1_real.txt")

def solution1():
    maxSum = 0
    curSum = 0

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            #If the line is empty (just \n) we check the current sum against the max
            if line == '\n':
                if maxSum < curSum:
                    maxSum = curSum
                curSum = 0
            # Otherwise we keep adding the line's amount to the current sum
            else:
                curSum += int(line)
    # Doing one last check since the end of file isn't a "new line"
    if maxSum < curSum:
        maxSum = curSum

    return maxSum


def solution2():
    sumList = []
    curSum = 0

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            #If the line is empty (just \n) we add the sum to the sum list
            if line == '\n':
                sumList.append(curSum)
                curSum = 0
            # Otherwise we keep adding the line's amount to the current sum
            else:
                curSum += int(line)
    # Adding the last sum, since the end of file isn't seen as a "new line"
    sumList.append(curSum)

    #Finding the sum of the 3 highest values
    sumList.sort(reverse=True)
    return sum(sumList[:3])


print("Year 2022, Day 1 solution part 1:", solution1())
print("Year 2022, Day 1 solution part 2:", solution2())