def combineRanges(inputList, mergeAdjacent=False):
    '''Function to combine a list of integer ranges as much as possible.
    - inputList: 2D list where each element is an inclusive range of integer values, such as [-1,5]
    - mergeAdjacent: If true, will combine ranges whose endpoints are 1 value off. Example: [-1,5] and [6,10] becomes [-1,10]
    - Returns: 2D list containing the merged integer ranges, if any are found.
    '''
    #Making a copy of the input list that we can modify
    rangeList = []
    for i in inputList:
        rangeList.append(i)

    while True:
        #List to hold any changes to do after looping since we can't do them in the loop
        #First index is i to remove, second is j to remove, and last is the new list to append
        newMerges = []

        for i in range(0, len(rangeList)-1):
            if len(newMerges) > 0:
                break
            for j in range(i+1, len(rangeList)):
                #If i is completely inside j
                if rangeList[i][0] >= rangeList[j][0] and rangeList[i][1] <= rangeList[j][1]:
                    newMerges = [i,j, rangeList[j]]
                    break
                #If j is completely inside i
                if rangeList[j][0] >= rangeList[i][0] and rangeList[j][1] <= rangeList[i][1]:
                    newMerges = [i,j, rangeList[i]]
                    break
                #If there's an overlap where i is smaller
                if rangeList[i][0] < rangeList[j][0] and rangeList[i][1] >= rangeList[j][0] and rangeList[i][1] <= rangeList[j][1]:
                    newMerges = [i,j, (rangeList[i][0], rangeList[j][1])]
                    break
                #If there's an overlap where j is smaller
                if rangeList[j][0] < rangeList[i][0] and rangeList[j][1] >= rangeList[i][0] and rangeList[j][1] <= rangeList[i][1]:
                    newMerges = [i,j, (rangeList[j][0], rangeList[i][1])]
                    break
                #If the left edge of i overlaps the right edge of j
                if rangeList[i][1] == rangeList[j][0]:
                    newMerges = [i,j, (rangeList[i][0], rangeList[j][1])]
                    break
                #If the left edge of j overlaps the right edge of i
                if rangeList[j][1] == rangeList[i][0]:
                    newMerges = [i,j, (rangeList[j][0], rangeList[i][1])]
                    break

                #Checking adjacent values if needed
                if mergeAdjacent:
                    #If the left edge of i touches the right edge of j
                if rangeList[i][1] == rangeList[j][0]-1:
                    newMerges = [i,j, (rangeList[i][0], rangeList[j][1])]
                    break
                #If the left edge of j touches the right edge of i
                if rangeList[j][1] == rangeList[i][0]-1:
                    newMerges = [i,j, (rangeList[j][0], rangeList[i][1])]
                    break

        #If there are ranges to merge together we do that
        if len(newMerges) > 0:
            rangeList.append(newMerges[2]) #Append the merged list
            rangeList.pop(newMerges[1]) #Remove index j
            rangeList.pop(newMerges[0]) #Remove index i
        #If there are no merges left, we return the finished list
        else:
            rangeList.sort()
            return rangeList