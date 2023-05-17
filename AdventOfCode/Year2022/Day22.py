#https://adventofcode.com/2022/day/22
#https://adventofcode.com/2022/day/22#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d22_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d22_real.txt")

map = []
map2 = []
#2D list to store the layout of which part of the map corresponds to which cube face
faces = []
#Storing which faces are in which orientation from each face. Index 0: UP, 1: RIGHT, 2: DOWN, 3: LEFT
faceOrientations = {
    "Fr":["Tp","Rt","Bt","Lf"],
    "Bk":["Tp","Lf","Bt","Rt"],
    "Rt":["Tp","Bk","Bt","Fr"],
    "Lf":["Tp","Fr","Bt","Bk"],
    "Tp":["Bk","Rt","Fr","Lf"],
    "Bt":["Fr","Rt","Bk","Lf"]
    }
dir = []

def getInput():
    onMap = True
    maxWidth = 0

    with open(inFile, 'r') as f:
        for line in f:
            if line == '\n':
                onMap = False
            elif onMap:
                line = line[:-1] + ' '
                map.append(line)
                map2.append(line)
                if len(line) > maxWidth:
                    maxWidth = len(line)
            elif not onMap:
                i = 0
                while i < len(line):
                    if line[i] == 'R' or line[i] == 'L':
                        dir.append(int(line[0:i]))
                        dir.append(line[i])
                        line = line[i+1:]
                        i = 0
                    else:
                        i += 1
                dir.append(int(line))

    for r in range(0, len(map)):
        if len(map[r]) < maxWidth:
            fillSpace = ''
            for s in range(0, maxWidth-len(map[r])):
                fillSpace += ' '
            map[r] = map[r] + fillSpace
            map2[r] = map2[r] + fillSpace
    return


def identifyOrientation(f_, i_, j_):
    '''Recursive function called from makeCube to identify the orientation of the given cube face and fill in unknown sides in the global "faces" 2D list.
    param f_: String for which face is being looked at. One of the following: Fr, Bk, Lf, Rt, Tp, Bt.
    param i_: The row index of the current face in the "faces" 2D list.
    param j_: The column index of the current face in the "faces" 2D list.
    '''
    #List to track which faces to recursively call this method on. Bools for if we should recursively call on Up, Right, Down, Left positions
    recur = [False, False, False, False]
    #Identifying which faces are adjacent. "None" indicates it goes off the map, "?" is an unknown face, and otherwise it's a known face.
    up = None
    if i_ > 0 and faces[i_-1][j_] != "  ":
        up = faces[i_-1][j_]
        if faces[i_-1][j_] == "??":
            recur[0] = True

    right = None
    if j_+1 < len(faces[i_]) and faces[i_][j_+1] != "  ":
        right = faces[i_][j_+1]
        if faces[i_][j_+1] == "??":
            recur[1] = True

    down = None
    if i_+1 < len(faces) and faces[i_+1][j_] != "  ":
        down = faces[i_+1][j_]
        if faces[i_+1][j_] == "??":
            recur[2] = True

    left = None
    if j_ > 0 and faces[i_][j_-1] != "  ":
        left = faces[i_][j_-1]
        if faces[i_][j_-1] == "??":
            recur[3] = True

    #Checking all 4 orientation rotations for the current face
    for x in range(0, 4):
        #If the current orientation matches up with one other face, it's the correct orientation
        if (up != None and up == faceOrientations[f_][0]) or (right != None and right == faceOrientations[f_][1]) or (down != None and down == faceOrientations[f_][2]) or (left != None and left == faceOrientations[f_][3]):
            #We can set the labels of each of the unknown faces
            if up != None:
                faces[i_-1][j_] = faceOrientations[f_][0]
            if right != None:
                faces[i_][j_+1] = faceOrientations[f_][1]
            if down != None:
                faces[i_+1][j_] = faceOrientations[f_][2]
            if left != None:
                faces[i_][j_-1] = faceOrientations[f_][3]
            break
        #Otherwise, we rotate the orientation 90 degrees clockwise and try again
        else:
            newOrient = faceOrientations[f_]
            newOrient.append(newOrient[0])
            newOrient.pop(0)
            faceOrientations[f_] = newOrient
            
    #Recursively calling this method on any of the faces that initially showed up as "?"
    if recur[0]:
        identifyOrientation(faceOrientations[f_][0], i_-1, j_)
    if recur[1]:
        identifyOrientation(faceOrientations[f_][1], i_, j_+1)
    if recur[2]:
        identifyOrientation(faceOrientations[f_][2], i_+1, j_)
    if recur[3]:
        identifyOrientation(faceOrientations[f_][3], i_, j_-1)
    return


