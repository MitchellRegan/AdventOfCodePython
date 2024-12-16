aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    p1 = None
    p2 = None

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            if p1 is None:
                p1 = int(line[-1])
            else:
                p2 = int(line[-1])

    return p1, p2
            

def solution1():
    p1_pos, p2_pos = getInput()
    p1_score = 0
    p2_score = 0
    isP1Turn = True
    dieNum = 1 #Die that goes from 1 to 100 in incriments of +1 at a time
    dieRolls = 0 #Total number of times the die was rolled
    
    turnNum = 1
    while p1_score < 1000 and p2_score < 1000:
        if isP1Turn:
            p1_pos += 3 + (3 * dieNum)
            while p1_pos > 10:
                p1_pos -= 10
            p1_score += p1_pos
            #testing and print("Turn", turnNum, "Player 1 moves", (3 + (3 * dieNum)), "spaces to space", p1_pos, "    Score:", p1_score)
        else:
            p2_pos += 3 + (3 * dieNum)
            while p2_pos > 10:
                p2_pos -= 10
            p2_score += p2_pos
            #testing and print("Turn", turnNum, "Player 2 moves", (3 + (3 * dieNum)), "spaces to space", p2_pos, "    Score:", p2_score)
            
        dieNum += 3
        dieRolls += 3
        isP1Turn = not isP1Turn
        turnNum += 1

    #testing and print("==== P1 Final Score:", p1_score, "    P2 Final Score:", p2_score, "    Total Die Rolls:", dieRolls)
    if p1_score < 1000:
        return p1_score * dieRolls
    return p2_score * dieRolls


def solution2():
    p1_pos, p2_pos = getInput()
    p1_score = 0
    p2_score = 0
    isP1Turn = True
    dieNum = 1 #Die that goes from 1 to 100 in incriments of +1 at a time
    dieRolls = 0 #Total number of times the die was rolled
    
    turnNum = 1
    while p1_score < 1000 and p2_score < 1000:
        if isP1Turn:
            p1_pos += 3 + (3 * dieNum)
            while p1_pos > 10:
                p1_pos -= 10
            p1_score += p1_pos
            testing and print("Turn", turnNum, "Player 1 moves", (3 + (3 * dieNum)), "spaces to space", p1_pos, "    Score:", p1_score)
        else:
            p2_pos += 3 + (3 * dieNum)
            while p2_pos > 10:
                p2_pos -= 10
            p2_score += p2_pos
            testing and print("Turn", turnNum, "Player 2 moves", (3 + (3 * dieNum)), "spaces to space", p2_pos, "    Score:", p2_score)
            
        dieNum += 3
        dieRolls += 3
        isP1Turn = not isP1Turn
        turnNum += 1

    testing and print("==== P1 Final Score:", p1_score, "    P2 Final Score:", p2_score, "    Total Die Rolls:", dieRolls)
    if p1_score < 1000:
        return p1_score * dieRolls
    return p2_score * dieRolls


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())