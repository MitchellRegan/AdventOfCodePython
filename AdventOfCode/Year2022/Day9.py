#https://adventofcode.com/2022/day/9
#https://adventofcode.com/2022/day/9#part2

#inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2022\\InputTestFiles\\d9_test.txt"
inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2022\\InputRealFiles\\d9_real.txt"

def solution1():
    tailVisits = {(0,0):1}
    headPos = [0,0] #row, col
    tailPos = [0,0]

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            dir = line[0]
            steps = int(line[2:].replace('\n', ''))
            headSteps = [0,0]

            if dir == 'U':
                headSteps[0] = 1
            elif dir == 'D':
                headSteps[0] = -1
            elif dir == 'R':
                headSteps[1] = 1
            elif dir == 'L':
                headSteps[1] = -1

            for i in range(0, steps):
                #Move head
                headPos[0] += headSteps[0]
                headPos[1] += headSteps[1]

                #Move tail if not touching
                if abs(headPos[0]-tailPos[0]) > 1 or abs(headPos[1]-tailPos[1]) > 1:
                    if headPos[0] == tailPos[0]:#same row
                        if headPos[1] > tailPos[1]:
                            tailPos[1] += 1
                        elif headPos[1] < tailPos[1]:
                            tailPos[1] -= 1
                    elif headPos[1] == tailPos[1]:#same col
                        if headPos[0] > tailPos[0]:
                            tailPos[0] += 1
                        elif headPos[0] < tailPos[0]:
                            tailPos[0] -= 1
                    else: #not in same row or col
                        yDiff = headPos[0] - tailPos[0]
                        xDiff = headPos[1] - tailPos[1]
                        if yDiff > 0 and xDiff > 0:#head is up-right
                            tailPos[0] += 1
                            tailPos[1] += 1
                        elif yDiff < 0 and xDiff > 0:#head down-right
                            tailPos[0] -= 1
                            tailPos[1] += 1
                        elif yDiff < 0 and xDiff < 0:#head down-left
                            tailPos[0] -= 1
                            tailPos[1] -= 1
                        else:#head up-left
                            tailPos[0] += 1
                            tailPos[1] -= 1

                    #adding tail pos to dictionary
                    newTailPos = (tailPos[0], tailPos[1])
                    if newTailPos not in tailVisits.keys():
                        tailVisits[newTailPos] = 1

    return len(tailVisits.keys())


def solution2():
    tailVisits = {(0,0):1}
    knots = []
    for i in range(0, 10):
        knots.append([0,0])

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            dir = line[0]
            steps = int(line[2:].replace('\n', ''))
            headSteps = [0,0]

            if dir == 'U':
                headSteps[0] = 1
            elif dir == 'D':
                headSteps[0] = -1
            elif dir == 'R':
                headSteps[1] = 1
            elif dir == 'L':
                headSteps[1] = -1

            for i in range(0, steps):
                #Move head
                knots[0][0] += headSteps[0]
                knots[0][1] += headSteps[1]

                #Looping through to move each trailing knot in sequence
                for i in range(1, 10):
                    headPos = knots[i-1]
                    tailPos = knots[i]

                    #Move tail if not touching
                    if abs(headPos[0]-tailPos[0]) > 1 or abs(headPos[1]-tailPos[1]) > 1:
                        if headPos[0] == tailPos[0]:#same row
                            if headPos[1] > tailPos[1]:
                                tailPos[1] += 1
                            elif headPos[1] < tailPos[1]:
                                tailPos[1] -= 1
                        elif headPos[1] == tailPos[1]:#same col
                            if headPos[0] > tailPos[0]:
                                tailPos[0] += 1
                            elif headPos[0] < tailPos[0]:
                                tailPos[0] -= 1
                        else: #not in same row or col
                            yDiff = headPos[0] - tailPos[0]
                            xDiff = headPos[1] - tailPos[1]
                            if yDiff > 0 and xDiff > 0:#head is up-right
                                tailPos[0] += 1
                                tailPos[1] += 1
                            elif yDiff < 0 and xDiff > 0:#head down-right
                                tailPos[0] -= 1
                                tailPos[1] += 1
                            elif yDiff < 0 and xDiff < 0:#head down-left
                                tailPos[0] -= 1
                                tailPos[1] -= 1
                            else:#head up-left
                                tailPos[0] += 1
                                tailPos[1] -= 1

                #adding tail pos to dictionary
                newTailPos = (knots[9][0], knots[9][1])
                if newTailPos not in tailVisits.keys():
                    tailVisits[newTailPos] = 1

    return len(tailVisits.keys())


print("Year 2022, Day 9 solution part 1:", solution1())
print("Year 2022, Day 9 solution part 2:", solution2())