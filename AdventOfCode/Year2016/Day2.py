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
    
    keypad = [[1,2,3],[4,5,6],[7,8,9]]
    
    ans = ""
    r = 1
    c = 1
    for line in inpt:
        testing and print("Instruction:", line)
        for x in line:
            if x == 'U' and r > 0:
                r -= 1
                testing and print("\t^", (r,c), "    Key:", keypad[r][c])
            elif x == 'D' and r < 2:
                r += 1
                testing and print("\tv", (r,c), "    Key:", keypad[r][c])
            elif x == 'R' and c < 2:
                c += 1
                testing and print("\t>", (r,c), "    Key:", keypad[r][c])
            elif x == 'L' and c > 0:
                c -= 1
                testing and print("\t<", (r,c), "    Key:", keypad[r][c])
                
        ans = ans + str(keypad[r][c])

    return ans


def solution2():
    inpt = getInput()
    
    keypad = [(0,0,1,0,0),
              (0,2,3,4,0),
              (5,6,7,8,9),
              (0,'A','B','C',0),
              (0,0,'D',0,0)]
    
    ans = ""
    r = 2
    c = 0
    for line in inpt:
        testing and print("Instruction:", line)
        for x in line:
            if x == 'U' and r > 0 and keypad[r-1][c] != 0:
                r -= 1
                testing and print("\t^", (r,c), "    Key:", keypad[r][c])
            elif x == 'D' and r < 4 and keypad[r+1][c] != 0:
                r += 1
                testing and print("\tv", (r,c), "    Key:", keypad[r][c])
            elif x == 'R' and c < 4 and keypad[r][c+1] != 0:
                c += 1
                testing and print("\t>", (r,c), "    Key:", keypad[r][c])
            elif x == 'L' and c > 0 and keypad[r][c-1] != 0:
                c -= 1
                testing and print("\t<", (r,c), "    Key:", keypad[r][c])
                
        ans = ans + str(keypad[r][c])

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())