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
            end, nums = line.split(': ')
            end = int(end)
            nums = [int(x) for x in nums.split(' ')]
            inpt.append([end, nums])

    return inpt
            

def solution1():
    inpt = getInput()
    
    def recursiveEquation(testVal_:int, nums_:list, ops_:list=[])->bool:
        '''Performs a recursive equation where each permutation of operators (addition, multiplication)
        are used between each of the given list of numbers to see if it equates to the given test value.
        '''
        if len(ops_) == len(nums_)-1:
            testing and print('\t', nums_, ops_, "  ==  ", testVal_)
            result = nums_[0]
            for i in range(len(ops_)):
                if ops_[i] == '+':
                    result += nums_[i+1]
                elif ops_[i] == '*':
                    result *= nums_[i+1]
            return result == testVal_

        opsPlus = [x for x in ops_]
        opsPlus.append('+')
        opsMult = [x for x in ops_]
        opsMult.append('*')
        return (recursiveEquation(testVal_, nums_, opsPlus) or recursiveEquation(testVal_, nums_, opsMult))

    #Performing the recursive evaluation on each line of the input
    ans = 0
    for line in inpt:
        if recursiveEquation(line[0], line[1], []):
            ans += line[0]

    return ans


def solution2():
    inpt = getInput()
    
    def recursiveEquation(testVal_:int, nums_:list, ops_:list=[])->bool:
        '''Performs a recursive equation where each permutation of operators (addition, multiplication, concatination)
        are used between each of the given list of numbers to see if it equates to the given test value.
        '''
        if len(ops_) == len(nums_)-1:
            result = nums_[0]
            for i in range(len(ops_)):
                if ops_[i] == '+':
                    result += nums_[i+1]
                elif ops_[i] == '*':
                    result *= nums_[i+1]
                elif ops_[i] == '|':
                    result = int(str(result) + str(nums_[i+1]))
            testing and print('\t', nums_, ops_, "=", result, "    ==", testVal_, "?")
            return result == testVal_

        opsPlus = [x for x in ops_]
        opsPlus.append('+')
        opsMult = [x for x in ops_]
        opsMult.append('*')
        opsCnct = [x for x in ops_]
        opsCnct.append('|')
        return (recursiveEquation(testVal_, nums_, opsPlus) or recursiveEquation(testVal_, nums_, opsMult) or recursiveEquation(testVal_, nums_, opsCnct))

    #Performing the recursive evaluation on each line of the input
    ans = 0
    for line in inpt:
        if recursiveEquation(line[0], line[1], []):
            ans += line[0]

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())