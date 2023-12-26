#https://adventofcode.com/2023/day/12
#https://adventofcode.com/2023/day/12#part2

from ast import Num
import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 1:
    inFile = os.path.join(inFileDir, "InputTestFiles/d12_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d12_real.txt")


def getInput():
    input = []

    with open(inFile, 'r') as f:

        for line in f:
            line = line.replace('\n','').split(' ')
            code = line[0]
            nums = line[1].split(',')
            for i in range(0, len(nums)):
                nums[i] = int(nums[i])
            input.append((code, nums))
    return input


def analyzeRow(row_:str)->list:
    rowDupe = row_.split('.')
    ans = []
    for group in rowDupe:
        if group != '':
            ans.append(len(group))
    return ans


def solution1():
    input = getInput()

    valid = 0
    for line in input:
        #print(line)
        numQuestion = line[0].count('?')

        for i in range(0, 2**(numQuestion)):
            lineCpy = line[0]
            binary = '{0:020b}'.format(i)
            for b in range(len(binary)-1, -1, -1):
                if binary[b] == '0':
                    lineCpy = lineCpy.replace('?', '.', 1)
                else:
                    lineCpy = lineCpy.replace('?', '#', 1)

            if analyzeRow(lineCpy) == line[1]:
                valid += 1
                #print("\t\tVALID:", lineCpy, binary)

    return valid


def groupCombos()->int:

    return 1

def solution2():
    input = getInput()
    
    #Extending each line in the input 5 times
    for i in range(0, len(input)):
        newStr = input[i][0] + '?' + input[i][0] + '?' + input[i][0] + '?' + input[i][0] + '?' + input[i][0]
        newList = []
        for x in range(0,5):
            newList.extend(input[i][1])
        input[i] = (newStr, newList)

    #Iterating through each line to get the number of combinations
    totalValid = 0
    for line in input:
        valid = 1

        code = line[0].split('.')
        while '' in code:
            code.remove('')
        nums = line[1]

        print("code:", code)
        print("nums:", nums)
        
        while len(code) > 0:
            group = code.pop(0)
            print("\tGroup", group)
            if len(group) == nums[0]:
                print("\t\tOne valid option:", nums[0])
                nums.pop(0)
            else:
                space = nums[0]
                ind = 0
                while True:
                    if space + nums[ind+1] + 1 > len(group):
                        break
                    else:
                        space += 1 + nums[ind+1]
                        ind += 1
                numberGroup = nums[:ind+1]
                print("\t\tOptions that fit in space:", numberGroup)
                while ind > -1:
                    nums.pop(0)
                    ind -= 1

        totalValid += valid
        print(line, "has", valid)
        return

    return totalValid


#print("Year 2023, Day 12 solution part 1:", solution1())
print("Year 2023, Day 12 solution part 2:", solution2())