import time
import random
from HelperFunctions import binaryTree
from HelperFunctions import heap
from HelperFunctions import sortingAlgorithms as sa

def binaryTreeTimeTest(iterations=100, elements=100):
    '''Compares the search time for the binary search tree and list.contains
    '''
    #Lists to store the search time for the list.contains time, the binary search time, and complex binary search time
    overallTime = [0,0,0]
    firstIndexTime = [0,0,0]
    quarterIndexTime = [0,0,0]
    middleIndexTime = [0,0,0]
    threeQuarterIndexTime = [0,0,0]
    lastIndexTime = [0,0,0]

    initialList = [x for x in range(0,elements)]
    random.shuffle(initialList)
    binTree = binaryTree.BinarySearchTree()
    binTree.listToBinaryTree(initialList)
    binTree.balanceTree()
    cbinTree = binaryTree.BinarySearchTreeComplex((lambda x,y: x<y))
    cbinTree.listToBinaryTree(initialList)
    cbinTree.balanceTree()

    print("Comparing the Binary Search Tree search time with %d elements over %d iterations" %(elements, iterations))

    for i in range(iterations):
        #Getting the first index
        start = time.time()
        initialList.index(initialList[0])
        firstIndexTime[0] += time.time() - start
        start = time.time()
        binTree.inTree(initialList[0])
        firstIndexTime[1] += time.time() - start
        start = time.time()
        cbinTree.inTree(initialList[0])
        firstIndexTime[2] += time.time() - start

        #Getting the quarter index
        quarter = int(elements // 4)
        start = time.time()
        initialList.index(initialList[quarter])
        quarterIndexTime[0] += time.time() - start
        start = time.time()
        binTree.inTree(initialList[quarter])
        quarterIndexTime[1] += time.time() - start
        start = time.time()
        cbinTree.inTree(initialList[quarter])
        quarterIndexTime[2] += time.time() - start

        #Getting the middle index
        half = int(elements // 2)
        start = time.time()
        initialList.index(initialList[half])
        middleIndexTime[0] += time.time() - start
        start = time.time()
        binTree.inTree(initialList[half])
        middleIndexTime[1] += time.time() - start
        start = time.time()
        cbinTree.inTree(initialList[half])
        middleIndexTime[2] += time.time() - start

        #Getting the three quarter index
        quarter = 3 * int(elements // 4)
        start = time.time()
        initialList.index(initialList[quarter])
        threeQuarterIndexTime[0] += time.time() - start
        start = time.time()
        binTree.inTree(initialList[quarter])
        threeQuarterIndexTime[1] += time.time() - start
        start = time.time()
        cbinTree.inTree(initialList[quarter])
        threeQuarterIndexTime[2] += time.time() - start

        #Getting the quarter index
        last = elements -1
        start = time.time()
        initialList.index(initialList[last])
        lastIndexTime[0] += time.time() - start
        start = time.time()
        binTree.inTree(initialList[last])
        lastIndexTime[1] += time.time() - start
        start = time.time()
        cbinTree.inTree(initialList[last])
        lastIndexTime[2] += time.time() - start
       
        for j in range(0, elements):
            start = time.time()
            initialList.index(initialList[j])
            overallTime[0] += time.time() - start
            start = time.time()
            binTree.inTree(initialList[j])
            overallTime[1] += time.time() - start
            start = time.time()
            cbinTree.inTree(initialList[j])
            overallTime[2] += time.time() - start


    print("\tAverage search times overall:\n\t\tList:                  %f\n\t\tBinary Tree:           %f\n\t\tBinary Tree (Complex): %f" %(overallTime[0]/iterations, overallTime[1]/iterations, overallTime[2]/iterations))
    print("\tAverage search times for the first index:\n\t\tList:                  %f\n\t\tBinary Tree:           %f\n\t\tBinary Tree (Complex): %f" %(firstIndexTime[0]/iterations, firstIndexTime[1]/iterations, firstIndexTime[2]/iterations))
    print("\tAverage search times for the index at the 1/4 mark:\n\t\tList:                  %f\n\t\tBinary Tree:           %f\n\t\tBinary Tree (Complex): %f" %(quarterIndexTime[0]/iterations, quarterIndexTime[1]/iterations, quarterIndexTime[2]/iterations))
    print("\tAverage search times for the middle index:\n\t\tList:                  %f\n\t\tBinary Tree:           %f\n\t\tBinary Tree (Complex): %f" %(middleIndexTime[0]/iterations, middleIndexTime[1]/iterations, middleIndexTime[2]/iterations))
    print("\tAverage search times for the index at the 3/4 mark:\n\t\tList:                  %f\n\t\tBinary Tree:           %f\n\t\tBinary Tree (Complex): %f" %(threeQuarterIndexTime[0]/iterations, threeQuarterIndexTime[1]/iterations, threeQuarterIndexTime[2]/iterations))
    print("\tAverage search times for the last index:\n\t\tList:                  %f\n\t\tBinary Tree:           %f\n\t\tBinary Tree (Complex): %f" %(lastIndexTime[0]/iterations, lastIndexTime[1]/iterations, lastIndexTime[2]/iterations))
    print("\n")


def heapTimeTest(iterations=100, elements=100):
    start = [1,2,3,4,5]
    print("List before Heap:", start)
    bmHeap = heap.BinaryMaxHeap(start)
    print("Heap:", bmHeap)
    bmHeap.insert(0)
    print("After Insert:", bmHeap)
    print("Heap index 3:", bmHeap[3])
    print("Heap slice [2:4]", bmHeap[2:4])
    print("Heap slice [1:]", bmHeap[1:])
    print("Heap slice [:3]", bmHeap[:3])
    print("Length of heap:", len(bmHeap))
    bmHeap.printDepths()
    bmHeap.extend([8,9,10,14,11, -1, -5])
    print(bmHeap)
    bmHeap.printDepths()
    print("Extracting root:", bmHeap.popFront())
    print(bmHeap)
    bmHeap.printDepths()
    print("Is 11 in the heap:", (11 in bmHeap))
    print("Index of element 11:", bmHeap.index(11))
    print("Index of element 99:", bmHeap.index(99))
    bmHeap.remove(11)
    bmHeap.printDepths()
    bmHeap.remove(4)
    bmHeap.printDepths()
    for i in range(0, len(bmHeap)):
        p = bmHeap.getParent(i)
        l = bmHeap.getLeftChild(i)
        r = bmHeap.getRightChild(i)
        print("Element", bmHeap[i], " at index", i)
        if p is None:
            print("\tparent index:", p, "element:", None)
        else:
            print("\tparent index:", p, "element:", bmHeap[p])
        if l is None:
            print("\tleft child index:", l, "element:", None)
        else:
            print("\tleft child index:", l, "element:", bmHeap[l])
        if r is None:
            print("\tright child index:", r, "element:", None)
        else:
            print("\tright child index:", r, "element:", bmHeap[r])

        inOrder = True
        if p is not None and bmHeap[i] > bmHeap[p]:
            print("\tIn order: False.", bmHeap[i], "> parent", bmHeap[p])
        elif l is not None and bmHeap[i] < bmHeap[l]:
            print("\tIn order: False.", bmHeap[i], "< left child", bmHeap[l])
        elif r is not None and bmHeap[i] < bmHeap[r]:
            print("\tIn order: False.", bmHeap[i], "< right child", bmHeap[r])
        else:
            print("\tIn order: True")


def sortingAlgorithmTimeTest(iterations=100):
    print("Testing sorting algorithms")
    import time
    import random
    import HelperFunctions.sortingAlgorithms as sa

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


heapTimeTest()
sortingAlgorithmTimeTest()