#https://adventofcode.com/2022/day/13
#https://adventofcode.com/2022/day/13#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d13_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d13_real.txt")


def parseListString(str):
    listOfLists = [[]]
    listValStr = ""

    for c in range(0, len(str)):
        #If the char is '[' we need to create a new internal list
        if str[c] is '[':
            listOfLists.append([])
        #If the char is ']', the internal list is finished and we add it to the next outer list
        elif str[c] is ']':
            #Making sure to check for unconverted values
            if len(listValStr) > 0:
                val = int(listValStr)
                #If the last element in the list of lists is a list, this value is added to it
                if len(listOfLists) > 0 and type(listOfLists[-1]) == list:
                    listOfLists[-1].append(val)
                #Otherwise the value is just appended to the whole list
                else:
                    listOfLists.append(val)

                listValStr = ''

            completedList = listOfLists.pop()
            listOfLists[-1].append(completedList)
        #If the char is ',' then we convert the list value string into an int and add it to the current list
        elif str[c] is ',':
           if len(listValStr) > 0:
                val = int(listValStr)
                #If the last element in the list of lists is a list, this value is added to it
                if len(listOfLists) > 0 and type(listOfLists[-1]) == list:
                    listOfLists[-1].append(val)
                #Otherwise the value is just appended to the whole list
                else:
                    listOfLists.append(val)

                listValStr = ''
        #Otherwise it should be a char for an int that we combine in the list value string to convert later
        else:
            listValStr += str[c]

    return listOfLists[0].pop()


def getInputList():
    input = []

    with open(inFile, 'r') as f:
        lineCount = 0
        left = []
        right = []
        for line in f:
            #Getting the left input
            if lineCount == 0:
                str = line
                if str[-1] == '\n':
                    str = str[:-1]
                left = parseListString(str)
            #Getting the right input
            elif lineCount == 1:
                str = line
                if str[-1] == '\n':
                    str = str[:-1]
                right = parseListString(str)
                #Adding the left and right to the input list as its own list pair
                input.append([left,right])
            #Resetting on blank lines
            else:
                left = []
                right = []
                lineCount = -1

            lineCount += 1

    return input


def compareLists(left, right):
    '''Compares 2 given lists to see if the nested values in the left are smaller than on the right.
    Returns: -1 if right is smaller (out of order).
    Returns: 0 if both are the same.
    Returns: 1 if left is smaller (in order).
    '''
    #If the given inputs are of mixed type, we need to convert them to both be lists
    if type(left) == list and type(right) is not list:
        return compareLists(left, [right])
    elif type(left) is not list and type(right) == list:
        return compareLists([left], right)

    #If the left list is empty while the right isn't, it's in order
    if len(left) == 0 and len(right) > 0:
        return 1
    #If the right list is empty while the left isn't, it's out of order
    elif len(left) > 0 and len(right) == 0:
        return -1

    #Iterating through each value in the lists to compare
    for i in range(0, min(len(right), len(left))):
        #If both values at the current index are ints, we compare directly
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] < right[i]:
                return 1
            elif left[i] > right[i]:
                return -1
        #Otherwise we compare the mixed types
        else:
            compVal = compareLists(left[i], right[i])
            if compVal != 0:
                return compVal

    #If all of the int comparisons are inconclusive, we check the length of the lists. Right must be longer to be in order
    if len(left) > len(right):
        return -1
    elif len(left) < len(right):
        return 1

    #If we make it this far, the result is inconclusive
    return 0


def solution1():
    sum = 0
    #Getting the input as a list of pairs of lists to compare
    groups = getInputList()

    #Iterating through each pair of lists to see if they're in order
    for g in range(0, len(groups)):
        inOrder = compareLists(groups[g][0], groups[g][1])
        #If the lists are in the correct order, we add the index of this group to the sum
        if inOrder == 1:
            sum += g + 1
    return sum


def solution2():
    #Getting the input as a list of pairs of lists to compare
    groups = getInputList()
    #List to contain every packet, regardles of pair
    packets = []

    #Adding each packet from the group to our packet list
    for g in groups:
        packets.append(g[0])
        packets.append(g[1])
    #Adding the two new divider packets
    packets.append([[2]])
    packets.append([[6]])

    #Doing a super slow bubble sort to make sure all packets are in order
    for i in range(0, len(packets)-1):
        for j in range(i+1, len(packets)):
            #Comparing the lists to see which is smaller
            compVal = compareLists(packets[i], packets[j])
            #If the right value is smaller, we shuffle them
            if compVal == -1:
                placeholder = packets[i]
                packets[i] = packets[j]
                packets[j] = placeholder

    return (packets.index([[2]])+1) * (packets.index([[6]])+1)


print("Year 2022, Day 13 solution part 1:", solution1())
print("Year 2022, Day 13 solution part 2:", solution2())