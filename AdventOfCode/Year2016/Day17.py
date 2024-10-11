import hashlib
aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = ""

    with open(inFile, 'r') as f:
        for line in f:
            inpt = line.replace('\n', '')

    return inpt
            

def solution1():
    inpt = getInput()
    
    q = [(inpt,0,0)] #Each value is (string to hash, row pos, column pos)
    while True:
        s,r,c = q.pop(0)
        if r == 3 and c == 3:
            return s[len(inpt):]
        hs = hashlib.md5(s.encode()).hexdigest()
        
        if r > 0 and hs[0] in "bcdef": #UP
            q.append((s+"U", r-1, c))
        if r < 3 and hs[1] in "bcdef": #DOWN
            q.append((s+"D", r+1, c))
        if c > 0 and hs[2] in "bcdef": #LEFT
            q.append((s+"L", r, c-1))
        if c < 3 and hs[3] in "bcdef": #RIGHT
            q.append((s+"R", r, c+1))

    return


def solution2():
    inpt = getInput()
    
    ans = 0
    q = [(inpt,0,0)] #Each value is (string to hash, row pos, column pos)
    while len(q) > 0:
        s,r,c = q.pop(0)
        if r == 3 and c == 3:
            ans = max(ans, len(s)-len(inpt))
        else:
            hs = hashlib.md5(s.encode()).hexdigest()
        
            if r > 0 and hs[0] in "bcdef": #UP
                q.append((s+"U", r-1, c))
            if r < 3 and hs[1] in "bcdef": #DOWN
                q.append((s+"D", r+1, c))
            if c > 0 and hs[2] in "bcdef": #LEFT
                q.append((s+"L", r, c-1))
            if c < 3 and hs[3] in "bcdef": #RIGHT
                q.append((s+"R", r, c+1))

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())