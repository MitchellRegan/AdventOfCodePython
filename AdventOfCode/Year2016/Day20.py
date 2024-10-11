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
            line = line.replace('\n', '').split('-')
            inpt.append((int(line[0]), int(line[1])))

    return inpt
            

def solution1():
    inpt = getInput()
    inpt.sort()
    
    i = 0
    while i < len(inpt)-1:
        testing and print("Index", i, ":", inpt[i])
        if inpt[i][1] < inpt[i+1][0]:
            testing and print("\tCan't combine", inpt[i], "any further")
            i += 1
        else:
            testing and print("\tCombining", inpt[i], "with", inpt[i+1])
            min1,max1 = inpt[i]
            min2,max2 = inpt[i+1]

            if min1 <= min2 and max1 >= max2: #Range 1 fully contains range 2
                inpt.pop(i+1)
                testing and print("\t\t", inpt[i], "fully contains", inpt[i+1])
            elif min2 <= min1 and max2 >= max1: #Range 2 fully contains range 1
                testing and print("\t\t", inpt[i+1], "fully contains", inpt[i])
                inpt.pop(i)
            elif min1 < min2 and max1 < max2: #Overlap
                inpt.pop(i+1)
                inpt[i] = (min1, max2)
                testing and print("\t\tOverlap to make", inpt[i])
            else:
                testing and print("\t\t==== Bwuh?")
                
    if inpt[0][0] > 0:
        return 0
    return inpt[0][1]+1


def solution2():
    inpt = getInput()
    inpt.sort()
    
    i = 0
    while i < len(inpt)-1:
        if inpt[i][1] < inpt[i+1][0]:
            i += 1
        else:
            min1,max1 = inpt[i]
            min2,max2 = inpt[i+1]

            if min1 <= min2 and max1 >= max2: #Range 1 fully contains range 2
                inpt.pop(i+1)
            elif min2 <= min1 and max2 >= max1: #Range 2 fully contains range 1
                inpt.pop(i)
            elif min1 < min2 and max1 < max2: #Overlap
                inpt.pop(i+1)
                inpt[i] = (min1, max2)
                
    ans = 0
    prevVal = 0
    for i in inpt:
        ans += i[0] - prevVal
        prevVal = i[1] + 1
    ans += 4294967296 - prevVal
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())