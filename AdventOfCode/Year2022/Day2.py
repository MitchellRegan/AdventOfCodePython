#https://adventofcode.com/2022/day/2
#https://adventofcode.com/2022/day/2#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d2_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d2_real.txt")

def solution1():
    totalScore = 0

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            #delineating the line into opponent move and my move
            opMove = ord(line[0]) - 65
            myMove = ord(line[2]) - 88

            #Finding the score for the current round
            if opMove == myMove: #draw = 3
                totalScore += 3
            elif opMove == 0 and myMove == 1: #op rock, me paper win
                totalScore += 6
            elif opMove == 1 and myMove == 2: #op paper, me scissors win
                totalScore += 6
            elif opMove == 2 and myMove == 0: #op scissors, me rock win
                totalScore += 6
            # otherwise it's a loss for 0 points

            # adding the points for the shape chosen
            totalScore += myMove + 1

    return totalScore


def solution2():
    totalScore = 0

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            #delineating the line into opponent move and the intended result
            opMove = ord(line[0]) - 65
            result = ord(line[2]) - 88
            myMove = -1

            # Picking my move based on the outcome needed and the opponent's move
            if result == 0: #lose
                myMove = opMove - 1
                if myMove == -1:
                    myMove = 2
                #totalScore += 0
            elif result == 1: #draw
                myMove = opMove
                totalScore += 3
            elif result == 2: #win
                myMove = opMove + 1
                if myMove == 3:
                    myMove = 0
                totalScore += 6

            totalScore += myMove + 1

    return totalScore


print("Year 2022, Day 2 solution part 1:", solution1())
print("Year 2022, Day 2 solution part 2:", solution2())