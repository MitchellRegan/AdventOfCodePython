#https://adventofcode.com/2019/day/7
#https://adventofcode.com/2019/day/7#part2

import os
import itertools
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 1
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
        self.intcodeList = [x for x in intcodeList_]
        self.inputVal = inputVal_
        self.phase = phase_
        self.index = 0
        self.debugMode = debugMode_
        self.outVal = 0
        self.modes = [0,0,0]
        

    def setInputVal(self, newInputVal_:int):
        self.inputVal = newInputVal_
        

    def setIndex(self, newIndex_:int):
        if newIndex_ >= 0 and newIndex_ < len(self.intcodeList):
            self.index = newIndex_


    def add(self):
        '''Opcode 1: Adds the 2 values following the current index, and sets the sum to the position of the current index + 3.'''
        sumIndex = self.intcodeList[self.index + 3]
        
        val1 = 0
        if self.modes[0] == 0: #position mode
            val1 = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val1 = self.intcodeList[self.index+1]
            
        val2 = 0
        if self.modes[1] == 0: #position mode
            val2 = self.intcodeList[self.intcodeList[self.index+2]]
        else: #immediate mode
            val2 = self.intcodeList[self.index+2]
            
        self.intcodeList[sumIndex] = val1 + val2
        
        if self.debugMode:
            print("\tInd:", self.index, "   ADD:", self.intcodeList[self.index : self.index+4], "modes:", self.modes)
            print("\t  ", val1, "+", val2)
            print("\t  New value at index", sumIndex, ":", self.intcodeList[sumIndex])
        self.index += 4
        

    def mult(self):
        '''Opcode 2: Multiplies the 2 values following the current index, and sets the product to the position of the current index + 3.'''
        prodIndex = self.intcodeList[self.index + 3]
        
        val1 = 0
        if self.modes[0] == 0: #position mode
            val1 = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val1 = self.intcodeList[self.index+1]
            
        val2 = 0
        if self.modes[1] == 0: #position mode
            val2 = self.intcodeList[self.intcodeList[self.index+2]]
        else: #immediate mode
            val2 = self.intcodeList[self.index+2]
            
        self.intcodeList[prodIndex] = val1 * val2
        
        if self.debugMode:
            print("\tInd:", self.index, "   MULT:", self.intcodeList[self.index : self.index+4], "modes:", self.modes)
            print("\t  ", val1, "*", val2)
            print("\t  New value at index", prodIndex, ":", self.intcodeList[prodIndex])
        self.index += 4
        

    def inputParam(self):
        '''Opcode 3: Sets the input value given to the position at the current index + 1's position.'''
        inputIndex = self.intcodeList[self.index+1]
        
        self.intcodeList[inputIndex] = self.phase
        if self.phase != self.inputVal:
            self.phase = self.inputVal
        
        if self.debugMode:
            print("\tInd:", self.index, "   INPUT:", self.intcodeList[self.index : self.index+2], self.inputVal)
            print("\t  New value at index", inputIndex, ":", self.intcodeList[inputIndex])
            
        self.index += 2


    def output(self):
        '''Opcode 4: Outputs the value at the current index + 1.'''
        outIndex = self.intcodeList[self.index+1]
        self.outVal = self.intcodeList[outIndex]
        
        if self.debugMode:
            print("\tInd:", self.index, "   OUTPUT:", self.intcodeList[self.index : self.index+2])
            print("\t  Value at index", outIndex, ":", self.intcodeList[outIndex])
        self.index += 2
        

    def jumpIfTrue(self):
        '''Opcode 5: If the input value is non-zero, current index jumps to the value of current index + 1. Otherwise does nothing'''
        val = 0
        if self.modes[0] == 0: #position mode
            val = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val = self.intcodeList[self.index+1]
            
        newIndex = self.index + 3
        if val != 0:
            if self.modes[1] == 0: #position mode
                newIndex = self.intcodeList[self.intcodeList[self.index+2]]
            else: #immediate mode
                newIndex = self.intcodeList[self.index+2]
        
        if self.debugMode:
            print("\tInd:", self.index, "   JUMP IF TRUE:", self.intcodeList[self.index : self.index+3], "modes:", self.modes)
            print("\t  ", val, "!= 0 ?")
            print("\t  Value:", val, "   New index:", newIndex)
            
        self.index = newIndex
        

    def jumpIfFalse(self):
        '''Opcode 6: If the following index is zero, current index jumps to the value of current index + 1. Otherwise does nothing'''
        val = 0
        if self.modes[0] == 0: #position mode
            val = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val = self.intcodeList[self.index+1]
            
        newIndex = self.index + 3
        if val == 0:
            if self.modes[1] == 0: #position mode
                newIndex = self.intcodeList[self.intcodeList[self.index+2]]
            else: #immediate mode
                newIndex = self.intcodeList[self.index+2]
        
        if self.debugMode:
            print("\tInd:", self.index, "   JUMP IF FALSE:", self.intcodeList[self.index : self.index+3], "modes:", self.modes)
            print("\t  ", val, "== 0 ?")
            print("\t  Value:", val, "   New index:", newIndex)
            
        self.index = newIndex
        

    def lessThan(self):
        '''Opcode 7: If value of index+1 < value of index+2, the value 1 is stored in the position of index+3. Otherwise the value 0 is stored in position of index+3'''
        resultIndex = self.intcodeList[self.index + 3]
        
        val1 = 0
        if self.modes[0] == 0: #position mode
            val1 = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val1 = self.intcodeList[self.index+1]
            
        val2 = 0
        if self.modes[1] == 0: #position mode
            val2 = self.intcodeList[self.intcodeList[self.index+2]]
        else: #immediate mode
            val2 = self.intcodeList[self.index+2]
            
        if val1 < val2:
            self.intcodeList[resultIndex] = 1
        else:
            self.intcodeList[resultIndex] = 0
            
        if self.debugMode:
            print("\tInd:", self.index, "   LESS THAN:", self.intcodeList[self.index : self.index+4], "modes:", self.modes)
            print("\t  ", val1, "<", val2, "?")
            print("\t  New value at index", resultIndex, ":", self.intcodeList[resultIndex])
        self.index += 4


    def equals(self):
        '''Opcode 8: If value of index+1 == value of index+2, the value 1 is stored in the position of index+3. Otherwise the value 0 is stored in position of index+3'''
        resultIndex = self.intcodeList[self.index + 3]
        
        val1 = 0
        if self.modes[0] == 0: #position mode
            val1 = self.intcodeList[self.intcodeList[self.index+1]]
        else: #immediate mode
            val1 = self.intcodeList[self.index+1]
            
        val2 = 0
        if self.modes[1] == 0: #position mode
            val2 = self.intcodeList[self.intcodeList[self.index+2]]
        else: #immediate mode
            val2 = self.intcodeList[self.index+2]
            
        if val1 == val2:
            self.intcodeList[resultIndex] = 1
        else:
            self.intcodeList[resultIndex] = 0
            
        if self.debugMode:
            print("\tInd:", self.index, "   EQUALS:", self.intcodeList[self.index : self.index+4], "modes:", self.modes)
            print("\t  ", val1, "==", val2, "?")
            print("\t  New value at index", resultIndex, ":", self.intcodeList[resultIndex])
        self.index += 4


    def process(self)->int:
        '''Reads through every instruction in this program's intcode list and performs each instruction sequentially.
        Returns the final output value stored once all instructions have been performed.'''
        while self.index < len(self.intcodeList) and self.index > -1:
            code = self.intcodeList[self.index]

            #If the code is triple-digit, it indicates different input modes
            if code > 99:
                self.modes[0] = (code // 100) % 10
                self.modes[1] = (code // 1000) % 10
                self.modes[2] = (code // 10000) % 10
                code = code % 100
            
            #if self.debugMode:
            #    print("Index:", self.index, "    Code:", code, "    Modes:", modes)
                
            if code == 99:
                if self.debugMode:
                    print("\tTERMINATION at instruction", self.index)
                return self.outVal
            elif code == 1:
                self.add()
            elif code == 2:
                self.mult()
            elif code == 3:
                self.inputParam()
            elif code == 4:
                self.output()
            elif code == 5:
                self.jumpIfTrue()
            elif code == 6:
                self.jumpIfFalse()
            elif code == 7:
                self.lessThan()
            elif code == 8:
                self.equals()
            else:
                print("Invalid code:", code, "at index", self.index)
                return
            
        print("\tEND OF INTCODE")
        return self.outVal
    

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
        p = [9,8,7,6,5]
        print("Permutation", p, "=====================================================")
        #Initializing each amplifier for this permutation
        doingDebug = False
        ampA = IntcodeReader_v3(intcode, 0, p[0], doingDebug)
        ampB = IntcodeReader_v3(intcode, 0, p[1], doingDebug)
        ampC = IntcodeReader_v3(intcode, 0, p[2], doingDebug)
        ampD = IntcodeReader_v3(intcode, 0, p[3], doingDebug)
        ampE = IntcodeReader_v3(intcode, 0, p[4], doingDebug)
        
        currInput = 0
        while True:
            print("----Input:", currInput)
            ampA.setInputVal(currInput)
            currInput = ampA.process()
            print("----Amp A:", currInput)
            
            ampB.setInputVal(currInput)
            currInput = ampB.process()
            print("----Amp B:", currInput)
            
            ampC.setInputVal(currInput)
            currInput = ampC.process()
            print("----Amp C:", currInput)
            
            ampD.setInputVal(currInput)
            currInput = ampD.process()
            print("----Amp D:", currInput)
            
            ampE.setInputVal(currInput)
            currInput = ampE.process()
            print("----Amp E:", currInput)
            #testing and print("Amp States: A", ampA.getIsFinished(), "  B", ampB.getIsFinished(), "  C", ampC.getIsFinished(), "  D", ampD.getIsFinished(), "  E", ampE.getIsFinished())
            input()
            
        if currInput > highestOutput:
            highestOutput = currInput
            bestPhase = p
        
    return highestOutput, bestPhase


#print("Year 2019, Day 7 solution part 1:", solution1())
print("Year 2019, Day 7 solution part 2:", solution2())