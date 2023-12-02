#https://adventofcode.com/2023/day/1
#https://adventofcode.com/2023/day/1#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if False:
    inFile = os.path.join(inFileDir, "InputTestFiles/d1_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d1_real.txt")

def solution1():
    sum = 0
    with open(inFile, 'r') as f:
        for line in f:
            num = ''
            for start in line:
                if start in ['1','2','3','4','5','6','7','8','9','0']:
                    num = num + start
                    break
            for end in line[::-1]:
                if end in ['1','2','3','4','5','6','7','8','9','0']:
                    num = num + end
                    break
            sum += int(num)
    return sum


def solution2():
    sum = 0
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    with open(inFile, 'r') as f:
        for line in f:
            num = ''
            foundStart = False
            foundEnd = False

            for start in range(0, len(line)):
                if line[start] in ['1','2','3','4','5','6','7','8','9','0']:
                    num = num + line[start]
                    foundStart = True
                    break
                else:
                    for n in range(0, len(words)):
                        if line[start:start+len(words[n])] == words[n]:
                            num = num + str(1 + n)
                            foundStart = True
                            break
                    if foundStart:
                        break

            for end in range(len(line)-1, -1, -1):
                if line[end] in ['1','2','3','4','5','6','7','8','9','0']:
                    num = num + line[end]
                    foundEnd = True
                    break
                else:
                    for n in range(0, len(words)):
                        if line[end-len(words[n]):end] == words[n]:
                            num = num + str(1 + n)
                            foundEnd = True
                            break
                    if foundEnd:
                        break
            sum += int(num)
    return sum


#print("Year 2023, Day 1 solution part 1:", solution1())
print("Year 2023, Day 1 solution part 2:", solution2())