#https://adventofcode.com/2022/day/16
#https://adventofcode.com/2022/day/16#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = os.path.join(inFileDir, "InputTestFiles/d16_test.txt")
#inFile = os.path.join(inFileDir, "InputRealFiles/d16_real.txt")


def getInput():
    #Dictionary to store the flow rate of each valve as an int
    valveFlows = {}
    #Dictionary to store the valves that each valve is connected to
    valveEdges = {}
    #Name of the first valve where we start at
    startValve = None

    with open(inFile, 'r') as f:
        for line in f:
            line = line.split(' ')
            name = line[1]
            if startValve is None:
                startValve = name
            flow = int(line[4][5:-1])
            edges = line[9:]
            #Getting rid of the commas and newline chars at the end of each connected valve ID name
            for e in range(0, len(edges)):
                if edges[e][-1] is ',' or edges[e][-1] is '\n':
                    edges[e] = edges[e][:-1]

            valveFlows[name] = flow
            valveEdges[name] = edges

    return [valveFlows, valveEdges, startValve]


def makeDirectionalValveDict():
    valveDict = {}

    #Looping through every valve option available
    for v in valveEdges.keys():
        #If this valve has a flow of 0, we don't care about it
        if valveFlows[v] == 0:
            continue

        

    return valveDict


def bfs_findValves(startValve, steps, valveEdges, valveFlows):
    found = {startValve:0}
    q = [startValve]
    valvesToRemove = [startValve]

    while len(q) > 0:
        curValve = q.pop(0)
        for edge in valveEdges[curValve]:
            #If the current valve hasn't already been seen, we add it to the que and store it's distance
            if edge not in found.keys() and edge not in q:
                q.append(edge)
                found[edge] = found[curValve] + 1
                #If the valve has zero flow, we mark it to be removed later
                if valveFlows[edge] == 0:
                    valvesToRemove.append(edge)

    #Looping through and removing all valves that have a flow of zero, because they're worthless to us
    for r in valvesToRemove:
        found.pop(r)

    return found


def solution0():
    #Getting the starting dictionaries for the flow for each valve, the connections for each valves, and which valve to start at
    valveFlows, valveEdges, startValve = getInput()
    #The total amount of pressure that has been released
    currentPressure = 0
    #The number of steps remaining to perform actions
    remainingSteps = 30
    #List to track all of the valves that are currently open. The last index is the valve we're currently at
    openValves = [startValve]

    #Loop until there are no more non-zero-flow pipes in range
    while True:
        print("Min", remainingSteps, "currently at valve", openValves[-1])
        #Do a bfs search from the current valve (last in openValves) to all others that are within the step range and not in openValves
        #availableValves = bfs_findValves(openValves[-1], remainingSteps, valveEdges, valveFlows, openValves)
        availableValves = {startValve:0}
        q = [startValve]
        valvesToRemove = [startValve]

        while len(q) > 0:
            curValve = q.pop(0)
            for edge in valveEdges[curValve]:
                #If the current valve hasn't already been seen, we add it to the que and store it's distance
                if edge not in availableValves.keys() and edge not in q:
                    q.append(edge)
                    availableValves[edge] = availableValves[curValve] + 1
                    #If the valve has zero flow, we mark it to be removed later
                    if valveFlows[edge] == 0:
                        valvesToRemove.append(edge)
                    #If the valve has already been turned on, mark it to be removed
                    elif edge in openValves:
                        valvesToRemove.append(edge)

        #Looping through and removing all valves that have a flow of zero, because they're worthless to us
        for r in valvesToRemove:
            availableValves.pop(r)

        #If no valves remain, break loop
        if len(availableValves.keys()) == 0:
            break

        #weight each valve based on (remaining steps - steps to the valve - 1 to turn on) * valve flow
            #This gets the amount of pressure the valve will release over the entire duration
        bestFlow = 0
        bestValve = None
        for v in availableValves.keys():
            weight = valveFlows[v] * (remainingSteps - availableValves[v] - 1)
            print(" - Option", v, "- steps away:", availableValves[v], " flow:", valveFlows[v], " weight:", weight)
            if weight > bestFlow:
                bestFlow = weight
                bestValve = v
        
        #If there is no best valve to go to, we're out of options so we break the loop
        if bestValve is None:
            break

        print(" - - Traveling from to", bestValve, "with a flow of", valveFlows[bestValve], "and heuristic of", bestFlow)
        #Otherwise we travel to the valve with the highest weight
        openValves.append(bestValve)
        #Remove (steps to valve + 1) from remaining steps
        remainingSteps -= (availableValves[bestValve] + 1)
        #Add the weight of the valve to the current amount of pressure relieved
        currentPressure += weight

    return currentPressure


def solution1():
    #Create a DIRECTIONAL dictionary outside of the functions to store the distance each valve is from any other valve
        #Make a bfs function that does this
        #Automatically exclude valves with flow of zero
        #for each stored distance be sure to include the +1 for turning it on
    #Make a DFS function to search all possible permutations
        #Parameters:
            #list of visited valves, starting with the first
            #number of steps remaining
        #Get a list of every other non-zero valve
        #remove any that are already in the visited valves list
        #Remove any that are more steps away than are available
        #If none are available
            #calculate the total 
        #For any that remain, do a recursive call to get the most pressure it can relieve (store the largest one returned)
        #return the largest value
        return

def solution2():
    return

#Getting the starting dictionaries for the flow for each valve, the connections for each valves, and which valve to start at
valveFlows, valveEdges, startValve = getInput()
directionalValvDict = makeDirectionalValveDict()
print("Year 2022, Day 16 solution part 1:", solution1())
print("Year 2022, Day 16 solution part 2:", solution2())