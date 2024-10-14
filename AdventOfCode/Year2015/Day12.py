import json
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
    
    def checkList(cl_:list)->int:
        '''Recursive method that looks through every element in the given list and returns the sum of all ints.'''
        s = 0
        for i in cl_:
            if type(i) is int:
                s += i
            elif type(i) is list:
                s += checkList(i)
            elif type(i) is dict:
                s += checkDict(i)
        testing and print("++++ List", cl_, "sum:", s)
        return s
    
    def checkDict(cd_:dict)->int:
        '''Recursive method that looks through every key/value pair in the given dictionary and returns the sum of all ints.'''
        s = 0
        for k in cd_.keys():
            if type(k) is int:
                s += k
            if type(cd_[k]) is int:
                s += cd_[k]
            elif type(cd_[k]) is dict:
                s += checkDict(cd_[k])
            elif type(cd_[k]) is list:
                s += checkList(cd_[k])
        testing and print("==== Dict", cd_, "sum:", s)
        return s
    
    js = json.loads(inpt)

    return checkDict(js)


def solution2():
    inpt = getInput()
    
    def checkList(cl_:list)->int:
        '''Recursive method that looks through every element in the given list and returns the sum of all ints.'''
        s = 0
        for i in cl_:
            if type(i) is int:
                s += i
            elif type(i) is list:
                s += checkList(i)
            elif type(i) is dict:
                s += checkDict(i)
        testing and print("++++ List", cl_, "sum:", s)
        return s
    
    def checkDict(cd_:dict)->int:
        '''Recursive method that looks through every key/value pair in the given dictionary and returns the sum of all ints.'''
        s = 0
        for k in cd_.keys():
            if type(k) is int:
                s += k
                
            if type(cd_[k]) is int:
                s += cd_[k]
            elif type(cd_[k]) is dict:
                s += checkDict(cd_[k])
            elif type(cd_[k]) is list:
                s += checkList(cd_[k])
            elif type(cd_[k]) is str and cd_[k] == "red":
                s = 0
                break
        testing and print("==== Dict", cd_, "sum:", s)
        return s
    
    js = json.loads(inpt)

    return checkDict(js)


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())