#https://adventofcode.com/2023/day/7
#https://adventofcode.com/2023/day/7#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d7_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d7_real.txt")


def getInput():
    input = []

    with open(inFile, 'r') as f:
        lineNum = 0

        for line in f:
            line = line.split(" ")
            line[1] = int(line[1])
            input.append(line)
            lineNum += 1

    return input


def cardValue(card_:str, v2_:bool=False)->int:
    if not v2_:
        if card_ is 'A': return 14
        if card_ is 'K': return 13
        if card_ is 'Q': return 12
        if card_ is 'J': return 11
        if card_ is 'T': return 10
        return int(card_)
    else:
        if card_ is 'A': return 14
        if card_ is 'K': return 13
        if card_ is 'Q': return 12
        if card_ is 'J': return 1
        if card_ is 'T': return 10
        return int(card_)


def handRank(hand_:str, v2_:bool=False):
    pairs = {}
    for c in hand_:
        if c in pairs.keys():
            pairs[c] += 1
        else:
            pairs[c] = 1

    #recursive search replacing jokers replaceing any other card
    if v2_ and 'J' in hand_:
        bestVal = 0
        handCpy = hand_

        while 'J' in handCpy:
            handCpy = handCpy.replace('J', '')

        for c in ['A','K','Q','T','9','8','7','6','5','4','3','2']:
            tempHand = handCpy
            while len(tempHand) < 5:
                tempHand = tempHand + c
            tempScore = handRank(tempHand)
            if tempScore > bestVal:
                bestVal = tempScore
        return bestVal

    # five of a kind
    if len(pairs.keys()) == 1:
        return 7

    if len(pairs.keys()) == 2:
        highestNum = 0
        for k in pairs.keys():
            if pairs[k] > highestNum:
                highestNum = pairs[k]
        #4 of a kind = 4 of a card and 1 of another
        if highestNum == 4:
            return 6
        #full house is 2 of a card and 3 of another
        else:
            return 5
        
    if len(pairs.keys()) == 3:
        highestNum = 0
        twoPair = False
        for k in pairs.keys():
            if pairs[k] > highestNum:
                highestNum = pairs[k]
            elif pairs[k] == 2 and highestNum == 2:
                twoPair = True
        #3 of a kind = 3 of a card and 2 non-pairs
        if highestNum == 3:
            return 4
        #two pair = 2 of one card, 2 of another, and 1 other
        if twoPair:
            return 3

    if len(pairs.keys()) == 4:
        return 2

    return 1


def solution1():
    input = getInput()

    for i in range(0, len(input)-1):
        for j in range(i+1, len(input)):
            iRank = handRank(input[i][0])
            jRank = handRank(input[j][0])

            if iRank > jRank:
                placeholder = input[i]
                input[i] = input[j]
                input[j] = placeholder
            elif iRank == jRank:
                for x in range(0, 5):
                    if cardValue(input[i][0][x]) == cardValue(input[j][0][x]):
                        continue
                    elif cardValue(input[i][0][x]) < cardValue(input[j][0][x]):
                        break
                    else:
                        placeholder = input[i]
                        input[i] = input[j]
                        input[j] = placeholder
                        break

    sum = 0
    for r in range(0, len(input)):
        #print("rank of", input[r][0], "=", r+1)
        sum += (r+1) * input[r][1]

    return sum


def solution2():
    input = getInput()

    for i in range(0, len(input)-1):
        for j in range(i+1, len(input)):
            iRank = handRank(input[i][0], True)
            jRank = handRank(input[j][0], True)

            if iRank > jRank:
                placeholder = input[i]
                input[i] = input[j]
                input[j] = placeholder
            elif iRank == jRank:
                for x in range(0, 5):
                    if cardValue(input[i][0][x], True) == cardValue(input[j][0][x], True):
                        continue
                    elif cardValue(input[i][0][x], True) < cardValue(input[j][0][x], True):
                        break
                    else:
                        placeholder = input[i]
                        input[i] = input[j]
                        input[j] = placeholder
                        break

    sum = 0
    for r in range(0, len(input)):
        sum += (r+1) * input[r][1]

    return sum


print("Year 2023, Day 7 solution part 1:", solution1())
print("Year 2023, Day 7 solution part 2:", solution2())