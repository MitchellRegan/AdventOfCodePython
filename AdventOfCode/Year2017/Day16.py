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
        for line in f:
            inpt = line.replace('\n', '').split(',')

    return inpt
            

def solution1():
    inpt = getInput()
    dancers = [x for x in "abcdefghijklmnop"]
    if testing:
        dancers = dancers[:5]
        print("Dancers:", dancers)
        print("Instructions:", inpt)
        
    for move in inpt:
        if move[0] == 's': #spin
            spinNum = int(move[1:])
            frontDancers = dancers[:len(dancers)-spinNum]
            dancers = dancers[len(dancers)-spinNum:]
            dancers.extend(frontDancers)
            testing and print("Spin", spinNum, "    Dancers:", dancers)
            
        elif move[0] == 'x': #exchange
            move = move.replace('x','').split('/')
            index1 = int(move[0])
            index2 = int(move[1])
            placeholder = dancers[index1]
            dancers[index1] = dancers[index2]
            dancers[index2] = placeholder
            testing and print("Exchange", index1, index2, "    Dancers:", dancers)
            
        else: #partner
            d1 = move[1]
            d1ind = dancers.index(d1)
            d2 = move[3]
            d2ind = dancers.index(d2)
            dancers[d1ind] = d2
            dancers[d2ind] = d1
            testing and print("Exchange", d1, d2, "    Dancers:", dancers)

    return ''.join(dancers)


def solution2():
    inpt = getInput()
    dancers = [x for x in "abcdefghijklmnop"]
    if testing:
        dancers = dancers[:5]
        print("Dancers:", dancers)

    #Looping until we find a pattern that has been seen before
    danceOrders = {''.join(dancers):[0]} #Key = string for the order of the dancers, Value = dance iteration when seen
    fullCycle = -1 #number of loops at which the dance completes a full cycle and returns to the starting configuration
    for i in range(10000):
        for move in inpt:
            if move[0] == 's': #spin
                spinNum = int(move[1:])
                frontDancers = dancers[:len(dancers)-spinNum]
                dancers = dancers[len(dancers)-spinNum:]
                dancers.extend(frontDancers)
            
            elif move[0] == 'x': #exchange
                move = move.replace('x','').split('/')
                index1 = int(move[0])
                index2 = int(move[1])
                placeholder = dancers[index1]
                dancers[index1] = dancers[index2]
                dancers[index2] = placeholder
            
            else: #partner
                d1 = move[1]
                d1ind = dancers.index(d1)
                d2 = move[3]
                d2ind = dancers.index(d2)
                dancers[d1ind] = d2
                dancers[d2ind] = d1

        curOrder = ''.join(dancers)
        if curOrder in danceOrders.keys():
            danceOrders[curOrder].append(i+1)
            testing and print("\tOrder", curOrder, "seen again in i =", i+1)
            if len(danceOrders[curOrder]) == 5:
                testing and print("\t\tOrder", curOrder, "was seen in i =", danceOrders[curOrder])
                fullCycle = danceOrders[curOrder][1] - danceOrders[curOrder][0]
                testing and print("\t\tDance repeats every", fullCycle, "cycles. 1000000000 %", fullCycle, "=", 1000000000 % fullCycle)
                break
        else:
            danceOrders[curOrder] = [i+1]

    #Performing the dance for only the last loop
    for i in range(1000000000 % fullCycle):
        for move in inpt:
            if move[0] == 's': #spin
                spinNum = int(move[1:])
                frontDancers = dancers[:len(dancers)-spinNum]
                dancers = dancers[len(dancers)-spinNum:]
                dancers.extend(frontDancers)
            
            elif move[0] == 'x': #exchange
                move = move.replace('x','').split('/')
                index1 = int(move[0])
                index2 = int(move[1])
                placeholder = dancers[index1]
                dancers[index1] = dancers[index2]
                dancers[index2] = placeholder
            
            else: #partner
                d1 = move[1]
                d1ind = dancers.index(d1)
                d2 = move[3]
                d2ind = dancers.index(d2)
                dancers[d1ind] = d2
                dancers[d2ind] = d1

    return ''.join(dancers)


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())