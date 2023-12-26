#https://adventofcode.com/2023/day/24
#https://adventofcode.com/2023/day/24#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 1
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d24_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d24_real.txt")


class HailLine():
    def __init__(self, pos:list, vel:list):
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.xSpeed = vel[0]
        self.ySpeed = vel[1]
        self.zSpeed = vel[2]
        self.xySlope = self.ySpeed / self.xSpeed

        #Finding the y intercept
            #y - y_1 = m(x - x_1)
            #y - self.y = (yspeed/xspeed)(x - self.x)
            #y = (yspeed/xspeed)x - (yspeed/xspeed)*self.x + self.y
            #y = -(yspeed/xspeed)*self.x + self.y
        self.yIntercept = (self.xySlope * (-1 * self.x)) + self.y

        #Finding the x intercept
            #y = mx + b
            #y = (yspeed/xspeed)*x + yIntercept
            #0 = (yspeed/xspeed)*x + yIntercept
            #(yspeed/xspeed)*x = - yIntercept
            #x = - (xspeed/yspeed)*yIntercept
        self.xIntercept = (self.xSpeed / self.ySpeed) * -1 * self.yIntercept

    def __str__(self):
        return "Hail Pos: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "), Velocity: (" + str(self.xSpeed) + ", " + str(self.ySpeed) + ", " + str(self.zSpeed) + ")"

    def getYatX(self, x_):
        #y = mx + b
        return (self.xySlope * x_) + self.yIntercept

    def getXatY(self, y_):
        #y = mx + b
        #(1/m)y = x + (1/m)b
        #x = (1/m)y - (1/m)b
        return  ((self.xSpeed / self.ySpeed) * y_) - ((self.xSpeed / self.ySpeed) * self.yIntercept)

    def getPosAtTime(self, time_:int):
        return (self.x + (time_ * self.xSpeed), self.y + (time_ * self.ySpeed), self.z + (time_*self.zSpeed))



def getInput():
    input = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').replace(' ', '').replace('@', ',').split(',')
            for i in range(0, len(line)):
                line[i] = int(line[i])
            hail = HailLine(line[:3], line[3:])
            input.append(hail)

    return input


def solution1():
    input = getInput()
    
    valueRange = [7, 27]
    if not testing:
        valueRange = [200000000000000, 400000000000000]

    numCollisions = 0
    #Iterating through every pair of chunks of hail to see if they collide
    for i in range(0, len(input)-1):
        for j in range(i+1, len(input)):
            a = input[i]
            b = input[j]
            testing and print()
            testing and print(a)
            testing and print(b)

            #If the lines are parallel, we need to do extra checks
            if a.xySlope == b.xySlope:
                testing and print("\tPARALLEL")
            #If not parallel
            else:
                #Get the (x,y) point where the lines intercept
                    #y = (m_a * x) + b_a  compared to  y = (m_b * x) + b_b
                    #Set lines equal to each other at the same y-value
                    #(m_a * x) + b_a = (m_b * x) + b_b
                    #(m_a - m_b) * x = b_b - b_a
                    #x = (b_b - b_a) / (m_a - m_b)
                x = (b.yIntercept - a.yIntercept) / (a.xySlope - b.xySlope)
                y = a.getYatX(x)
                testing and print("\tCollide at point", x, y)

                collision = True
                #Collisions could happen outside the testing zone, which don't count
                if x < valueRange[0] or y < valueRange[0] or x > valueRange[1] or y > valueRange[1]:
                    testing and print("\t\tPoint out of bounds")
                    collision = False
                #Since we're dealing with RAYS and not just LINES, the collision must happen after each ray's starting point
                else:
                    if (x < a.x and a.xSpeed > 0) or (x > a.x and a.xSpeed < 0) or \
                        (y < a.y and a.ySpeed > 0) or (y > a.y and a.ySpeed < 0):
                        testing and print("\t\tHappened in A's past")
                        collision = False
                    elif (x < b.x and b.xSpeed > 0) or (x > b.x and b.xSpeed < 0) or \
                        (y < b.y and b.ySpeed > 0) or (y > b.y and b.ySpeed < 0):
                        testing and print("\t\tHappened in B's past")
                        collision = False

                if collision:
                    numCollisions += 1

    return numCollisions


def solution2():
    input = getInput()
    


    return


print("Year 2023, Day 24 solution part 1:", solution1())
print("Year 2023, Day 24 solution part 2:", solution2())