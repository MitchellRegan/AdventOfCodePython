aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = ""

    with open(inFile, 'r') as f:
        for line in f:
            inpt = line.replace('\n', '')

    return inpt
            

def solution1():
    inpt = getInput()
    
    blockChunks = [] #List of tuples for chunks of blocks in the format (blockID, starting block index, number of blocks)
    blockID = 0 #Index number for each file (whole file, not just the blocks). Empty chunks have ID of -1
    isBlock = True #If true, we mark the position of a file block. If False, we mark the position of empty space
    blockIndex = 0 #Current block position we're assigning either "empty" or part of a file

    for i in inpt:
        if isBlock:
            if i != '0':
                blockChunks.append([blockID, blockIndex, int(i)])
            blockID += 1
        elif i != '0':
            blockChunks.append([-1, blockIndex, int(i)])
        isBlock = not isBlock
        blockIndex += int(i)

    #Filling in empty spaces at the front of the emptyChunks with blocks of files from the back of the blockChunks list
    while True:
        ec = 0
        fc = len(blockChunks)-1
        while blockChunks[ec][0] != -1:
            ec += 1
        while blockChunks[fc][0] == -1:
            fc -= 1

        if ec > fc:
            break
        
        #If the file has exactly as many chunks as the current empty space
        if blockChunks[ec][2] == blockChunks[fc][2]:
            testing and print("\tFile", blockChunks[fc][0], "is same size as gap")
            blockChunks[ec][0] = blockChunks[fc][0]
            blockChunks[fc][0] = -1

        #If the file is smaller than the size of empty spaces
        elif blockChunks[ec][2] > blockChunks[fc][2]:
            testing and print("\tFile", blockChunks[fc][0], "is smaller than space")
            blockChunks.insert(ec, [blockChunks[fc][0], blockChunks[ec][1], blockChunks[fc][2]])
            blockChunks[ec+1][1] += blockChunks[fc+1][2]
            blockChunks[ec+1][2] -= blockChunks[fc+1][2]
            blockChunks[fc+1][0] = -1
            
        #If the file is larger than the size of empty spaces
        else:
            testing and print("\tFile", blockChunks[fc][0], "is larger than space")
            blockChunks[ec][0] = blockChunks[fc][0]
            blockChunks.insert(fc+1, [-1, blockChunks[fc][1] + blockChunks[ec][2], blockChunks[ec][2]])
            blockChunks[fc][2] -= blockChunks[ec][2]

    #Merging all consecutive empty chunks
    ec = 0
    while ec < len(blockChunks):
        if blockChunks[ec][0] != -1:
            ec += 1
        elif ec+1 < len(blockChunks):
            blockChunks[ec][2] += blockChunks[ec+1][2]
            blockChunks.pop(ec+1)
        else:
            break

    #Answer is the sum of each block's index multiplied by its file ID
    ans = 0
    for bc in blockChunks:
        if bc[0] != -1:
            for i in range(bc[1], bc[1]+bc[2]):
                val = bc[0] * i
                ans += val
    return ans


def solution2():
    inpt = getInput()
    
    blockChunks = [] #List of tuples for chunks of blocks in the format (blockID, starting block index, number of blocks)
    blockID = 0 #Index number for each file (whole file, not just the blocks). Empty chunks have ID of -1
    isBlock = True #If true, we mark the position of a file block. If False, we mark the position of empty space
    blockIndex = 0 #Current block position we're assigning either "empty" or part of a file

    for i in inpt:
        if isBlock:
            if i != '0':
                blockChunks.append([blockID, blockIndex, int(i)])
            blockID += 1
        elif i != '0':
            blockChunks.append([-1, blockIndex, int(i)])
        isBlock = not isBlock
        blockIndex += int(i)

    #Filling in empty spaces at the front of the emptyChunks with blocks of files from the back of the blockChunks list
    fc = len(blockChunks)-1
    while blockChunks[fc][0] == -1:
        fc -= 1

    while fc > 0:
        #Finding an empty block that can fit the current file's size
        ec = 0
        while ec < fc:
            if blockChunks[ec][0] == -1 and blockChunks[ec][2] >= blockChunks[fc][2]:
                break
            ec += 1

        #If there's no empty space large enough for the current file to move up, we have to move to the next file
        if ec < fc and blockChunks[ec][2] >= blockChunks[fc][2]:
            #If the file has exactly as many chunks as the current empty space
            if blockChunks[ec][2] == blockChunks[fc][2]:
                blockChunks[ec][0] = blockChunks[fc][0]
                blockChunks[fc][0] = -1

            #If the file is smaller than the size of empty spaces
            elif blockChunks[ec][2] > blockChunks[fc][2]:
                blockChunks.insert(ec, [blockChunks[fc][0], blockChunks[ec][1], blockChunks[fc][2]])
                blockChunks[ec+1][1] += blockChunks[fc+1][2]
                blockChunks[ec+1][2] -= blockChunks[fc+1][2]
                blockChunks[fc+1][0] = -1
                fc += 1

        #Getting the next file to move
        fc -= 1
        while blockChunks[fc][0] == -1:
            fc -= 1

    #Merging all consecutive empty chunks
    ec = 0
    while ec < len(blockChunks):
        if blockChunks[ec][0] != -1:
            ec += 1
        elif ec+1 < len(blockChunks) and blockChunks[ec+1][0] == -1:
            blockChunks[ec][2] += blockChunks[ec+1][2]
            blockChunks.pop(ec+1)
        else:
            break
        
    #Answer is the sum of each block's index multiplied by its file ID
    ans = 0
    for bc in blockChunks:
        if bc[0] != -1:
            for i in range(bc[1], bc[1]+bc[2]):
                val = bc[0] * i
                ans += val
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())