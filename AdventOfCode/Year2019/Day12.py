#https://adventofcode.com/2019/day/12
#https://adventofcode.com/2019/day/12#part2

import os
import itertools
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 1
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d12_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d12_real.txt")


class Moon:
    '''Class to store each moon's XYZ position and XYZ velocity.'''
    
    def __init__(self, x_:int, y_:int, z_:int, xv_:int, yv_:int, zv_:int):
        #Setting the XYZ positions
        self.x = x_
        self.y = y_
        self.z = z_
        #Setting the XYZ velocities
        self.xVel = xv_
        self.yVel = yv_
        self.zVel = zv_
        
        
    def applyGravity(self, otherMoon_):
        if self.x < otherMoon_.x:
            self.xVel += 1
        elif self.x > otherMoon_.x:
            self.xVel -= 1
            
        if self.y < otherMoon_.y:
            self.yVel += 1
        elif self.y > otherMoon_.y:
            self.yVel -= 1
            
        if self.z < otherMoon_.z:
            self.zVel += 1
        elif self.z > otherMoon_.z:
            self.zVel -= 1
            

    def updatePos(self):
        self.x += self.xVel
        self.y += self.yVel
        self.z += self.zVel


def getInput():
    moons = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').replace('<', '').replace('>', '').split(',')
            x = int(line[0].split('=')[1])
            y = int(line[1].split('=')[1])
            z = int(line[2].split('=')[1])
            #newMoon = Moon(x,y,z,0,0,0)
            moons.append(Moon(x,y,z,0,0,0)) #First list is XYZ pos, second list is XYZ velocity

    return moons
            

def solution1():
    moons = getInput()
    
    for step in range(1000):
        #Applying gravitation changes to each moon's velocity
        for m1 in range(0, len(moons)-1):
            for m2 in range(m1+1, len(moons)):
                moons[m1].applyGravity(moons[m2])
                moons[m2].applyGravity(moons[m1])
        #Updating the positions of each moon due to their current velocity
        for m in moons:
            m.updatePos()

    totalEnergy = 0
    for m in moons:
        totalEnergy += (abs(m.x) + abs(m.y) + abs(m.z)) * (abs(m.xVel) + abs(m.yVel) + abs(m.zVel))
    return totalEnergy


def solution2():
    moons = getInput()
    moonStates = {}
    
    step = 1
    while True:
        #Applying gravitation changes to each moon's velocity
        for m1 in range(0, len(moons)-1):
            for m2 in range(m1+1, len(moons)):
                moons[m1].applyGravity(moons[m2])
                moons[m2].applyGravity(moons[m1])
        #Updating the positions of each moon due to their current velocity
        for m in moons:
            m.updatePos()
            
        #Getting the tuple to act as the state of all moon positions and velocities
        moonState = []
        for m in moons:
            moonState.extend([m.x, m.y, m.z, m.xVel, m.yVel, m.zVel])
        moonState = tuple(moonState)
        if moonState in moonStates.keys():
            return step
        else:
            moonStates[moonState] = True

        step += 1
    return -1


print("Year 2019, Day 12 solution part 1:", solution1())
print("Year 2019, Day 12 solution part 2:", solution2())