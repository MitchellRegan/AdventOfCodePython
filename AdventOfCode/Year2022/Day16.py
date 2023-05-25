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
    #Dictionary to store the path list of nodes from each non-zero-value node to every other non-zero-value node
    valvePaths = {}
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
        path = {v:None}
        zeroValves = [v]
        while len(q) > 0:
            cur = q.pop(0)
            #Getting every valve connected to this one
            for edge in valveEdges[cur]:
                if edge not in q and edge not in found:
                    q.append(edge)
                    found[edge] = found[cur] + 1
                    #If this valve has no flow value, we mark it to be removed later (unless it's the starting valve)
                    if valveFlows[edge] == 0 and edge is not startValve:
                        zeroValves.append(edge)
                    #Keeping track of which node this came from
                    path[edge] = cur
                    #If this valve has a flow value, we store the path to it
                    if valveFlows[edge] > 0:
                        newPath = [edge]
                        while path[newPath[-1]] != None:
                            newPath.append(path[newPath[-1]])
                        newPath.reverse()
                        valvePaths[(min(v,edge), max(v,edge))] = newPath

        #Removing the distances to valves with zero flow
        for z in zeroValves:
            found.pop(z)

        # Adding 1 to each distance to compensate for the step for turning it on
        for a in found.keys():
            found[a] += 1
            if (min(v,a), max(v,a)) not in valveDists.keys():
                valveDists[(min(v,a), max(v,a))] = found[a]
                #print("Dist from", min(v,a), "to", max(v,a), "=", found[a])

    return [valveFlows, valveEdges, startValve, valveDists, valvePaths]


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


def pathPermutationsList(path, curPath=[], index=0):
    '''Recursive function to output a list of all possible permutations for visiting each valve along a given path.
    - path: The starting path of valves that's referenced when creating each permutation.
    - curPath: The path of valves being created for this recursion.
    - index: The index of the valve in the starting path to either include or exclude for further recursions.
    - returns: A list of every possible path between the first and last valves in the given starting path.
    '''
    #On the first loop we make sure the current path always includes the first valve of the starting path
    if index == 0:
        curPath.append(path[0])
        return permutationsList(path, curPath, index+1)
        
    #On the final loop we make sure the current path always includes the last valve of the starting path before returning
    if index == len(path)-1:
        lastPath = [x for x in curPath]
        lastPath.append(path[index])
        return [lastPath]
        
    #For each valve between the first and last valves, we run permutations with and without the valve at the current index
    else:
        path1 = [x for x in curPath]
        path1.append(path[index])
        path2 = [x for x in curPath]
        
        perm1 = permutationsList(path, path1, index+1)
        perm2 = permutationsList(path, path2, index+1)

        #Once we get all possible permutations, we combine the results into a single list to return
        combinedPaths = [x for x in perm1]
        for x in perm2:
            combinedPaths.append(x)
        return combinedPaths


def getPathHeuristicScore(path_, steps_):
    '''Function that finds the highest heuristics score (i.e. potential pressure release) possible from valves along a given path.
    - path_: The list of valves along a path.
    - steps_: The number of steps remaining, which limits how far can be traveled.
    - returns: Ordered list of (highest score, optimal list of valves)
    '''
    #Getting the list of all possible valve permutations along the given path
    pathPerm = pathPermutationsList(path_)
    #Vars to store the best path
    bestPath = []
    highestScore = 0

    #Iterating through each possible permutation along the given path
    for p in pathPerm:
        curSteps = steps_
        curScore = 0
        #Going from valve to valve along the path
        for i in range(0, len(p)-1):
            curSteps -= valveDists[(min(p[i], p[i+1]), max(p[i], p[i+1]))]
            if curSteps > 0:
                curScore += curSteps * valveFlows[p[i+1]]
            else:
                curScore = 0
                break
        #If this path nets a higher score than the previous best, we store it
        if curScore > highestScore:
            highestScore = curScore
            bestPath = p

    #Returning the best score and it's path
    return (highestScore, bestPath)


