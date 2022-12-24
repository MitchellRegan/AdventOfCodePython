print(" Advent of Code Solutions")
y = input(" - Select a year: ")

if y == '2015':
    import Year2015
elif y == '2016':
    import Year2016
elif y == '2017':
    import Year2017
elif y == '2018':
    import Year2018
elif y == '2019':
    import Year2019
elif y == '2020':
    import Year2020
elif y == '2021':
    import Year2021
elif y == '2022':
    import Year2022


if True:
    inFile = "D:\\Users\\mrega\\Documents\\AdventOfCodePython\\AdventOfCode\\Year2022\\InputRealFiles\\d23_real.txt"
    import time
    from HelperFunctions import binaryTree as bt

    bin = bt.BinaryTree()
    lc = lambda a,b: a[0] < b[0] or (a[0] == b[0] and a[1] < b[1])
    #bin.lambdaComp = lc
    elfLocs = []
    with open(inFile, 'r') as f:
        row = 0
        for line in f:
            for col in range(0, len(line)):
                if line[col] == '#':
                    elfLocs.append((row, col))
                    bin.insert((row, col))
            row += 1

    #bin.printTree()
    #print(bin.toList())

    bin.balanceTree()
    print("Length of list:", len(elfLocs))
    print("Length of tree:", bin.size)

    start1 = time.time()
    inCount1 = 0
    for i in range(0, len(elfLocs)):
        if elfLocs[i] in elfLocs:
            inCount1 += 1
    end1 = time.time() - start1

    start2 = time.time()
    inCount2 = 0
    for i in range(0, len(elfLocs)):
        if bin.inTree(elfLocs[i]):
            inCount2 += 1
    end2 = time.time() - start2

    print(inCount1, "list check time:", end1)
    print(inCount2, "bin check time: ", end2)
    print("Bin Tree faster?", end2 < end1, '\n')