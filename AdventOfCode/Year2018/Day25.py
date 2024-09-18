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
            line = line.replace('\n', '').split(',')
            inpt.append([int(x) for x in line])
    return inpt
            

def solution1():
    inpt = getInput()
    #dists = {} #Dictionary where key = (min,max) indeces of constellations, value = int for the manhattan distance between them
    starConnections = {} #Dist where key = index of star, value = list of stars with manhattan dist of 3 or less
    for i in range(0, len(inpt)-1):
        for j in range(i+1, len(inpt)):
            xdiff = abs(inpt[i][0] - inpt[j][0])
            ydiff = abs(inpt[i][1] - inpt[j][1])
            zdiff = abs(inpt[i][2] - inpt[j][2])
            tdiff = abs(inpt[i][3] - inpt[j][3])
            manDist = xdiff + ydiff + zdiff + tdiff
            if manDist <= 3:
                if i not in starConnections.keys():
                    starConnections[i] = [j]
                else:
                    starConnections[i].append(j)
                if j not in starConnections.keys():
                    starConnections[j] = [i]
                else:
                    starConnections[j].append(i)

    constellations = []
    q = [x for x in range(len(inpt))]
    while len(q) > 0:
        head = q.pop(0)
        seen = {head:True}
        q2 = [head]
        #BFS out from the head node to all star connections
        while len(q2) > 0:
            s = q2.pop(0)
            if s not in starConnections.keys():
                continue
            for adj in starConnections[s]:
                if adj not in seen.keys():
                    seen[adj] = True
                    q2.append(adj)
                    q.remove(adj)
        #Repeat for each connected star until none remain
        #Remove all stars found in BFS from the que
        
        #Append the new constellation to the list of constellations
        constellations.append([x for x in seen.keys()])
        
    if testing:
        print("Constellation Groups:")
        for c in constellations:
            print("\t", c)
        
    return len(constellations)


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())