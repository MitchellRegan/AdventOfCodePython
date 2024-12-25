aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"
from collections import deque

def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            inpt.append(line.replace('\n', ''))

    return inpt
            

numpadPos = {'7':(0,0), '8':(0,1), '9':(0,2), '4':(1,0), '5':(1,1), '6':(1,2), '1':(2,0), '2':(2,1), '3':(2,2), '0':(3,1), 'A':(3,2)}
def numpadBFS(b1:str, b2:str)->list:
    '''Finds the shortest path from button 1 (b1) to button 2 (b2) and returns the list of arrows needed to get there.'''
    startPos = numpadPos[b1]
    endPos = numpadPos[b2]
    seen = {startPos:None} #Key = (r,c) position, Value = ((r,c) of previous pos, arrow for direction taken)
    q = deque()
    q.append(startPos)
    while len(q) > 0:
        head = q.popleft()

        #If the end position is found, we return the arrow keys taken to get there
        if head == endPos:
            steps = []
            prev = seen[head]
            while prev is not None:
                steps.insert(0, prev[1])
                prev = seen[prev[0]]
            return steps

        r,c = head
        for adj in [(r+1,c,'v'), (r-1,c,'^'), (r,c+1,'>'), (r,c-1,'<')]:
            if (adj[0], adj[1]) not in seen.keys():
                #Checking if the adjacent tile is within the boundaries of the keypad
                if adj[0] > -1 and adj[0] < 4 and adj[1] > -1 and adj[1] < 3:
                    #Can't go over the empty position (3,0)
                    if not (adj[0] == 3 and adj[1] == 0):
                        seen[(adj[0], adj[1])] = (head, adj[2])
                        q.append((adj[0], adj[1]))
    return []


arrowKeyPos = {'^':(0,1), 'A':(0,2), '<':(1,0), 'v':(1,1), '>':(1,2)}
def arrowKeyBFS(b1:str, b2:str)->list:
    '''Finds the shortest path from button 1 (b1) to button 2 (b2) and returns the list of arrows needed to get there.'''
    startPos = arrowKeyPos[b1]
    endPos = arrowKeyPos[b2]
    seen = {startPos:None} #Key = (r,c) position, Value = ((r,c) of previous pos, arrow for direction taken)
    q = deque()
    q.append(startPos)
    while len(q) > 0:
        head = q.popleft()

        #If the end position is found, we return the arrow keys taken to get there
        if head == endPos:
            steps = []
            prev = seen[head]
            while prev is not None:
                steps.insert(0, prev[1])
                prev = seen[prev[0]]
            return steps

        r,c = head
        for adj in [(r+1,c,'v'), (r-1,c,'^'), (r,c+1,'>'), (r,c-1,'<')]:
            if (adj[0], adj[1]) not in seen.keys():
                #Checking if the adjacent tile is within the boundaries of the keypad
                if adj[0] > -1 and adj[0] < 2 and adj[1] > -1 and adj[1] < 3:
                    #Can't go over the empty position (0,0)
                    if not (adj[0] == 0 and adj[1] == 0):
                        seen[(adj[0], adj[1])] = (head, adj[2])
                        q.append((adj[0], adj[1]))
    return []


class RobotArm():
    def __init__(self, isKeypad:True):
        self.curPos = ()


def solution1():
    inpt = getInput()
    
    for i in inpt:
        testing and print("Sequence:", i)
        
        path1 = []
        bot1Pos = 'A'
        for b in i:
            path1.extend(numpadBFS(bot1Pos, b))
            path1.append('A')
            bot1Pos = b
        print("Path 1:", ''.join(path1))

        path2 = []
        bot2Pos = 'A'
        for b in path1:
            path2.extend(arrowKeyBFS(bot2Pos, b))
            path2.append('A')
            bot2Pos = b
        print("Path 2:", ''.join(path2))

        
        path3 = []
        bot3Pos = 'A'
        for b in path2:
            path3.extend(arrowKeyBFS(bot3Pos, b))
            path3.append('A')
            bot3Pos = b
        print("Path 3:", ''.join(path3))
        print("Optimal <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A")
        break
    return


def solution2():
    inpt = getInput()



    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())