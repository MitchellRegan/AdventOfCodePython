aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    list1 = []
    list2 = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            list1.append(int(line[0]))
            list2.append(int(line[-1]))

    return list1, list2
            

def solution1():
    list1, list2 = getInput()
    list1.sort()
    list2.sort()
    
    ans = 0
    for i in range(len(list1)):
        ans += abs(list1[i] - list2[i])

    return ans


def solution2():
    list1, list2 = getInput()

    ans = 0
    for i in list1:
        ans += list2.count(i) * i

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())