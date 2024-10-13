aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            n = line[0]
            speed = int(line[3])
            flyDur = int(line[6])
            restDur = int(line[-2])
            inpt.append((n, speed, flyDur, restDur))

    return inpt
            

def solution1():
    inpt = getInput()
    raceTime = 2503
    if testing:
        raceTime = 1000

    ans = 0
    for line in inpt:
        n, s, fd, rd = line
        testing and print(n, "flies", s, "km/s for", fd, "then rests", rd)
        
        dist = 0
        t = 0
        flying = True
        while t < raceTime:
            if flying:
                flying = False
                dist += s * fd
                t += fd
            else:
                flying = True
                t += rd
        #If the reindeer was flying when they passed over the end of the race time, we subtract the overshoot dist
        if not flying:
            dist -= (t - raceTime) * s
        testing and print("\t", dist, "after", raceTime, "sec")
        ans = max(ans, dist)

    return ans


def solution2():
    inpt = getInput()
    #Re-initializing each input to [Name, speed, fly duration, rest duration, is flying, total dist, remaining state time, score]
    for i in range(len(inpt)):
        n, s, fd, rd = inpt[i]
        inpt[i] = [n, s, fd, rd, True, 0, fd, 0]

    raceTime = 2503
    if testing:
        raceTime = 1000

    for sec in range(raceTime):
        bestDeer = None #(best distance, index of best distance)
        
        #Updating all reindeer movement
        for r in range(len(inpt)):
            #Decreasing the remaining state time by 1 sec
            inpt[r][6] -= 1
            
            if inpt[r][4]: #If flying, add speed to distance
                inpt[r][5] += inpt[r][1]
                #If fly timer is done, stop flying and set state time to rest duration
                if inpt[r][6] == 0:
                    inpt[r][4] = False
                    inpt[r][6] = inpt[r][3]
            else: #If not flying, do nothing
                #If rest timer is done, start flying and set state time to fly duration
                if inpt[r][6] == 0:
                    inpt[r][4] = True
                    inpt[r][6] = inpt[r][2]
                    
            #Tracking the best distance
            if bestDeer is None or bestDeer[0] < inpt[r][5]:
                bestDeer = (inpt[r][5], [r])
            elif bestDeer is not None and bestDeer[0] == inpt[r][5]:
                bestDeer[1].append(r)
                
        #Awarding 1 point to the deer (possibly plural) with the best distance this second
        for bd in bestDeer[1]:
            inpt[bd][7] += 1

    ans = 0
    for d in inpt:
        testing and print(d[0], "score is", d[-1], "after", raceTime, "sec")
        ans = max(ans, d[7])
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())