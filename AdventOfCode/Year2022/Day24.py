#https://adventofcode.com/2022/day/24
#https://adventofcode.com/2022/day/24#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d24_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d24_real.txt")

#2D list where each row index represents the minute in time, and each value in the row is the position of every storm
stormStates = []
#Map boundaries so that we can know when storms need to loop
minMaxRow = [1,None]
minMaxCol = [1,None]
#Coordinates for the starting location and the exit to reach
start = [0,1]
exit = [None,None]


def getInput():
    #List to store initial positions of all of the storms found. Each value is [row, col, direction]
    storms = []

    with open(inFile, 'r') as f:
        row = 0
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]

            #Storing the maximum col index allowed
            if minMaxCol[1] == None:
                minMaxCol[1] = len(line) - 2

            #When a storm icon is found, we store it's position and direction it faces
            for col in range(0, len(line)):
                if line[col] in ['>', '<', '^', 'v']:
                    storms.append([row, col, line[col]])
            row += 1

        #Storing the maximum row index allowed
        minMaxRow[1] = row - 2

    #Keeping track of where we need to start pathfinding and where our exit is
    #start = (0, 1)
    exit[0] = minMaxRow[1]+1
    exit[1] = minMaxCol[1]
    #Storing the initial storm state
    stormStates.append(storms)
    return


def displayMapState(stormIndex_, userLoc_=None, potentialMoves_=None):
    #Creating the 2D list to display the map
    stateMap = []
    for x in range(0, minMaxRow[1]+2):
        if x == 0 or x == minMaxRow[1]+1:
            row = []
            for i in range(0, minMaxCol[1]+2):
                row.append('█')
            stateMap.append(row)
        else:
            row = ['█']
            for i in range(0,minMaxCol[1]):
                row.append(' ')
            row.append('█')
            stateMap.append(row)

    #Displaying the start and exit points
    stateMap[start[0]][start[1]] = ' '
    stateMap[exit[0]][exit[1]] = ' '

    #Displaying each storm location
    for s in stormStates[stormIndex_]:
        #If the position is empty, we display the storm arrow
        if stateMap[s[0]][s[1]] == ' ':
            stateMap[s[0]][s[1]] = s[2]
        #If a storm arrow is already in this position, we display a number for how many storms are here
        elif stateMap[s[0]][s[1]] in ['>', '<', '^', 'v']:
            stateMap[s[0]][s[1]] = '2'
        #If a number is already in this position, we increment it by 1
        else:
            val = int(stateMap[s[0]][s[1]]) + 1
            stateMap[s[0]][s[1]] = str(val)

    #If the user's location is given, we display them with an '@' symbol
    if userLoc_ != None:
        if stateMap[userLoc_[0]][userLoc_[1]] != ' ':
            print("Position", userLoc_, "was", stateMap[userLoc_[0]][userLoc_[1]])
            stateMap[userLoc_[0]][userLoc_[1]] = 'E'
        else:
            stateMap[userLoc_[0]][userLoc_[1]] = '@'

    #If potential moves are given, we display them
    if potentialMoves_ != None:
        for pm in potentialMoves_:
            if stateMap[pm[0]][pm[1]] != ' ' and stateMap[pm[0]][pm[1]] != '@':
                print("Position", (pm[0], pm[1]), "has ", stateMap[pm[0]][pm[1]])
                stateMap[pm[0]][pm[1]] = 'E'
            else:
                stateMap[pm[0]][pm[1]] = '+'

    #Showing the map visualization
    print("\tMap At Min", stormIndex_)
    for row in stateMap:
        print(''.join(row))
    print()


def generateNextStormState():
    print("Creating state", len(stormStates))
    #Creating a new state for the storm positions, starting from their most recent locations
    newState = []
    for x in stormStates[-1]:
        newState.append([x[0], x[1], x[2]])

    #Looping through each storm to update their position
    for s in newState:
        #s[0] = row, s[1] = col, s[2] = direction
        if s[2] == '^':
            s[0] -= 1
            if s[0] < minMaxRow[0]:
                s[0] = minMaxRow[1]
        elif s[2] == 'v':
            s[0] += 1
            if s[0] > minMaxRow[1]:
                s[0] = minMaxRow[0]
        elif s[2] == '<':
            s[1] -= 1
            if s[1] < minMaxCol[0]:
                s[1] = minMaxCol[1]
        elif s[2] == '>':
            s[1] += 1
            if s[1] > minMaxCol[1]:
                s[1] = minMaxCol[0]

    #Adding this new state to the global list of states
    stormStates.append(newState)


