#https://adventofcode.com/2019/day/7
#https://adventofcode.com/2019/day/7#part2

import os
import itertools
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 0
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d7_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d7_real.txt")


def getInput():
    inputSeq = []

    with open(inFile, 'r') as f:
        for line in f:
            inputSeq = line.replace('\n', '').split(',')
            for i in range(0, len(inputSeq)):
                inputSeq[i] = int(inputSeq[i])

    return inputSeq


class IntcodeReader_v3:
    '''Reads through intcode from AoC y2019 d5.
        - Uses instructions 1 (add), 2 (mult), 3 (input), 4 (output).
        - Supports Position Mode and Parameter Mode.
    '''
    
    def __init__(self, intcodeList_:list, inputVal_:int, phase_:int, debugMode_:bool=False):
        self.intcodeList = intcodeList_
        self.inputVal = inputVal_
        self.phase = phase_
        self.index = 0
        self.debugMode = debugMode_
        self.outVal = 0
        

    def setInputVal(self, newInputVal_:int):
        self.inputVal = newInputVal_
        

    def setIndex(self, newIndex_:int):
        if newIndex_ >= 0 and newIndex_ < len(self.intcodeList):
            self.index = newIndex_


    def add(self, modes_:list):
        '''Opcode 1: Adds the 2 values following the current index, and sets the sum to the position of the current index + 3.'''
        sumIndex = self.intcodeList[self.index + 3]
        
        val1 = 0
        if modes_[0] == 0: #position mode
            val1 = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val1 = self.intcodeList[self.index+1]
            
        val2 = 0
        if modes_[1] == 0: #position mode
            val2 = self.intcodeList[self.intcodeList[self.index+2]]
        else: #immediate mode
            val2 = self.intcodeList[self.index+2]
            
        self.intcodeList[sumIndex] = val1 + val2
        
        if self.debugMode:
            print("\tADD:", self.intcodeList[self.index : self.index+4], "modes:", modes_)
            print("\t", val1, "+", val2)
            print("\tNew value at index", sumIndex, ":", self.intcodeList[sumIndex])
        self.index += 4
        

    def mult(self, modes_:list):
        '''Opcode 2: Multiplies the 2 values following the current index, and sets the product to the position of the current index + 3.'''
        prodIndex = self.intcodeList[self.index + 3]
        
        val1 = 0
        if modes_[0] == 0: #position mode
            val1 = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val1 = self.intcodeList[self.index+1]
            
        val2 = 0
        if modes_[1] == 0: #position mode
            val2 = self.intcodeList[self.intcodeList[self.index+2]]
        else: #immediate mode
            val2 = self.intcodeList[self.index+2]
            
        self.intcodeList[prodIndex] = val1 * val2
        
        if self.debugMode:
            print("\tMULT:", self.intcodeList[self.index : self.index+4], "modes:", modes_)
            print("\t", val1, "*", val2)
            print("\tNew value at index", prodIndex, ":", self.intcodeList[prodIndex])
        self.index += 4
        

    def inputParam(self):
        '''Opcode 3: Sets the input value given to the position at the current index + 1's position.'''
        inputIndex = self.intcodeList[self.index+1]
        
        self.intcodeList[inputIndex] = self.phase
        if self.phase != self.inputVal:
            self.phase = self.inputVal
        
        if self.debugMode:
            print("\tINPUT:", self.intcodeList[self.index : self.index+2], self.inputVal)
            print("\tNew value at index", inputIndex, ":", self.intcodeList[inputIndex])
            
        self.index += 2


    def output(self):
        '''Opcode 4: Outputs the value at the current index + 1.'''
        outIndex = self.intcodeList[self.index+1]
        self.outVal = self.intcodeList[outIndex]
        
        if self.debugMode:
            print("\tOUTPUT:", self.intcodeList[self.index : self.index+2])
            print("\tValue at index", outIndex, ":", self.intcodeList[outIndex])
        self.index += 2
        

    def jumpIfTrue(self, modes_:list):
        '''Opcode 5: If the input value is non-zero, current index jumps to the value of current index + 1. Otherwise does nothing'''
        val = 0
        if modes_[0] == 0: #position mode
            val = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val = self.intcodeList[self.index+1]
            
        newIndex = self.index + 3
        if val != 0:
            if modes_[1] == 0: #position mode
                newIndex = self.intcodeList[self.intcodeList[self.index+2]]
            else: #immediate mode
                newIndex = self.intcodeList[self.index+2]
        
        if self.debugMode:
            print("\tJUMP IF TRUE:", self.intcodeList[self.index : self.index+3], "modes:", modes_)
            print("\t", val, "!= 0 ?")
            print("\tValue:", val, "   New index:", newIndex)
            
        self.index = newIndex
        

    def jumpIfFalse(self, modes_:list):
        '''Opcode 6: If the following index is zero, current index jumps to the value of current index + 1. Otherwise does nothing'''
        val = 0
        if modes_[0] == 0: #position mode
            val = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val = self.intcodeList[self.index+1]
            
        newIndex = self.index + 3
        if val == 0:
            if modes_[1] == 0: #position mode
                newIndex = self.intcodeList[self.intcodeList[self.index+2]]
            else: #immediate mode
                newIndex = self.intcodeList[self.index+2]
        
        if self.debugMode:
            print("\tJUMP IF FALSE:", self.intcodeList[self.index : self.index+3], "modes:", modes_)
            print("\t", val, "== 0 ?")
            print("\tValue:", val, "   New index:", newIndex)
            
        self.index = newIndex
        

    def lessThan(self, modes_:list):
        '''Opcode 7: If value of index+1 < value of index+2, the value 1 is stored in the position of index+3. Otherwise the value 0 is stored in position of index+3'''
        resultIndex = self.intcodeList[self.index + 3]
        
        val1 = 0
        if modes_[0] == 0: #position mode
            val1 = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val1 = self.intcodeList[self.index+1]
            
        val2 = 0
        if modes_[1] == 0: #position mode
            val2 = self.intcodeList[self.intcodeList[self.index+2]]
        else: #immediate mode
            val2 = self.intcodeList[self.index+2]
            
        if val1 < val2:
            self.intcodeList[resultIndex] = 1
        else:
            self.intcodeList[resultIndex] = 0
            
        if self.debugMode:
            print("\tLESS THAN:", self.intcodeList[self.index : self.index+4], "modes:", modes_)
            print("\t", val1, "<", val2, "?")
            print("\tNew value at index", resultIndex, ":", self.intcodeList[resultIndex])
        self.index += 4


    def equals(self, modes_:list):
        '''Opcode 8: If value of index+1 == value of index+2, the value 1 is stored in the position of index+3. Otherwise the value 0 is stored in position of index+3'''
        resultIndex = self.intcodeList[self.index + 3]
        
        val1 = 0
        if modes_[0] == 0: #position mode
            val1 = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val1 = self.intcodeList[self.index+1]
            
        val2 = 0
        if modes_[1] == 0: #position mode
            val2 = self.intcodeList[self.intcodeList[self.index+2]]
        else: #immediate mode
            val2 = self.intcodeList[self.index+2]
            
        if val1 == val2:
            self.intcodeList[resultIndex] = 1
        else:
            self.intcodeList[resultIndex] = 0
            
        if self.debugMode:
            print("\tEQUALS:", self.intcodeList[self.index : self.index+4], "modes:", modes_)
            print("\t", val1, "==", val2, "?")
            print("\tNew value at index", resultIndex, ":", self.intcodeList[resultIndex])
        self.index += 4


    def process(self):
        '''Reads through each instruction in the given intcode list and performs each instruction sequentially.'''
        while self.index < len(self.intcodeList):
            code = self.intcodeList[self.index]
            modes = [0,0,0]

            #If the code is triple-digit, it indicates different input modes
            if code > 99:
                modes[0] = (code // 100) % 10
                modes[1] = (code // 1000) % 10
                modes[2] = (code // 10000) % 10
                code = code % 100
            
            if self.debugMode:
                print("Index:", self.index, "    Code:", code, "    Modes:", modes)
                
            if code == 99:
                if self.debugMode:
                    print("\tTERMINATION at instruction", self.index)
                return self.outVal
            elif code == 1:
                self.add(modes)
            elif code == 2:
                self.mult(modes)
            elif code == 3:
                self.inputParam()
            elif code == 4:
                self.output()
            elif code == 5:
                self.jumpIfTrue(modes)
            elif code == 6:
                self.jumpIfFalse(modes)
            elif code == 7:
                self.lessThan(modes)
            elif code == 8:
                self.equals(modes)
            else:
                print("Invalid code:", code, "at index", self.index)
                return
            
        return self.outVal
    

    def processStep(self):
        '''Processes a single step using the currently-stored index and input value.'''
        code = self.intcodeList[self.index]
        modes = [0,0,0]

        #If the code is triple-digit, it indicates different input modes
        if code > 99:
            modes[0] = (code // 100) % 10
            modes[1] = (code // 1000) % 10
            modes[2] = (code // 10000) % 10
            code = code % 100
            
        if self.debugMode:
            print("Index:", self.index, "    Code:", code, "    Modes:", modes)
                
        if code == 99:
            if self.debugMode:
                print("\tTERMINATION at instruction", self.index)
            return self.outVal
        elif code == 1:
            self.add(modes)
        elif code == 2:
            self.mult(modes)
        elif code == 3:
            self.inputParam()
        elif code == 4:
            self.output()
        elif code == 5:
            self.jumpIfTrue(modes)
        elif code == 6:
            self.jumpIfFalse(modes)
        elif code == 7:
            self.lessThan(modes)
        elif code == 8:
            self.equals(modes)
        else:
            print("Invalid code:", code, "at index", self.index)
            

def solution1():
    intcode = getInput()
    phasePermutations = list(itertools.permutations(range(5), 5))
    
    highestOutput = 0
    bestPhase = None
    for p in phasePermutations:
        ampA = IntcodeReader_v3(intcode, 0, p[0], False).process()
        ampB = IntcodeReader_v3(intcode, ampA, p[1], False).process()
        ampC = IntcodeReader_v3(intcode, ampB, p[2], False).process()
        ampD = IntcodeReader_v3(intcode, ampC, p[3], False).process()
        ampE = IntcodeReader_v3(intcode, ampD, p[4], False).process()
        if ampE > highestOutput:
            highestOutput = ampE
            bestPhase = p
        
    return highestOutput, bestPhase


def solution2():
    intcode = getInput()
    phasePermutations = list(itertools.permutations([5,6,7,8,9], 5))
    
    highestOutput = 0
    bestPhase = None
    for p in phasePermutations:
        currInput = -1
        nextInput = 0
        while currInput != nextInput:
            currInput = nextInput
            print(currInput)
            ampA = IntcodeReader_v3(intcode, currInput, p[0], False).process()
            #print("Amp A:", ampA)
            ampB = IntcodeReader_v3(intcode, ampA, p[1], False).process()
            #print("Amp B:", ampB)
            ampC = IntcodeReader_v3(intcode, ampB, p[2], False).process()
            #print("Amp C:", ampC)
            ampD = IntcodeReader_v3(intcode, ampC, p[3], False).process()
            #print("Amp D:", ampD)
            ampE = IntcodeReader_v3(intcode, ampD, p[4], False).process()
            #print("Amp E:", ampE)
            nextInput = ampE
            
        if currInput > highestOutput:
            highestOutput = currInput
            bestPhase = p
        
    return highestOutput, bestPhase


print("Year 2019, Day 7 solution part 1:", solution1())
print("Year 2019, Day 7 solution part 2:", solution2())