#https://adventofcode.com/2021/day/12
#https://adventofcode.com/2021/day/12#part2

data = [["pg","CH"],["pg","yd"],["yd","start"],["fe","hv"],["bi","CH"],["CH","yd"],["end","bi"],["fe","RY"],["ng","CH"],["fe","CH"],["ng","pg"],["hv","FL"],["FL","fe"],["hv","pg"],["bi","hv"],["CH","end"],["hv","ng"],["yd","ng"],["pg","fe"],["start","ng"],["end","FL"],["fe","bi"],["FL","ks"],["pg","start"]]
#data = [["start","A"],["start","b"],["A","c"],["A","b"],["b","d"],["A","end"],["b","end"]]

# Creating a dictionary to hold each edge in the data array for easier access
edgeDict = {}
for e in data:
    if e[0] in edgeDict.keys():
        edgeDict[e[0]].append(e[1])
    else:
        edgeDict[e[0]] = [e[1]]
        
    if e[1] in edgeDict.keys():
        edgeDict[e[1]].append(e[0])
    else:
        edgeDict[e[1]] = [e[0]]


def solution1(currVert_, path_=[]):
    # Creating a copy of the path and adding the current vertex tot he end
    newPath = path_.copy()
    newPath.append(currVert_)

    # The end condition is if this path hits the "end" vertex
    if currVert_ == "end":
        #print(newPath)
        return 1

    # Iterating through the current vert's neighbors and finding the number of solutions
    solutions = 0
    for nbr in edgeDict[currVert_]:
        # Checking for upper-case IDs since we can visit them multiple times
        if (not nbr.isupper() and nbr not in newPath) or nbr.isupper():
            solutions += solution1(nbr, newPath)

    return solutions


def solution2(currVert_, path_=[], copyUsed_=False):
    # Creating a copy of the path and adding the current vertex tot he end
    newPath = path_.copy()
    newPath.append(currVert_)

    # The end condition is if this path hits the "end" vertex
    if currVert_ == "end":
        #print(newPath)
        return 1

    # Iterating through the current vert's neighbors and finding the number of solutions
    solutions = 0
    for nbr in edgeDict[currVert_]:
        # Checking for upper-case IDs since we can visit them multiple times
        # Upper-case IDs can be visited any number of times
        if nbr.isupper():
            solutions += solution2(nbr, newPath, copyUsed_)
        # Only one lower-case ID can be visited twice, otherwise it can only be visited once
        elif nbr != "start":
            # If this lower-case ID hasn't been visited before, we can go there
            if nbr not in newPath:
                solutions += solution2(nbr, newPath, copyUsed_)
            # If this ID has already been seen and we haven't copied a lower-case ID yet, we use the copy for subsequent paths
            elif not copyUsed_:
                solutions += solution2(nbr, newPath, True)

    return solutions

    
print("Year 2021, Day 12 solution part 1:", solution1("start"))
print("Year 2021, Day 12 solution part 2:", solution2("start"))