# USE THE FOLLOWING LINES TO IMPORT THIS CLASS TO ANY DAY IN Y2019
#import sys
#sys.path.append(".")
#from Year2019.IntcodeComputer import IntcodeReader

class IntcodeReader:
    '''Reads through intcode from AoC problems in y2019.
        - Supports Opcodes:
            99 (terminate)     from d2p1
            1 (add)            from d2p1
            2 (mult)           from d2p1
            3 (input)          from d5p1
            4 (output)         from d5p1
            5 (jump if true)   from d5p2
            6 (jump if false)  from d5p2
            7 (less than)      from d5p2
            8 (equals)         from d5p2
            9 (adjust relative base) from d9p1
        - Supports Modes:
            Position Mode      from d2p1
            Parameter Mode     from d5p1
            Phases             from d7p1
            Relative Mode      from d9p1
    '''
    
    def __init__(self, intcodeList_:list, inputVal_:int, phase_:int, debugMode_:bool=False):
        self.intcodeList = intcodeList_
        self.inputVal = inputVal_
        self.phase = phase_
        self.index = 0
        self.debugMode = debugMode_
        self.outVal = 0
        self.relativeBase = 0
        

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
        

    def adjustRelativeBase(self, shift_:int):
        '''Opcode 9: Shifts the relative base by adding the parameter value.'''
        if self.debugMode:
            print("\tADJUST RELATIVE BASE: current base:", self.relativeBase, "\n\tModes:", shift_)
        self.relativeBase += shift_
        if self.debugMode:
            print("\tNew base:", self.relativeBase)


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
                if True: #self.debugMode:
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
            elif code == 9:
                self.adjustRelativeBase(modes)
            else:
                print("Invalid code:", code, "at index", self.index)
                return
            
        print("\tEND OF INTCODE")
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
            if True: #self.debugMode:
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
            