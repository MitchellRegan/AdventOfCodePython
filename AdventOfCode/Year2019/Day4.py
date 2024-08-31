#https://adventofcode.com/2019/day/4
#https://adventofcode.com/2019/day/4#part2

inputRange = []
if 1:
    inputRange = [246515,739105]
else:
    inputRange = [111111,123444]
    

def solution1():
    validPW = 0

    valStr = ""
    #Looping through every value in the given input range
    for val in range(inputRange[0], inputRange[1]+1):
        valStr = str(val)
        #bool for if the pw has values that are never decreasing and has a double
        notDec = True
        hasDbl = False
        
        #Looping through each char in the string
        for c in range(0,5):
            #Checking for 2 digits of equal value next to each other
            if valStr[c] == valStr[c+1]:
                hasDbl = True
            #Checking for digits that are decreasing
            if int(valStr[c]) > int(valStr[c+1]):
                notDec = False

        if notDec and hasDbl:
            validPW += 1

    return validPW


def solution2():
    validPW = 0

    valStr = ""
    #Looping through every value in the given input range
    for val in range(inputRange[0], inputRange[1]+1):
        valStr = str(val)
        #bool for if the pw has values that are never decreasing, has a double, and 
        decreasing = False
        
        #Looping through each char in the string
        for c in range(0,5):
            #Checking for any digit sequences that decrease in value
            if int(valStr[c]) > int(valStr[c+1]):
                decreasing = True
                break
            
        #If digits decrease, invalid
        if decreasing:
            continue
            
        #Checking for different lengths of same-digit sequences
        digitSeq = []
        ptr = 0
        while ptr < 6:
            c = valStr.count(valStr[ptr])
            if c > 1: #Ignoring sequences of 1
                digitSeq.append(c)
            ptr += c
            
        #If there aren't any sequences of 2+ of the same digit, invalid
        if len(digitSeq) == 0:
            continue
        
        #Must contain at least a single instance of a sequence of exactly 2 similar digits
        if 2 not in digitSeq:
            continue
        
        #If it made it this far, the value is valid
        validPW += 1

    return validPW

    
print("Year 2019, Day 4 solution part 1:", solution1())
print("Year 2019, Day 4 solution part 2:", solution2())