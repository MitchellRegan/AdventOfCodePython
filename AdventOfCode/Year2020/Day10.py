#https://adventofcode.com/2020/day/10
#https://adventofcode.com/2020/day/10#part2

# Real data
data = [99,3,1,11,48,113,131,43,82,19,4,153,105,52,56,109,27,119,147,31,34,13,129,17,61,10,29,24,12,104,152,103,80,116,79,73,21,133,44,18,74,112,136,30,146,100,39,130,91,124,70,115,81,28,151,2,122,87,143,62,7,126,95,75,20,123,63,125,53,45,141,14,67,69,60,114,57,142,150,42,78,132,66,88,140,139,106,38,85,37,51,94,98,86,68]
# Test data
#data = [16,10,15,5,1,11,7,19,6,12,4]
#data = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]


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


def recursiveValidationCheck(checkIndex_=1, arr_=[])->int:
    #Exit check for the recursion, counting the current array as valid
    if checkIndex_ >= len(arr_)-1:
        #print("\t\t\t", arr_)
        return 1
    
    #If the value at the current index is necessary, we move to the next index
    offset = 0
    while checkIndex_ + offset < len(arr_)-1:
        #print("\tIndex:", checkIndex_, "+ offset:", offset)
        #print("\tComparing values", arr_[checkIndex_+offset-1], arr_[checkIndex_+offset+1])
        if arr_[checkIndex_+offset+1] - arr_[checkIndex_+offset-1] > 3:
            #print("\t\tDifference > 3. Moving to next index")
            offset += 1
        #Breaking the loop once an unnecessary index value is found
        else:
            #print("\t\tDifference <= 3, value", arr_[checkIndex_+offset], "unnecessary")
            break
        
    if checkIndex_ + offset < len(arr_) - 1:
        smallArr_ = arr_[:]
        smallArr_.pop(checkIndex_+offset)
        return recursiveValidationCheck(checkIndex_+offset, smallArr_) + recursiveValidationCheck(checkIndex_+offset+1, arr_)
    return 1


def solution2():
    cpy = data[:]
    cpy.sort()
    cpy.insert(0, 0)
    cpy.append(3+cpy[-1])
    return recursiveValidationCheck(1, cpy)

    
print("Year 2020, Day 10 solution part 1:", solution1())
print("Year 2020, Day 10 solution part 2:", solution2())
