#https://adventofcode.com/2023/day/25
#https://adventofcode.com/2023/day/25#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 1
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d25_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d25_real.txt")


def getInput():
    wires = {}

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            wire1 = line.split(': ')[0]
            otherWires = line.split(": ")[1].split(' ')
            if wire1 not in wires.keys():
                wires[wire1] = []

            for w in otherWires:
                wires[wire1].append(w)
                if w not in wires.keys():
                    wires[w] = []
                wires[w].append(wire1)

    return wires


def bfsDist(graph:dict, edge:tuple)->int:
    '''Using Breadth-First Search to find the minimum distance between components if the wire connecting them is severed.
    
    Parameters
    ----------
        graph: Dictionary where keys are strings for component names, and values are the list of connected components.
        edge: Tuple of (component 1, component 2) denoting a wire connection between components.
        
    Returns
    ----------
        Int for the minimum distance between the components.
    '''
    
    start = edge[0]
    end = edge[1]
    
    q = []
    dist = {start:0}
    for x in graph[start]:
        if x != end:
            q.append(x)
            dist[x] = 1

    while len(q) > 0:
        head = q.pop(0)
        if head == end:
            return dist[head]
        for e in graph[head]:
            if e not in dist.keys():
                q.append(e)
                dist[e] = dist[head] + 1
                
    return -1 #Default value if error found


def groupSizes(graph:dict)->list:
    '''Removes the three wire connections from the graph and finds the sizes of each group of remaining connections.
    
    Parameters
    ----------
        graph: Dictionary where keys are strings for component names, and values are the list of connected components. This is a copy of the original, but with wires already severed.
        
    Returns
    ----------
        2D list of strings where each sub-list contains all components in a connected group.
    '''
    
    components = [x for x in graph.keys()]
    componentGroups = []
    while len(components) > 0:
        #If components still exist in the components list, they weren't found in previous groups of connected components
        newGroup = [components.pop(0)]
        q = graph[newGroup[0]]
        # Performing a bfs search 
        while len(q) > 0:
            head = q.pop(0)
            #If we've seen this component before, ignore it and move on
            if head in newGroup:
                continue
            #If the component hasn't been seen yet, we remove it from the unseen component list, add it to this group's list, and add it's connections to the queue
            else:
                newGroup.append(head)
                components.remove(head)
                for conn in graph[head]:
                    if conn not in q and conn in components:
                        q.append(conn)
            
        componentGroups.append(newGroup)
        
    return componentGroups
                


def solution1():
    wires = getInput()
    
    #Get a list of each edge as (min(u,v), max(u,v)) where u and v are verts
    edges = {}

    #Creating the initial list of graph edges
    for u in wires.keys():
        for v in wires[u]:
            if (min(u,v), max(u,v)) not in edges.keys():
                e = (min(u,v), max(u,v))
                edges[e] = bfsDist(wires, e)

    #for e in edges.keys():
    #    print(e, edges[e])
    
    distances = [(e, edges[e]) for e in edges.keys()]
    distances.sort(key=lambda x: x[1], reverse=True)
    #for d in distances:
    #    print(d)
    
    topIndexes = 5
    bestSize = 0
    for i1 in range(0, topIndexes-2):
        for i2 in range(i1+1, topIndexes-1):
            for i3 in range(i2+1, topIndexes):
                #Creating a copy of the graph of connections and severing each of the 3 chosen wires
                newGraph = {}
                for k in wires.keys():
                    newGraph[k] = [x for x in wires[k]]
                    
                newGraph[distances[i1][0][0]].remove(distances[i1][0][1])
                newGraph[distances[i1][0][1]].remove(distances[i1][0][0])
                
                newGraph[distances[i2][0][0]].remove(distances[i2][0][1])
                newGraph[distances[i2][0][1]].remove(distances[i2][0][0])
                
                newGraph[distances[i3][0][0]].remove(distances[i3][0][1])
                newGraph[distances[i3][0][1]].remove(distances[i3][0][0])
                
                wireGroups = groupSizes(newGraph)
                
                #We need to find the largest product of group sizes as long as there's 2 separate groups
                if len(wireGroups) > 1:
                    groupSize = len(wireGroups[0]) * len(wireGroups[1])
                    if groupSize > bestSize:
                        bestSize = groupSize
                        
    return bestSize


def solution2():
    input = getInput()
    


    return


print("Year 2023, Day 25 solution part 1:", solution1())
print("Year 2023, Day 25 solution part 2:", solution2())