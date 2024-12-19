aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    colors = []
    designs = []

    with open(inFile, 'r') as f:
        onColors = True
        for line in f:
            line = line.replace('\n', '')

            if len(line) == 0:
                onColors = False
            elif onColors:
                colors = line.split(', ')
            else:
                designs.append(line)

    return colors, designs
            

def solution1():
    colors, designs = getInput()
    colors.sort(key=lambda x: len(x))
    print("Longest color:", len(colors[-1]))
    print("Shortest color:", len(colors[0]))
    #Sorting all colors into a dictionary where Key = first letter of the color, Value = [list of all colors starting with that letter]
    colorDict = {}
    for c in colors:
        if c[0] not in colorDict.keys():
            colorDict[c[0]] = [c]
        elif c not in colorDict[c[0]]:
            colorDict[c[0]].append(c)
    #Sorting so that largest color names come first (easier to weed them out by being too large rather than do tons of recursion first)
    for c in colorDict.keys():
        colorDict[c].sort(key=lambda x: len(x), reverse=True)
    
    if testing:
        print("Colors:", colors, "\nDesigns:")
        for x in designs:
            print("\t", x)


    def isDesignPossible(d_:str, i_:int)->bool:
        '''Recursively checks if the given design (d_) is possible to be made with at least 1 combination of the colors available.'''
        #print("\t\t\t\t", d_)

        if i_ == len(d_):
            testing and print("\t\tDesign", d_, "is POSSIBLE")
            return True

        if d_[i_] in colorDict.keys():
            for c in colorDict[d_[i_]]:
                if len(c) <= len(d_) - i_ and c == d_[i_:i_+len(c)]:
                    testing and print("\tColor", c, "fits at index", i_)
                    #pgap = ['_'] * i_
                    #print("\t\t\t\t", ''.join(pgap)+c)
                    if isDesignPossible(d_, i_+len(c)):
                        return True

        testing and print("\t\tDesign", d_, "is impossible")
        return False


    ans = 0
    for d in range(len(designs)):
        #for d in range(343, len(designs)):
        if d == 343 or d == 362:
            continue
        print("On design", d, "/", len(designs), "\t\t", designs[d])

        #Checking if the end of the design is possible (a form of early exit I guess)
        #endingPossible = False
        possible = False
        #for i in range(1, len(colors[-1])+1):
        for i in range(len(colors[-1]), 0, -1):
            subStr = designs[d][len(designs[d])-i:]
            print("--Checking substring", subStr)
            if subStr in colorDict[subStr[0]]:
                frontStr = designs[d][:len(designs[d])-i]
                print("Front String:", frontStr)
                #endingPossible = True
                if isDesignPossible(frontStr, 0):
                    possible = True
                    break

        if possible:
            ans += 1
            print("\tPOSSIBLE, current valid:", ans)
        else:
            print("\tNOT POSSIBLE, current valid:", ans)
        #if not endingPossible:
        #    print("\tEND NOT POSSIBLE. Current valid:", ans)
        #elif isDesignPossible(designs[d], 0):
        #    print("\tPOSSIBLE, Current valid:", ans)
        #    ans += 1
        #else:
        #    print("\tNOT POSSIBLE. Current valid:", ans)

    return ans


def solution2():
    colors, designs = getInput()
    #Sorting all colors into a dictionary where Key = first letter of the color, Value = [list of all colors starting with that letter]
    colorDict = {}
    for c in colors:
        if c[0] not in colorDict.keys():
            colorDict[c[0]] = [c]
        elif c not in colorDict[c[0]]:
            colorDict[c[0]].append(c)
    #Sorting so that largest color names come first (easier to weed them out by being too large rather than do tons of recursion first)
    for c in colorDict.keys():
        colorDict[c].sort(key=lambda x: len(x), reverse=True)
    
    if testing:
        print("Colors:", colors, "\nDesigns:")
        for x in designs:
            print("\t", x)


    def isDesignPossible(d_:str, i_:int)->bool:
        '''Recursively checks if the given design (d_) is possible to be made with at least 1 combination of the colors available.'''
        #print("\t\t\t\t", d_)

        if i_ == len(d_):
            testing and print("\t\tDesign", d_, "is POSSIBLE")
            return True

        if d_[i_] in colorDict.keys():
            for c in colorDict[d_[i_]]:
                if len(c) <= len(d_) - i_ and c == d_[i_:i_+len(c)]:
                    testing and print("\tColor", c, "fits at index", i_)
                    #pgap = ['_'] * i_
                    #print("\t\t\t\t", ''.join(pgap)+c)
                    if isDesignPossible(d_, i_+len(c)):
                        return True

        testing and print("\t\tDesign", d_, "is impossible")
        return False
    

    def numDesignCombos(d_:str, i_:int)->int:
        '''Recursively checks if the given design (d_) is possible to be made with at least 1 combination of the colors available.'''
        #print("\t\t\t\t", d_)

        if i_ == len(d_):
            testing and print("\t\tDesign", d_, "is POSSIBLE")
            return 1

        numCombos = 0
        if d_[i_] in colorDict.keys():
            for c in colorDict[d_[i_]]:
                if len(c) <= len(d_) - i_ and c == d_[i_:i_+len(c)]:
                    numCombos += numDesignCombos(d_, i_+len(c))

        return numCombos


    ans = 0
    for d in range(len(designs)):
        #for d in range(343, len(designs)):
        if d == 343 or d == 362:
            continue
        print("On design", d, "/", len(designs), "\t\t", designs[d])

        #Checking if the end of the design is possible (a form of early exit I guess)
        #endingPossible = False
        possible = False
        #for i in range(1, len(colors[-1])+1):
        for i in range(len(colors[-1]), 0, -1):
            subStr = designs[d][len(designs[d])-i:]
            if subStr[0] in colorDict.keys() and subStr in colorDict[subStr[0]]:
                frontStr = designs[d][:len(designs[d])-i]
                if isDesignPossible(frontStr, 0):
                    ans += numDesignCombos(frontStr, 0)
        print("\t\tCombos:", ans, '\n')
    return ans


#print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
#274 too low
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())