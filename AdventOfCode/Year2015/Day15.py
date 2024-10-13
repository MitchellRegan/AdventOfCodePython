aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = {}#Key = ingredient name, Value = [capacity, durability, flavor, texture, calories]

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').replace(',', '').split(' ')
            n = line[0][:-1]
            inpt[n] = [int(line[2]), int(line[4]), int(line[6]), int(line[8]), int(line[10])]

    return inpt
            

def solution1():
    inpt = getInput()
    
    for k in inpt.keys():
        print(k, ":", inpt[k])

    return


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())