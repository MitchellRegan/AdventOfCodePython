#https://adventofcode.com/2023/day/22
#https://adventofcode.com/2023/day/22#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 1:
    inFile = os.path.join(inFileDir, "InputTestFiles/d22_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d22_real.txt")


class Brick:
    def __init__(self, xMin, yMin, zMin, xMax, yMax, zMax):
        self.xRange = [min(xMin, xMax), max(xMin, xMax)]
        self.yRange = [min(yMin, yMax), max(yMin, yMax)]
        self.zRange = [min(zMin, zMax), max(zMin, zMax)]
        self.touchingBelow = None
        self.touchingAbove = None

    def __eq__(self, other):
        return self.xRange == other.xRange and self.yRange == other.yRange and self.zRange == other.zRange

    def __str__(self):
        return "[" + str(self.xRange[0]) + ", " + str(self.yRange[0]) + ", " + str(self.zRange[0]) + "] - [" +\
                str(self.xRange[1]) + ", " + str(self.yRange[1]) + ", " + str(self.zRange[1]) + "]"

    def width(self)->int:
        '''How wide this block is on the x-axis'''
        return self.xRange[1] - self.xRange[0]

    def depth(self)->int:
        '''How deep this block is on the y-axis'''
        return self.yRange[1] - self.yRange[0]

    def height(self)->int:
        '''How tall this block is on the z-axis'''
        return self.zRange[1] - self.zRange[0]

    def getBlocksTouchingBelow(self, blockList:list, saveResults:bool=True)->list:
        '''Returns the list of blocks that this block is resting on top of.'''
        if self.touchingBelow is not None:
            return self.touchingBelow
        touching = []

        for b in blockList:
            valid = True
            #The block must not be this block we're checking
            if b == self:
                valid = False
            #The other block's top z-value must be equal to this block's z-value minus 1
            elif b.zRange[1] != self.zRange[0]-1:
                valid = False
            #This block's x range must have at least one coordinate in common
            elif b.xRange[1] < self.xRange[0] or self.xRange[1] < b.xRange[0]:
                valid = False
            #This block's y range must have at least one coordinate in common
            elif b.yRange[1] < self.yRange[0] or self.yRange[1] < b.yRange[0]:
                valid = False

            if valid:
                touching.append(b)
        
        if saveResults:
            self.touchingBelow = touching
        return touching
    
    def getBlocksTouchingAbove(self, blockList:list)->list:
        '''Returns the list of blocks that are resting on top of this one.'''
        if self.touchingAbove is not None:
            return self.touchingAbove
        touching = []
        
        for b in blockList:
            valid = True
            #The block must not be this block we're checking
            if b == self:
                valid = False
            #The other block's bottom z-value must be equal to this block's z-value + 1
            elif b.zRange[0] != self.zRange[1]+1:
                valid = False
            #This block's x range must have at least one coordinate in common
            elif b.xRange[1] < self.xRange[0] or self.xRange[1] < b.xRange[0]:
                valid = False
            #This block's y range must have at least one coordinate in common
            elif b.yRange[1] < self.yRange[0] or self.yRange[1] < b.yRange[0]:
                valid = False

            if valid:
                touching.append(b)
             
        self.touchingAbove = touching
        return touching
    
    def fall(self):
        if self.zRange[0] > 1:
            self.zRange = [self.zRange[0]-1, self.zRange[1]-1]


def getInput():
    bricks = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split("~")
            pos1 = line[0].split(',') #Bottom of the brick
            pos2 = line[1].split(',') #Top of the brick

            for p in range(0, 3):
                pos1[p] = int(pos1[p])
                pos2[p] = int(pos2[p])

            newBrick = Brick(pos1[0], pos1[1], pos1[2], pos2[0], pos2[1], pos2[2])
            bricks.append(newBrick)

    return bricks


def solution1():
    brickList = getInput()

    #Sorting the bricks so that they're in ascending order of falling distance (z-value)
    brickList.sort(key=lambda b: b.zRange[0])

    #Tracking the indexes of all of the bricks that still need to fall
    fallingInd = [i for i in range(0, len(brickList))]
    while len(fallingInd) > 0:
        stillFalling = []
        for bi in fallingInd:
            #If the brick at this brick index (bi) has a lower height above 1 (ground) and isn't touching any bricks from below
            if brickList[bi].zRange[0] > 1 and len(brickList[bi].getBlocksTouchingBelow(brickList, False)) == 0:
                stillFalling.append(bi)
                brickList[bi].fall()

        #Updating the list of indexes that are still falling
        fallingInd = stillFalling

    #Iterating through each brick to see if it can be removed without others falling
    numRemovable = 0
    
    for bi in range(0, len(brickList)):
        brick = brickList[bi]
        removable = True

        #Finding all of the bricks resting on this one
        above = brick.getBlocksTouchingAbove(brickList)
        for aboveBrick in above:
            #If this above-brick is resting on only our current brick, our current brick can't be removed
            if len(aboveBrick.getBlocksTouchingBelow(brickList)) == 1:
                removable = False

        if removable:
            numRemovable += 1
    
    return numRemovable


def solution2():
    brickList = getInput()

    #Sorting the bricks so that they're in ascending order of falling distance (z-value)
    brickList.sort(key=lambda b: b.zRange[0])

    #Tracking the indexes of all of the bricks that still need to fall
    fallingInd = [i for i in range(0, len(brickList))]
    while len(fallingInd) > 0:
        stillFalling = []
        for bi in fallingInd:
            #If the brick at this brick index (bi) has a lower height above 1 (ground) and isn't touching any bricks from below
            if brickList[bi].zRange[0] > 1 and len(brickList[bi].getBlocksTouchingBelow(brickList)) == 0:
                stillFalling.append(bi)
                brickList[bi].fall()

        #Updating the list of indexes that are still falling
        fallingInd = stillFalling

    #Iterating through each brick to see if it can be removed without others falling
    numRemovable = 0
    
    for bi in range(0, len(brickList)):
        brick = brickList[bi]
        removable = True

        #Finding all of the bricks resting on this one
        above = brick.getBlocksTouchingAbove(brickList)
        for aboveBrick in above:
            #If this above-brick is resting on only our current brick, our current brick can't be removed
            if len(aboveBrick.getBlocksTouchingBelow(brickList)) == 1:
                removable = False

        if removable:
            numRemovable += 1
    
    return numRemovable


#print("Year 2023, Day 22 solution part 1:", solution1())
print("Year 2023, Day 22 solution part 2:", solution2())