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
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())