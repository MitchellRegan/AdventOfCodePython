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
            if line[0] == "bot":
                bot = 'b'+line[1]
                l = line[5][0] + line[6]
                h = line[-2][0] + line[-1]
                inpt.append((bot, l, h))
            else:
                inpt.append((int(line[1]), line[-2][0]+line[-1]))

    return inpt
            

def solution1():
    inpt = getInput()
    nodes = {} #Key = string for node name, Value = [input 1, input 2, low output, high output]
    outputNodes = []
    
    for i in inpt:
        if len(i) == 2:
            testing and print("Value", i[0], "-> bot", i[1])
            if i[1] not in nodes.keys():
                nodes[i[1]] = [None, None, None, None]
            if nodes[i[1]][0] is None:
                nodes[i[1]][0] = i[0]
            else:
                nodes[i[1]][1] = i[0]
        else:
            testing and print("Bot", i[0], "low:", i[1], "high:", i[2])
            for n in i:
                if n not in nodes.keys():
                    nodes[n] = [None, None, None, None]
                if n[0] == 'o':
                    outputNodes.append(n)
            #Setting the current node's low/high outputs
            nodes[i[0]][2] = i[1]
            nodes[i[0]][3] = i[2]
            #Setting the low/high nodes' inputs
            if nodes[i[1]][0] is None:
                nodes[i[1]][0] = i[0]
            else:
                nodes[i[1]][1] = i[0]
            if nodes[i[2]][0] is None:
                nodes[i[2]][0] = i[0]
            else:
                nodes[i[2]][1] = i[0]
            

    if testing:
        print("\nNodes:")
        for n in nodes.keys():
            print("\t", n, ":", nodes[n])
        print("\nOutput Nodes:", outputNodes)
        
    def getNodeVal(n_:str, next_:str)->int:
        '''Determines which int value is passed from the given node to the next node.'''
        #Making sure both of this node's inputs are ints
        if type(nodes[n_][0]) is not int:
            nodes[n_][0] = getNodeVal(nodes[n_][0], n_)
        if type(nodes[n_][1]) is not int:
            nodes[n_][1] = getNodeVal(nodes[n_][1], n_)
            
        #If the next node gets the low output
        if nodes[n_][2] == next_:
            return min(nodes[n_][0], nodes[n_][1])
        #If the next node gets the high output
        return max(nodes[n_][0], nodes[n_][1])
    

    for on in outputNodes:
        nodes[on][0] = getNodeVal(nodes[on][0], on)
        
    testing and print("\nNodes after setting ints:")
    for n in nodes.keys():
        testing and print("\t", n, ":", nodes[n])
        i = (nodes[n][0], nodes[n][1])
        if i == (61,17) or i == (17,61):
            return n[1:]

    return


def solution2():
    inpt = getInput()
    nodes = {} #Key = string for node name, Value = [input 1, input 2, low output, high output]
    outputNodes = []
    
    for i in inpt:
        if len(i) == 2:
            if i[1] not in nodes.keys():
                nodes[i[1]] = [None, None, None, None]
            if nodes[i[1]][0] is None:
                nodes[i[1]][0] = i[0]
            else:
                nodes[i[1]][1] = i[0]
        else:
            for n in i:
                if n not in nodes.keys():
                    nodes[n] = [None, None, None, None]
                if n[0] == 'o':
                    outputNodes.append(n)
            #Setting the current node's low/high outputs
            nodes[i[0]][2] = i[1]
            nodes[i[0]][3] = i[2]
            #Setting the low/high nodes' inputs
            if nodes[i[1]][0] is None:
                nodes[i[1]][0] = i[0]
            else:
                nodes[i[1]][1] = i[0]
            if nodes[i[2]][0] is None:
                nodes[i[2]][0] = i[0]
            else:
                nodes[i[2]][1] = i[0]
        
    def getNodeVal(n_:str, next_:str)->int:
        '''Determines which int value is passed from the given node to the next node.'''
        #Making sure both of this node's inputs are ints
        if type(nodes[n_][0]) is not int:
            nodes[n_][0] = getNodeVal(nodes[n_][0], n_)
        if type(nodes[n_][1]) is not int:
            nodes[n_][1] = getNodeVal(nodes[n_][1], n_)
            
        #If the next node gets the low output
        if nodes[n_][2] == next_:
            return min(nodes[n_][0], nodes[n_][1])
        #If the next node gets the high output
        return max(nodes[n_][0], nodes[n_][1])
    

    for on in outputNodes:
        nodes[on][0] = getNodeVal(nodes[on][0], on)
        
    return nodes['o0'][0] * nodes['o1'][0] * nodes['o2'][0]


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())