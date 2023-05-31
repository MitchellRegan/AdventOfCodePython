#https://adventofcode.com/2021/day/17
#https://adventofcode.com/2021/day/17#part2

useRealInput = True
# Real data target area: x=117..164, y=-140..-89
# Test data target area: x=20...30,  y=-10...-5


def getInput():
    '''Gives the coordinates for the target zone designated by the input.
    returns: xMin, xMax, yMin, yMax
    '''
    #If we use the real input, we give the real x and y ranges
    if useRealInput:
        return 117, 164, -140, -89
    #If we don't use the real input, we give the test x and y ranges
    return 20, 30, -10, -5


def simulateYHeight(vel_, yMin_, yMax_):
    yPos = 0
    prevPos = 0
    bestPos = 0
    curVel = vel_

    while yPos >= yMin_:
        prevPos = yPos
        yPos += curVel

        if yPos > bestPos:
            bestPos = yPos

        curVel -= 1

    if prevPos >= yMin_ and prevPos <= yMax_:
        return bestPos
    else:
        return -1


def solution1():
    xMin, xMax, yMin, yMax = getInput()

    highestY = 0
    consecutiveMisses = 0
    yStartVel = 0

    while consecutiveMisses < 100:
        yStartVel += 1

        height = simulateYHeight(yStartVel, yMin, yMax)

        if height == -1:
            consecutiveMisses += 1
        elif height > highestY:
            highestY = height

    return highestY


def solution2():
    #Getting the coordinate ranges for the target zone
    xMin, xMax, yMin, yMax = getInput()
    #List to contain all valid ordered pairs
    validPairs = []

    #The maximum x velocity is equal to the value of xMax, because any higher and it would tunnel through the target zone
    maxXVelocity = xMax
    #Finding the minimum x velocity needed to reach the target zone
    minXVelocity = 1
    while True:
        maxDistance = 0
        for i in range(0, minXVelocity):
            maxDistance += minXVelocity - i

        if maxDistance >= xMin:
            break
        else:
            minXVelocity += 1
            
    #The minimum y velocity is equal to the value of yMin, because any smaller value would undershoot the target entirely
    minYVelocity = yMin
    #The maximum y velocity is 1 less than the absolute value of yMin, because any larger value would make the downward velocity tunnel through the target zone
    maxYVelocity = abs(yMin)-1

    #Looping through all x and y velocities within the bounds we've found
    for x in range(minXVelocity, maxXVelocity+1):
        for y in range(minYVelocity, maxYVelocity+1):
            #Variables to designate the probe's current coordinate point, starting with the xy velocities given
            vel = [x, y]
            pos = [x, y]

            #While the probe hasn't gone past the target zone, we update its position
            while pos[0] <= xMax and pos[1] >= yMin:
                #If the probe is inside the target zone, we add it to the list of valid pairs
                if xMin <= pos[0] and pos[0] <= xMax and yMin <= pos[1] and pos[1] <= yMax:
                    validPairs.append((pos[0], pos[1]))
                    break
                #Otherwise we update the position and velocity
                else:
                    #Drag reduces the x velocity by 1 each movement (to a min of 0), and gravity reduces y velocity by 1 (no minimum)
                    if vel[0] > 0:
                        vel[0] -= 1
                    vel[1] -= 1

                    pos[0] += vel[0]
                    pos[1] += vel[1]
    
    #print("X velocities must be between", minXVelocity, "and", maxXVelocity)
    #print("Y velocities must be between", minYVelocity, "and", maxYVelocity)

    #Returning the total number of ordered pair velocities that are valid
    #print(validPairs)
    return len(validPairs)

    
print("Year 2021, Day 17 solution part 1:", solution1())
print("Year 2021, Day 17 solution part 2:", solution2())