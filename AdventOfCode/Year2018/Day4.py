from statistics import harmonic_mean


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
            line = line.replace('\n', '').replace('[', '').replace(']', '').split(' ')
            year = int(line[0].split('-')[0])
            mon = int(line[0].split('-')[1])
            day = int(line[0].split('-')[2])
            hour = int(line[1].split(':')[0])
            minute = int(line[1].split(':')[1])
            state = ""
            if line[2] == "Guard":
                state = int(line[3].replace('#', ''))
            elif line[2] == "falls":
                state = "sleep"
            else:
                state = "awake"
                
            inpt.append([year, mon, day, hour, minute, state])
    return inpt
            

def solution1():
    inpt = getInput()
    
    #Sorting the entries based on their times (using bubble-sort I know it's bad)
    for i in range(0, len(inpt)-1):
        for j in range(i+1, len(inpt)):
            yr1,mo1,dy1,hr1,mn1,st1 = inpt[i]
            yr2,mo2,dy2,hr2,mn2,st2 = inpt[j]
            min1 = mn1 + (hr1 * 60) + (dy1 * 1440)
            min2 = mn2 + (hr2 * 60) + (dy2 * 1440)

            if yr1 > yr2 or (yr1 == yr2 and mo1 > mo2) or (yr1 == yr2 and mo1 == mo2 and min1 > min2):
                placeholder = inpt[i]
                inpt[i] = inpt[j]
                inpt[j] = placeholder
            
    
    prevMin = None
    guardID = None
    guardState = "awake"
    guardTimes = {}
    for line in inpt:
        testing and print(line)
        yr,mo,dy,hr,mn,state = line
        curMin = mn
        if hr != 0:
            curMin = 0
        
        #Setting our initial guard/time state
        if guardID is None:
            guardID = state
            prevMin = curMin
            guardState = "awake"
            continue
        
        #If the previous state was sleep, we keep track of all minutes he was asleep up til this point
        if guardState == "sleep":
            for x in range(prevMin, curMin):
                gt = (guardID, x)
                if gt in guardTimes.keys():
                    guardTimes[gt] += 1
                else:
                    guardTimes[gt] = 1

        #If there's a change in guard shifts
        if type(state) is int:
            testing and print("\tSwitching to guard", state)
            guardID = state
            guardState = "awake"
        else:
            guardState = state
            
        prevMin = curMin
        
    #Finding the guard that slept the most number of minutes
    guardSleepCount = {}
    bestGuard = None
    for x in guardTimes.keys():
        g,m = x
        if g in guardSleepCount.keys():
            guardSleepCount[g] += guardTimes[x]
        else:
            guardSleepCount[g] = guardTimes[x]
            
        if bestGuard is None or guardSleepCount[g] > guardSleepCount[bestGuard]:
            bestGuard = g
            
    testing and print("\nGuard sleep counts:", guardSleepCount, "\n\tBest Guard:", bestGuard, ":", guardSleepCount[bestGuard])
    
    #Finding the minute that the sleepiest guard slept the most
    sleepMinCount = {}
    bestMin = None
    for x in guardTimes.keys():
        g,m = x
        if g != bestGuard:
            continue
        
        if m not in sleepMinCount.keys():
            sleepMinCount[m] = guardTimes[x]
        else:
            sleepMinCount[m] += guardTimes[x]
            
        if bestMin is None or sleepMinCount[m] > sleepMinCount[bestMin]:
            bestMin = m
            
    testing and print("\tBest Minute:", bestMin, ":", sleepMinCount[bestMin])
    return bestMin * bestGuard


def solution2():
    inpt = getInput()
    
    #Sorting the entries based on their times (using bubble-sort I know it's bad)
    for i in range(0, len(inpt)-1):
        for j in range(i+1, len(inpt)):
            yr1,mo1,dy1,hr1,mn1,st1 = inpt[i]
            yr2,mo2,dy2,hr2,mn2,st2 = inpt[j]
            min1 = mn1 + (hr1 * 60) + (dy1 * 1440)
            min2 = mn2 + (hr2 * 60) + (dy2 * 1440)

            if yr1 > yr2 or (yr1 == yr2 and mo1 > mo2) or (yr1 == yr2 and mo1 == mo2 and min1 > min2):
                placeholder = inpt[i]
                inpt[i] = inpt[j]
                inpt[j] = placeholder
            
    prevMin = None
    guardID = None
    guardState = "awake"
    guardTimes = {}
    for line in inpt:
        yr,mo,dy,hr,mn,state = line
        curMin = mn
        if hr != 0:
            curMin = 0
        
        #Setting our initial guard/time state
        if guardID is None:
            guardID = state
            prevMin = curMin
            guardState = "awake"
            continue
        
        #If the previous state was sleep, we keep track of all minutes he was asleep up til this point
        if guardState == "sleep":
            for x in range(prevMin, curMin):
                gt = (guardID, x)
                if gt in guardTimes.keys():
                    guardTimes[gt] += 1
                else:
                    guardTimes[gt] = 1

        #If there's a change in guard shifts
        if type(state) is int:
            guardID = state
            guardState = "awake"
        else:
            guardState = state
            
        prevMin = curMin
        
    #Finding the most consistent minute that any guard was asleep for
    bestGuardMin = None
    for x in guardTimes.keys():
        if bestGuardMin is None or guardTimes[x] > guardTimes[bestGuardMin]:
            bestGuardMin = x
            
    testing and print("Guard", bestGuardMin[0], "was asleep on min", bestGuardMin[1], guardTimes[bestGuardMin], "times")        
    return bestGuardMin[0] * bestGuardMin[1]


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())