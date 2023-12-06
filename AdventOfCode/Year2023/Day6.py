#https://adventofcode.com/2023/day/6
#https://adventofcode.com/2023/day/6#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d6_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d6_real.txt")


def getInput():
    time = []
    dist = []

    with open(inFile, 'r') as f:
        lineNum = 0

        for line in f:
            line = line.split(':')[1].split(' ')
            while '' in line:
                line.remove('')

            for i in range(0, len(line)):
                line[i] = int(line[i])

            if lineNum == 0:
                time = line
            else:
                dist = line
            lineNum += 1

    return time, dist


def solution1():
    time, dist = getInput()
    solution = 1

    #Iterating through each of the races to win
    for race in range(0, len(time)):
        numWins = 0


        #Iterating through each amount of milliseconds to hold the button
        for sec in range(1, time[race]):
            boatDistance = sec * (time[race] - sec)
            if boatDistance > dist[race]:
                numWins += 1
        solution *= numWins

    return solution


def solution2():
    time, dist = getInput()

    newTime = ''
    for i in time:
        newTime = newTime + str(i)
    newTime = int(newTime)
    
    newDist = ''
    for d in dist:
        newDist = newDist + str(d)
    newDist = int(newDist)
    
    numWins = 0

    #Iterating through each amount of milliseconds to hold the button
    for sec in range(1, newTime+1):
        boatDistance = sec * (newTime - sec)
        if boatDistance > newDist:
            numWins += 1

    return numWins


print("Year 2023, Day 6 solution part 1:", solution1())
print("Year 2023, Day 6 solution part 2:", solution2())