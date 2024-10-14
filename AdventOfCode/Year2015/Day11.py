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
    testing and print("Original Input:", inpt)
    
    #Converting every char into the ASCII int value for faster comparisson and incrimenting
    inpt = [ord(x) for x in inpt]
    testing and print("New Input:     ", inpt)
    for i in range(len(inpt)):
        if inpt[i] == ord('i') or inpt[i] == ord('o') or inpt[i] == ord('l'):
            testing and print("\tStarting value at index", i, "is", chr(inpt[i]))
            inpt[i] += 1
            for j in range(i+1, len(inpt)):
                inpt[j] = 97
    
    def req1(pw_:list)->bool:
        '''Must have 3 consecutive letters in ascending value'''
        for i in range(len(pw_)-2):
            if pw_[i+1] - pw_[i] == 1 and pw_[i+2] - pw_[i+1] == 1:
                return True
        return False
        
    def req2(pw_:list)->bool:
        '''Can't have letters i, o, or l.'''
        if 105 in pw_ or 111 in pw_ or 108 in pw_:
            return False
        return True
    
    def req3(pw_:list)->bool:
        '''Must have 2 different, non-overlapping pairs of the same letter.'''
        pairsFound = 0
        i = 0
        while i < len(pw_)-1:
            if pw_[i] == pw_[i+1]:
                pairsFound += 1
                i += 2
            else:
                i += 1
        return (pairsFound >= 2)
    

    #Looping until we get a valid password
    while True:
        testing and print(''.join([chr(x) for x in inpt]))
        if req1(inpt) and req2(inpt) and req3(inpt):
            break
        else:
            i = len(inpt)-1
            inpt[i] += 1
            
            while inpt[i] in [105, 111, 108, 123]:
                #If this letter is '(' that comes after 'z' we loop back to 'a' and incriment the previous letter
                if inpt[i] == 123:
                    inpt[i] = 97
                    i -= 1
                    if i > -1:
                        inpt[i] += 1
                #If this letter is an invalid letter (i, o, l) we skip it
                else:
                    inpt[i] += 1

    return ''.join([chr(x) for x in inpt])


def solution2():
    inpt = solution1()
    
    #Converting every char into the ASCII int value for faster comparisson and incrimenting
    inpt = [ord(x) for x in inpt]
    i = len(inpt)-1
    inpt[i] += 1
            
    while inpt[i] in [105, 111, 108, 123]:
        #If this letter is '(' that comes after 'z' we loop back to 'a' and incriment the previous letter
        if inpt[i] == 123:
            inpt[i] = 97
            i -= 1
            if i > -1:
                inpt[i] += 1
        #If this letter is an invalid letter (i, o, l) we skip it
        else:
            inpt[i] += 1
    
    def req1(pw_:list)->bool:
        '''Must have 3 consecutive letters in ascending value'''
        for i in range(len(pw_)-2):
            if pw_[i+1] - pw_[i] == 1 and pw_[i+2] - pw_[i+1] == 1:
                return True
        return False
        
    def req2(pw_:list)->bool:
        '''Can't have letters i, o, or l.'''
        if 105 in pw_ or 111 in pw_ or 108 in pw_:
            return False
        return True
    
    def req3(pw_:list)->bool:
        '''Must have 2 different, non-overlapping pairs of the same letter.'''
        pairsFound = 0
        i = 0
        while i < len(pw_)-1:
            if pw_[i] == pw_[i+1]:
                pairsFound += 1
                i += 2
            else:
                i += 1
        return (pairsFound >= 2)
    

    #Looping until we get a valid password
    while True:
        if req1(inpt) and req2(inpt) and req3(inpt):
            break
        else:
            i = len(inpt)-1
            inpt[i] += 1
            
            while inpt[i] in [105, 111, 108, 123]:
                #If this letter is '(' that comes after 'z' we loop back to 'a' and incriment the previous letter
                if inpt[i] == 123:
                    inpt[i] = 97
                    i -= 1
                    if i > -1:
                        inpt[i] += 1
                #If this letter is an invalid letter (i, o, l) we skip it
                else:
                    inpt[i] += 1

    return ''.join([chr(x) for x in inpt])


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())