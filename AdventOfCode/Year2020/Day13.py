#https://adventofcode.com/2020/day/13
#https://adventofcode.com/2020/day/13#part2
import math

# Real data
#data = [1001798,[19,'x','x','x','x','x','x','x','x',41,'x','x','x','x','x','x','x','x','x',859,'x','x','x','x','x','x','x',23,'x','x','x','x',13,'x','x','x',17,'x','x','x','x','x','x','x','x','x','x','x',29,'x',373,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',37]]
# Test data
data = [939,[7,13,'x','x',59,'x',31,19]]


def solution1():
    bestInd = 0
    bestTime = data[1][0] - (data[0] % data[1][0])

    for i in range(1, len(data[1])):
        if data[1][i] is not 'x':
            time = data[1][i] - (data[0] % data[1][i])
            if time < bestTime:
                bestInd = i
                bestTime = time

    return (data[1][bestInd] * bestTime)


def solution2():
    # Starting the timer at the first time bus with the longest timer leaves AFTER the initial leaving
    startInd = 0
    for i in range(1, len(data[1])):
        if data[1][i] is not 'x' and data[1][i] > data[1][startInd]:
            startInd = i
    #curTime = data[1][startInd] + startInd
    curTime = data[1][startInd] * 116414435389

    # Looping until we get a time that matches our requirements
    count = 0
    while True:
        if count % 100000 == 0:
            print(" - Count:", count, " Current time:", curTime)
        count += 1

        valid = True
        # Checking each subsequent bus
        for i in range(0, len(data[1])):
            # Ignoring non-active bus lines (x) and the bus with the longest timer since we know the time will be divisible 
            if data[1][i] is not 'x' and i != startInd:
                if (curTime + i - startInd) % data[1][i] != 0:
                    valid = False
                    break

        # If we don't find a match, we increase the time
        if not valid:
            curTime += data[1][startInd]
        # If we did find a match, we return
        else:
            return curTime - startInd

    
def solution2_v2():
    ans = 1
    for i in range(0, len(data[1])):
        if data[1][i] is not 'x':
            ans = int((ans * data[1][i]) / math.gcd(ans, data[1][i])) - i

    return ans

print("Year 2020, Day 13 solution part 1:", solution1())
print("Year 2020, Day 13 solution part 2:", solution2_v2())

