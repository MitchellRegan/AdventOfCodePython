#https://adventofcode.com/2016/day/24
#https://adventofcode.com/2016/day/24#part2

from HelperFunctions import pathfinding as pf
from HelperFunctions import inputReaders as ir
import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d24_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d24_real.txt")


def solution1():
    #The 2D grid for our maze input
    grid = ir.to2DList(inFile)
    #Dict to hold all graph connections between points and their distances. Key is (node, node) in numerical order, value is int for distance
    graph = {}
    #List to store all node values in the graph
    graphNodes = []

    #Dict to store the grid positions of each node in the grid
    allNodePos = {}

    #Finding the row,col positions of every node (number) in the grid
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            if grid[r][c] is not '#' and grid[r][c] is not '.':
                allNodePos[grid[r][c]] = (r,c)
                graphNodes.append(grid[r][c])

    #Doing a bfs from each node to every other node to find uninterrupted distances
    for node in allNodePos.keys():
        for other in allNodePos.keys():
            #Making sure not to bfs from one node to itself
            if node is not other:
                #Making sure the node path isn't already stored
                if (min(node,other), max(node,other)) not in graph.keys():
                    start = allNodePos[node]
                    end = allNodePos[other]
                    dist = pf.bfs_2Dgrid_getDist(grid, start, end, blockedTiles=['#'])
                    #If the path isn't blocked, we store the graph connection between the two nodes
                    if dist > 0:
                        graph[(min(node, other), max(node,other))] = dist


    #for k in graph.keys():
    #    print(k, ":", graph[k])

    return pf.dfs_graph_shortestPathDist(graph, graphNodes, '0')


def solution2():
    #The 2D grid for our maze input
    grid = ir.to2DList(inFile)
    #Dict to hold all graph connections between points and their distances. Key is (node, node) in numerical order, value is int for distance
    graph = {}
    #List to store all node values in the graph
    graphNodes = []

    #Dict to store the grid positions of each node in the grid
    allNodePos = {}

    #Finding the row,col positions of every node (number) in the grid
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            if grid[r][c] is not '#' and grid[r][c] is not '.':
                allNodePos[grid[r][c]] = (r,c)
                graphNodes.append(grid[r][c])

    #Doing a bfs from each node to every other node to find uninterrupted distances
    for node in allNodePos.keys():
        for other in allNodePos.keys():
            #Making sure not to bfs from one node to itself
            if node is not other:
                #Making sure the node path isn't already stored
                if (min(node,other), max(node,other)) not in graph.keys():
                    start = allNodePos[node]
                    end = allNodePos[other]
                    dist = pf.bfs_2Dgrid_getDist(grid, start, end, blockedTiles=['#'])
                    #If the path isn't blocked, we store the graph connection between the two nodes
                    if dist > 0:
                        graph[(min(node, other), max(node,other))] = dist


    return pf.dfs_graph_shortestHamiltonianDist(graph, graphNodes, '0')

print("Year 2016, Day 24 solution part 1:", solution1())
print("Year 2016, Day 24 solution part 2:", solution2())