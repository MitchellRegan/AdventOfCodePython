aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    grid = []
    keys = {}#Key = char for the lower-case key ID, Value = (row,col) position
    doors = {}#Key = char for upper-case door ID, Value = (row,col) position
    startPos = None

    with open(inFile, 'r') as f:
        r = 0
        for line in f:
            line = line.replace('\n', '')
            for c in range(len(line)):
                if line[c] != '.' and line[c] != '#':
                    if line[c] == '@':
                        startPos = (r,c)
                    elif ord(line[c]) < 97: #Upper-case letter
                        doors[line[c]] = (r,c)
                    else: #Lower-case letter
                        keys[line[c]] = (r,c)
                    line = line[:c] + '.' + line[c+1:]
            grid.append(line)
            r += 1

    return grid, keys, doors, startPos


from collections import deque
def shortestBFS(grid_:list, s_:tuple, e_:tuple, getPath_:bool=True):
    '''BFS to find the shortest path to a destination and return the list of moves to take.'''
    seen = {s_:(None, 0)}#Key = (row,col) position, Value = [(row,col) for previous tile, distance from start]
    q = deque()
    q.append(s_)
    while len(q) > 0:
        head = q.popleft()
        
        #Found target
        if head == e_:
            #If getPath_ is true, we return the whole path from start to end
            if getPath_:
                path = deque()
                ptr = head
                while ptr is not None:
                    path.append(ptr)
                    ptr = seen[ptr][0]
                path.reverse()
                return list(path)
            #If getPath_ is false, we only return the distance from start to end
            else:
                return seen[head][1]
        
        #Checking tiles up, down, left, and right
        for adj in [(head[0]-1, head[1]), (head[0]+1, head[1]), (head[0], head[1]-1), (head[0], head[1]+1)]:
            if adj[0] > -1 and adj[1] > -1 and adj[0] < len(grid_) and adj[1] < len(grid_[0]):
               if adj not in seen.keys() and grid_[adj[0]][adj[1]] != '#':
                    seen[adj] = (head, seen[head][1] + 1)
                    q.append(adj)
    #No path found.
    return None


def solution1():
    grid, keys, doors, startPos = getInput()
    keyBlockers = {}#Key = key ID char, Value = [list of doors in the way]
    keyToKey = {}#Key = (min(keyID), max(keyID)) for every pair of keys, Value = distance between keys
    
    if testing:
        print("Grid:")
        for line in grid:
            print(line)
        print("Start Pos:", startPos)
        print("Key Locations:")
        for k in keys.keys():
            print("\t", k, ":", keys[k])
        print("Door Locations:")
        for d in doors.keys():
            print("\t", d, ":", doors[d])
            
    for k in keys.keys():
        kp = shortestBFS(grid, startPos, keys[k])
        testing and print("Path from start", startPos, "to key", k, keys[k], "=", kp)
        testing and print("\tDistance:", shortestBFS(grid, startPos, keys[k], False))
        keyBlockers[k] = []
        for d in doors.keys():
            if doors[d] in kp:
                keyBlockers[k].append(d)
        print("\tDoors in path to key", k, ":", keyBlockers[k])
        
    bestAns = 6270
    def stepsToAllKeys(pos_:tuple, keysFound_:str, steps_:int)->int:
        '''Recursive function to collect all remaining keys in the shortest number of steps possible.'''
        testing and print("S.T.A.K.    Pos:", pos_, "    Held Keys:", keysFound_, "    Steps:", steps_)
        nonlocal bestAns
        #Early exit if we know this recursion is already longer than the best one found
        if bestAns is not None and steps_ > bestAns:
            return steps_
        #Recursion break if we have all keys
        if len(keysFound_) == len(keys.keys()):
            testing and print("\t\tFound all keys", keysFound_, "in", steps_)
            if bestAns is None or bestAns > steps_:
                print("Updating best answer:", steps_)
                bestAns = steps_
            return steps_

        #Finding all possible next keys to grab
        nextKeys = []
        for k in keys.keys():
            #Ignoring already-found keys
            if k not in keysFound_:
                valid = True
                for d in keyBlockers[k]:
                    #Ignoring any keys blocked by doors we can't unlock yet
                    if d.lower() not in keysFound_:
                        valid = False
                        break
                if valid:
                    nextKeys.append(k)
                    
        #Recursively checking the best path for all possible next keys
        testing and print("\tValid keys to get:", nextKeys)
        bestSteps = None
        for nk in nextKeys:
            nextPos = keys[nk]
            nextKeysFound = keysFound_ + nk
            dist = shortestBFS(grid, pos_, nextPos, False) + steps_
            totalSteps = stepsToAllKeys(nextPos, nextKeysFound, dist)
            if bestSteps is None or totalSteps < bestSteps:
                bestSteps = totalSteps
        return bestSteps
    return stepsToAllKeys(startPos, "", 0)

    #Dijkstra search for all keys to prioritize least steps taken
    q = [(startPos, '', 0)]#Every element is (current position, keys found, steps taken)
    testing and print("\n\nStarting Dijkstra Search________________")
    while len(q) > 0:
        #testing and print("\tQ:", q)
        pos, kf, steps = q.pop(0)
        
        #The first element with all keys will have the shortest number of steps possible
        if len(kf) == len(keys.keys()):
            print("Final key order:", kf)
            return steps
        
        #Finding all possible next keys to grab
        nextKeys = []
        for k in keys.keys():
            #Ignoring already-found keys
            if k not in kf:
                valid = True
                for d in keyBlockers[k]:
                    #Ignoring any keys blocked by doors we can't unlock yet
                    if d.lower() not in kf:
                        valid = False
                        break
                if valid:
                    q.append((keys[k], kf+k, steps + shortestBFS(grid, pos, keys[k], False)))
                    
        #Sorting the queue so that the shortest distance is at the front
        q.sort(key=lambda x: x[2])

    return


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
#6270 too high
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())