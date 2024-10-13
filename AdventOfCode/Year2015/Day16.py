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
            line = line.replace('\n', '').replace(':', '').replace(',', '').split(' ')
            gm = [line[1]]
            for i in range(2, len(line), 2):
                gm.append((line[i], int(line[i+1])))
            inpt.append(gm)

    return inpt
            

def solution1():
    inpt = getInput()
    #Dictionary of known details about the correct grandma
    known = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1
        }
    
    for gm in inpt:
        valid = True
        for i in range(1, len(gm)):
            if gm[i][0] in known.keys() and gm[i][1] != known[gm[i][0]]:
                valid = False
                break
        if valid:
            return gm[0]

    return


def solution2():
    inpt = getInput()
    #Dictionary of known details about the correct grandma
    known = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1
        }
    
    for gm in inpt:
        valid = True
        for i in range(1, len(gm)):
            detail, quantity = gm[i]
            if detail in known.keys():
                if detail == "cats" or detail == "trees":
                    if quantity <= known[detail]:
                        valid = False
                        break
                elif detail == "pomeranians" or detail == "goldfish":
                    if quantity >= known[detail]:
                        valid = False
                        break
                elif quantity != known[detail]:
                    valid = False
                    break

        if valid:
            return gm[0]

    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())