aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        machine = []
        for line in f:
            line = line.replace('\n', '').replace(',','').split(' ')

            if line[0] == '':
                inpt.append(machine)
                machine = []
            elif line[1] == 'A:':
                machine.append((int(line[2][2:]), int(line[3][2:])))
            elif line[1] == 'B:':
                machine.append((int(line[2][2:]), int(line[3][2:])))
            else:
                machine.append((int(line[1][2:]), int(line[2][2:])))
        if machine is not []:
            inpt.append(machine)

    return inpt
          

def positionMachine(x_:int, y_:int, amtA_:tuple, costA_:int, amtB_:tuple, costB_:int, prizePos_:tuple, seen_:dict, pressA_:int=0, pressB_:int=0)->int:
    '''Recursive method to find the optimal number of presses of A and B buttons to position the crane above the prize.
    
    Parameters
    ----------
    x_: Int for the current X position of the crane
    y_: Int for the current Y position of the crane
    amtA_: Tuple representing how much the crane moves (x,y) when A is pressed
    costA_: Int for the number of coins it costs to press A
    amtB_: Tuple representing how much the crane moves (x,y) when B is pressed
    costB_: Int for the number of coins it costs to press B
    prizePos_: Tuple for the (x,y) position of the prize to reach
    pressA_: Int for the number of times the A button was pressed so far
    pressB_: Int for the number of times the B button was pressed so far

    Returns
    ----------
    Int for the fewest number of coins it takes to reach the prize. If the prize can't be reached, returns -1
    '''

    #Preventing duplicate recursions
    if (pressA_,pressB_) in seen_.keys():
        return -1
    else:
        seen_[(pressA_,pressB_)] = True

    #Recursion break for overshooting the prize
    if x_ > prizePos_[0] or y_ > prizePos_[1]:
        return -1

    #If positioned over the prize, returns the number of tokens used
    if x_ == prizePos_[0] and y_ == prizePos_[1]:
        testing and print("\tFound position", (x_,y_), "  A presses:", pressA_, "  B presses:", pressB_, "  Tokens:", (pressA_ * costA_) + (pressB_ * costB_))
        return (pressA_ * costA_) + (pressB_ * costB_)

    #Testing recursions with each button press
    pa = positionMachine(x_+amtA_[0], y_+amtA_[1], amtA_, costA_, amtB_, costB_, prizePos_, seen_, pressA_+1, pressB_)
    pb = positionMachine(x_+amtB_[0], y_+amtB_[1], amtA_, costA_, amtB_, costB_, prizePos_, seen_, pressA_, pressB_+1)

    if pa == -1:
        pa = pb
    if pb == -1:
        pb = pa

    return min(pa,pb)
    print("WTF happened?    pa:", pa, "    pb:", pb)
    return -1


def solution1():
    inpt = getInput()
    costA = 3
    costB = 1
    
    ans = 0
    for m in inpt:
        moveA, moveB, prize = m
        seen = {}
        cost = positionMachine(0, 0, m[0], costA, m[1], costB, m[2], seen, 0, 0)
        if cost != -1:
            ans += cost

    return ans


def solution2():
    inpt = getInput()
    
    ans = 0
    for i in range(len(inpt)):
        Ax, Ay = inpt[i][0]
        Bx, By = inpt[i][1]
        Px, Py = inpt[i][2]
        Px += 10000000000000
        Py += 10000000000000

        # Following formula derived from these steps:
        #       Equation 1: Prize_X = (A_X * num A presses) + (B_X * num B presses)
        #           Solve for "num of A presses" in terms of "num of B presses"
        #           num A presses = ((-1 * B_X * num B presses) - Prize_X) / (-1 * A_X)
        #       Equation 2: Prize_Y = (A_Y * num A presses) + (B_Y * num B presses)
        #           Replace "num A presses" with equation
        #           Re-arrange equation to be in the format of "num B presses = ..."
        #                             (A_Y * Prize_Y)
        #                           ( _______________ - Prize_Y ) 
        #                                   A_X
        #           num B presses = ______________________________
        #                                 (A_Y * B_X)
        #                             ( _______________ - B_Y )
        #                                     A_X
        cost1 = -1
        numB = round((((Ay * Px) / Ax) - Py) / (((Ay * Bx) / Ax) - By))
        if (Px - (numB * Bx)) % Ax == 0 and (Py - (numB * By)) % Ay == 0 and (Px - (numB * Bx)) // Ax == (Py - (numB * By)) // Ay:
            numA = (Px - (numB * Bx)) // Ax
            cost1 = (numA * 3) + numB

        #Same equation as before but with vars for A and B swapped. This is because the previous equation could come
        #up with an invalid solution where this one is valid, or vice-versa, so we run both
        cost2 = -1
        numA = round((((By * Px) / Bx) - Py) / (((By * Ax) / Bx) - Ay))
        if (Px - (numA * Ax)) % Bx == 0 and (Py - (numA * Ay)) % By == 0 and (Px - (numA * Ax)) // Bx == (Py - (numA * Ay)) // By:
            numA = (Px - (numB * Bx)) // Ax
            cost2 = (numA * 3) + numB

        #If at least one of the cost values found is valid (i.e. not -1), we take the smaller cost
        if cost1 != -1 and cost2 != -1:
            ans += min(cost1,cost2)
        elif cost1 != -1:
            ans += cost1
        elif cost2 != -1:
            ans += cost2

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())