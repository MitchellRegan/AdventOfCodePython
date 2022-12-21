#https://adventofcode.com/2022/day/16
#https://adventofcode.com/2022/day/16#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d16_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d16_real.txt")


def getInput():
    #Dictionary to store the flow rate of each valve as an int
    valveFlows = {}
    #Dictionary to store the valves that each valve is connected to
    valveEdges = {}
    #Name of the first valve where we start at
    startValve = "AA"

    with open(inFile, 'r') as f:
        for line in f:
            line = line.split(' ')
            name = line[1]
            flow = int(line[4][5:-1])
            edges = line[9:]
            #Getting rid of the commas and newline chars at the end of each connected valve ID name
            for e in range(0, len(edges)):
                if edges[e][-1] is ',' or edges[e][-1] is '\n':
                    edges[e] = edges[e][:-1]

            valveFlows[name] = flow
            valveEdges[name] = edges

    valveDists = {}

    #Looping through every valve option available
    for v in valveEdges.keys():
        #If this valve has a flow of 0, we don't care about it
        if valveFlows[v] == 0 and v != startValve:
            continue

        #Otherwise we do a bfs search to get its distance to every other non-zero valve
        q = [v]
        found = {v:0}
        zeroValves = [v]
        while len(q) > 0:
            cur = q.pop(0)
            #Getting every valve connected to this one
            for edge in valveEdges[cur]:
                if edge not in q and edge not in found:
                    q.append(edge)
                    found[edge] = found[cur] + 1
                    if valveFlows[edge] == 0 and edge is not startValve:
                        zeroValves.append(edge)

        #Removing the distances to valves with zero flow
        for z in zeroValves:
            found.pop(z)

        # Adding 1 to each distance to compensate for the step for turning it on
        for a in found.keys():
            found[a] += 1
            if (min(v,a), max(v,a)) not in valveDists.keys():
                valveDists[(min(v,a), max(v,a))] = found[a]
                #print("Dist from", min(v,a), "to", max(v,a), "=", found[a])

    return [valveFlows, valveEdges, startValve, valveDists]


def solution1(visited=[], steps=30, pressure=0):
    '''DFS function to search all possible permutations
    - visited: List of visited valves, starting with the first
    - steps: The number of steps remaining
    '''
    #Get a list of every other non-zero valve that are not already in the visited valves list
    potential = []
    for i in valveDists.keys():
        #The edge also has to include the last valve in our visited list (i.e. where we're currently at)
        if i[0] == visited[-1] and i[1] not in visited:
            #Only adding it to the list of options if the distance is less than the number of steps remaining
            if valveDists[i] < steps:
                potential.append(i[1])
        elif i[1] == visited[-1] and i[0] not in visited:
            #Only adding it to the list of options if the distance is less than the number of steps remaining
            if valveDists[i] < steps:
                potential.append(i[0])

    #If none are available, calculate and return the total pressure
    if len(potential) == 0:
        #print("Path", visited, "has pressure", pressure, "With", steps, "steps remaining")
        return pressure

    #For any that remain, do a recursive call to get the most pressure it can relieve (store the largest one returned)
    maxPressure = 0
    for p in potential:
        newVisited = [x for x in visited]
        newVisited.append(p)
        newSteps = steps - valveDists[(min(p, visited[-1]), max(p, visited[-1]))]
        newPressure = pressure + (newSteps * valveFlows[p])
        val = solution1(newVisited, newSteps, newPressure)
        if val > maxPressure:
            maxPressure = val
    #return the largest pressure value found
    return maxPressure