def makeCube(faceSize):
    '''Function to identify which parts of the input map is which face.
    Fr = Front
    Bk = Back
    Rt = Right
    Lf = Left
    Tp = Top
    Bt = Bottom
             Bk
          ___V___
         /  Tp  /|
        /_____ / |
       |      |Rt|
    Lf |  Fr  | /
       |______|/
          ^
          Bt
    '''
    #Determining which areas of the map are faces of the cube
    foundFront = False
    frow = 0
    fcol = 0
    for i in range(0, len(map), faceSize):
        row = []
        for j in range(0, len(map[0]), faceSize):
            #Empty sections of the map are just spaces
            if map[i][j] == ' ':
                row.append('  ')
            #The first identified space of the map on the top row is the "Front" face
            else:
                if not foundFront:
                    row.append("Fr")
                    frow = i
                    fcol = len(row)-1
                    foundFront = True
                #All other faces will be determined later
                else:
                    row.append("??")
        faces.append(row)

    #Identifying the faces that are adjacent to the front (bottom or right) and recursively identifying other faces
    if fcol+1 < len(faces[0]) and faces[frow][fcol+1] == "??":
        faces[frow][fcol+1] = "Rt"
        identifyOrientation("Rt", frow, fcol+1)
    if frow+1 < len(faces) and faces[frow+1][fcol] == "??":
        faces[frow+1][fcol] = "Bt"
        identifyOrientation("Bt", frow+1, fcol)

    #for row in faces:
    #    print(" ".join(row))

    #print("Orientations:")
    #for key in faceOrientations.keys():
    #    print(" -", key, ":", faceOrientations[key])


