#https://adventofcode.com/2023/day/15
#https://adventofcode.com/2023/day/15#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d15_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d15_real.txt")


def getInput():
    input = []

    with open(inFile, 'r') as f:
        for line in f:
            input = line.replace('\n','').split(',')
    return input


def hashFunction(ins_:str)->int:
    value = 0
    for c in ins_:
        value += ord(c)
        value *= 17
        value = value % 256
    return value


def solution1():
    input = getInput()

    total = 0
    for instruction in input:
        total += hashFunction(instruction)

    return total


def solution2():
    input = getInput()
    
    #Dictionary for boxes and their contents
    #   key: Box ID # from taking the hash function on each instruction
    #   value: List of ordered pairs for (lense ID, lense focus power)
    boxes = {}

    for instruction in input:
        #Instruction to store a lense in a box
        if '=' in instruction:
            label = instruction.split('=')[0]
            lense = int(instruction.split('=')[1])
            box = hashFunction(label)

            if box in boxes.keys():
                found = False
                for item in range(0, len(boxes[box])):
                    if boxes[box][item][0] == label:
                        boxes[box][item][1] = lense
                        found = True
                        break
                if not found:
                    boxes[box].append([label,lense])
            else:
                boxes[box] = [[label,lense]]
        #Instruction to retrieve a lense from a box
        elif '-' in instruction:
            label = instruction[:-1]
            box = hashFunction(label)

            if box in boxes.keys():
                foundIndex = None
                for item in range(0, len(boxes[box])):
                    if boxes[box][item][0] == label:
                        foundIndex = item
                        break
                if foundIndex is not None:
                    boxes[box].pop(foundIndex)

    #Adding the focusing power of lenses
    fp = 0
    for k in boxes.keys():
        for i in range(0, len(boxes[k])):
            lensePower = (k+1) * (i+1) * boxes[k][i][1]
            fp += lensePower

    return fp


print("Year 2023, Day 15 solution part 1:", solution1())
print("Year 2023, Day 15 solution part 2:", solution2())