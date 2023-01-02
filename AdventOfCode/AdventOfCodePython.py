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
    import time
    import random
    import HelperFunctions.sortingAlgorithms as sa

    iterations = 100
    exampleList = [x for x in range(25, -1, -1)]
    random.shuffle(exampleList)

    print("Start:         ", exampleList)

    start = time.time()
    for i in range(iterations):
        bubbleList = [x for x in exampleList]
        sa.bubble_sort(bubbleList)
    end = time.time() - start
    print("Bubble Sort:   ", bubbleList, "Time: %.8f" % end)

    start = time.time()
    for i in range(iterations):
        coctailList = [x for x in exampleList]
        sa.coctail_shaker_sort(coctailList)
    end = time.time() - start
    print("Coctail Sort:  ", coctailList, "Time: %.8f" % end)

    start = time.time()
    for i in range(iterations):
        insertList = [x for x in exampleList]
        sa.insertion_sort(insertList)
    end = time.time() - start
    print("Insertion Sort:", insertList, "Time: %.8f" % end)

    start = time.time()
    for i in range(iterations):
        shellList = [x for x in exampleList]
        sa.shell_sort(shellList)
    end = time.time() - start
    print("Shell Sort:    ", shellList, "Time: %.8f" % end)

    start = time.time()
    for i in range(iterations):
        combList = [x for x in exampleList]
        sa.comb_sort(combList)
    end = time.time() - start
    print("Comb Sort:     ", combList, "Time: %.8f" % end)

    start = time.time()
    for i in range(iterations):
        mergeList = [x for x in exampleList]
        sa.merge_sort_top_down(mergeList)
    end = time.time() - start
    print("Merge Sort:    ", mergeList, "Time: %.8f" % end)

    start = time.time()
    for i in range(iterations):
        selectionList = [x for x in exampleList]
        sa.selection_sort(selectionList)
    end = time.time() - start
    print("Selection Sort:", selectionList, "Time: %.8f" % end)


if False:
    inFile = "D:\\Users\\mrega\\Documents\\AdventOfCodePython\\AdventOfCode\\Year2022\\InputRealFiles\\d23_real.txt"
    #inFile = "D:\\Users\\mrega\\Documents\\AdventOfCodePython\\AdventOfCode\\Year2022\\InputTestFiles\\d23_test.txt"
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