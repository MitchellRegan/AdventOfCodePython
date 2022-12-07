#https://adventofcode.com/2022/day/7
#https://adventofcode.com/2022/day/7#part2

#inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2022\\InputTestFiles\\d7_test.txt"
inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2022\\InputRealFiles\\d7_real.txt"

def solution1():
    curDir = ''
    allDirs = {'/':0}

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            if line[0:4] == "$ cd":
                if line[5:7] == '..':
                    tDir = curDir.split('/')
                    if tDir[-1] == '':
                        tDir.pop(-2)
                    else:
                        tDir.pop(-1)
                    curDir = '/'.join(tDir)
                    if curDir == '':
                        curDir = '/'
                else:
                    curDir += line[5:len(line)-1]
                    if curDir is not '/':
                        curDir += '/'
            elif line[0:4] == "$ ls":
                continue
            elif line[0:3] == "dir":
                continue
            else:
                size = int(line.split(' ')[0])
                slashI = []
                for i in range(0, len(curDir)):
                    if curDir[i] == '/':
                        slashI.append(i)

                for i in slashI:
                    dir = curDir[0:i+1]
                    if dir is not '':
                        if dir in allDirs.keys():
                            allDirs[dir] += size
                        else:
                            allDirs[dir] = size

    sum = 0
    for dir in allDirs.keys():
        if allDirs[dir] <= 100000:
            sum += allDirs[dir]

    return sum


def solution2():
    curDir = ''
    allDirs = {'/':0}

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            if line[0:4] == "$ cd":
                if line[5:7] == '..':
                    tDir = curDir.split('/')
                    if tDir[-1] == '':
                        tDir.pop(-2)
                    else:
                        tDir.pop(-1)
                    curDir = '/'.join(tDir)
                    if curDir == '':
                        curDir = '/'
                else:
                    curDir += line[5:len(line)-1]
                    if curDir is not '/':
                        curDir += '/'
            elif line[0:4] == "$ ls":
                continue
            elif line[0:3] == "dir":
                continue
            else:
                size = int(line.split(' ')[0])
                slashI = []
                for i in range(0, len(curDir)):
                    if curDir[i] == '/':
                        slashI.append(i)

                for i in slashI:
                    dir = curDir[0:i+1]
                    if dir is not '':
                        if dir in allDirs.keys():
                            allDirs[dir] += size
                        else:
                            allDirs[dir] = size

    bestDir = '/'
    diskSpace = 70000000
    reqSpace = 30000000
    unusedSpace = diskSpace - allDirs['/']

    for dir in allDirs.keys():
        if allDirs[dir] + unusedSpace >= reqSpace and allDirs[dir] < allDirs[bestDir]:
            bestDir = dir

    return allDirs[bestDir]


print("Year 2022, Day 7 solution part 1:", solution1())
print("Year 2022, Day 7 solution part 2:", solution2())