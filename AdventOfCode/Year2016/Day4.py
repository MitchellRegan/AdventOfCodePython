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
            line = line.replace('\n', '')
            inpt.append(line)

    return inpt
            

def solution1():
    inpt = getInput()
    
    ans = 0
    for x in inpt:
        sectorID = int(x.split('-')[-1][:-7])
        ename = ''.join(x.split('-')[:-1])
        checksum = x.split('[')[1][:-1]
        testing and print(x, "   ename:", ename, "    ID:", sectorID, "    checksum:", checksum)
        
        charCounts = {}
        for c in ename:
            if c not in charCounts.keys():
                charCounts[c] = 1
            else:
                charCounts[c] += 1

        prevChar = None
        prevCount = len(ename) + 1
        valid = True
        for c in checksum:
            cCount = ename.count(c)
            testing and print("\t", c, "count:", cCount, "    ord:", ord(c.lower()))
            if cCount == 0:
                valid = False
                testing and print("\t\tInvalid.", c, "not in string")
                break
            elif cCount > prevCount:
                valid = False
                testing and print("\t\tInvalid. Greater than previous count", prevCount)
                break
            elif cCount == prevCount and ord(c.lower()) <= ord(prevChar):
                valid = False
                testing and print("\t\tInvalid.", c, "comes before", prevChar)
                break
            elif charCounts[c] != max([charCounts[x] for x in charCounts.keys()]):
                valid = False
                testing and print("\t\tInvalid.", c, "isn't the next most-common letter.")
                break
            else:
                prevCount = cCount
                prevChar = c.lower()
                charCounts.pop(c)
        if valid:
            testing and print("\t\tValid. Adding", sectorID)
            ans += sectorID

    return ans


def solution2():
    inpt = getInput()
    
    alphaStr = "abcdefghijklmnopqrstuvwxyz"
    for x in inpt:
        sectorID = int(x.split('-')[-1][:-7])
        ename = ''.join(x.split('-')[:-1])
        checksum = x.split('[')[1][:-1]
        
        charCounts = {}
        for c in ename:
            if c not in charCounts.keys():
                charCounts[c] = 1
            else:
                charCounts[c] += 1

        prevChar = None
        prevCount = len(ename) + 1
        valid = True
        for c in checksum:
            cCount = ename.count(c)
            
            if cCount == 0:
                valid = False
                break
            elif cCount > prevCount:
                valid = False
                break
            elif cCount == prevCount and ord(c.lower()) <= ord(prevChar):
                valid = False
                break
            elif charCounts[c] != max([charCounts[x] for x in charCounts.keys()]):
                valid = False
                break
            else:
                prevCount = cCount
                prevChar = c.lower()
                charCounts.pop(c)
        if valid:
            testing and print(x, "Valid")
            newStr = ""
            for c in '-'.join(x.split('-')[:-1]):
                if c == "-":
                    newStr = newStr + ' '
                else:
                    ind = (alphaStr.index(c) + sectorID) % len(alphaStr)
                    newStr = newStr + alphaStr[ind]
            
            #print("\t", newStr, sectorID)
            if newStr[:5] == "north":
                return sectorID
    return 


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())