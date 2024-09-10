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
    
    tiles = {}
    for line in inpt:
        i = 0 #Index for the current instruction in the line
        x = 0.0 #Row, col position of our current location
        y = 0.0
        
        while i < len(line):
            if line[i] == 'e':
                i += 1
                x += 1
            elif line[i] == 'w':
                i += 1
                x -= 1
            elif line[i:i+2] == 'se':
                i += 2
                x += 0.5
                y -= 1
            elif line[i:i+2] == 'sw':
                i += 2
                x -= 0.5
                y -= 1
            elif line[i:i+2] == 'ne':
                i += 2
                x += 0.5
                y += 1
            elif line[i:i+2] == 'nw':
                i += 2
                x -= 0.5
                y += 1
                
        testing and print("Final position:", (x,y))
        if (x,y) not in tiles.keys():
            tiles[(x,y)] = True
        else:
            tiles[(x,y)] = not tiles[(x,y)]
            
    ans = 0
    for x in tiles.keys():
        if tiles[x]:
            ans += 1
    return ans


def solution2():
    inpt = getInput()
    
    #Getting the initial state for the flipped tiles
    tiles = {}
    for line in inpt:
        i = 0 #Index for the current instruction in the line
        x = 0.0 #Row, col position of our current location
        y = 0.0
        
        while i < len(line):
            if line[i] == 'e':
                i += 1
                x += 1
            elif line[i] == 'w':
                i += 1
                x -= 1
            elif line[i:i+2] == 'se':
                i += 2
                x += 0.5
                y -= 1
            elif line[i:i+2] == 'sw':
                i += 2
                x -= 0.5
                y -= 1
            elif line[i:i+2] == 'ne':
                i += 2
                x += 0.5
                y += 1
            elif line[i:i+2] == 'nw':
                i += 2
                x -= 0.5
                y += 1
                
        if (x,y) not in tiles.keys():
            tiles[(x,y)] = True
        else:
            tiles[(x,y)] = not tiles[(x,y)]
            
        #Adding the adjacent tiles as white (False) so we can check them later
        for adj in [(x+1,y), (x+0.5,y+1), (x-0.5,y+1), (x-1,y), (x-0.5,y-1), (x+0.5,y-1)]:
            if adj not in tiles.keys():
                tiles[adj] = False
    
    #Applying the flipping rules based on adjacent tiles
    for day in range(0, 100):
        newTiles = {}
        
        for tile in tiles.keys():
            x,y = tile
            adjacentBlack = 0
            for adj in [(x+1,y), (x+0.5,y+1), (x-0.5,y+1), (x-1,y), (x-0.5,y-1), (x+0.5,y-1)]:
                #Counting the number of black tiles around the current tile
                if adj in tiles.keys() and tiles[adj]:
                    adjacentBlack += 1

                #Adding all adjacent tiles as white (False) to check later
                if adj not in newTiles.keys():
                    newTiles[adj] = False
                    
            if tiles[tile]:
                if adjacentBlack == 0 or adjacentBlack > 2:
                    newTiles[tile] = False
                else:
                    newTiles[tile] = True
            else:
                if adjacentBlack == 2:
                    newTiles[tile] = True
                else:
                    newTiles[tile] = False

        tiles = newTiles
        
    #Counting the number of black (True) tiles
    ans = 0    
    for k in tiles.keys():
        if tiles[k]:
           ans += 1 
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())