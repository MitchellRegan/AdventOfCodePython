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
            line = line.replace('\n', '').split('x')
            inpt.append([int(x) for x in line])

    return inpt
            

def solution1():
    inpt = getInput()
    
    ans = 0
    for line in inpt:
        l,w,h = line
        sa = (2*l*w) + (2*w*h) + (2*h*l)
        slack = min([(l*w), (w*h), (h*l)])
        testing and print(line, "    SA:", sa, "    Slack:", slack)
        ans += sa + slack

    return ans


def solution2():
    inpt = getInput()
    
    ans = 0
    for line in inpt:
        l,w,h = line
        bow = l*w*h
        p = min([(l+l+w+w), (w+w+h+h), (l+l+h+h)])
        testing and print(line, "    Perimeter:", p, "    Bow:", bow, "    Total:", bow+p)
        ans += bow + p

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())