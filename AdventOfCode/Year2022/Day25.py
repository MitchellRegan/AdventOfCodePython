#https://adventofcode.com/2022/day/25
#https://adventofcode.com/2022/day/2#part25

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d25_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d25_real.txt")


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
    remainder = val + 0
    snafuVals = [1, 2, -2, -1, 0]
    snafuSymb = ["1", "2", "=", "-", "0"]
    pwr = 0

    i = (val-1) % 5
    snafu.insert(0, snafuSymb[i])
    remainder -= snafuVals[i] * 5**pwr
    pwr += 1
    
    #print("Remainder", remainder)
    while remainder != 0:
        i = int((remainder - 2*(5**(pwr-1))) / 5**pwr) % 5 #IDK what this monstrosity is. Was very tired when writing it, but it seems to work
        snafu.insert(0, snafuSymb[i])
        remainder -= snafuVals[i] * 5**pwr
        pwr += 1
        
    return ''.join(snafu)


def solution1():
    sum = 0
    #Converting each line in the file from the SNAFU format to int and addint it to our sum
    with open(inFile, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            val = snafuToInt(line)
            #print("Snafu:", line, "\tDecimal:", val)
            sum += val

    #Converting our sum back to snafu format for our final answer
    #print("Int sum:", sum)
    return intToSnafu(sum)


def solution2():
    return


print("Year 2022, Day 25 solution part 1:", solution1())
print("Year 2022, Day 25 solution part 2:", solution2())