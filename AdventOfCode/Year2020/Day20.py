aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    tileStack = {}

    with open(inFile, 'r') as f:
        tileNum = 0
        tile = []
        for line in f:
            line = line.replace('\n', '')
            if line == "":
                tileStack[tileNum] = tile
                tile = []
                continue
            elif line[0] == 'T':
                tileNum = int(line[5:-1])
            else:
                tile.append(line)
                
        if len(tile) > 0:
            tileStack[tileNum] = tile
    return tileStack
            

def solution1():
    tileStack = getInput()
    tileOrient = {} #Dictionary where key = tile number, value = [top, left, right, bottom]
    
    #Getting the alignment strings for each tile's sides
    for tile in tileStack.keys():
        testing and print("Tile", tile)
        t = tileStack[tile][0]
        b = tileStack[tile][-1]
        l = ""
        r = ""
        
        for line in tileStack[tile]:
            testing and print('\t', line)
            r = r + line[-1]
            l = l + line[0]

        if testing:
            print("\tTop:   ", t)
            print("\tLeft:  ", l)
            print("\tRight: ", r)
            print("\tBottom:", b)
            print()
        tileOrient[tile] = [t,l,r,b]

    def compareTiles(tile1_, tile2_):
        '''Checks if the current orientations of both tiles align along one border. If not, returns None'''
        t1,l1,r1,b1 = tileOrient[tile1_]
        t2,l2,r2,b2 = tileOrient[tile2_]
        
        if t1 == b2: #Tile 2 is on top of tile 1
            return "top"
        if l1 == r2: #Tile 2 is to the left of tile 1
            return "left"
        if r1 == l2: #Tile 2 is to the right of tile 1
            return "right"
        if b1 == t2: #Tile 2 is below tile 1
            return "bottom"
        return None #No match

    #Comparing the orientation of every tile to every other tile
    tileNums = [x for x in tileOrient.keys()]
    tileMatches = {} #Dict where key = tileNum, value = matching tile orientation list [tileNum up, tileNum left, tileNum right, tileNum down]
    q = [tileNums[0]]
    while len(q) > 0:
        t1 = q.pop(0)
        testing and print("Checking", t1)
        for i in range(0, len(tileNums)):
            t2 = tileNums[i]
            testing and print("\tAgainst", t2)
            if t1 == t2:
                testing and print("\t\tSkipping, because they're the same")
                continue

            testing and print("Default comparing", t1, "-", t2)
            result = None
            for x in range(2): #One loop un-flipped, one loop after flip
                #Checking the initial orientation
                result = compareTiles(t1,t2)
                if result is not None or t2 in tileMatches.keys():
                    break
        
                for y in range(3): #Rotating up to 3 times
                    testing and print("\tRotating", t2)
                    t,l,r,b = tileOrient[t2]
                    tileOrient[t2] = [l[::-1], b, t, r[::-1]]
                    result = compareTiles(t1,t2)
                    if result is not None:
                        break
            
                #If no result after this loop, we flip t2
                if result is None:
                    testing and print("\tFlipping", t2)
                    t,l,r,b = tileOrient[t2]
                    tileOrient[t2] = [t[::-1], r, l, b[::-1]]
                else:
                    break
            
            if result is not None:
                testing and print("Result match:", result)
                if t1 not in tileMatches:
                    tileMatches[t1] = [None, None, None, None]
                if t2 not in tileMatches:
                    tileMatches[t2] = [None, None, None, None]
                    q.append(t2)
                    
                if result == "top":
                    tileMatches[t1][0] = t2
                    tileMatches[t2][3] = t1
                elif result == "left":
                    tileMatches[t1][1] = t2
                    tileMatches[t2][2] = t1
                elif result == "right":
                    tileMatches[t1][2] = t2
                    tileMatches[t2][1] = t1
                else:
                    tileMatches[t1][3] = t2
                    tileMatches[t2][0] = t1
    
    testing and print("\nMatches:")
    ans = 1
    for match in tileMatches:
        testing and print(match, ":", tileMatches[match])
        if tileMatches[match].count(None) == 2:
            testing and print("\tCORNER")
            ans *= match

    return ans