def solution1(showPath_=False, showDebug_=False):
    #Setting the global variables to their starting values
    getInput()
    
    #Creating the que of positions that have been located but not searched
    #Each element is (row, col, stateIndex/time)
    q = [(start[0], start[1], 0)]
    #Dictionary for each searched location/time and its previous location
    found = {(start[0], start[1], 0):None}

    #Pathfinding for as long as there are open locations to search
    while len(q) > 0:
        if showDebug_:
            print("==============================================================")
        cur = q.pop(0)
        #Making easier variables for the current location's row, column and time
        r = cur[0]
        c = cur[1]
        t = cur[2]

        #If we've found the exit to the maze, this location's time is the answer
        if r == exit[0] and c == exit[1]:
            #If we want to show the path taken to get to the exit, we trace back through each locations previous position
            if showPath_:
                path = [cur]
                while path[-1] in found.keys() and found[path[-1]] != None:
                    path.append(found[path[-1]])
                for i in range(len(path)-1, -1, -1):
                    print(path[i])
                    displayMapState(path[i][2], (path[i][0], path[i][1]))
            return t

        #If the next storm state in time doesn't exist yet, we make it
        if t+1 >= len(stormStates):
            generateNextStormState()
            if showDebug_:
                print("States:", t+1)

        #Making a list of all potential locations we can move to
        moves = [(r,c,t+1), (r+1,c,t+1), (r-1,c,t+1), (r,c+1,t+1), (r,c-1,t+1)]
        if showDebug_:
            print("\t\tPosition:", cur)
            print("Potential Moves 1:", moves)

        #Removing any of the movements that have already been located
        i = 0
        while i < len(moves):
            if moves[i] in q or moves[i] in found.keys():
                if showDebug_:
                    print("\tMove", moves[i], "already seen")
                moves.pop(i)
            else:
                i += 1

        if showDebug_:
            print("Potential Moves 2:", moves)

        #Removing any movements that go out of bounds
        #Checking up
        if (r-1,c,t+1) in moves:
            #Can't move to row -1
            if r-1 == -1:
                if showDebug_:
                    print("\tMove",(r-1,c,t+1), "removed. Off map up.")
                moves.remove((r-1,c,t+1))
            #Can't move to row 0 unless it's the starting point because walls are there
            elif r-1 == 0 and c != start[1]:
                if showDebug_:
                    print("\tMove",(r-1,c,t+1), "removed. Hitting wall up.")
                moves.remove((r-1,c,t+1))
        #Checking down
        if (r+1,c,t+1) in moves:
            #Can't move past the max row bound unless it's the exit because walls are there
            if r+1 > minMaxRow[1] and c != minMaxCol[1]:
                if showDebug_:
                    print("\tMove", (r+1,c,t+1), "removed. Hitting wall down.")
                moves.remove((r+1,c,t+1))
        #Checking left
        if (r,c-1,t+1) in moves:
            #Can't move to col 0 because walls are there
            if c-1 == 0 or r == 0:
                if showDebug_:
                    print("\tMove",(r,c-1,t+1), "removed. Hitting wall left.")
                moves.remove((r,c-1,t+1))
        #Checking right
        if (r,c+1,t+1):
            #Can't move past the max col bound because walls are there
            if c+1 > minMaxCol[1] or r == 0:
                if showDebug_:
                    print("\tMove",(r,c+1,t+1), "removed. Hitting wall right.")
                moves.remove((r,c+1,t+1))

        if showDebug_:
            print("Potential Moves 3:", moves)

        #Removing any movements that overlap with storms
        for s in range(0, len(stormStates[t+1])):
            stormNext = stormStates[t+1][s]
            stormCurr = stormStates[t][s]

            i = 0
            while i < len(moves):
                #Removing the movement if it results in a space occupied by storms
                if (moves[i][0], moves[i][1]) == (stormNext[0], stormNext[1]):
                    if showDebug_ and t+1 <= 18:
                        print("\tHit By Storm")
                        print("\tPlayer Pos:",(r,c), "\t Move Pos:", moves[i])
                        print("\tStorm Pos: ", stormCurr, " Storm Next:", stormNext)
                    moves.pop(i)
                #Removing the movement if it travels through an oncoming storm (Not needed?)
                #elif moves[i][0] == stormCurr[0] and moves[i][1] == stormCurr[1] and r == stormNext[0] and c == stormNext[1]:
                #    if showDebug_ and t+1 <= 18:
                #        print("\tOncoming Overlap")
                #        print("\tPlayer Pos:",(r,c), "\t Move Pos:", moves[i])
                #        print("\tStorm Pos: ", stormCurr, " Storm Next:", stormNext)
                #    moves.pop(i)
                else:
                    i += 1

        if showDebug_ and t+1 <= 18:
            print("Potential Moves 4:", moves)
            displayMapState(t, (r,c))
            displayMapState(t+1, None, moves)
            if t+1 == 18:
                return

        #Adding any remaining movements to the que to check
        for m in moves:
            q.append(m)
            found[m] = (r,c,t)

    #If we can't find the maze through pathfinding, we error out
    return -1


