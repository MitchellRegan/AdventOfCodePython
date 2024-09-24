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
            line = line.replace('\n', '').split("\t")
            inpt = [int(x) for x in line]
    return inpt
            

def solution1():
    blocks = getInput()
    
    seen = {tuple(blocks):True}
    while True:
        testing and print("Blocks:", blocks)
        bestInd = blocks.index(max(blocks))
        testing and print("\tBest index:", bestInd, "    Block size:", blocks[bestInd])
        
        for i in range(blocks[bestInd]):
            offset = bestInd + 1 + i
            while offset >= len(blocks):
                offset -= len(blocks)
            blocks[offset] += 1
            blocks[bestInd] -= 1
            
        testing and print("\tAfter distribution:", blocks)
        if tuple(blocks) in seen.keys():
            break
        else:
            seen[tuple(blocks)] = True

    return len(seen.keys())


def solution2():
    blocks = getInput()
    
    firstDupeState = None
    dupeCycles = 0
    seen = {tuple(blocks):True}
    while True:
        testing and print("Blocks:", blocks)
        bestInd = blocks.index(max(blocks))
        testing and print("\tBest index:", bestInd, "    Block size:", blocks[bestInd])
        
        for i in range(blocks[bestInd]):
            offset = bestInd + 1 + i
            while offset >= len(blocks):
                offset -= len(blocks)
            blocks[offset] += 1
            blocks[bestInd] -= 1
            
        testing and print("\tAfter distribution:", blocks)
        if firstDupeState is None:
            if tuple(blocks) in seen.keys():
                firstDupeState = tuple(blocks)
            else:
                seen[tuple(blocks)] = True
        else:
            dupeCycles += 1
            if tuple(blocks) == firstDupeState:
                break

    return dupeCycles


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())