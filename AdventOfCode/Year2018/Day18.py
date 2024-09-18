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
            line = line.replace('\n', '')
            inpt.append(line)
    return inpt
            

def solution1():
    inpt = getInput()
    
    if testing:
        print("Initial state:")
        for line in inpt:
            print(line)
            
    for m in range(10):
        nextState = []
        for r in range(len(inpt)):
            nextLine = ''
            for c in range(len(inpt[0])):
                #Checking the adjacent tiles for the count of open acres, trees, and lumberyards
                adjOpen = 0
                adjTree = 0
                adjLumb = 0
                for adj in [(r-1,c-1), (r-1,c), (r-1,c+1), (r,c-1), (r,c+1), (r+1,c-1), (r+1,c), (r+1,c+1)]:
                    if adj[0] > -1 and adj[0] < len(inpt) and adj[1] > -1 and adj[1] < len(inpt[0]):
                        if inpt[adj[0]][adj[1]] == '.':
                            adjOpen += 1
                        elif inpt[adj[0]][adj[1]] == '|':
                            adjTree += 1
                        elif inpt[adj[0]][adj[1]] == '#':
                            adjLumb += 1

                testing and print("Tile", inpt[r][c], "at pos", r,c, "adjacents:", adjOpen, adjTree, adjLumb)
                if inpt[r][c] == '.': #Open acre
                    if adjTree >= 3:
                        nextLine = nextLine + '|'
                    else:
                        nextLine = nextLine + '.'
                elif inpt[r][c] == '|': #tree
                    if adjLumb >= 3:
                        nextLine = nextLine + '#'
                    else:
                        nextLine = nextLine + '|'
                elif inpt[r][c] == '#': #lumber
                    if adjLumb >= 1 and adjTree >= 1:
                        nextLine = nextLine + '#'
                    else:
                        nextLine = nextLine + '.'
                        
            nextState.append(nextLine)

        if testing:
            print("\nAfter", m+1, "min:")
            for line in nextState:
                print(line)
        inpt = nextState

    numTree = 0
    numLumb = 0
    for line in inpt:
        numTree += line.count('|')
        numLumb += line.count('#')
    testing and print("Final trees:", numTree, "    Final lumber:", numLumb)
    return numTree * numLumb


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())