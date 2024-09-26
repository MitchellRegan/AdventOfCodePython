aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    weights = {}
    children = {}
    parents = {}

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').replace('(', '').replace(')', '').replace(',', '').replace(' -> ', ' ').split(' ')
            n = line[0]
            w = int(line[1])
            weights[n] = w
            #If this node has children
            if len(line) > 2:
                children[n] = line[2:]
                for c in line[2:]:
                    parents[c] = n

    return weights, children, parents
            

def solution1():
    weights, children, parents = getInput()
    
    for node in weights.keys():
        if node not in parents.keys():
            return node

    return


def solution2():
    weights, children, parents = getInput()
    
    if testing:
        print("Weights:")
        for w in weights.keys():
            print("\t", w, ":", weights[w])
        print("\nParents -> Children:")
        for c in children.keys():
            print("\t", c, ":", children[c])
    
    def getChildWeightSum(n_)->int:
        '''Recursive function to get the weight of each node's children, and all of their children's children, etc'''
        weightSum = weights[n_]
        if n_ in children.keys():
            for c in children[n_]:
                cWeight = getChildWeightSum(c)
                weightSum += cWeight
        return weightSum

    for node in children.keys():
        childWeights = []
        for c in children[node]:
            childWeights.append(getChildWeightSum(c))
        testing and print("Node", node, "balance:", childWeights)
        if min(childWeights) != max(childWeights):
            testing and print("\tUNBALANCED")
            #Finding the correct weight of all child nodes (all but 1 have the same)
            correctWeight = None
            #Finding the incorrect weight of the unbalanced node, and getting the name of that node
            wrongWeight = None
            unbalancedNode = None
            for cw in childWeights:
                if correctWeight is None and childWeights.count(cw) > 1:
                    correctWeight = cw
                elif childWeights.count(cw) == 1:
                    wrongWeight = cw
                    unbalancedNode = children[node][childWeights.index(wrongWeight)]
                    
            testing and print("\t\tCorrect weight:", correctWeight, "    Wrong weight:", wrongWeight, "\n\t\tUnblanaced child:", unbalancedNode)
            #The answer is the weight of the unbalanced node (just itself) plus the difference between the correct and incorrect weights
            return weights[unbalancedNode] + (correctWeight - wrongWeight)
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())