import hashlib
aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
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
    
    def hasTriple(s_:str)->bool:
        for i in range(len(s_)-2):
            if s_[i] == s_[i+1] and s_[i] == s_[i+2]:
                return s_[i]
        return
    
    ans = []
    i = 0
    q = [] #Every value is (String of the same char to look for, index in which to pop if not found)
    while len(ans) < 64:
        if len(q) > 0 and i > q[0][1]:
            #testing and print(q[0], "not found by i =", i)
            q.pop(0)
        s = inpt + str(i)
        hs = hashlib.md5(s.encode()).hexdigest()
            
        #Looking for the strings of 5 repeating characters to find any matches
        removeInd = []
        for r in range(len(q)):
            if q[r][0] in hs:
                ans.append(q[r][1]-1000)
                #testing and print("i =", i, "    Hash:", hs, "    Found x5:", q[r][0])
                removeInd.insert(0, r)
        for r in removeInd:
            q.pop(r)
            
        #Looking for strings of 3 repeating characters
        trip = hasTriple(hs)
        if trip:
            q.append((''.join([trip]*5), i+1000))
            #testing and print("i =", i, "    Hash:", hs, "    Found x3", trip)
            
        i += 1
        
    return ans[-1]


def solution2():
    inpt = getInput()
    
    def hasTriple(s_:str)->bool:
        for i in range(len(s_)-2):
            if s_[i] == s_[i+1] and s_[i] == s_[i+2]:
                return s_[i]
        return
    
    ans = []
    i = 0
    q = [] #Every value is (String of the same char to look for, index in which to pop if not found)
    while len(ans) < 64:
        if len(q) > 0 and i > q[0][1]:
            q.pop(0)
            
        s = inpt + str(i)
        hs = hashlib.md5(s.encode()).hexdigest()
        for salt in range(2016):
            hs = hashlib.md5(hs.encode()).hexdigest()
            
        #Looking for the strings of 5 repeating characters to find any matches
        removeInd = []
        for r in range(len(q)):
            if q[r][0] in hs:
                ans.append(q[r][1]-1000)
                print("i =", i, "    Hash:", hs, "    Found x5:", q[r][0], "for index", ans[-1], "    Key#", len(ans))
                removeInd.insert(0, r)
        for r in removeInd:
            q.pop(r)
            
        #Looking for strings of 3 repeating characters
        trip = hasTriple(hs)
        if trip:
            q.append((''.join([trip]*5), i+1000))
            #testing and print("i =", i, "    Hash:", hs, "    Found x3", trip)
            
        i += 1
        
    return ans[63]


#print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())
#20219 too high
#20119 too high
#20153 too high