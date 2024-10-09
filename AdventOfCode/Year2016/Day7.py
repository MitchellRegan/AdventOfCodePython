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
    
    def hasABBA(s_:str)->bool:
        testing and print("\tChecking hasABBA for", s_)
        if len(s_) < 4:
            return False
        for i in range(0, len(s_)-3):
            if s_[i] == s_[i+3] and s_[i+1] == s_[i+2] and s_[i] != s_[i+1]:
                testing and print("\t\tFound ABBA substring:", s_[i:i+4])
                return True
        return False

    
    ans = 0
    for line in inpt:
        testing and print(line)
        
        #List for index ranges of substrings inside brackets
        inside = []
        prevInd = 0
        bracketStack = []
        for i in range(0, len(line)):
            if line[i] == '[':
                bracketStack.append(i)
            elif line[i] == ']':
                if len(bracketStack) > 0:
                    inside.append((bracketStack.pop(-1), i))
                    
        outsideLine = line
        valid = True
        testing and print("\tInside Brackets:", inside)
        for i in range(len(inside)-1,-1,-1):
            s,e = inside[i]
            outsideLine = outsideLine[:s] + '-' + outsideLine[e+1:]
            testing and print("\t\t", line[s+1:e])
            if hasABBA(line[s+1:e]):
                testing and print("\t----INVALID: interior bracket has ABBA")
                valid = False
                break
        if valid:
            testing and print("\tOutside Brackets:", outsideLine)
            for x in outsideLine.split('-'):
                if hasABBA(x):
                    ans += 1
                    testing and print("\t----VALID: exterior has ABBA")
                    break

    return ans


def solution2():
    inpt = getInput()
    
    def hasABA(s_:str)->bool:
        abaList = []
        if len(s_) < 3:
            return abaList
        for i in range(0, len(s_)-2):
            if s_[i] == s_[i+2] and s_[i] != s_[i+1]:
                abaList.append(s_[i:i+3])
        return abaList

    
    ans = 0
    for line in inpt:
        testing and print(line)
        
        #Finding the indeces where bracket groups begin and end
        inside = []
        prevInd = 0
        bracketStack = []
        for i in range(0, len(line)):
            if line[i] == '[':
                bracketStack.append(i)
            elif line[i] == ']':
                if len(bracketStack) > 0:
                    inside.append((bracketStack.pop(-1), i))
                    
        #Using the bracket indeces to split the input string into substrings inside/outside brackets
        outside = line
        valid = True
        newInside = []
        for i in range(len(inside)-1,-1,-1):
            s,e = inside[i]
            outside = outside[:s] + '-' + outside[e+1:]
            newInside.append(line[s+1:e])
        outside = outside.split('-')
        testing and print("----Outside Brackets:", outside)
        testing and print("----Inside Brackets: ", newInside)
        
        for o in outside:
            abaList = hasABA(o)
            testing and print("--------", o, "list:", abaList)
            for aba in abaList:
                valid = False
                inverse = "" + aba[1] + aba[0] + aba[1]
                testing and print("---------- Checking for", inverse)
                for i in newInside:
                    testing and print("------------", inverse, "in", i, "????")
                    if inverse in i:
                        ans += 1
                        valid = True
                        testing and print("---------------- VALID")
                        break
                if valid:
                    break

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
#134 too high
#85 not it
#80 not it
#123 not it
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())