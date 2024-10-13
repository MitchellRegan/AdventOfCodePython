aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')

    return inpt
            

def solution1():
    inpt = getInput()
    
    print("Try converting the string into a list of ascii code values using ord() for faster incrimenting and comparisson")
    def req1(pw_:str)->bool:
        
    def req2(pw_:str)->bool:
        '''Can't have letters i, o, or l.'''
        if 'i' in pw_ or 'o' in pw_ or 'l' in pw_:
            return False
        return True
    
    def req3(pw_:str)->bool:
        '''Must have 2 different, non-overlapping pairs of the same letter.'''

    return


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())