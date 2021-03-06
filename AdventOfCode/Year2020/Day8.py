#https://adventofcode.com/2020/day/8
#https://adventofcode.com/2020/day/8#part2

# Real Data
data = [['acc',8],['nop',139],['nop',383],['jmp',628],['acc',-6],['acc',29],['acc',9],['jmp',457],['acc',29],['acc',38],['nop',451],['jmp',44],['acc',24],['nop',260],['acc',20],['jmp',24],['acc',36],['acc',41],['acc',31],['acc',42],['jmp',35],['acc',21],['nop',216],['acc',7],['jmp',42],['nop',408],['acc',18],['acc',-4],['jmp',532],['acc',-8],['acc',13],['jmp',529],['acc',36],['jmp',257],['acc',26],['acc',24],['acc',-11],['nop',508],['jmp',249],['acc',44],['acc',25],['jmp',464],['acc',47],['jmp',318],['acc',-6],['acc',-1],['jmp',175],['acc',19],['acc',25],['acc',24],['jmp',523],['acc',-7],['acc',45],['jmp',353],['jmp',67],['acc',-1],['jmp',-17],['acc',-9],['jmp',180],['acc',19],['acc',-15],['acc',5],['jmp',52],['nop',312],['acc',38],['jmp',-6],['acc',6],['acc',-11],['acc',-6],['jmp',357],['jmp',455],['acc',27],['acc',29],['acc',9],['nop',414],['jmp',380],['jmp',1],['acc',33],['jmp',47],['acc',12],['acc',34],['acc',-9],['acc',17],['jmp',214],['jmp',125],['acc',38],['acc',38],['acc',16],['jmp',310],['acc',9],['acc',10],['acc',-2],['nop',-84],['jmp',329],['nop',120],['nop',-70],['jmp',-88],['jmp',1],['jmp',1],['acc',23],['jmp',-34],['nop',372],['acc',18],['acc',3],['acc',24],['jmp',-50],['acc',-11],['acc',27],['nop',441],['jmp',443],['acc',44],['acc',-3],['acc',7],['jmp',389],['acc',-5],['acc',36],['acc',-17],['acc',15],['jmp',13],['acc',39],['jmp',407],['acc',8],['acc',21],['jmp',360],['jmp',425],['acc',7],['acc',29],['acc',6],['jmp',10],['jmp',1],['jmp',426],['acc',23],['jmp',3],['nop',2],['jmp',1],['jmp',240],['acc',16],['jmp',-2],['jmp',47],['jmp',488],['jmp',1],['acc',45],['jmp',1],['acc',20],['jmp',344],['jmp',407],['acc',2],['acc',3],['jmp',117],['acc',50],['jmp',-134],['acc',1],['jmp',238],['acc',27],['acc',-11],['acc',16],['nop',134],['jmp',116],['acc',-16],['nop',393],['jmp',2],['jmp',24],['nop',98],['acc',36],['acc',0],['nop',268],['jmp',131],['nop',294],['acc',23],['acc',26],['acc',43],['jmp',358],['nop',316],['jmp',300],['acc',22],['acc',47],['acc',19],['acc',2],['jmp',228],['jmp',176],['acc',-4],['acc',20],['nop',83],['acc',-19],['jmp',-99],['acc',39],['nop',374],['acc',3],['jmp',57],['jmp',1],['acc',42],['jmp',404],['acc',4],['acc',-4],['acc',-10],['nop',293],['jmp',349],['acc',-9],['acc',33],['jmp',284],['nop',1],['acc',18],['acc',-1],['acc',-5],['jmp',411],['acc',4],['acc',-6],['acc',16],['jmp',313],['acc',0],['acc',39],['jmp',3],['acc',-13],['jmp',148],['nop',51],['nop',-207],['nop',357],['acc',-19],['jmp',409],['acc',32],['jmp',103],['acc',5],['jmp',116],['nop',399],['acc',19],['acc',39],['nop',78],['jmp',298],['acc',-16],['acc',31],['jmp',1],['acc',45],['jmp',-207],['acc',6],['acc',36],['acc',34],['acc',47],['jmp',-112],['acc',23],['acc',4],['jmp',289],['acc',-17],['nop',307],['nop',-92],['jmp',-146],['jmp',293],['nop',44],['acc',5],['acc',2],['acc',-19],['jmp',172],['acc',10],['acc',49],['acc',-2],['jmp',6],['acc',3],['jmp',1],['acc',-19],['acc',35],['jmp',328],['acc',38],['acc',-5],['nop',-83],['jmp',-138],['jmp',-55],['acc',35],['jmp',1],['jmp',-216],['nop',220],['jmp',116],['jmp',-78],['nop',331],['jmp',118],['jmp',287],['jmp',-258],['jmp',-181],['nop',85],['acc',31],['acc',10],['acc',-13],['jmp',175],['jmp',66],['acc',34],['acc',6],['nop',-126],['acc',38],['jmp',4],['acc',18],['jmp',-13],['jmp',-8],['jmp',1],['acc',-9],['acc',31],['nop',92],['jmp',118],['nop',21],['jmp',110],['acc',20],['acc',20],['jmp',280],['jmp',-142],['jmp',8],['nop',-286],['jmp',170],['acc',22],['acc',29],['nop',-127],['jmp',36],['jmp',328],['acc',27],['jmp',-110],['acc',28],['acc',44],['acc',34],['acc',43],['jmp',-42],['acc',-19],['jmp',185],['acc',-8],['nop',-3],['acc',31],['acc',-11],['jmp',142],['acc',49],['acc',-2],['acc',28],['acc',17],['jmp',167],['acc',16],['jmp',165],['jmp',-190],['jmp',-117],['acc',0],['acc',16],['jmp',1],['acc',-10],['jmp',-39],['jmp',69],['jmp',-187],['nop',-101],['jmp',1],['acc',12],['jmp',218],['acc',-6],['jmp',-300],['acc',10],['jmp',104],['jmp',1],['acc',36],['jmp',-243],['nop',138],['acc',-15],['acc',13],['nop',278],['jmp',-192],['acc',13],['jmp',275],['acc',0],['nop',92],['nop',214],['jmp',-90],['acc',44],['nop',225],['acc',9],['jmp',-348],['acc',16],['jmp',-334],['nop',-335],['acc',-16],['acc',-9],['jmp',-89],['acc',35],['acc',2],['acc',26],['jmp',68],['acc',-19],['acc',14],['acc',-19],['acc',-19],['jmp',262],['acc',-16],['nop',-246],['nop',-251],['acc',26],['jmp',143],['nop',48],['acc',48],['jmp',249],['acc',-8],['jmp',9],['acc',42],['acc',12],['acc',19],['acc',-4],['jmp',213],['acc',1],['acc',29],['jmp',-259],['acc',3],['acc',17],['acc',-13],['jmp',-131],['acc',16],['acc',-9],['acc',28],['jmp',222],['acc',42],['acc',20],['acc',-3],['acc',50],['jmp',-339],['jmp',1],['acc',1],['nop',-315],['acc',44],['acc',50],['jmp',-143],['nop',-87],['nop',155],['jmp',1],['nop',44],['jmp',158],['nop',-10],['acc',9],['jmp',90],['jmp',89],['acc',27],['acc',-5],['acc',-8],['acc',40],['jmp',3],['nop',-360],['jmp',117],['acc',-14],['acc',-16],['nop',-184],['acc',20],['jmp',185],['acc',-2],['acc',36],['nop',24],['jmp',195],['acc',-8],['acc',-3],['acc',7],['jmp',-84],['acc',0],['acc',-12],['acc',43],['jmp',-270],['nop',-434],['acc',-15],['jmp',163],['acc',14],['jmp',29],['acc',32],['acc',26],['acc',13],['jmp',-91],['acc',30],['jmp',-163],['nop',175],['jmp',-175],['jmp',20],['acc',0],['nop',-426],['acc',22],['acc',-6],['jmp',-83],['acc',12],['acc',43],['acc',31],['jmp',-46],['acc',27],['acc',26],['acc',24],['acc',-12],['jmp',118],['nop',-88],['nop',-251],['acc',-15],['acc',3],['jmp',-450],['acc',11],['acc',19],['jmp',-406],['acc',39],['jmp',-45],['acc',40],['acc',-7],['acc',22],['nop',-329],['jmp',-160],['jmp',80],['acc',0],['acc',-4],['jmp',31],['acc',11],['acc',-2],['acc',3],['acc',48],['jmp',-366],['acc',-16],['jmp',-345],['jmp',-259],['acc',-8],['acc',29],['acc',4],['acc',2],['jmp',-208],['acc',-6],['acc',48],['acc',-3],['jmp',82],['acc',1],['acc',47],['acc',40],['acc',31],['jmp',-214],['acc',10],['jmp',-328],['acc',-18],['acc',39],['jmp',2],['jmp',-403],['jmp',48],['jmp',19],['jmp',-468],['jmp',-397],['acc',40],['acc',39],['acc',22],['jmp',1],['jmp',-305],['acc',22],['acc',-5],['acc',23],['jmp',-399],['acc',21],['jmp',17],['nop',-239],['acc',0],['acc',29],['acc',2],['jmp',-56],['acc',-14],['acc',23],['jmp',-375],['jmp',-450],['nop',1],['jmp',-29],['jmp',-208],['nop',50],['jmp',-468],['acc',3],['jmp',5],['jmp',-347],['acc',21],['acc',35],['jmp',-527],['acc',-4],['acc',-14],['acc',-5],['nop',24],['jmp',-418],['jmp',66],['acc',8],['acc',-16],['jmp',-447],['nop',-324],['acc',27],['acc',4],['jmp',-393],['jmp',-276],['jmp',1],['acc',37],['acc',15],['nop',-304],['jmp',-534],['acc',-16],['nop',-514],['acc',11],['jmp',-331],['nop',-69],['acc',14],['acc',44],['jmp',-125],['acc',3],['acc',5],['acc',0],['nop',-381],['jmp',-440],['acc',48],['nop',-561],['jmp',-543],['acc',-10],['acc',44],['acc',-16],['acc',45],['jmp',-177],['acc',36],['jmp',-576],['acc',36],['acc',14],['nop',-323],['jmp',-163],['jmp',-118],['acc',-1],['acc',-14],['acc',7],['acc',7],['jmp',11],['acc',31],['nop',-309],['jmp',-109],['acc',41],['acc',11],['acc',4],['jmp',-52],['acc',9],['acc',16],['jmp',-481],['jmp',-161],['acc',-8],['acc',13],['acc',16],['jmp',-488],['acc',30],['jmp',-390],['nop',-313],['jmp',-333],['jmp',-44],['acc',38],['acc',33],['acc',38],['jmp',-619],['jmp',-186],['acc',49],['acc',-5],['acc',-16],['jmp',-214],['acc',16],['acc',35],['nop',-584],['acc',-12],['jmp',1]]
# Test Data
#data = [['nop',0],['acc',1],['jmp',4],['acc',3],['jmp',-3],['acc',-99],['acc',1],['jmp',-4],['acc',6]]


