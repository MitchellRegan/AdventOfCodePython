aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    locations = {}
    ticket = []
    nearby = []

    fieldType = 0 #0 = "location", 1 = "your ticket", 2 = "nearby tickets"
    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')

            #Getting locations
            if fieldType == 0:
                if len(line) == 0:
                    fieldType += 1
                else:
                    locName = line.split(": ")[0]
                    range1 = line.split(' ')[-3].split('-')
                    range2 = line.split(' ')[-1].split('-')
                    locations[locName] = [int(range1[0]), int(range1[1]), int(range2[0]), int(range2[1])]
            #Your ticket
            elif fieldType == 1:
                if len(line) == 0:
                    fieldType += 1
                elif line != "your ticket:":
                    line = line.split(',')
                    ticket = [int(x) for x in line]
            #Nearby tickets
            elif fieldType == 2:
                if line != "nearby tickets:":
                    line = line.split(',')
                    nearby.append([int(x) for x in line])
    return locations, ticket, nearby
            

def solution1():
    locations, ticket, nearby = getInput()
    
    ans = 0
    #Checking every value in every ticket
    for t in nearby:
        for val in t:
            inRange = False
            #Comparing the value against the ranges in the locations map
            for k in locations:
                if (locations[k][0] <= val and val <= locations[k][1]) or (locations[k][2] <= val and val <= locations[k][3]):
                    inRange = True
                    break
            if not inRange:
                ans += val
    return ans


def solution2():
    locations, ticket, nearby = getInput()
    
    ticketIndex = 0
    while ticketIndex < len(nearby):
        testing and print("Checking ticket", nearby[ticketIndex])
        #Checking every value in every ticket
        for val in nearby[ticketIndex]:
            inRange = False
            #Comparing the value against the ranges in the locations map
            for k in locations:
                if (locations[k][0] <= val and val <= locations[k][1]) or (locations[k][2] <= val and val <= locations[k][3]):
                    inRange = True
                    testing and print("\t\tIn Range")
                    break
            if not inRange:
                testing and print("\t", val, "not in ranges", locations[k][0], "-", locations[k][1], "or", locations[k][2], "-", locations[k][3])
                print("Popping index", ticketIndex)
                nearby.pop(ticketIndex)
            else:
                ticketIndex += 1
               
    testing and print("\nRemaining:")
    for n in nearby:
        testing and print(n)
        
    locIndex = {}
    while len(locIndex.keys()) < len(ticket):
        for loc in locations.keys():
            validIndex = [i for i in range(0, len(nearby[0]))]
            testing and print(loc, "possible valid indeces:", validIndex)
            for n in nearby:
                for i in range(0, len(n)):
                    #Removing any indeces we know for certain aren't available
                    if i in locIndex.keys() and i in validIndex:
                        testing and print("\t\t", i, "already taken by", locIndex[i])
                        validIndex.remove(i)
                        testing and print("\t\tAfter remove")
                    #Removing any indeces whose values don't match with the known ranges
                    elif n[i] not in range(locations[loc][0], locations[loc][1]+1) and n[i] not in range(locations[loc][2], locations[loc][3]+1):
                        testing and print("\t\t", i, "not in ranges", locations[loc])
                        if i in validIndex:
                            validIndex.remove(i)
                        testing and print("\t\tAfter remove")
                    
            testing and print("\tRemaining indeces:", validIndex)
            if len(validIndex) == 1:
                locIndex[validIndex[0]] = loc
                testing and print(loc, "at index", validIndex[0])
                
        testing and print("Location indeces:", locIndex, '\n====================================================')
        
    ans = 1
    for i in locIndex.keys():
        if locIndex[i].split(' ')[0] == 'departure':
            ans *= ticket[i]
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())