def travelBetweenFaces(r_, c_, dir_, faceSize_):
    '''Function to find the next position on the map when traveling between cube faces with different orientations.
    param r_: Int for the current row position on the map.
    param c_: Int for the current col position on the map.
    param dir_: Int for the direction that is being traveled: U - Up, R - Right, D - Down, L - Left.
    param faceSize_: Int for the dimension of each cube face. 4x4 is the test input, 50x50 is for the real input.
    return: A tuple for (newRow, newCol, newDir).
    '''
    #Finding the ID of the face that we're currently on (Fr, Bk, Tp, Bt, Lf, Rt)
    currFace = faces[int(r_/faceSize_)][int(c_/faceSize_)]
    #Based on the direction we're traveling out of the current face, we can use our orientation to find the ID of the next face
    directionEnum = ["U", "R", "D", "L"]
    nextFace = faceOrientations[currFace][directionEnum.index(dir_)]
    #The new direction we're facing is the opposite of whichever side of the face we come out on (i.e if we arrive from the top, we're going Down)
    newDir = faceOrientations[nextFace].index(currFace) + 2
    newDir = directionEnum[newDir%4]

    #Finding which map coordinates are encompassed by each face
    currFaceRowRange = []
    currFaceColRange = []
    nextFaceRowRange = []
    nextFaceColRange = []
    for i in range(0, len(faces)):
        for j in range(0, len(faces[i])):
            if faces[i][j] == currFace:
                currFaceRowRange = [i*faceSize_, (i+1)*faceSize_ - 1]
                currFaceColRange = [j*faceSize_, (j+1)*faceSize_ - 1]
            elif faces[i][j] == nextFace:
                nextFaceRowRange = [i*faceSize_, (i+1)*faceSize_ - 1]
                nextFaceColRange = [j*faceSize_, (j+1)*faceSize_ - 1]

    #print("Current face:", currFace)
    #print("\t- Traveling", dir_)
    #print("\t- Face Orientation:", faceOrientations[currFace])
    #print("\t- Rows:", currFaceRowRange[0], "-", currFaceRowRange[1])
    #print("\t- Cols:", currFaceColRange[0], "-", currFaceColRange[1])

    #print("Next face:", nextFace)
    #print("\t- Traveling", newDir)
    #print("\t- Face Orientation:", faceOrientations[nextFace])
    #print("\t- Rows:", nextFaceRowRange[0], "-", nextFaceRowRange[1])
    #print("\t- Cols:", nextFaceColRange[0], "-", nextFaceColRange[1])

    #Finding the new row/column coordinates on the next face
    newRow = 0
    newCol = 0

    if newDir == "U":
        newRow = nextFaceRowRange[1]
    elif newDir == "D":
        newRow = nextFaceRowRange[0]
    elif newDir == "L":
        newCol = nextFaceColRange[1]
    elif newDir == "R":
        newCol = nextFaceColRange[0]

    dirCombo = dir_ + newDir
    #Same direction
    if dirCombo == "UU" or dirCombo == "DD":
        newCol = nextFaceColRange[0] + (c_ - currFaceColRange[0])
    elif dirCombo == "RR" or dirCombo == "LL":
        newRow = nextFaceRowRange[0] + (r_ - currFaceRowRange[0])
    #Opposite direction
    elif dirCombo == "UD" or dirCombo == "DU":
        newCol = nextFaceColRange[1] - (c_ - currFaceColRange[0])
    elif dirCombo == "RL" or dirCombo == "LR":
        newRow = nextFaceRowRange[1] - (r_ - currFaceRowRange[0])
    #Horizontal to vertical
    elif dirCombo == "RD" or dirCombo == "LU":
        newCol = nextFaceColRange[1] - (r_ - currFaceRowRange[0])
    elif dirCombo == "RU" or dirCombo == "LD":
        newCol = nextFaceColRange[0] + (r_ - currFaceRowRange[0])
    #Vertical to horizontal
    elif dirCombo == "UR" or dirCombo == "DL":
        newRow = nextFaceRowRange[0] + (c_ - currFaceColRange[0])
    elif dirCombo == "UL" or dirCombo == "DR":
        newRow = nextFaceRowRange[1] - (c_ - currFaceColRange[0])

    #print("New position:", newRow, newCol, newDir)
    #print("----------------------------------------------")
    return (newRow, newCol, newDir)


