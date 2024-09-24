aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    grid = []
    units = {} #Key = (r,c) position of the unit, Value = [unit ID, attack power, HP]
    numElf = 0
    numGob = 0

    with open(inFile, 'r') as f:
        row = 0
        for line in f:
            line = line.replace('\n', '')
            for col in range(len(line)):
                if line[col] == 'E' or line[col] == 'G':
                    units[(row,col)] = [line[col], 3, 200]
                    if line[col] == 'E':
                        numElf += 1
                    else:
                        numGob += 1
            grid.append(line.replace('E','.').replace('G', '.'))
            row += 1

    return grid, units, numElf, numGob
            

def solution1():
    grid, units, numElf, numGob = getInput()
    
    if testing:
        print("Units:", units)
        for line in grid:
            print(line)
            
    #For each turn, every living unit gets to move and attack. Looping until one faction is gone
    turnNum = 0
    while numElf > 0 and numGob > 0:
        testing and print("Turn", turnNum, "================================")
        #Sorting all remaining units based on ascending row, then ascending col
        unitInitiative = [x for x in units.keys()]
        unitInitiative.sort(key=lambda x: [x[0], x[1]])
        
        nextTurnUnits = {} #Units dict stored for the next turn
        killedUnits = [] #List of (r,c) for units that were killed this turn
        
        for u in range(len(unitInitiative)):
            #If this unit was killed before it could take its turn, we skip
            if unitInitiative[u] in killedUnits:
                testing and print("   ", unitInitiative[u], ": Died previously this turn")
                continue
            testing and print("   ", unitInitiative[u], ":", units[unitInitiative[u]])
            pos = unitInitiative[u]
            unitID, atk, hp = units[unitInitiative[u]]
            units.pop(pos)
            
            #BFS search from this unit to find the nearest enemy
            target = None
            seen={pos:(0, None)} #Position = (distance, previous pos)
            q = [pos]
            while len(q) > 0:
                r,c = q.pop(0)
                adj = [(r-1,c), (r,c-1), (r,c+1), (r+1,c)]
                for a in adj:
                    if grid[a[0]][a[1]] == '#':
                        continue
                    #Unit found
                    elif a in units.keys():
                        #It's an enemy unit
                        if unitID != units[a][0]:
                            target = a
                            seen[a] = (seen[(r,c)][0] + 1, (r,c))
                            break
                    #Empty space
                    elif a not in seen.keys():
                        q.append(a)
                        seen[a] = (seen[(r,c)][0] + 1, (r,c))
                        
                if target is not None:
                    testing and print("\tTarget found at", a, ":", units[a], " distance:", seen[a][0])
                    #If the distance from the target is more than 1 space away, we move to the next space along the found path
                    if seen[a][0] > 1:
                        nextPos = a
                        while seen[seen[nextPos][1]][1] is not None:
                            nextPos = seen[nextPos][1]
                        units[nextPos] = [unitID, atk, hp]
                        pos = nextPos
                        testing and print("\t\tUnit at new pos", nextPos, ":", units[nextPos])
                    #Otherwise the target is in attack range so we stay put
                    else:
                        units[pos] = [unitID, atk, hp]
                        testing and print("\t\tTarget already within attack range, so not moving")
                    break
                
            #If there's no enemy found, this unit stands still and ends their turn
            if target is None:
                testing and print("\tNo target found. Ending turn")
                units[pos] = [unitID, atk, hp]
            #If an enemy was found and it's in-range to attack, damage is dealt
            elif abs(target[0] - pos[0]) + abs(target[1] - pos[1]) == 1:
                testing and print("\tTarget in-range. Attacking target at", target)
                units[target][2] -= units[pos][1]
                testing and print("\t\tTarget took", units[pos][1], "damage. New HP:", units[target][2])
                if units[target][2] <= 0:
                    testing and print("\t\t\tTARGET DIED")
                    if units[target][0] == 'E':
                        numElf -= 1
                    else:
                        numGob -= 1
                    units.pop(target)
                    killedUnits.append(target)
                
        if testing:
            newGrid = [x for x in grid]
            print("Remaining Units:")
            for u in units.keys():
                newGrid[u[0]] = newGrid[u[0]][:u[1]] + units[u][0] + newGrid[u[0]][u[1]+1:]
                print(u, ":", units[u])
            print("Updated grid on turn", turnNum)
            for line in newGrid:
                print(line)
            print('\n')
            
        turnNum += 1


    #Answer is the sum of all remaining units' HP multiplied by the number of FULL TURNS that passed (last turn doesn't count)
    ans = 0
    testing and print("Final turn number:", turnNum)
    for u in units.keys():
        ans += units[u][2]
        testing and print("\t", units[u])
    return ans * turnNum


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())