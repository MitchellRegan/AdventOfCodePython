#https://adventofcode.com/2022/day/22
#https://adventofcode.com/2022/day/22#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = os.path.join(inFileDir, "InputTestFiles/d22_test.txt")
#inFile = os.path.join(inFileDir, "InputRealFiles/d22_real.txt")

map = []
cube = {
    "front":[],
    "top":[],
    "bottom":[],
    "back":[],
    "left":[],
    "right":[]
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
    return


def makeCube_old():
    real = True

    faces = []
    count = 0
    for i in range(0, len(map), 50):
        row = []
        for j in range(0, len(map[0]), 50):
            if map[i][j] == ' ':
                row.append('')
            else:
                if count == 0:
                    row.append("Front")
                else:
                    row.append(count)
                count += 1
        faces.append(row)
        print(row)



    if real:
        #Manually creating the real input for the cube
        for i in range(0, 50):
            cube["front"].append(map[i][50:100])
        for i in range(0, 50):
            cube["right"].append(map[i][100:150])
        for i in range(50,100):
            cube["bottom"].append(map[i][50:100])
        for i in range(100, 150):
            cube["back"].append(map[i][50:100])
        for i in range(100, 150):
            cube["left"].append(map[i][0:50])
        for i in range(150, 200):
            cube["top"].append(map[i][0:50])
    else:
        #Manually creating the test input for the cube
        for i in range(0,4):
            cube["front"].append(map[i][8:12])
        for i in range(4,8):
            cube["bottom"].append(map[i][8:12])
        #for i in range()
    return


def makeCube():
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
    #Determining if the face sizes are 50x50 tiles (real input) or 4x4 tiles (test input)
    faceSize = 4
    if len(map) % 50 == 0:
        faceSize = 50

    #Determining which faces are next to one another
    faces = []
    count = 0
    for i in range(0, len(map), faceSize):
        row = []
        for j in range(0, len(map[0]), faceSize):
            if map[i][j] == ' ':
                row.append(' ')
            else:
                if count == 0:
                    row.append("Fr")
                else:
                    row.append("?")
                count += 1
        faces.append(row)
        print("".join(row))
    print("-----")

    #Looping until all faces are identified
    while count > 0:
        #Determining which face is which
        for i in range(0, len(faces)):
            for j in range(0, len(faces[i])):
                #When we look at the "Front" face, we check the adjacent faces
                if faces[i][j] == "Fr":
                    #Looking for the "Bottom" face
                    if faces[i+1][j] == "?":
                        faces[i+1][j] = "Bt"
                        count -= 1
                    #Looking for the "Right" face
                    if faces[i][j+1] == "?":
                        faces[i][j+1] = "Rt"
                        count -= 1

                #When we look at non-front faces
                elif faces[i][j] != " ":
                    #Looking at faces in the same row
                    if j > 0 and j < len(faces[i])-1:
                        #If the face to the left is unknown, but the face to the right isn't
                        if faces[i][j-1] == "?" and faces[i][j+1] != "?" and faces[i][j+1] != " ":
                            #If it's either the front or back
                            if faces[i][j+1] in ["Fr","Bk"]:
                                newVal = ["Fr","Bk"]
                                newVal.remove(faces[i][j+1])
                                faces[i][j-1] = newVal[0]
                            #If it's either the right or left
                            elif faces[i][j+1] in ["Rt","Lf"]:
                                newVal = ["Rt","Lf"]
                                newVal.remove(faces[i][j+1])
                                faces[i][j-1] = newVal[0]
                                count -= 1
                            #If it's either the top or bottom
                            elif faces[i][j+1] in ["Tp","Bt"]:
                                newVal = ["Tp","Bt"]
                                newVal.remove(faces[i][j+1])
                                faces[i][j-1] = newVal[0]
                                count -= 1
                        #If the face to the right is unknown, but the face to the left isn't
                        elif faces[i][j+1] == "?" and faces[i][j-1] != "?" and faces[i][j-1] != " ":
                            #If it's either the front or back
                            if faces[i][j-1] in ["Fr","Bk"]:
                                newVal = ["Fr","Bk"]
                                newVal.remove(faces[i][j-1])
                                faces[i][j+1] = newVal[0]
                                count -= 1
                            #If it's either the right or left
                            elif faces[i][j-1] in ["Rt","Lf"]:
                                newVal = ["Rt","Lf"]
                                newVal.remove(faces[i][j-1])
                                faces[i][j+1] = newVal[0]
                                count -= 1
                            #If it's either the top or bottom
                            elif faces[i][j-1] in ["Tp","Bt"]:
                                newVal = ["Tp","Bt"]
                                newVal.remove(faces[i][j-1])
                                faces[i][j+1] = newVal[0]
                                count -= 1
                    #Looking at faces in the same column
                    if i > 0 and i < len(faces)-1:
                        #If the face above is unknown, but the face below isn't
                        if faces[i-1][j] == "?" and faces[i+1][j] != "?" and faces[i+1][j] != " ":
                            #If it's either the front or back
                            if faces[i+1][j] in ["Fr","Bk"]:
                                newVal = ["Fr","Bk"]
                                newVal.remove(faces[i+1][j])
                                faces[i-1][j] = newVal[0]
                                count -= 1
                            #If it's either the right or left
                            elif faces[i+1][j] in ["Rt","Lf"]:
                                newVal = ["Rt","Lf"]
                                newVal.remove(faces[i+1][j])
                                faces[i-1][j] = newVal[0]
                                count -= 1
                            #If it's either the top or bottom
                            elif faces[i+1][j] in ["Tp","Bt"]:
                                newVal = ["Tp","Bt"]
                                newVal.remove(faces[i+1][j])
                                faces[i-1][j] = newVal[0]
                                count -= 1
                        #If the face below is unknown, but the face above isn't
                        elif faces[i+1][j] == "?" and faces[i-1][j] != "?" and faces[i-1][j] != " ":
                            #If it's either the front or back
                            if faces[i-1][j] in ["Fr","Bk"]:
                                newVal = ["Fr","Bk"]
                                newVal.remove(faces[i-1][j])
                                faces[i+1][j] = newVal[0]
                                count -= 1
                            #If it's either the right or left
                            elif faces[i-1][j] in ["Rt","Lf"]:
                                newVal = ["Rt","Lf"]
                                newVal.remove(faces[i-1][j])
                                faces[i+1][j] = newVal[0]
                                count -= 1
                            #If it's either the top or bottom
                            elif faces[i-1][j] in ["Tp","Bt"]:
                                newVal = ["Tp","Bt"]
                                newVal.remove(faces[i-1][j])
                                faces[i+1][j] = newVal[0]
                                count -= 1
        for row in faces:
            print(row)
        break
    return


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
    makeCube()
    return


#print("Year 2022, Day 22 solution part 1:", solution1())
print("Year 2022, Day 22 solution part 2:", solution2())