def solution1():
    getInput()
    facing = 'R'
    r = 0
    c = 0
    for col in range(0, len(map[0])):
        if map[0][col] == '.':
            c = col
            break

    #print("Start pos is row", r, "col", c)
    while len(dir) > 0:
        #print("Instruction:", dir[0], "   Current pos:", r, ",", c)

        #Right turn means turn clockwise 90 degrees
        if dir[0] == 'R':
            if facing == 'R':
                facing = 'D'
            elif facing == 'D':
                facing = 'L'
            elif facing == 'L':
                facing = 'U'
            elif facing == 'U':
                facing = 'R'
            #print(" - Now facing", facing)
        #Left turn means turn anti-clockwise 90 degrees
        elif dir[0] == 'L':
            if facing == 'R':
                facing = 'U'
            elif facing == 'U':
                facing = 'L'
            elif facing == 'L':
                facing = 'D'
            elif facing == 'D':
                facing = 'R'
            #print(" - Now facing", facing)
        #A number means go that many spaces in the direction being faced
        else:
            if facing == 'R':
                for i in range(0, dir[0]):
                    if map[r][c+1] == '.':
                        c += 1
                    elif map[r][c+1] == '#':
                        break
                    elif map[r][c+1] == ' ':
                        opposite = c
                        while True:
                            if opposite - 1 < 0 or map[r][opposite - 1] == ' ':
                                break
                            else:
                                opposite -= 1

                        if map[r][opposite] == '.':
                            #print("Looping right from", r, c, "to", r, opposite)
                            c = opposite
                        elif map[r][opposite] == '#':
                            #print("Can't loop right. is blocked")
                            break
            elif facing == 'L':
                for i in range(0, dir[0]):
                    if c-1 < 0 or map[r][c-1] == ' ':
                        opposite = c
                        while True:
                            if opposite + 1 >= len(map[r]) or map[r][opposite + 1] == ' ':
                                break
                            else:
                                opposite += 1

                        if map[r][opposite] == '.':
                            #print("Looping left from", r, c, "to", r, opposite)
                            c = opposite
                        elif map[r][opposite] == '#':
                            #print("Can't loop left. is blocked")
                            break
                    if map[r][c-1] == '.':
                        c -= 1
                    elif map[r][c-1] == '#':
                        break
            elif facing == 'U':
                for i in range(0, dir[0]):
                    if r-1 < 0 or map[r-1][c] == ' ':
                        opposite = r
                        while True:
                            if opposite + 1 >= len(map) or map[opposite+1][c] == ' ':
                                break
                            else:
                                opposite += 1

                        if map[opposite][c] == '.':
                            #print("Looping up from", r, c, "to", opposite, c)
                            r = opposite
                        elif map[opposite][c] == '#':
                            #print("Can't loop up. is blocked")
                            break
                    elif map[r-1][c] == '.':
                        r -= 1
                    elif map[r-1][c] == '#':
                        break
            elif facing == 'D':
                for i in range(0, dir[0]):
                    if r+1 >= len(map) or map[r+1][c] == ' ':
                        opposite = r
                        while True:
                            if opposite - 1 < 0 or map[opposite-1][c] == ' ':
                                break
                            else:
                                opposite -= 1

                        if map[opposite][c] == '.':
                            #print("Looping down from", r, c, "to", opposite, c)
                            r = opposite
                        elif map[opposite][c] == '#':
                            #print("Can't loop down. is blocked")
                            break
                    elif map[r+1][c] == '.':
                        r += 1
                    elif map[r+1][c] == '#':
                        break
        dir.pop(0)

    score = (1000 * (r+1)) + (4 * (c+1))
    if facing == 'R':
        score += 0
    elif facing == 'D':
        score += 1
    elif facing == 'L':
        score += 2
    elif facing == 'U':
        score += 3

    print("End row:", r, "col:", c, "facing:", facing)
    return score


