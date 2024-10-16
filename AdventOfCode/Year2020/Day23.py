aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    startNum = None
    inpt = {}#Key = cup number, Value = next cup clockwise

    with open(inFile, 'r') as f:
        for line in f:
            line = [int(x) for x in line.replace('\n', '')]
            startNum = line[0]
            for i in range(len(line)-1):
                inpt[line[i]] = line[i+1]
            inpt[line[-1]] = line[0]

    return inpt, startNum
            

def solution1():
    inpt, curNum = getInput()
    
    for x in range(100):
        testing and print("\n---- Move", x+1, "----")
        n1 = inpt[curNum]
        n2 = inpt[n1]
        n3 = inpt[n2]
        afterPickup = inpt[n3]
        dest = curNum - 1
        while True:
            if dest == 0:
                dest = 9
            if dest == n1 or dest == n2 or dest == n3:
                dest -= 1
            else:
                break
        inpt[n3] = inpt[dest]
        inpt[curNum] = afterPickup
        inpt[dest] = n1
        
        if testing:
            print("\tCurrent number:", curNum, "\n\tPicking up cups", n1, n2, n3, "\n\tDestination cup:", dest)
            for k in inpt.keys():
                print("\t\t", k, "->", inpt[k])
        curNum = inpt[curNum]

    ans = ""
    ptr = inpt[1]
    while ptr != 1:
        ans = ans + str(ptr)
        ptr = inpt[ptr]
    return ans


def solution2():
    inpt, curNum = getInput()
    ptr = curNum
    while inpt[ptr] != curNum:
        testing and print(ptr, "->", inpt[ptr])
        ptr = inpt[ptr]
    testing and print("Final number:", ptr)
    testing and print("Next number to add:", max(inpt.keys())+1)
    for x in range(10, 1000001):
        if testing and x < 50:
            print(ptr, "->", x)
        inpt[ptr] = x
        ptr = x
    inpt[ptr] = curNum
    testing and print("Final number:", ptr, "->", inpt[ptr])
    testing and print("Number of cups in input:", len(inpt.keys()))
    testing and print("Starting number:", curNum)
    
    for x in range(10000000):
        if testing and x % 500000 == 0:
            print("Cycle", x)
        n1 = inpt[curNum]
        n2 = inpt[n1]
        n3 = inpt[n2]
        afterPickup = inpt[n3]
        dest = curNum - 1
        while True:
            if dest == 0:
                dest = 1000000
            if dest == n1 or dest == n2 or dest == n3:
                dest -= 1
            else:
                break
        inpt[n3] = inpt[dest]
        inpt[curNum] = afterPickup
        inpt[dest] = n1
        curNum = inpt[curNum]

    c1 = inpt[1]
    c2 = inpt[c1]
    testing and print("Cup 1 ->", inpt[1], "->", inpt[inpt[1]])
    return c1 * c2


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())