def solution2(visited = [["AA"], ["AA"]], steps=[26, 26], pressure = 0):
    '''DFS function to find the most optimal travel paths for both people to release the maximum amount of pressure.
    - visited: The lists for person 1 and person 2 containing the valves that each has gone to.
    - steps: The starting number of steps for person 1 and person 2.
    - pressure: The total amount of pressure that has been released.
    - returns: Int for the maximum amount of pressure released.
    '''

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
        #If person 1 and person 2 have the same number of steps, we figure out which goes first
        if steps[0] > 0 and steps[1] > 0:
            bestValve1 = None
            bestValve2 = None
            maxPressure = 0
            tieValvePairs = []
            
            #Comparing each option for person 1 against each option for person 2 to find which next pair of valves is the best
            for a in potential1:
                for b in potential2:
                    if a != b:
                        p1dist = valveDists[(min(visited[0][-1], a), max(visited[0][-1], a))]
                        p1score = (steps[0] - p1dist) * valveFlows[a]

                        p2dist = valveDists[(min(visited[1][-1], b), max(visited[1][-1], b))]
                        p2score = (steps[1] - p2dist) * valveFlows[b]

                        #If this pair of valves produces the most pressure release, we make a note of it
                        if (p1score + p2score) > maxPressure:
                            maxPressure = p1score + p2score
                            bestValve1 = a
                            bestValve2 = b
                            tieValvePairs = []
                        #If there's an equally optimal pair of valves, we add them to the tie valve pairs list to check later
                        elif (p1score + p2score) == maxPressure:
                            if not (steps[0] == steps[1] and a == bestValve2 and b == bestValve1):
                                tieValvePairs.append((a,b))

            #If there is only one pair of valves that offers the best result, we go with them
            if len(tieValvePairs) == 0:
                visited[0].append(bestValve1)
                visited[1].append(bestValve2)
                steps[0] -= valveDists[(min(visited[0][-1], visited[0][-2]), max(visited[0][-1], visited[0][-2]))]
                steps[1] -= valveDists[(min(visited[1][-1], visited[1][-2]), max(visited[1][-1], visited[1][-2]))]
                pressure += maxPressure
                print("\tPerson 1 turns on valve", bestValve1, "at time:", 26-steps[0])
                print("\tPerson 2 turns on valve", bestValve2, "at time:", 26-steps[1])
                print("===============================================================")
            #If there are multiple pairs of valves that offer the same best result, we need to check them all with DFS
            else:
                result = 0
                tieValvePairs.append((bestValve1, bestValve2))
                print("TIE IN MAX PRESSURE! Heuristic value:", maxPressure)
                print("Valve pairs:", tieValvePairs)

                for maxPair in tieValvePairs:
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Valve pair to DFS:", maxPair)
                    #Making shallow copies of the person 1 visited list and steps to pass to the dfs
                    newP1Visited = visited[0].copy()
                    newP1Visited.append(maxPair[0])
                    newP1Steps = steps[0] - valveDists[(min(newP1Visited[-1], newP1Visited[-2]), max(newP1Visited[-1], newP1Visited[-2]))]

                    #Making shallow copies of the person 2 visited list and steps to pass to the dfs
                    newP2Visited = visited[1].copy()
                    newP2Visited.append(maxPair[1])
                    newP2Steps = steps[1] - valveDists[(min(newP2Visited[-1], newP2Visited[-2]), max(newP2Visited[-1], newP2Visited[-2]))]

                    #Keeping track of the highest max pressure release from this DFS
                    print("\tP1 visited:", newP1Visited)
                    print("\tP1 steps:", newP1Steps)
                    print("\tP2 visited:", newP2Visited)
                    print("\tP2 steps:", newP2Steps)
                    dfsResult = solution2([newP1Visited, newP2Visited], [newP1Steps, newP2Steps], pressure + maxPressure)
                    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< DFS result:", dfsResult, "\n")
                    if dfsResult > result:
                        result = dfsResult

                #Returning the best result from the DFS because we can't continue this current function's cycle with a better result
                print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, DFS return")
                return result

        #If person 1 is the only one with steps remaining
        elif steps[0] > 0 and steps[1] == 0:

            bestValve = None
            maxPressure = 0
            
            for p in potential1:
                #Getting the pressure that would be released (score) if p1 opened the valve
                p1dist = valveDists[ ( min(visited[0][-1], p), max(visited[0][-1], p) ) ]
                p1score = (steps[0] - p1dist) * valveFlows[p]
                

                if p1score >= maxPressure:
                    maxPressure = p1score
                    bestValve = p
                    
            if bestValve is None:
                steps[0] = 0
            else:
                #Once we've found the best valve to go to, we travel there
                visited[0].append(bestValve)
                pressure += maxPressure
                steps[0] -= valveDists[(min(visited[0][-1], visited[0][-2]), max(visited[0][-1], visited[0][-2]))]
                print("\tPerson 1 turns on valve", bestValve1, "at time:", 26-steps[0])
        #If person 2 is the only one with steps remaining
        else:
            bestValve = None
            maxPressure = 0
            
            #Finding the valve with the best score
            for p in potential2:
                #Getting the pressure that would be released (score) if p2 opened the valve
                p2dist = valveDists[(min(visited[1][-1], p), max(visited[1][-1], p))]
                p2score = (steps[1] - p2dist) * valveFlows[p]
                
                if p2score >= maxPressure:
                    maxPressure = p2score
                    bestValve = p
                    
            if bestValve is None:
                steps[1] = 0
            else:
                #Once we've found the best valve to go to, we travel there
                visited[1].append(bestValve)
                pressure += maxPressure
                steps[1] -= valveDists[(min(visited[1][-1], visited[1][-2]), max(visited[1][-1], visited[1][-2]))]
                print("\tPerson 2 turns on valve", bestValve2, "at time:", 26-steps[1])

    print("Person 1 Path:", visited[0])
    print("Person 2 Path:", visited[1])
    return pressure


#Getting the starting dictionaries for the flow for each valve, the connections for each valves, the distances from/to each non-zero valve, and which valve to start at
valveFlows, valveEdges, startValve, valveDists, valvePaths = getInput()
#print("Year 2022, Day 16 solution part 1:", solution1([startValve], 30))
print("Year 2022, Day 16 solution part 2:", solution2())
#1213 too low
#1897 too low
#1921 too low
#1922 too low