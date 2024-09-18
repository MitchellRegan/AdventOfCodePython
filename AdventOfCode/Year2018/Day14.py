aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = ''

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            inpt = line
    return inpt
            

def solution1():
    inpt = int(getInput())
    #The initial string of recipe numbers
    r = "37"
    #Starting indeces of each of the elves playing
    e1 = 0
    e2 = 1
    
    #Looping as many times as given by our input
    recipe = 0
    while len(r) < 10 + inpt:
        score = int(r[e1]) + int(r[e2])
        r = r + str(score)
        e1 = (e1 + int(r[e1]) + 1) % len(r)
        e2 = (e2 + int(r[e2]) + 1) % len(r)
        recipe += 1

    return r[inpt:10+inpt]


def solution2():
    inpt = getInput()
    testing and print("Looking for string", inpt)
    #The initial string of recipe numbers
    r = "37"
    #Starting indeces of each of the elves playing
    e1 = 0
    e2 = 1
    
    #Looping until we find the substring of our input
    recipe = 1
    lastSearchIndex = 0
    while True:
        score = int(r[e1]) + int(r[e2])
        r = r + str(score)
        e1 = (e1 + int(r[e1]) + 1) % len(r)
        e2 = (e2 + int(r[e2]) + 1) % len(r)
        
        #Every 10 loops we check for a substring
        if recipe % 10 == 0:
            i = r.find(inpt, max(0,lastSearchIndex-5))
            if i != -1:
                testing and print("...", r[i-5:i], r[i:i+5], r[i+5:i+10], "...")
                return i
            else:
                lastSearchIndex = len(r)-1
        recipe += 1
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())