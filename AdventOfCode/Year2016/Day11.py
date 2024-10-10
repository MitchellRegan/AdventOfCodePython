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
            line = line.replace('\n', '').replace('.', '').replace(',', '').split(' ')
            floorContents = []
            for i in range(len(line)):
                if line[i] == "microchip":
                    floorContents.append(line[i-1][0].upper() + 'M')
                elif line[i] == "generator":
                    floorContents.append(line[i-1][0].upper() + 'G')
            inpt.append(floorContents)

    return inpt
            

def solution1():
    floors = getInput()
    
    print("Floors:")
    for f in range(len(floors)):
        print(f+1, ":", floors[f])

    return


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())