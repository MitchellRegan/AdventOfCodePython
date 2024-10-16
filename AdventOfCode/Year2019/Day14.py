aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = {}#Key = chem name, Value = [quantity of chem produced, and list of required (quantity of chem, chem name)]

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').replace(',', '').replace('=> ', '').split(' ')
            
            inpt[line[-1]] = [int(line[-2])]
            
            for i in range(0, len(line)-3, 2):
                inpt[line[-1]].append((int(line[i]), line[i+1]))

    return inpt
            

def solution1():
    inpt = getInput()
    chemToOre = {"ORE":(1,1)}#Key = chem name, Value = ratio of (# chem to # ore)
    extras = {}#Key = chem name, Value = amount of the chem that's currently unused
    for c in inpt.keys():
        extras[c] = 0

    def getNumOre(chem_:str, qnty_:int)->int:
        '''Recursive function that finds the total amount of ore needed to make one item of the given chem.'''
        testing and print("Getting number of ore for chem", chem_)
        numOre = 0
        for r in range(1, len(inpt[chem_])):
            n,x = inpt[chem_][r]
            testing and print("\tIngredient:", x, "    Qnty:", n)
            ratio = None
            if x in chemToOre.keys():
                ratio = chemToOre[x]
            else:
                ratio = getNumOre(x)
                
            #use quantity (n) and the ratio to find the minimum amount of ore required
            while n > 0:
                n -= ratio[0]
                numOre += ratio[1]
                
        if chem_ not in chemToOre.keys():
            chemToOre[chem_] = (inpt[chem_][0], numOre)
            testing and print("\t\t", chem_, ": ORE ratio:", chemToOre[chem_])
        return chemToOre[chem_]

    ans = getNumOre("FUEL", 1)
    return ans


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())