def runInstructions(d_):
    # List to track which instruction index has been seen already
    seenInd = []

    # Tracking the index of the current instruction index and the accumulator
    curInd = 0
    acc = 0

    # Looping until we find that a duplicate instruction is called
    while True:
        # If the current index has already been called, we know to break the loop
        if curInd in seenInd:
            acc = -1
            break
        else:
            seenInd.append(curInd)

        # If the current index reaches the end of the list, the instructions have finished
        if curInd == len(d_):
            break

        # Making sure the index is valid
        if curInd < 0:
            acc = -1
            break

        # Calling the instruction at the current index
        if d_[curInd][0] == 'nop':
            curInd += 1
        elif d_[curInd][0] == 'acc':
            acc += d_[curInd][1]
            curInd += 1
        elif d_[curInd][0] == 'jmp':
            curInd += d_[curInd][1]

    return acc


def solution1():
    # List to track which instruction index has been seen already
    seenInd = []

    # Tracking the index of the current instruction index and the accumulator
    curInd = 0
    acc = 0

    # Looping until we find that a duplicate instruction is called
    while True:
        # If the current index has already been called, we know to break the loop
        if curInd in seenInd:
            break
        else:
            seenInd.append(curInd)

        # Making sure the index is valid
        if curInd < 0 or curInd >= len(data):
            print("Index", curInd, "is out of bounds")
            break

        # Calling the instruction at the current index
        if data[curInd][0] == 'nop':
            curInd += 1
        elif data[curInd][0] == 'acc':
            acc += data[curInd][1]
            curInd += 1
        elif data[curInd][0] == 'jmp':
            curInd += data[curInd][1]

    print("Year 2020, Day 8 solution part 1:", acc)


def solution2():
    # Iterating through each instruction in the list
    for i in range(0, len(data)):
        # If the instruction is NOP, we try swapping it to JMP
        if data[i][0] == 'nop':
            cpy = data[:]
            cpy[i] = ['jmp', cpy[i][1]]
            # Running the instructions with the change
            acc = runInstructions(cpy)
            # If the result isn't -1 (fail), we return the accumulator value
            if acc != -1:
                print("Year 2020, Day 8 solution part 2:", acc)
                return
        # If the instruction is JMP, we try swapping it to NOP
        elif data[i][0] == 'jmp':
            cpy = data[:]
            cpy[i] = ['nop', cpy[i][1]]
            # Running the instructions with the change
            acc = runInstructions(cpy)
            # If the result isn't -1 (fail), we return the accumulator value
            if acc != -1:
                print("Year 2020, Day 8 solution part 2:", acc)
                return

    print("Year 2020, Day 8 solution part 2: FAILED")


solution1()
solution2()