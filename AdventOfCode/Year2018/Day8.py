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
            line = line.replace('\n', '').split(' ')
            inpt = [int(x) for x in line]
    return inpt
            

def solution1():
    inpt = getInput()
    
    def recursiveNodeTraversal(start_:int)->list:
        '''Recursively searches through the input array to identify nodes.
        
        Parameters
        ----------
            start_: Index for this node's starting point in the input array.
            
        Returns
        ----------
            Sum of all metadata values found.
            Final index of this node in the input array.
        '''
        numChildren = inpt[start_]
        metaEntries = inpt[start_+1]
        testing and print("Node starting at", start_, "    Children:", numChildren, "    Entries:", metaEntries)
        metaSum = 0
        
        #Recursively looping through each child node
        childIndex = start_+2
        for c in range(numChildren):
            testing and print("\tNode", start_, "searching child", c+1, "at index", childIndex)
            childMetaSum, newChildIndex = recursiveNodeTraversal(childIndex)
            metaSum += childMetaSum
            childIndex = newChildIndex
            
        #Looping through all metadata values and adding them to our sum
        for m in range(metaEntries):
            testing and print("\tNode", start_, "metadata value", inpt[childIndex+m], "at index", childIndex+m)
            metaSum += inpt[childIndex + m]
            
        testing and print("\t\tNode", start_, "metadata sum:", metaSum, "    Final index:", childIndex+metaEntries, "==========================")
        return metaSum, childIndex+metaEntries

    return recursiveNodeTraversal(0)[0]


def solution2():
    inpt = getInput()
    
    def recursiveNodeTraversal_v2(start_:int)->list:
        '''Recursively searches through the input array to identify nodes.
        
        Parameters
        ----------
            start_: Index for this node's starting point in the input array.
            
        Returns
        ----------
            Node score, based on number of children and metadata.
            Final index of this node in the input array.
        '''
        numChildren = inpt[start_]
        metaEntries = inpt[start_+1]
        testing and print("Node starting at", start_, "    Children:", numChildren, "    Entries:", metaEntries)
        nodeVal = 0
        
        #Recursively looping through each child node
        childIndex = start_+2
        childVals = []
        for c in range(numChildren):
            testing and print("\tNode", start_, "searching child", c+1, "at index", childIndex)
            childVal, newChildIndex = recursiveNodeTraversal_v2(childIndex)
            childVals.append(childVal)
            childIndex = newChildIndex
            
        #Looping through all metadata values
        for m in range(metaEntries):
            testing and print("\t\tNode", start_, "metadata value", inpt[childIndex+m], "at index", childIndex+m)
            #If this node has no children, the value is the sum of metadata values
            if numChildren == 0:
                nodeVal += inpt[childIndex + m]
            #If this node has children, each metadata value is an index in the childVals array to get a value from
            else:
                if inpt[childIndex+m] <= len(childVals):
                    testing and print("\t\t\tChild at index", inpt[childIndex+m], "value:", childVals[inpt[childIndex+m]-1])
                    nodeVal += childVals[inpt[childIndex+m]-1]
                else:
                    testing and print("\t\t\tChild index", inpt[childIndex+m], "out of bounds and ignored")
            
        testing and print("\t\tNode", start_, "value:", nodeVal, "    Final index:", childIndex+metaEntries, "==========================")
        return nodeVal, childIndex+metaEntries

    return recursiveNodeTraversal_v2(0)[0]


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())