def solution2():
    getInput()

    #Determining if the face sizes are 50x50 tiles (real input) or 4x4 tiles (test input)
    faceSize = 4
    if len(map) % 50 == 0:
        faceSize = 50

    #Identifying the faces and their orientations
    makeCube(faceSize)

    facing = 'R'
    r = 0
    c = 0
    for col in range(0, len(map[0])):
        if map[0][col] == '.':
            c = col
            break

    #print("Start pos is row", r, "col", c)
    while len(dir) > 0:
        #print("Instruction:", dir[0], "   Current pos:", r, ",", c)

        #Right turn means turn clockwise 90 degrees
        if dir[0] == 'R':
            if facing == 'R':
                facing = 'D'
            elif facing == 'D':
                facing = 'L'
            elif facing == 'L':
                facing = 'U'
            elif facing == 'U':
                facing = 'R'
            #print(" - Now facing", facing)
        #Left turn means turn anti-clockwise 90 degrees
        elif dir[0] == 'L':
            if facing == 'R':
                facing = 'U'
            elif facing == 'U':
                facing = 'L'
            elif facing == 'L':
                facing = 'D'
            elif facing == 'D':
                facing = 'R'
            #print(" - Now facing", facing)
        #A number means go that many spaces in the direction being faced
        else:
            if facing == 'R':
                for i in range(0, dir[0]):
                    map2[r] = map2[r][:c] + ">" + map2[r][c+1:]
                    if map[r][c+1] == '.':
                        c += 1
                    elif map[r][c+1] == '#':
                        break
                    elif map[r][c+1] == ' ':
                        #print("\tGoing out of bounds RIGHT at row", r, "col", c)
                        nextPos = travelBetweenFaces(r, c, facing, faceSize)

                        if map[nextPos[0]][nextPos[1]] == '.':
                            #print("Looping right from", r, c, "to", r, opposite)
                            r = nextPos[0]
                            c = nextPos[1]
                            facing = nextPos[2]
                            dir.insert(1, dir[0] - i - 1)
                            break
                        elif map[nextPos[0]][nextPos[1]] == '#':
                            #print("Can't loop right. is blocked")
                            break
            elif facing == 'L':
                for i in range(0, dir[0]):
                    map2[r] = map2[r][:c] + "<" + map2[r][c+1:]
                    if c-1 < 0 or map[r][c-1] == ' ':
                        #print("\tGoing out of bounds LEFT at row", r, "col", c)
                        nextPos = travelBetweenFaces(r, c, facing, faceSize)

                        if map[nextPos[0]][nextPos[1]] == '.':
                            #print("Looping left from", r, c, "to", r, opposite)
                            r = nextPos[0]
                            c = nextPos[1]
                            facing = nextPos[2]
                            dir.insert(1, dir[0] - i - 1)
                            break
                        elif map[nextPos[0]][nextPos[1]] == '#':
                            #print("Can't loop left. is blocked")
                            break
                    if map[r][c-1] == '.':
                        c -= 1
                    elif map[r][c-1] == '#':
                        break
            elif facing == 'U':
                for i in range(0, dir[0]):
                    map2[r] = map2[r][:c] + "^" + map2[r][c+1:]
                    if r-1 < 0 or map[r-1][c] == ' ':
                        #print("\tGoing out of bounds UP at row", r, "col", c)
                        nextPos = travelBetweenFaces(r, c, facing, faceSize)

                        if map[nextPos[0]][nextPos[1]] == '.':
                            #print("Looping left from", r, c, "to", r, opposite)
                            r = nextPos[0]
                            c = nextPos[1]
                            facing = nextPos[2]
                            dir.insert(1, dir[0] - i - 1)
                            break
                        elif map[nextPos[0]][nextPos[1]] == '#':
                            #print("Can't loop left. is blocked")
                            break
                    elif map[r-1][c] == '.':
                        r -= 1
                    elif map[r-1][c] == '#':
                        break
            elif facing == 'D':
                for i in range(0, dir[0]):
                    map2[r] = map2[r][:c] + "V" + map2[r][c+1:]
                    if r+1 >= len(map) or map[r+1][c] == ' ':
                        #print("\tGoing out of bounds DOWN at row", r, "col", c)
                        nextPos = travelBetweenFaces(r, c, facing, faceSize)

                        if map[nextPos[0]][nextPos[1]] == '.':
                            #print("Looping left from", r, c, "to", r, opposite)
                            r = nextPos[0]
                            c = nextPos[1]
                            facing = nextPos[2]
                            dir.insert(1, dir[0] - i - 1)
                            break
                        elif map[nextPos[0]][nextPos[1]] == '#':
                            #print("Can't loop left. is blocked")
                            break
                    elif map[r+1][c] == '.':
                        r += 1
                    elif map[r+1][c] == '#':
                        break
        dir.pop(0)

    score = (1000 * (r+1)) + (4 * (c+1))
    if facing == 'R':
        score += 0
    elif facing == 'D':
        score += 1
    elif facing == 'L':
        score += 2
    elif facing == 'U':
        score += 3

    #print("End row:", r, "col:", c, "facing:", facing)
    #for row in map2:
    #    print("".join(row))
    return score


print("Year 2022, Day 22 solution part 1:", solution1())
print("Year 2022, Day 22 solution part 2:", solution2())