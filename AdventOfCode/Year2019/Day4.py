#https://adventofcode.com/2019/day/4
#https://adventofcode.com/2019/day/4#part2

input = []
if 1:
    input = [246515,739105]
else:
    input = [111111,111111]
    

def solution1():
    validPW = 0

    valStr = ""
    #Looping through every value in the given input range
    for val in range(input[0], input[1]+1):
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
    for val in range(input[0], input[1]+1):
        valStr = str(val)
        #bool for if the pw has values that are never decreasing and has a double
        notDec = True
        hasDbl = False
        concurrentVals = 1
        dupeStrings = []
        
        #Looping through each char in the string
        for c in range(0,5):
            #Checking for digits that are decreasing
            if valStr[c] > valStr[c+1]:
                hasDbl = False
                notDec = False
                break

            #Checking for 2 digits of equal value next to each other
            if valStr[c] == valStr[c+1]:
                concurrentVals += 1
                hasDbl = True
                if c == 4:
                    subStr = ""
                    for s in range(concurrentVals):
                        subStr += valStr[c]
                    dupeStrings.append(subStr)
            #If a string of concurrent values are broken, we check if there was an odd number
            elif concurrentVals > 1:
                subStr = ""
                for s in range(concurrentVals):
                    subStr += valStr[c]
                dupeStrings.append(subStr)
                concurrentVals = 1

        # If a double value was found
        if hasDbl:
            if len(dupeStrings[len(dupeStrings)-1]) > 2:
                hasDbl = False
            #else:
            #    print(dupeStrings)
            #If only one double was found, it must have only 2 values in it
            #if len(dupeStrings) == 1 and len(dupeStrings[0]) != 2:
            #    hasDbl = False
            # If there's more than 1 group of doubles
            #elif len(dupeStrings) > 1:
                #If the largest double value is greater than 2
            #    for s in range(len(dupeStrings)-1):
            #        if len(dupeStrings[s]) < len(dupeStrings[-1]):
            #            hasDbl = False
            #            break

        #The valid password must have a double and no decreasing values
        if notDec and hasDbl:
            validPW += 1

    return validPW

    
print("Year 2019, Day 4 solution part 1:", solution1())
print("Year 2019, Day 4 solution part 2:", solution2())

#283 too low
#417 too low
#547 not it
#579 not it
#583 not it (dunno if too low or high)
#735 too high