#https://adventofcode.com/2020/day/15
#https://adventofcode.com/2020/day/15#part2

# Real data
#data = [2,0,1,7,4,14,18]
# Test data
data = [0,3,6]


def solution1():
    valOrder = data[:]

    for turn in range(len(data), 2020):
        # If the current value hasn't been seen before, we add 0 this turn
        if valOrder[turn-1] not in valOrder[:turn-1]:
            valOrder.append(0)
        # If it has been seen, we add the difference in index values from when it was last seen
        else:
            prevInd = turn-2
            for i in range(turn-2, -1, -1):
                if valOrder[i] == valOrder[turn-1]:
                    prevInd = i + 1
                    break
            valOrder.append(turn - (prevInd))

    return valOrder[len(valOrder)-1]


def solution2():
    # Dictionary to store a value that's been seen, and what turn it was last seen on
    valDict = {}
    prevVal = data[0]
    for v in range(1, len(data)):
        valDict[prevVal] = v+1
        prevVal = data[v]

    #for turn in range(len(data), 30000000):
    for turn in range(len(data), 10):
        print("Turn", turn+1, "previous number:", prevVal)
        print(" -", valDict)
        # If the previous value hasn't been seen before, we add 0 this turn
        if prevVal not in valDict.keys():
            print(" - Not seen", prevVal, "adding 0")
            valDict[prevVal] = turn+1
            prevVal = 0
        # If it has been seen, we add the difference in index values from when it was last seen
        else:
            print(" - Seen", prevVal, "on turn", valDict[prevVal], "adding", (turn + 1 - valDict[prevVal]))
            prevVal = turn + 1 - valDict[prevVal]
            valDict[prevVal] = turn+1

    return prevVal

    
print("Year 2020, Day 15 solution part 1:", solution1())
print("Year 2020, Day 15 solution part 2:", solution2())

