#https://adventofcode.com/2022/day/6
#https://adventofcode.com/2022/day/6#part2

#inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2022\\InputTestFiles\\d6_test.txt"
inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2022\\InputRealFiles\\d6_real.txt"

def solution1():
    strIn = ""
    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            strIn += line

    for i in range(3,len(strIn)):
        if strIn[i:i+4].count(strIn[i]) == 1 and strIn[i:i+4].count(strIn[i+1]) == 1 and strIn[i:i+4].count(strIn[i+2]) == 1 and strIn[i:i+4].count(strIn[i+3]) == 1:
            return i+4
    return 0


def solution2():
    strIn = ""
    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            strIn += line

    for i in range(3,len(strIn)):
        isValid = True
        for j in range(i, i+14):
            if strIn[i:i+14].count(strIn[j]) > 1:
                isValid = False
                break
        if isValid:
            return i+14
    return 0


print("Year 2022, Day 6 solution part 1:", solution1())
print("Year 2022, Day 6 solution part 2:", solution2())