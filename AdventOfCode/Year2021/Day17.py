#https://adventofcode.com/2021/day/17
#https://adventofcode.com/2021/day/17#part2

# Real data
# target area: x=117..164, y=-140..-89
#data = [[117,164], [-140, -89]]
# Test data
# target area: x=20..30, y=-10..-5
data = [[20, 30], [-10, -5]]


def simulateYHeight(vel_):
    yPos = 0
    prevPos = 0
    bestPos = 0
    curVel = vel_

    while yPos >= data[1][0]:
        prevPos = yPos
        yPos += curVel

        if yPos > bestPos:
            bestPos = yPos

        curVel -= 1

    if prevPos >= data[1][0] and prevPos <= data[1][1]:
        return bestPos
    else:
        return -1


def solution1():
    highestY = 0
    consecutiveMisses = 0
    yStartVel = 0

    while consecutiveMisses < 100:
        yStartVel += 1

        height = simulateYHeight(yStartVel)

        if height == -1:
            consecutiveMisses += 1
        elif height > highestY:
            highestY = height

    print("Year 2021, Day 17 solution part 1:", highestY)


def solution2():
    validX = []
    for x in range(0, data[0][1]+1):
        pos = 0
        curVel = x
        while curVel > 0:
            pos += curVel
            curVel -= 1

            if pos >= data[0][0] and pos <= data[0][1]:
                validX.append(x)
                break

    print("All valid x velocities:", validX)
    print("Year 2021, Day 17 solution part 2:")


solution1()
solution2()