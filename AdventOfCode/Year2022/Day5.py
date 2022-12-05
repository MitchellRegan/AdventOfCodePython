#https://adventofcode.com/2022/day/5
#https://adventofcode.com/2022/day/5#part2

#inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2022\\InputTestFiles\\d5_test.txt"
inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2022\\InputRealFiles\\d5_real.txt"

def solution1():
    readMode = 0
    boxGrid = {}
    instructions = []

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            #If the line is empty, we switch modes
            if line is '\n':
                readMode = 1
            else:
                # Getting initial input
                if readMode == 0:
                    #If the first char is not '1' we're getting boxes
                    if line[1] is not '1':
                        str = ""
                        i = 1
                        col = 1
                        while i < len(line):
                            if line[i] != ' ':
                                if col in boxGrid.keys():
                                    boxGrid[col] = boxGrid[col] + line[i]
                                else:
                                    boxGrid[col] = line[i]
                            i += 4
                            col += 1

                # Reading instructions
                elif readMode == 1:
                    ins = line.split(' ')
                    instructions.append((int(ins[1]), int(ins[3]), int(ins[5])))

    
    for i in instructions:
        fromBox = i[1]
        toBox = i[2]
        num = i[0]

        for j in range(num):
            str = boxGrid[i[1]][0]
            boxGrid[i[1]] = boxGrid[i[1]][1:]
            boxGrid[i[2]] = str + boxGrid[i[2]]
    
    answer = ""
    for b in sorted(boxGrid.keys()):
        answer += boxGrid[b][0]
    return answer


def solution2():
    readMode = 0
    boxGrid = {}
    instructions = []

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            #If the line is empty, we switch modes
            if line is '\n':
                readMode = 1
            else:
                # Getting initial input
                if readMode == 0:
                    #If the first char is not '1' we're getting boxes
                    if line[1] is not '1':
                        str = ""
                        i = 1
                        col = 1
                        while i < len(line):
                            if line[i] != ' ':
                                if col in boxGrid.keys():
                                    boxGrid[col] = boxGrid[col] + line[i]
                                else:
                                    boxGrid[col] = line[i]
                            i += 4
                            col += 1

                # Reading instructions
                elif readMode == 1:
                    ins = line.split(' ')
                    instructions.append((int(ins[1]), int(ins[3]), int(ins[5])))

    
    for i in instructions:
        fromBox = i[1]
        toBox = i[2]
        num = i[0]

        str = boxGrid[i[1]][0:num]
        boxGrid[i[1]] = boxGrid[i[1]][num:]
        boxGrid[i[2]] = str + boxGrid[i[2]]
    
    answer = ""
    for b in sorted(boxGrid.keys()):
        answer += boxGrid[b][0]
    return answer


print("Year 2022, Day 5 solution part 1:", solution1())
print("Year 2022, Day 5 solution part 2:", solution2())