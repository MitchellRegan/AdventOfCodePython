aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = {}

    with open(inFile, 'r') as f:
        pNum = 0
        for line in f:
            pos,vel,acc = line.replace('\n', '').split(', ')
            pos = [int(x) for x in pos[3:-1].split(',')]
            vel = [int(x) for x in vel[3:-1].split(',')]
            acc = [int(x) for x in acc[3:-1].split(',')]
            inpt[pNum] = (pos,vel,acc)
            pNum += 1

    return inpt
            

def solution1():
    inpt = getInput()
    
    def distAtTime(t_:int, pNum_:int)->int:
        '''Finding the Manhattan distance of a particle from (0,0,0) at a given time.
        Displacement = vt + 0.5at^2
        
        Parameters
        ----------
            t_: Time in seconds.
            pNum_: Particle number which gives the initial position, velocity, and acceleration for XYZ coordinates.
        '''
        pos,vel,acc = inpt[pNum_]
        xDist = pos[0] + (vel[0] * t_) + (0.5 * acc[0] * t_**2)
        yDist = pos[1] + (vel[1] * t_) + (0.5 * acc[1] * t_**2)
        zDist = pos[2] + (vel[2] * t_) + (0.5 * acc[2] * t_**2)
        totalDist = int(abs(xDist) + abs(yDist) + abs(zDist))
        testing and print("Particle", pNum_, "displacement at t =", t_, ":", totalDist)
        return totalDist

    bestDist = None
    bestpNum = None
    for i in inpt.keys():
        testing and print(i, "Pos:", inpt[i][0], "    Vel:", inpt[i][1], "    Acc:", inpt[i][2])
        mdist = distAtTime(100000, i)
        if bestDist is None or mdist < bestDist:
            bestDist = mdist
            bestpNum = i

    return bestpNum


def solution2():
    inpt = getInput()
    
    t = 0
    pDists = {} #Key = (min pNum, max pNum) of a pair of particles, Value = [distances at t=5,000 and t=10,000]
    for t in range(1, 10001):
        collisions = {}#Key = (XYZ) pos, Value = [list of particles at pos]
        
        for p in inpt.keys():
            #Applying the particle's acceleration value to it's velocity
            inpt[p][1][0] += inpt[p][2][0]
            inpt[p][1][1] += inpt[p][2][1]
            inpt[p][1][2] += inpt[p][2][2]
            #Applying the velocity to the particle's current position
            inpt[p][0][0] += inpt[p][1][0]
            inpt[p][0][1] += inpt[p][1][1]
            inpt[p][0][2] += inpt[p][1][2]
            
            #Saving the XYZ position
            ppos = tuple(inpt[p][0])
            if ppos in collisions.keys():
                collisions[ppos].append(p)
            else:
                collisions[ppos] = [p]
                
        for c in collisions.keys():
            if len(collisions[c]) > 1:
                testing and print("\tParticles colliding at", c, ":", collisions[c])
                for p in collisions[c]:
                    inpt.pop(p)

    return len(inpt.keys())


def solution2_v1():
    inpt = getInput()
    
    def getCollisionTime(a_, b_, c_):
        '''Uses the quadratic equation to find the two possible time values for two particles colliding.'''
        #If a is 0, we can't use the quadratic equation because the denominator is 0
        if a_ == 0:
            #No acceleration means we just take c (distance) and divide it by b (velocity) to get t (time)
            if b_ != 0:
                return (-1 * c_) / b_
            else:
                #No velocity and no acceleration means these objects won't collide at all
                return None
        
        #Otherwise we need to use the quadratic equation because the difference in our displacement formula becomes at^2 + bt +c = 0
        numerator = ((b_**2) - (4 * a_ * c_))**0.5
        ans1 = ((-1 * b_) + numerator) / (2 * a_)
        ans2 = ((-1 * b_) - numerator) / (2 * a_)
        
        #Only returning answers with positive time
        if ans1 >= 0 and ans2 < 0:
            return ans1
        elif ans1 < 0 and ans2 >= 0:
            return ans2
        elif ans1 < 0 and ans2 < 0:
            return None
        return min(ans1, ans2)
    

    collisions = {} #Key = timestamp of collision, Value = [list of pnums that collide at this timestamp]
    for i in range(0, len(inpt.keys())-1):
        for j in range(i+1, len(inpt.keys())):
            pos1, vel1, acc1 = inpt[i]
            pos2, vel2, acc2 = inpt[j]
            print(inpt[i])
            print(inpt[j])
            # x1 + v1t + 0.5a1t^2 = x2 + v2t + 0.5a2t^2     get both on one side to set equal to 0
            # 0 = (0.5a1 - 0.5a2)t^2 + (v1 - v2)t + (x1 - x2)    Use quadratic equation, so figure out vars
            # Quadratic Equation Vars:
            #   a = (0.5a1 - 0.5a2)
            #   b = (v1 - v2)
            #   c = (x1 - x2)
            validCollision = True
            
            xCollisionTime = getCollisionTime(acc1[0]/2 - acc2[0]/2, vel1[0] - vel2[0], pos1[0] - pos2[0])
            if xCollisionTime is None and pos1[0] != pos2[0]:
                validCollision = False
                
            yCollisionTime = getCollisionTime(acc1[1]/2 - acc2[1]/2, vel1[1] - vel2[1], pos1[1] - pos2[1])
            if yCollisionTime is None and pos1[1] != pos2[1]:
                validCollision = False
            elif yCollisionTime is not None and xCollisionTime is not None and yCollisionTime != xCollisionTime:
                validCollision = False
                
            zCollisionTime = getCollisionTime(acc1[2]/2 - acc2[2]/2, vel1[2] - vel2[2], pos1[2] - pos2[2])
            if zCollisionTime is None and pos1[2] != pos2[2]:
                validCollision = False
            
            if xCollisionTime is None and yCollisionTime is None and zCollisionTime is None:
                validCollision = False
            
            print("\tX Collision Time:", xCollisionTime, "\n")
            print("\tY Collision Time:", yCollisionTime, "\n")
            print("\tZ Collision Time:", zCollisionTime, "\n")

    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())