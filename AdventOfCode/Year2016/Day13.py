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
            inpt = int(line.replace('\n', ''))

    return inpt
            

def solution1():
    inpt = getInput()
    target = (31,39) #(x,y) coordinate, not (r,c)
    if testing:
        target = (7,4)
    testing and print("Input:", inpt)
    
    seen = {(1,1):[0,True]} #Key = (x,y) pos, Value = [distance from (1,1), Bool for if it's an open space]
    q = [(1,1)]
    while len(q) > 0:
        testing and print("Head:", q[0])
        head = q.pop(0)
        x,y = head
        if head == target:
            return seen[head][0]
        
        for adj in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            testing and print("\tAdjacent:", adj)
            if adj not in seen.keys() and adj[0] >= 0 and adj[1] >= 0:
                posVal = (adj[0]*adj[0]) + (3*adj[0]) + (2*adj[0]*adj[1]) + adj[1] + (adj[1]*adj[1]) + inpt
                binStr = '{0:08b}'.format(posVal)
                if binStr.count('1') % 2 != 0:
                    testing and print("\t\tWall", seen[head])
                    seen[adj] = [seen[head][0]+1, False]
                else:
                    testing and print("\t\tOpen")
                    seen[adj] = [seen[head][0]+1, True]
                    q.append(adj)

    return


def solution2():
    inpt = getInput()
    
    seen = {(1,1):[0,True]} #Key = (x,y) pos, Value = [distance from (1,1), Bool for if it's an open space]
    q = [(1,1)]
    ans = 0
    while len(q) > 0:
        head = q.pop(0)
        x,y = head
        
        if seen[head][0] < 51:
            ans += 1
            for adj in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if adj not in seen.keys() and adj[0] >= 0 and adj[1] >= 0:
                    posVal = (adj[0]*adj[0]) + (3*adj[0]) + (2*adj[0]*adj[1]) + adj[1] + (adj[1]*adj[1]) + inpt
                    binStr = '{0:08b}'.format(posVal)
                    if binStr.count('1') % 2 != 0:
                        seen[adj] = [seen[head][0]+1, False]
                    else:
                        seen[adj] = [seen[head][0]+1, True]
                        q.append(adj)

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())