def bfs_2Dgrid_getDist(grid, start, end, openTiles=[], blockedTiles=[]):
    '''Breadth-First Search algorithm for a 2D list to find the distance between two given nodes.
    - grid: 2D list of objects to iterate through.
    - start: List or tuple containing the row,col values of where to start the search.
    - end: List or tuple containing the row,col values of where to find.
    - openTiles: List of values that this algorithm can traverse through (i.e. are "open").
    - blockedTiles: List of values that this algorithm is prevented from traversing through.
    - returns: Int value for the distance from start to end. Returns -1 if there is no path.
    '''

    #print("BFS. Start:", start, "  End:", end)
    #Que of tiles that have been located but not searched yet
    q = [start]
    #Dictionary to store each found tile (key), its previous tile in the path, and its distance (value as List of 2)
    found = {start:[None,0]}

    while len(q) > 0:
        cur = q.pop(0)
        curDist = found[cur][1]
        r = cur[0]
        c = cur[1]

        #If we've found the endpoint, we return the distance
        #print(" - Current:", cur, "=", grid[r][c])
        if grid[r][c] is grid[end[0]][end[1]]:
            return found[cur][1]

        #If this tile isn't the endpoint and isn't in one of the open tiles, we skip it
        if grid[r][c] is not grid[start[0]][start[1]] and len(openTiles) > 0 and grid[r][c] not in openTiles:
            #print(" - - - Non-open tile", grid[r][c])
            continue

        #Otherwise we check the orthagonal tiles adjacent to this current tile
        #Looking up
        if r-1 > -1:
            if (r-1,c) not in q and (r-1,c) not in found.keys():
                if grid[r-1][c] not in blockedTiles:
                    q.append((r-1,c))
                    found[(r-1,c)] = [cur, curDist+1]
        #Looking down
        if r+1 < len(grid):
            if (r+1,c) not in q and (r+1,c) not in found.keys():
                if grid[r+1][c] not in blockedTiles:
                    q.append((r+1,c))
                    found[(r+1,c)] = [cur, curDist+1]
        #Looking left
        if c-1 > -1:
            if (r,c-1) not in q and (r,c-1) not in found.keys():
                if grid[r][c-1] not in blockedTiles:
                    q.append((r,c-1))
                    found[(r,c-1)] = [cur, curDist+1]
        #Looking right
        if c+1 < len(grid[0]):
            if (r,c+1) not in q and (r,c+1) not in found.keys():
                if grid[r][c+1] not in blockedTiles:
                    q.append((r,c+1))
                    found[(r,c+1)] = [cur, curDist+1]
        
    #If we make it through the loop without returning, there is no valid path
    return -1


def dfs_graph_shortestPathDist(graph, listOfNodes, start, currentPath=[]):
    '''Depth-First Search recursive algorithm to find the distance of the shortest path to traverse every node in a graph (a mathematical graph theory graph).
    - graph: Dictionary where the keys are ordered pairs of (node, node) and the value is the length of thier connecting edge.
    - listOfNodes: List containing each individual node in the graph.
    - start: The node where the path must start from.
    - returns: List of the nodes in the order that results in the shortest path of traversal. Returns 'infinity' if no traversal path exists.
    '''
    #print("Current Path:", currentPath)
    #If this is the first call in the stack, we have to check if the graph is even traversable
    if currentPath is None or len(currentPath) == 0:
        # Checking to make sure each node has at least one edge connection
        for node in listOfNodes:
            valid = False
            for edge in graph.keys():
                #If an edge connection is found, we can move to the next node
                #print("Checking edge", edge)
                if node in edge:
                    valid = True
                    continue

            #If no edge connection is found, there is no path to this node, so the graph can't be fully traversed
            if not valid:
                #print("Graph cannot be traversed. Node", node, "has no connecting edge.")
                return float('inf')

        #If it is traversable, we add the start node to the current path and remove it from the available list of nodes
        currentPath = [start]
        listOfNodes.remove(start)
        #print(" - Starting Current Path:", currentPath)
    
    #If this call has no more nodes to check, we return the distance of the path taken
    if len(listOfNodes) == 0:
        dist = 0
        for i in range(0, len(currentPath)-1):
            edge = (min(currentPath[i], currentPath[i+1]), max(currentPath[i], currentPath[i+1]))
            dist += graph[edge]
        #print("Found Path", currentPath, "   Distance:", dist)
        return dist

    #print(" - - Current Path:", currentPath)
    #Getting all edges connected to the most recent node in the path
    connectedNodes = []
    for k in graph.keys():
        if currentPath[-1] in k:
            other = k[0]
            if other is currentPath[-1]:
                other = k[1]
            #Only adding the connected node if it hasn't already appeared in the current path before
            if other not in currentPath:
                connectedNodes.append(other)

    #If there are no more connected edges while there are still nodes to traverse, the graph isn't traversable
    if len(connectedNodes) == 0:
        return float('inf')

    #Creating a new DFS call for each node path that can be taken
    minDist = float('inf')
    for n in connectedNodes:
        #print(" - - - - Going to node", n)
        newNodeList = [x for x in listOfNodes if x is not n]
        newPath = [x for x in currentPath]
        newPath.append(n)
        #Saving the shortest path found by any of the recursive calls
        #print(" - - - - - Recursive call with path:", newPath)
        minDist = min(minDist, dfs_graph_shortestPathDist(graph, newNodeList, start, newPath))

    return minDist


