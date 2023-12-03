#https://adventofcode.com/2023/day/3
#https://adventofcode.com/2023/day/3#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if False:
    inFile = os.path.join(inFileDir, "InputTestFiles/d3_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d3_real.txt")


def getInput():
    input = []
    symbols = []
    with open(inFile, 'r') as f:
        lineNum = 0
        for line in f:
            line = line.replace('\n', '')
            line = line.replace('.', ' ')
            input.append(line)
            for s in range(0, len(line)):
                if line[s] is not " " and not line[s].isdigit():
                    symbols.append((s, lineNum))
            lineNum += 1

    return input, symbols


def getNum(line, ind):
    num = line[ind]
    for i in range(ind-1, -1, -1):
        if line[i].isdigit():
            num = line[i] + num
        else:
            break

    for i in range(ind+1, len(line)):
        if line[i].isdigit():
            num = num + line[i]
        else:
            break
        
    return int(num)


def solution1():
    sum = 0
    input, symbols = getInput()

    for s in symbols:
        addedNums = []
        row = s[1]
        col = s[0]

        #left
        if col > 0 and input[row][col-1].isdigit():
            newNum = getNum(input[row], col-1)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #top left
        if col > 0 and row > 0 and input[row-1][col-1].isdigit():
            newNum = getNum(input[row-1], col-1)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #top
        if row > 0 and input[row-1][col].isdigit():
            newNum = getNum(input[row-1], col)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #top right
        if col < len(input[row])-1 and row > 0 and input[row-1][col+1].isdigit():
            newNum = getNum(input[row-1], col+1)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #right
        if col < len(input[row])-1 and input[row][col+1].isdigit():
            newNum = getNum(input[row], col+1)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #bottom right
        if col < len(input[row])-1 and row < len(input)-1 and input[row+1][col+1].isdigit():
            newNum = getNum(input[row+1], col+1)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #bottom
        if row < len(input)-1 and input[row+1][col].isdigit():
            newNum = getNum(input[row+1], col)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #bottom left
        if col > 0 and row < len(input)-1 and input[row+1][col-1].isdigit():
            newNum = getNum(input[row+1], col-1)
            if newNum not in addedNums:
                addedNums.append(newNum)

        for num in addedNums:
            sum += int(num)
    return sum


def solution2():
    sum = 0
    input, symbols = getInput()

    for s in symbols:
        addedNums = []
        row = s[1]
        col = s[0]

        isGear = input[row][col] == '*'
        if not isGear:
            continue
        gearNumCount = 0

        #left
        if col > 0 and input[row][col-1].isdigit():
            newNum = getNum(input[row], col-1)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #top left
        if col > 0 and row > 0 and input[row-1][col-1].isdigit():
            newNum = getNum(input[row-1], col-1)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #top
        if row > 0 and input[row-1][col].isdigit():
            newNum = getNum(input[row-1], col)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #top right
        if col < len(input[row])-1 and row > 0 and input[row-1][col+1].isdigit():
            newNum = getNum(input[row-1], col+1)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #right
        if col < len(input[row])-1 and input[row][col+1].isdigit():
            newNum = getNum(input[row], col+1)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #bottom right
        if col < len(input[row])-1 and row < len(input)-1 and input[row+1][col+1].isdigit():
            newNum = getNum(input[row+1], col+1)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #bottom
        if row < len(input)-1 and input[row+1][col].isdigit():
            newNum = getNum(input[row+1], col)
            if newNum not in addedNums:
                addedNums.append(newNum)
        #bottom left
        if col > 0 and row < len(input)-1 and input[row+1][col-1].isdigit():
            newNum = getNum(input[row+1], col-1)
            if newNum not in addedNums:
                addedNums.append(newNum)

        if isGear and len(addedNums) == 2:
            sum += addedNums[0] * addedNums[1]

    return sum


print("Year 2023, Day 3 solution part 1:", solution1())
print("Year 2023, Day 3 solution part 2:", solution2())