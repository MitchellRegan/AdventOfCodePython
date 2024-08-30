#https://adventofcode.com/2019/day/8
#https://adventofcode.com/2019/day/8#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 0

r, c = [0, 0]
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d8_test.txt")
    r, c = [2, 2]
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d8_real.txt")
    r, c = [6, 25]


def getInput():
    layers = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            for l in range(0, len(line), (r*c)):
                layers.append(line[l : l + (r*c)])

    return layers
            

def solution1():
    layers = getInput()
    
    bestLayer = 0
    leastZeros = -1
    score = 0
    for i in range(0, len(layers)):
        layer = layers[i]
        zeroCount = layer.count('0')
                
        if leastZeros == -1 or zeroCount < leastZeros:
            bestLayer = layer
            leastZeros = zeroCount
            score = layer.count('1') * layer.count('2')
        
    return score


def solution2(r:int, c:int):
    layers = getInput()
    
    topLayer = [''] * (r * c)
    
    for i in range(0, len(topLayer)):
        for l in layers:
            if l[i] == '0': #black
                topLayer[i] = ' '
                break
            elif l[i] == '1': #white
                topLayer[i] = '#'
                break
            
    for x in range(0, len(topLayer)):
        if x > 0 and x % c == 0:
            print()
        print(topLayer[x], end='')
    print()
    
    return


print("Year 2019, Day 8 solution part 1:", solution1())
print("Year 2019, Day 8 solution part 2:", solution2(r, c))