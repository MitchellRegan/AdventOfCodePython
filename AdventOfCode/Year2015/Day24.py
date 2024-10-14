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
            inpt.append(int(line))

    return inpt
            

def solution1():
    inpt = getInput()
    groupWeight = sum(inpt) // 3
    
    def makeGroup(i_:int=0, weight_:int=0, numGift_=0, qe_:int=1):
        '''Finds every combination of values from the input who's sum is equal to the designated group weight.
        
        Parameters
        ----------
            i_: Index for the next input value to look at.
            weight_: Current weight of all gifts in this combination.
            numGift_: Current number of gifts in this combination.
            qe_: Quantum Entanglement (i.e. product) of all gifts in this combination.
            
        Returns
        ----------
            Tuple for (number of gifts, quantum entanglement) for the combination.
        '''
        best = (len(inpt), 9999999)
        testing and print("i", i_, "    Weight:", weight_, "    #Gifts:", numGift_, "    QE:", qe_)
        #Recursion break
        if i_ == len(inpt):
            if weight_ == groupWeight:
                return (numGift_, qe_)
            else:
                return best
        
        if weight_ + inpt[i_] <= groupWeight:
            #Starting the next recursion without the current value at index i
            res = makeGroup(i_+1, weight_, numGift_, qe_)
            if res[0] < best[0] or (res[0] == best[0] and res[1] < best[1]):
                best = res
            #Next recursion with the current value at index i
            res = makeGroup(i_+1, weight_+inpt[i_], numGift_+1, qe_*inpt[i_])
            if res[0] < best[0] or (res[0] == best[0] and res[1] < best[1]):
                best = res
        return best

    return makeGroup()[1]


def solution2():
    inpt = getInput()
    groupWeight = sum(inpt) // 4

    def makeGroup(i_:int=0, weight_:int=0, numGift_=0, qe_:int=1):
        '''Finds every combination of values from the input who's sum is equal to the designated group weight.
        
        Parameters
        ----------
            i_: Index for the next input value to look at.
            weight_: Current weight of all gifts in this combination.
            numGift_: Current number of gifts in this combination.
            qe_: Quantum Entanglement (i.e. product) of all gifts in this combination.
            
        Returns
        ----------
            Tuple for (number of gifts, quantum entanglement) for the combination.
        '''
        best = (len(inpt), 9999999)
        
        #Recursion break
        if i_ == len(inpt):
            if weight_ == groupWeight:
                return (numGift_, qe_)
            else:
                return best
        
        if weight_ + inpt[i_] <= groupWeight:
            #Starting the next recursion without the current value at index i
            res = makeGroup(i_+1, weight_, numGift_, qe_)
            if res[0] < best[0] or (res[0] == best[0] and res[1] < best[1]):
                best = res
            #Next recursion with the current value at index i
            res = makeGroup(i_+1, weight_+inpt[i_], numGift_+1, qe_*inpt[i_])
            if res[0] < best[0] or (res[0] == best[0] and res[1] < best[1]):
                best = res
        return best

    return makeGroup()[1]


#print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())