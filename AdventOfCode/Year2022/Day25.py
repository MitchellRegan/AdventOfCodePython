#https://adventofcode.com/2022/day/25
#https://adventofcode.com/2022/day/2#part25

import os
inFileDir = os.path.dirname(__file__)
inFile = os.path.join(inFileDir, "InputTestFiles/d25_test.txt")
#inFile = os.path.join(inFileDir, "InputRealFiles/d25_real.txt")


def snafuToInt(snafu):
    val = 0
    #Iterating through each index of the snafu string
    for i in range(0, len(snafu)):
        start = 5**(len(snafu) - i-1)

        #'1' means 1 x the power of 5
        if snafu[i] == '1':
            val += start
        #'2' means 2 x the power of 5
        elif snafu[i] == '2':
            val += 2*start
        #'-' means -1 x the power of 5
        elif snafu[i] == '-':
            val -= start
        #'=' means -2 x the power of 5
        elif snafu[i] == '=':
            val -= 2*start

    return val


def intToSnafu(val):
    snafu = []
    #Finding the largest power of 5 that we can remove from the int
    i = 0
    while i < 6:
        remainder = val % 5**i
        print(val, "%", (5**i), "=", remainder)
        if remainder == 0:
            snafu.append('0')
        if remainder == 1:
            snafu.append('1')
        elif remainder == 2:
            snafu.append('2')
        elif remainder == 3:
            snafu.append('')

        i+=1
        val -= remainder

    print("Remainder:", val)
    return ''.join(snafu)


def solution1():
    sum = 0
    #Converting each line in the file from the SNAFU format to int and addint it to our sum
    with open(inFile, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            sum += snafuToInt(line)

    #Converting our sum back to snafu format for our final answer
    print("Int sum:", sum)
    return intToSnafu(sum)


def solution2():
    return


print("Year 2022, Day 25 solution part 1:", solution1())
print("Year 2022, Day 25 solution part 2:", solution2())