#https://adventofcode.com/2021/day/24
#https://adventofcode.com/2021/day/24#part2

import os
import math
inFileDir = os.path.dirname(__file__)
inFile = ""
if 1:
    inFile = os.path.join(inFileDir, "InputTestFiles/d24_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d24_real.txt")


def getInput():
    inputVals = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n','').split(' ')
            if len(line) > 2 and line[2] not in ['w', 'x', 'y', 'z']:
                line[2] = int(line[2])
            inputVals.append(line)
            
    return inputVals


def MONAD_v1(instructions:list, modelNum:str)->int:
    #Checking the model number to make sure it doesn't contain any 0's
    if '0' in modelNum:
        print("Invalid model number. Contains '0'")
        return False
    #Making sure the model number has exactly 14 characters
    if len(modelNum) != 14:
        print("Invalid model number. String has", len(modelNum), "characters, not 14")
        return False

    inputIndex = 0
    vals = {'w':0, 'x':0, 'y':0, 'z':0}
    
    for ins in instructions:
        #print("Instruction:", ins)
        if ins[0] == "inp":
            #If we've run out of input values, we cycle back around
            if inputIndex >= len(modelNum):
                print("More than 14 inputs required. Cycling index back to 0")
                inputIndex = 0
            vals[ins[1]] = int(modelNum[inputIndex])
            inputIndex += 1

        elif ins[0] == "add":
            if type(ins[2]) is int:
                vals[ins[1]] += ins[2]
            else:
                vals[ins[1]] += vals[ins[2]]
                
        elif ins[0] == "mul":
            if type(ins[2]) is int:
                vals[ins[1]] *= ins[2]
            else:
                vals[ins[1]] *= vals[ins[2]]
                
        elif ins[0] == "div":
            if type(ins[2]) is int:
                if ins[2] != 0:
                    vals[ins[1]] = math.trunc(vals[ins[1]] / ins[2])
                else:
                    print("Divide by 0 error:", ins[0], vals[ins[1]], ins[2])
                    return False
            elif vals[ins[2]] != 0:
                vals[ins[1]] = math.trunc(vals[ins[1]] / vals[ins[2]])
            else:
                print("Divide by 0 error:", ins[0], vals[ins[1]], vals[ins[2]])
                return False
                
        elif ins[0] == "mod":
            if vals[ins[1]] < 0:
                return False
            if type(ins[2]) is int:
                if ins[2] <= 0:
                    return False
                else:
                    vals[ins[1]] = vals[ins[1]] % ins[2]
            else:
                if vals[ins[2]] <= 0:
                    return False
                else:
                    vals[ins[1]] = vals[ins[1]] % vals[ins[2]]
                
        elif ins[0] == "eql":
            if type(ins[2]) is int:
                if vals[ins[1]] == ins[2]:
                    vals[ins[1]] = 1
                else:
                    vals[ins[1]] = 0
            else:
                if vals[ins[1]] == vals[ins[2]]:
                    vals[ins[1]] = 1
                else:
                    vals[ins[1]] = 0
                    
        #print('\t', vals)
    #After all instructions are done, if the value of 'z' is 0, the model number is invalid
    print("End result of 'z':", vals['z'])                
    return vals['z']              


def solution1():
    instructions = getInput()
    modelNum = 1111111111111
    ind = 13
    prevNum = 11111111111111
    bestResult = None
    
    while ind > -1:
        modelNum += 10**ind
        modelString = str(modelNum)
        result = MONAD_v1(instructions, modelString)
        if bestResult is None or abs(result) < abs(bestResult[1]):
            bestResult = (modelNum, result)
            print("\t\tBest Result:", bestResult)

        if result == 0:
            prevNum = modelNum
            print(prevNum, "is valid.")
            if (modelNum // 10**ind) % 10 == 9:
                ind -= 1
                print("\tHighest index of '9' reached. Lowering index to", ind)
        else:
            ind -= 1
            print(modelNum, "is invalid. Reverting to", prevNum, "and lowering index to", ind)
            modelNum = prevNum
            
    
    return modelNum


def solution2():
    
    return 0 


print("Year 2021, Day 24 solution part 1:", solution1())
print("Year 2021, Day 24 solution part 2:", solution2())