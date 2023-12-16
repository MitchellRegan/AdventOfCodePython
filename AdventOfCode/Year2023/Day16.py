#https://adventofcode.com/2023/day/16
#https://adventofcode.com/2023/day/16#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d16_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d16_real.txt")


def getInput():
    input = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n','')
            input.append(list(line.replace('\n','')))

    return input


def solution1(startRow_:int=0, startCol_:int=-1, startDir_:str='R'):
    input = getInput()
    
    beams = [[startRow_, startCol_, startDir_]]
    energized = {}
    reflections = {}
    
    while len(beams) > 0:
        finished = []
        newBeams = []

        for i in range(0, len(beams)):
            row = beams[i][0]
            col = beams[i][1]
            beamDir = beams[i][2]

            if beamDir == "R":
                if col == len(input[0])-1:
                    finished.append(i)
                else:
                    col += 1
                    beams[i][1] = col
                    energized[(row,col)] = 1

                    if input[row][col] != '.':
                        if (row,col) in reflections and beamDir in reflections[(row,col)]:
                            finished.append(i)
                            continue
                        else:
                            if (row,col) in reflections:
                                reflections[(row,col)].append(beamDir)
                            else:
                                reflections[(row,col)] = [beamDir]

                    if input[row][col] == '/':
                        beams[i][2] = 'U'
                    elif input[row][col] == '\\':
                        beams[i][2] = 'D'
                    elif input[row][col] == '|':
                        finished.append(i)
                        newBeams.append([row, col, 'U'])
                        newBeams.append([row, col, 'D'])

            elif beamDir == "L":
                if col == 0:
                    finished.append(i)
                else:
                    col -= 1
                    beams[i][1] = col
                    energized[(row,col)] = 1

                    if input[row][col] != '.':
                        if (row,col) in reflections and beamDir in reflections[(row,col)]:
                            finished.append(i)
                            continue
                        else:
                            if (row,col) in reflections:
                                reflections[(row,col)].append(beamDir)
                            else:
                                reflections[(row,col)] = [beamDir]

                    if input[row][col] == '/':
                        beams[i][2] = 'D'
                    elif input[row][col] == '\\':
                        beams[i][2] = 'U'
                    elif input[row][col] == '|':
                        finished.append(i)
                        newBeams.append([row, col, 'U'])
                        newBeams.append([row, col, 'D'])

            elif beamDir == "U":
                if row == 0:
                    finished.append(i)
                else:
                    row -= 1
                    beams[i][0] = row
                    energized[(row,col)] = 1

                    if input[row][col] != '.':
                        if (row,col) in reflections and beamDir in reflections[(row,col)]:
                            finished.append(i)
                            continue
                        else:
                            if (row,col) in reflections:
                                reflections[(row,col)].append(beamDir)
                            else:
                                reflections[(row,col)] = [beamDir]

                    if input[row][col] == '/':
                        beams[i][2] = 'R'
                    elif input[row][col] == '\\':
                        beams[i][2] = 'L'
                    elif input[row][col] == '-':
                        finished.append(i)
                        newBeams.append([row, col, 'L'])
                        newBeams.append([row, col, 'R'])

            elif beamDir == "D":
                if row == len(input)-1:
                    finished.append(i)
                else:
                    row += 1
                    beams[i][0] = row
                    energized[(row,col)] = 1

                    if input[row][col] != '.':
                        if (row,col) in reflections and beamDir in reflections[(row,col)]:
                            finished.append(i)
                            continue
                        else:
                            if (row,col) in reflections:
                                reflections[(row,col)].append(beamDir)
                            else:
                                reflections[(row,col)] = [beamDir]

                    if input[row][col] == '/':
                        beams[i][2] = 'L'
                    elif input[row][col] == '\\':
                        beams[i][2] = 'R'
                    elif input[row][col] == '-':
                        finished.append(i)
                        newBeams.append([row, col, 'L'])
                        newBeams.append([row, col, 'R'])

        #Removing any beams that have completed their run
        for f in range(len(finished)-1, -1, -1):
            beams.pop(finished[f])

        #Adding any newly split beams to the next loop
        for nb in newBeams:
            beams.append(nb)

    return len(energized.keys())


def solution2():
    input = getInput()
    
    maxEnergy = 0

    for row in range(0, len(input)):
        #For this row, we do one pass from the left coming in right
        e = solution1(row, -1, 'R')
        if e > maxEnergy:
            maxEnergy = e
        #And one pass from the right coming in left
        e = solution1(row, len(input[0]), 'L')
        if e > maxEnergy:
            maxEnergy = e

    for col in range(0, len(input[0])):
        #For this col, we do one pass from the top coming in downward
        e = solution1(-1, col, 'D')
        if e > maxEnergy:
            maxEnergy = e
        #And one pass from the bottom coming in upwards
        e = solution1(len(input), col, 'U')
        if e > maxEnergy:
            maxEnergy = e

    return maxEnergy


print("Year 2023, Day 16 solution part 1:", solution1())
print("Year 2023, Day 16 solution part 2:", solution2())