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

    return [valveFlows, valveEdges]


def solution1():
    valveFlows, valveEdges = getInput()
    
    for v in valveFlows.keys():
        print("Valve", v, "connected to valves", valveEdges[v])
    return


def solution2():
    valveFlows, valveEdges = getInput()

    return


print("Year 2022, Day 16 solution part 1:", solution1())
print("Year 2022, Day 16 solution part 2:", solution2())