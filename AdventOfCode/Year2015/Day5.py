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
    for line in inpt:
        testing and print(line)
        isNice = True
        
        for bs in ['ab', 'cd', 'pq', 'xy']:
            if bs in line:
                isNice = False
                testing and print("\tHas naughty substring")
                break
        
        if isNice:
            numVowel = 0
            hasDouble = False
            for i in range(len(line)):
                if line[i] in "aeiou":
                    numVowel += 1
                if i < len(line)-1 and line[i] == line[i+1]:
                    hasDouble = True
            if numVowel > 2 and hasDouble:
                ans += 1
                testing and print("\tNice")
            else:
                testing and print("\tNaughty. NumVowel:", numVowel, "    Has Double:", hasDouble)
    return ans


def solution2():
    inpt = getInput()
    
    ans = 0
    for line in inpt:
        testing and print("\n", line)
        isValid = False
        
        #Checking for matching pairs of substrings length 2
        for i in range(len(line)-3):
            for j in range(i+2, len(line)-1):
                s1 = line[i:i+2]
                s2 = line[j:j+2]
                #testing and print("\tComparing", s1, "==", s2, ":", s1==s2)
                if s1 == s2:
                    isValid = True
                    testing and print("\tFound duplicate length-2 substrings:", line[i:i+2], line[j:j+2])
                    break
            if isValid:
                break
            
        #Checking for letters that repeat with a single gap
        if isValid:
            for i in range(len(line)-2):
                if line[i] == line[i+2]:
                    testing and print("\tFound duplicate char with gap:", line[i:i+3])
                    ans += 1
                    break
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())