def dfs_graph_shortestHamiltonianDist(graph, listOfNodes, start, currentPath=[]):
    '''Depth-First Search recursive algorithm to find the distance of the shortest Hamiltonian path to traverse every node in a graph and return to the beginning.
    - graph: Dictionary where the keys are ordered pairs of (node, node) and the value is the length of thier connecting edge.
    - listOfNodes: List containing each individual node in the graph.
    - start: The node where the path must start from.
    - returns: List of the nodes in the order that results in the shortest path of traversal. Returns 'infinity' if no traversal path exists.
    '''
    #print("Current Path:", currentPath)
    #If this is the first call in the stack, we have to check if the graph is even traversable
    if currentPath is None or len(currentPath) == 0:
        # Checking to make sure each node has at least one edge connection
        for node in listOfNodes:
            valid = False
            for edge in graph.keys():
                #If an edge connection is found, we can move to the next node
                #print("Checking edge", edge)
                if node in edge:
                    valid = True
                    continue

            #If no edge connection is found, there is no path to this node, so the graph can't be fully traversed
            if not valid:
                #print("Graph cannot be traversed. Node", node, "has no connecting edge.")
                return float('inf')

        #If it is traversable, we add the start node to the current path and remove it from the available list of nodes
        currentPath = [start]
        listOfNodes.remove(start)
        #print(" - Starting Current Path:", currentPath)
    
    #If this call has no more nodes to check, we return the distance of the path taken
    if len(listOfNodes) == 0:
        #Adding the start value back to the graph as the last node
        currentPath.append(start)
        dist = 0
        for i in range(0, len(currentPath)-1):
            edge = (min(currentPath[i], currentPath[i+1]), max(currentPath[i], currentPath[i+1]))
            dist += graph[edge]
        #print("Found Path", currentPath, "   Distance:", dist)
        return dist

    #print(" - - Current Path:", currentPath)
    #Getting all edges connected to the most recent node in the path
    connectedNodes = []
    for k in graph.keys():
        if currentPath[-1] in k:
            other = k[0]
            if other is currentPath[-1]:
                other = k[1]
            #Only adding the connected node if it hasn't already appeared in the current path before
            if other not in currentPath:
                connectedNodes.append(other)

    #If there are no more connected edges while there are still nodes to traverse, the graph isn't traversable
    if len(connectedNodes) == 0:
        return float('inf')

    #Creating a new DFS call for each node path that can be taken
    minDist = float('inf')
    for n in connectedNodes:
        #print(" - - - - Going to node", n)
        newNodeList = [x for x in listOfNodes if x is not n]
        newPath = [x for x in currentPath]
        newPath.append(n)
        #Saving the shortest path found by any of the recursive calls
        #print(" - - - - - Recursive call with path:", newPath)
        minDist = min(minDist, dfs_graph_shortestHamiltonianDist(graph, newNodeList, start, newPath))

    return minDist