def solution2():
    #The lists for person 1 and person 2 containing the valves that each has gone to
    visited = [["AA"], ["AA"]]
    #The starting number of steps for person 1 and person 2
    steps=[26, 26]
    #The total amount of pressure that has been released
    pressure = 0

    while steps[0] > 0 and steps[1] > 0:
        #Get a list of every other non-zero valve that are not already in the visited valves list
        potential1 = []
        potential2 = []
        
        for i in valveDists.keys():
            #Checking for person 1
            #The edge also has to include the last valve in our visited list (i.e. where we're currently at)
            if i[0] == visited[0][-1] and i[1] not in visited[0] and i[1] not in visited[1]:
                #Only adding it to the list of options if the distance is less than the number of steps remaining
                if valveDists[i] < steps[0]:
                    potential1.append(i[1])
            elif i[1] == visited[0][-1] and i[0] not in visited[0] and i[0] not in visited[1]:
                #Only adding it to the list of options if the distance is less than the number of steps remaining
                if valveDists[i] < steps[0]:
                    potential1.append(i[0])
    
            #Checking for person 2
            #The edge also has to include the last valve in our visited list (i.e. where we're currently at)
            if i[0] == visited[1][-1] and i[1] not in visited[0] and i[1] not in visited[1]:
                #Only adding it to the list of options if the distance is less than the number of steps remaining
                if valveDists[i] < steps[1]:
                    potential2.append(i[1])
            elif i[1] == visited[1][-1] and i[0] not in visited[0] and i[0] not in visited[1]:
                #Only adding it to the list of options if the distance is less than the number of steps remaining
                if valveDists[i] < steps[1]:
                    potential2.append(i[0])
    
        #If none are available for either person, we have a final answer
        if len(potential1) == 0:
            steps[0] = 0
        if len(potential2) == 0:
            steps[1] = 0
        if steps[0] == 0 and steps[1] == 0:
            break
    
        #For any options that remain, we look for the most optimal valve to go to
        #If person 1 has equal or more steps than person 2, they go first
        if steps[0] >= steps[1]:
            bestValve = None
            maxPressure = 0
            
            for p in potential1:
                #Getting the pressure that would be released (score) if p1 opened the valve
                p1dist = valveDists[ ( min(visited[0][-1], p), max(visited[0][-1], p) ) ]
                p1score = (steps[0] - p1dist) * valveFlows[p]
                #Getting the pressure that would be released (score) if p2 opened the valve
                p2dist = valveDists[(min(visited[1][-1], p), max(visited[1][-1], p))]
                p2score = (steps[1] - p2dist) * valveFlows[p]
                
                if p1score >= maxPressure and p1score >= p2score:
                    maxPressure = p1score
                    bestValve = p
                    
            if bestValve is None:
                steps[0] = 0
            else:
                #Once we've found the best valve to go to, we travel there
                visited[0].append(bestValve)
                pressure += maxPressure
                steps[0] -= valveDists[ ( min(visited[0][-1], visited[0][-2]), max(visited[0][-1], visited[0][-2]) ) ]
                print("Person 1 going from valve", visited[0][-2], "to valve", visited[0][-1], "With a score of", maxPressure)
        #If person 2 has more steps, they go first
        else:
            bestValve = None
            maxPressure = 0
            
            #Finding the valve with the best score
            for p in potential2:
                #Getting the pressure that would be released (score) if p1 opened the valve
                p1dist = valveDists[ ( min(visited[0][-1], p), max(visited[0][-1], p) ) ]
                p1score = (steps[0] - p1dist) * valveFlows[p]
                #Getting the pressure that would be released (score) if p2 opened the valve
                p2dist = valveDists[(min(visited[1][-1], p), max(visited[1][-1], p))]
                p2score = (steps[1] - p2dist) * valveFlows[p]
                
                if p2score >= maxPressure and p2score >= p1score:
                    maxPressure = p2score
                    bestValve = p
                    
            if bestValve is None:
                steps[1] = 0
            else:
                #Once we've found the best valve to go to, we travel there
                visited[1].append(bestValve)
                pressure += maxPressure
                steps[1] -= valveDists[(min(visited[1][-1], visited[1][-2]), max(visited[1][-1], visited[1][-2]))]
                print("Person 2 going from valve", visited[1][-2], "to valve", visited[1][-1], "With a score of", maxPressure)

    #return the largest pressure value found
    print("Person 1 path:", visited[0])
    print("Person 2 path:", visited[1])
    return pressure


#Getting the starting dictionaries for the flow for each valve, the connections for each valves, the distances from/to each non-zero valve, and which valve to start at
valveFlows, valveEdges, startValve, valveDists = getInput()
#print("Year 2022, Day 16 solution part 1:", solution1([startValve], 30))
print("Year 2022, Day 16 solution part 2:", solution2())
#1213 too low
#1897 too low