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
            wire1 = line.split(':')[0]
            otherWires = line.split(": ")[1].split(' ')
            if wire1 not in wires.keys():
                wires[wire1] = []

            for w in otherWires:
                wires[wire1].append(w)
                if w not in wires.keys():
                    wires[w] = []
                wires[w].append(wire1)

    return wires


def bfsDist(graph:dict, edge:list)->int:
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


def solution1():
    wires = getInput()
    
    #Get a list of each edge as (min(u,v), max(u,v)) where u and v are verts
    edges = {}

    #Creating the initial list of graph edges
    for u in wires.keys():
        for v in wires[u]:
            if (min(u,v), max(u,v)) not in edges.keys():
                e = (min(u,v), max(u,v))
                edges[e] = 0

    removed = 0
    while removed < 3:
        #Tracking which edges will be removed and their max distance weight
        removedEdges = []
        maxDist = 0

        #Perform a bfs search from u to v without being able to take the direct route
        #The weight of edge (u,v) is equal to the bfs distance
        for e in edges:
            edges[e] = bfsDist(wires, e)

            if edges[e] > maxDist:
                maxDist = edges[e]
                removedEdges = [e]
            elif edges[e] == maxDist:
                removedEdges.append(e)

        #Removing the top 3 edges with the highest distance weight
        for e in removedEdges:
            edges.pop(e)
            wires[e[0]].remove(e[1])
            wires[e[1]].remove(e[0])
            removed += 1
            print("Removing edge", e)
            if removed == 3:
                print("TOO MANY EDGES. REMAINING EDGES:", removedEdges)
                break

            
    for point in wires.keys():
        #Doing a bfs search from this point to all others in the connected group
        seen = {point:True}
        q = [point]
        while len(q) > 0:
            head = q.pop(0)
            for c in wires[head]:
                if c not in seen.keys():
                    seen[c] = True
                    q.append(c)
        print("Total points:", len(wires.keys()))
        print("Points in group:", len(seen.keys()))
        print("Points in other group:", len(wires.keys()) - len(seen.keys()))
        return (len(wires.keys()) - len(seen.keys())) * len(seen.keys())


def solution2():
    input = getInput()
    


    return


print("Year 2023, Day 25 solution part 1:", solution1())
print("Year 2023, Day 25 solution part 2:", solution2())