def solution2():
    #Setting the global variables to their starting values
    getInput()
    
    #Creating the que of positions that have been located but not searched
    #Each element is (row, col, stateIndex/time)
    q = [(start[0], start[1], 0)]
    #Dictionary for each searched location/time and its previous location
    found = {(start[0], start[1], 0):None}

    #Count for how many times we've gone from end-to-end. Once it reaches 4, we have our answer
    numTrips = 0

    #Pathfinding for as long as there are open locations to search
    while len(q) > 0:
        cur = q.pop(0)
        #Making easier variables for the current location's row, column and time
        r = cur[0]
        c = cur[1]
        t = cur[2]

        #If we've found the exit to the maze
        if r == exit[0] and c == exit[1]:
            #If we're on trip 0, we end trip 1 and have to double-back to the start
            if numTrips == 0:
                print("\tFirst time at exit. Beginning trip 2 at time", t)
                numTrips = 1
                q = []
                found = {(r,c,t):None}
            #If we're done with trip 2, we're at the end and have the answer
            elif numTrips == 2:
                return t
        #If we've found the start of the maze and doubling-back
        elif r == start[0] and c == start[1] and numTrips == 1:
            numTrips = 2
            q = []
            found = {(r,c,t):None}
            print("\tBack at the start again. Beginning trip 3 at time", t)

        #If the next storm state in time doesn't exist yet, we make it
        if t+1 >= len(stormStates):
            generateNextStormState()

        #Making a list of all potential locations we can move to
        #In order:  up,          down,        left,        right,   Standing Still
        moves = [(r-1,c,t+1), (r+1,c,t+1), (r,c-1,t+1), (r,c+1,t+1), (r,c,t+1)]

        #Removing any movements that go out of bounds
        #Checking up
        #Can't move to row -1
        if r-1 == -1:
            moves[0] = None
        #Can't move to row 0 unless it's the starting point because walls are there
        elif r-1 == 0 and c != start[1]:
            moves[0] = None

        #Checking down
        #Can't move below the last row
        if r+1 == minMaxRow[1]+2:
            moves[1] = None
        #Can't move past the max row bound unless it's the exit because walls are there
        elif r+1 == minMaxRow[1]+1 and c != minMaxCol[1]:
            moves[1] = None

        #Checking left
        #Can't move to col 0 because walls are there
        if c-1 == 0 or r == 0:
            moves[2] = None

        #Checking right
        #Can't move past the max col bound because walls are there
        if c+1 > minMaxCol[1] or r == 0:
            moves[3] = None
                
        #Removing any of the movements that have already been located
        for i in range(0, len(moves)):
            if moves[i] != None and (moves[i] in q or moves[i] in found.keys()):
                moves[i] = None

        #Removing any movements that overlap with storms
        for s in range(0, len(stormStates[t+1])):
            stormNext = stormStates[t+1][s]
            stormCurr = stormStates[t][s]

            for i in range(0, len(moves)):
                #Removing the movement if it results in a space occupied by storms
                if moves[i] != None and moves[i][0] == stormNext[0] and moves[i][1] == stormNext[1]:
                        moves[i] = None

        #Adding any remaining movements to the que to check
        for m in moves:
            if m != None:
                q.append(m)
                found[m] = (r,c,t)

    #If we can't find the maze through pathfinding, we error out
    return -1


#print("Year 2022, Day 24 solution part 1:", solution1())
print("Year 2022, Day 24 solution part 2:", solution2())
#660 too low