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
            inpt = line.replace('\n', '')

    return inpt
            

def knotHash(inpt):
    inpt = [ord(c) for c in inpt]
    inpt.extend([17, 31, 73, 47, 23])
    
    currIndex = 0
    skipSize = 0
    numberRope = [x for x in range(256)]
        
    #Looping 64 times
    for loop in range(64):
        for ropeLen in inpt:
            #If the length of rope is 1, there's no point in reversing the numbers because it's the same
            if ropeLen != 1:
                revNums = []
                if currIndex + ropeLen >= len(numberRope):
                    revNums = numberRope[currIndex:]
                    revNums.extend(numberRope[:currIndex+ropeLen-len(numberRope)])
                else:
                    revNums = numberRope[currIndex:currIndex+ropeLen]
                    
                revNums.reverse()
        
                for i in range(ropeLen):
                    if currIndex + i >= len(numberRope):
                        numberRope[currIndex+i-len(numberRope)] = revNums[i]
                    else:
                        numberRope[currIndex+i] = revNums[i]
                
            currIndex += ropeLen + skipSize
            while currIndex >= len(numberRope):
                currIndex -= len(numberRope)
            skipSize += 1
            
    hashStr = ""
    curVal = None
    for i in range(len(numberRope)):
        if i % 16 == 0:
            curVal = numberRope[i]
        else:
            #Performing a bitwise XOR
            curVal = curVal ^ numberRope[i]
            if i % 16 == 15:
                if curVal < 16:
                    hashStr = hashStr + '0' + hex(curVal)[2:]
                else:
                    hashStr = hashStr + hex(curVal)[2:]
    return hashStr


def solution1():
    inpt = getInput()
    
    print(inpt)
    ans = 0
    for row in range(0, 128):
        inputString = inpt + '-' + str(row)
        outputString = knotHash(inputString)
        binString = bin(int(outputString, 16))[2:].zfill(128)
        
        if testing and row < 8:
            print(binString[:8].replace('1','#').replace('0','.'), "    ", outputString[:2], "     Hex size:", len(outputString))
        ans += binString.count('1')

    return ans


def solution2():
    inpt = getInput()
    grid = []
    
    for row in range(0, 128):
        inputString = inpt + '-' + str(row)
        outputString = knotHash(inputString)
        binString = bin(int(outputString, 16))[2:].zfill(128)
        grid.append([c for c in binString])
        
    #Iterating through every (row,col) position to look for a non-0 value to begin a BFS search for groups
    numGroups = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                numGroups += 1
                seen = {(r,c):True}
                q = [(r,c)]
                while len(q) > 0:
                    hr,hc = q.pop(0)
                    grid[hr][hc] = '0'
                    for adj in [(hr+1,hc), (hr-1,hc), (hr,hc+1), (hr,hc-1)]:
                        if adj not in seen.keys() and adj[0] > -1 and adj[0] < 128 and adj[1] > -1 and adj[1] < 128:
                            if grid[adj[0]][adj[1]] == '1':
                                q.append(adj)
                            seen[adj] = True

    return numGroups


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())