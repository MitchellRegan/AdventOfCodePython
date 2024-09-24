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
            line = line.replace('\n', '').split(" ")
            inpt.append(line)

    return inpt
            

def solution1():
    inpt = getInput()
    
    ans = 0
    for pw in inpt:
        isValid = True
        testing and print("PW:", pw)
        for i in range(len(pw)):
            if pw.count(pw[i]) > 1:
                isValid = False
                testing and print("\tINVALID.", pw[i], "shows up more than once")
                break

        if isValid:
            ans += 1

    return ans


def solution2():
    inpt = getInput()
    
    ans = 0
    for pw in inpt:
        isValid = True
        testing and print("PW:", pw)
        for i in range(0, len(pw)-1):
            for j in range(i+1, len(pw)):
                if ''.join(sorted(pw[i])) == ''.join(sorted(pw[j])):
                    isValid = False
                    testing and print("\tINVALID.", pw[i], "==", pw[j])
                    break
            if not isValid:
                break

        if isValid:
            ans += 1

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())