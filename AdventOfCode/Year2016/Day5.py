import hashlib
aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = None

    with open(inFile, 'r') as f:
        for line in f:
            inpt = line.replace('\n', '')

    return inpt
            

def solution1():
    inpt = getInput()
    
    ans = ''
    i = 0
    while len(ans) < 8:
        s = inpt + str(i)
        hs = hashlib.md5(s.encode()).hexdigest()
        if hs[:5] == "00000":
            ans = ans + hs[5]
            testing and print("i =", i, "String:", s, "    Hash:", hs, "    Pw:", ans)
        i += 1
        
    return ans


def solution2():
    inpt = getInput()
    
    ans = [None] * 8
    i = 0
    while True:
        s = inpt + str(i)
        hs = hashlib.md5(s.encode()).hexdigest()
        if hs[0] == '0' and hs[1] == '0' and hs[2] == '0' and hs[3] == '0' and hs[4] == '0':
            testing and print("Possible hash:", hs)
            if hs[5] in "01234567":
                ind = int(hs[5])
                if ans[ind] is None:
                    ans[ind] = hs[6]
                    testing and print("i =", i, "String:", s, "    Hash:", hs, "    Pw:", ans)
                    if None not in ans:
                        return ''.join(ans)
        i += 1
        
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())