def solution2():
    tileStack = getInput()
    tileOrient = {} #Dictionary where key = tile number, value = [top, left, right, bottom]
    
    #Getting the alignment strings for each tile's sides
    for tile in tileStack.keys():
        t = tileStack[tile][0]
        b = tileStack[tile][-1]
        l = ""
        r = ""
        
        for line in tileStack[tile]:
            r = r + line[-1]
            l = l + line[0]

        tileOrient[tile] = [t,l,r,b]

    def compareTiles(tile1_, tile2_):
        '''Checks if the current orientations of both tiles align along one border. If not, returns None'''
        t1,l1,r1,b1 = tileOrient[tile1_]
        t2,l2,r2,b2 = tileOrient[tile2_]
        
        if t1 == b2: #Tile 2 is on top of tile 1
            return "top"
        if l1 == r2: #Tile 2 is to the left of tile 1
            return "left"
        if r1 == l2: #Tile 2 is to the right of tile 1
            return "right"
        if b1 == t2: #Tile 2 is below tile 1
            return "bottom"
        return None #No match

    #Comparing the orientation of every tile to every other tile
    tileNums = [x for x in tileOrient.keys()]
    tileMatches = {} #Dict where key = tileNum, value = matching tile orientation list [tileNum up, tileNum left, tileNum right, tileNum down]
    q = [tileNums[0]]
    while len(q) > 0:
        t1 = q.pop(0)
        for i in range(0, len(tileNums)):
            t2 = tileNums[i]
            if t1 == t2:
                continue

            result = None
            for x in range(2): #One loop un-flipped, one loop after flip
                #Checking the initial orientation
                result = compareTiles(t1,t2)
                if result is not None or t2 in tileMatches.keys():
                    break
        
                for y in range(3): #Rotating up to 3 times
                    #Rotating the quick-reference orientation
                    t,l,r,b = tileOrient[t2]
                    tileOrient[t2] = [l[::-1], b, t, r[::-1]]
                    
                    #Rotating the whole tile
                    rotated = list(zip(*tileStack[t2][::-1]))
                    for ti in range(len(rotated)):
                        rotated[ti] = ''.join(rotated[ti])
                    tileStack[t2] = rotated

                    result = compareTiles(t1,t2)
                    if result is not None:
                        break
            
                #If no result after this loop, we flip t2
                if result is None:
                    #Flipping the quick-reference orientation
                    t,l,r,b = tileOrient[t2]
                    tileOrient[t2] = [t[::-1], r, l, b[::-1]]
                    
                    #Flipping the whole tile
                    for ti in range(0, len(tileStack[t2])):
                        tileStack[t2][ti] = tileStack[t2][ti][::-1]
                else:
                    break
            
            #If a match is found, we store the directional relation of each tile to one-another
            if result is not None:
                if t1 not in tileMatches:
                    tileMatches[t1] = [None, None, None, None]
                if t2 not in tileMatches:
                    tileMatches[t2] = [None, None, None, None]
                    q.append(t2)
                    
                if result == "top":
                    tileMatches[t1][0] = t2
                    tileMatches[t2][3] = t1
                elif result == "left":
                    tileMatches[t1][1] = t2
                    tileMatches[t2][2] = t1
                elif result == "right":
                    tileMatches[t1][2] = t2
                    tileMatches[t2][1] = t1
                else:
                    tileMatches[t1][3] = t2
                    tileMatches[t2][0] = t1
    
    #Making a 2D grid to map-out the final locations of every tile, starting with the one in the top-left
    tileLocs = []
    topLeftCorner = None
    for match in tileMatches:
        if tileMatches[match][0] is None and tileMatches[match][1] is None:
            testing and print("\tTop-Left Corner", match, ":", tileMatches[match])
            tileLocs.append([match])
            break
    #Filling out the 2D grid of locations based on each tile's right and bottom relations
    row = 0
    while True:
        if row > 0:
            b = tileMatches[tileLocs[row-1][0]][3]
            if b is not None:
                tileLocs.append([b])
            else:
                break

        col = 0
        while col < len(tileLocs[row]):
            tile = tileLocs[row][col]
            t,l,r,b = tileMatches[tile]
            if r is not None:
                tileLocs[row].append(r)
            col += 1
        row += 1
    
    if testing:
        print("Location Grid")
        for x in tileLocs:
            print(x)

    testing and print("\nCombining tiles")
    #Combining the strings of the lines of each tile, index by index, before adding them to the final map
    finalMap = []
    for r in tileLocs:
        testing and print("\tLocation Row:", r)
        #Since we have to remove the outside edge of each tile, we ignore the first and last rows
        for line in range(1, len(tileStack[r[0]])-1):
            testing and print("\t\tLine:", line)
            mapLine = ""
            for c in r:
                testing and print("\t\t\tLocation Col:", c)
                #Making sure to ignore the first and last char of every line to remove the outside edge
                mapLine = mapLine + tileStack[c][line][1:-1]
            finalMap.append(mapLine)

    if testing:
        print("Final Map:")
        for line in finalMap:
            print(line)
            
    #Looking for the sea serpent in this 2D array
    serpent = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]
    #Storing the (row,col) positions of each '#' in the serpent
    serpentLocs = []
    for r in range(len(serpent)):
        for c in range(len(serpent[r])):
            if serpent[r][c] == '#':
                serpentLocs.append((r,c))

                
    def findSerpent():
        '''Sub-function to align the sea serpent array against the final map's current orientation to find any matching locations'''
        for r in range(len(finalMap) - len(serpent)):
            for c in range(len(finalMap[0]) - len(serpent[0])):
                valid = True
                for sl in serpentLocs:
                    #If any of the positions of the serpent locations (at the offset r,c) are empty, it's not a valid serpent location
                    if finalMap[r+sl[0]][c+sl[1]] != '#':
                        valid = False
                        break
                #If it's a valid serpent location, we mark the tiles
                if valid:    
                    testing and print("Valid serpent location at offset", r, c)
                    for sl in serpentLocs:
                        finalMap[r+sl[0]] = finalMap[r+sl[0]][:c+sl[1]] + 'O' + finalMap[r+sl[0]][c+sl[1]+1:]
                    
                    if testing:
                        print("\nNew final map:")
                        for line in finalMap:
                            print(line)
                        
    findSerpent() #Initial orientation
    finalMap = list(zip(*finalMap[::-1])) #Rotate 90deg clockwise
    for line in range(len(finalMap)):
        finalMap[line] = ''.join(finalMap[line])
    findSerpent()
    finalMap = list(zip(*finalMap[::-1])) #Rotate 180deg clockwise
    for line in range(len(finalMap)):
        finalMap[line] = ''.join(finalMap[line])
    findSerpent()
    finalMap = list(zip(*finalMap[::-1])) #Rotate 270deg clockwise
    for line in range(len(finalMap)):
        finalMap[line] = ''.join(finalMap[line])
    findSerpent()
    for line in range(0, len(finalMap)): #Flipping along y-axis
        finalMap[line] = finalMap[line][::-1]
    findSerpent()
    finalMap = list(zip(*finalMap[::-1])) #Rotate 90deg clockwise, flipped
    for line in range(len(finalMap)):
        finalMap[line] = ''.join(finalMap[line])
    findSerpent()
    finalMap = list(zip(*finalMap[::-1])) #Rotate 180deg clockwise, flipped
    for line in range(len(finalMap)):
        finalMap[line] = ''.join(finalMap[line])
    findSerpent()
    finalMap = list(zip(*finalMap[::-1])) #Rotate 270deg clockwise, flipped
    for line in range(len(finalMap)):
        finalMap[line] = ''.join(finalMap[line])
    findSerpent()
    
    #Counting all remaining '#' tiles
    ans = 0
    for line in finalMap:
        ans += line.count('#')
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())