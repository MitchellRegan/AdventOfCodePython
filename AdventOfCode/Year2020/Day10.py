#https://adventofcode.com/2020/day/10
#https://adventofcode.com/2020/day/10#part2

# Real data
#data = [99,3,1,11,48,113,131,43,82,19,4,153,105,52,56,109,27,119,147,31,34,13,129,17,61,10,29,24,12,104,152,103,80,116,79,73,21,133,44,18,74,112,136,30,146,100,39,130,91,124,70,115,81,28,151,2,122,87,143,62,7,126,95,75,20,123,63,125,53,45,141,14,67,69,60,114,57,142,150,42,78,132,66,88,140,139,106,38,85,37,51,94,98,86,68]
# Test data
#data = [16,10,15,5,1,11,7,19,6,12,4]
data = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]


def solution1():
    cpy = data[:]
    cpy.sort()
    cpy.insert(0, 0)
    cpy.append(cpy[len(cpy)-1] + 3)

    diff1 = 0
    diff3 = 0

    for i in range(0, len(cpy)-1):
        if cpy[i+1] - cpy[i] == 1:
            diff1 += 1
        elif cpy[i+1] - cpy[i] == 3:
            diff3 += 1
    return diff1 * diff3


def solution2():
    cpy = data[:]
    cpy.sort()
    cpy.insert(0, 0)
    print(cpy)

    unneeded = 0
    unneededInd = []
    neededInd = [0]
    for i in range(0, len(cpy)):
        for j in range(i+2, len(cpy)):
            if cpy[j] - cpy[i] < 3:
                #print("Don't need", cpy[i+1])
                unneeded += 1
                unneededInd.append(cpy[i+1])
            else:
                neededInd.append(i+1)
                break
    print("Needed:", neededInd)
    print("Unneeded:", unneededInd)
    sum = 1
    for i in range(0, len(neededInd)-1):
        sum *= 2**(neededInd[i+1] - neededInd[i])
    return sum

    
print("Year 2020, Day 10 solution part 1:", solution1())
print("Year 2020, Day 10 solution part 2:", solution2())
