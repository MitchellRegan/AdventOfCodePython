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
            inpt.append([x for x in line])

    return inpt
            

def tileSimilarSides(r:int, c:int, letter:str, inpt:list)->list:
    '''Checks the letter at the given row,col position and returns a list of bools for if the adjacen tiles share the same letter.'''
    adj = [True, True, True, True] #UP, DOWN, LEFT RIGHT in this order

    #up
    if r == 0 or inpt[r-1][c] != letter:
        adj[0] = False
    #down
    if r == len(inpt)-1 or inpt[r+1][c] != letter:
        adj[1] = False
    #left
    if c == 0 or inpt[r][c-1] != letter:
        adj[2] = False
    #right
    if c == len(inpt[0])-1 or inpt[r][c+1] != letter:
        adj[3] = False

    return adj


def solution1():
    inpt = getInput()
    
    ans = 0
    for r in range(len(inpt)):
        for c in range(len(inpt[0])):
            #Skipping spots already found
            if inpt[r][c] == '.':
                continue

            #Performing a bfs to find all connected regions with the same letter
            letter = inpt[r][c]
            q = [(r,c)]
            seen = {(r,c):True}
            area = 0
            perim = 0
            while len(q) > 0:
                lr,lc = q.pop(0)

                perim += tileSimilarSides(lr,lc,letter,inpt).count(False)

                #up
                if lr > 0 and inpt[lr-1][lc] == letter and (lr-1,lc) not in seen.keys():
                    q.append((lr-1,lc))
                    seen[(lr-1,lc)] = True
                #down
                if lr < len(inpt)-1 and inpt[lr+1][lc] == letter and (lr+1,lc) not in seen.keys():
                    q.append((lr+1,lc))
                    seen[(lr+1,lc)] = True
                #left
                if lc > 0 and inpt[lr][lc-1] == letter and (lr,lc-1) not in seen.keys():
                    q.append((lr,lc-1))
                    seen[(lr,lc-1)] = True
                #right
                if lc < len(inpt[0])-1 and inpt[lr][lc+1] == letter and (lr,lc+1) not in seen.keys():
                    q.append((lr,lc+1))
                    seen[(lr,lc+1)] = True

            area = len(seen.keys())
            ans += (area*perim)

            #Marking this entire area to be skipped in future searches
            for s in seen.keys():
                inpt[s[0]][s[1]] = '.'

    return ans


def solution2():
    inpt = getInput()
    
    ans = 0
    for r in range(len(inpt)):
        for c in range(len(inpt[0])):
            #Skipping spots already found
            if inpt[r][c] == '.':
                continue

            #Performing a bfs to find all connected regions with the same letter
            letter = inpt[r][c]
            q = [(r,c)]
            seen = {(r,c):tileSimilarSides(r,c,letter,inpt)}
            perim = 0
            while len(q) > 0:
                lr,lc = q.pop(0)

                perim += seen[(lr,lc)].count(False)

                #up
                if lr > 0 and inpt[lr-1][lc] == letter and (lr-1,lc) not in seen.keys():
                    q.append((lr-1,lc))
                    seen[(lr-1,lc)] = tileSimilarSides(lr-1,lc,letter,inpt)
                #down
                if lr < len(inpt)-1 and inpt[lr+1][lc] == letter and (lr+1,lc) not in seen.keys():
                    q.append((lr+1,lc))
                    seen[(lr+1,lc)] = tileSimilarSides(lr+1,lc,letter,inpt)
                #left
                if lc > 0 and inpt[lr][lc-1] == letter and (lr,lc-1) not in seen.keys():
                    q.append((lr,lc-1))
                    seen[(lr,lc-1)] = tileSimilarSides(lr,lc-1,letter,inpt)
                #right
                if lc < len(inpt[0])-1 and inpt[lr][lc+1] == letter and (lr,lc+1) not in seen.keys():
                    q.append((lr,lc+1))
                    seen[(lr,lc+1)] = tileSimilarSides(lr,lc+1,letter,inpt)

            area = len(seen.keys())
            
            #Checking horizontal sides (top/bottom of adjacent tiles)
            tiles = [x for x in seen.keys()]
            tiles.sort(key = lambda x: (x[0],x[1]))
            testing and print("Tiles for letter", letter, "sorted by ROW (looking for horizontals)\n", tiles)
            for t in range(1, len(tiles)):
                #If two tiles are on the same row and the col is different by 1
                if tiles[t][0] == tiles[t-1][0] and abs(tiles[t][1] - tiles[t-1][1]) == 1:
                    testing and print("\tTiles", tiles[t-1], "and", tiles[t], "are adjacent")
                    #If both tiles are below tiles with different letters
                    if seen[tiles[t]][0] is False and seen[tiles[t-1]][0] is False:
                        perim -= 1
                        testing and print("\t\tSame line above")

                    #If both tiles are above tiles with different letters
                    if seen[tiles[t]][1] is False and seen[tiles[t-1]][1] is False:
                        perim -= 1
                        testing and print("\t\tSame line below")

            #Checking vertical sides (left/right of adjacent tiles)
            tiles.sort(key = lambda x: (x[1],x[0]))
            testing and print("Tiles for letter", letter, "sorted by COL (looking for verticals)\n", tiles)
            for t in range(1, len(tiles)):
                #If two tiles are on the same col and the row is different by 1
                if tiles[t][1] == tiles[t-1][1] and abs(tiles[t][0] - tiles[t-1][0]) == 1:
                    testing and print("\tTiles", tiles[t-1], "and", tiles[t], "are adjacent")
                    #If both tiles are to the right of tiles with different letters
                    if seen[tiles[t]][2] is False and seen[tiles[t-1]][2] is False:
                        perim -= 1
                        testing and print("\t\tSame line left")

                    #If both tiles are to the left of tiles with different letters
                    if seen[tiles[t]][3] is False and seen[tiles[t-1]][3] is False:
                        perim -= 1
                        testing and print("\t\tSame line right")

            testing and print("================", letter, "  Area:", area, "  Sides:", perim, "  total:", area*perim, "\n")
            ans += (area*perim)
            for s in seen.keys():
                inpt[s[0]][s[1]] = '.'

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())