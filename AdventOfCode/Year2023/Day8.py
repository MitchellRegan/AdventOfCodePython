#https://adventofcode.com/2023/day/8
#https://adventofcode.com/2023/day/8#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d8_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d8_real.txt")


def getInput():
    input = ''
    map = {}

    with open(inFile, 'r') as f:
        lineNum = 0

        for line in f:
            line = line.replace('\n', '')
            if lineNum == 0:
                input = line
            elif lineNum > 1:
                line = line.replace('(', '').replace(')', '').split(" = ")
                key = line[0]
                line = line[1].split(', ')
                map[key] = line
            lineNum += 1

    return input, map


def solution1():
    input, map = getInput()

    node = 'AAA'
    steps = 0
    while True:
        for c in range(0, len(input)):
            if input[c] == 'R':
                node = map[node][1]
            else:
                node = map[node][0]

            if node == 'ZZZ':
                return c+1 + steps

        steps += len(input)


    return


def getCycle(input, map, start):
    '''Follows the path from the starting point given to it's end 
    point and returns the number of steps it takes before it starts looping.'''
    steps = 0
    curNode = start
    endNodes = {}
    while True:
        instructionIndex = steps % len(input)

        #if a node ending in Z is found, it's an end node
        if curNode[-1] == 'Z':
            #Tracking the index in the instruction string when a valid end node is first seen
            if curNode not in endNodes.keys():
                endNodes[curNode] = [(instructionIndex, steps)]
            #If an end node has already been seen
            else:
                #If we see the same node at the same instruction index, we know a cycle has happened
                for e in endNodes[curNode]:
                    if e[0] == instructionIndex:
                        endNodes[curNode].append((instructionIndex, steps))
                        #return [y for x,y in endNodes[curNode]]
                        return endNodes[curNode][0][1]

                #Otherwise, we track the index that it appeared again
                endNodes[curNode].append((instructionIndex, steps))
                
        #If we haven't found a cycle yet, we iterate on this one's step pattern
        if input[steps % len(input)] == 'L':
            curNode = map[curNode][0]
        else:
            curNode = map[curNode][1]
        steps += 1


def primeFactorization(val_:int)->list:
    '''Helper function to find the prime factorization of a given number.
    i.e. the list of all prime numbers used to multiply together to get the given number.'''
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,\
                73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,\
                179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,\
                283,293,307,311,313,317]
    
    result = val_
    factors = []
    while result > 1:
        for p in primes:
            if result % p == 0:
                factors.append(p)
                result = result / p
    return factors


def solution2():
    input, map = getInput()
    
    factors = []
    for n in map.keys():
        if n[-1] == 'A':
            #Getting the number of steps before the path for this starting node begins to loop
            cycle = getCycle(input, map, n)
            #Getting the list of all prime factors for the cycle
            factors.append(primeFactorization(cycle))
            #print("\tNode", n, "cycle:", cycle, "   prime factorization:", primeFactorization(cycle))
    
    #Dictionary to keep track of which primes appear (keys) and
    #the most number of times that prime appears in a single factor
    factorCount = {}
    for pf in factors:
        curCount = {}
        for prime in pf:
            if prime in curCount.keys():
                curCount[prime] += 1
            else:
                curCount[prime] = 1

        for prime in curCount.keys():
            if prime not in factorCount.keys():
                factorCount[prime] = curCount[prime]
            elif factorCount[prime] < curCount[prime]:
                factorCount[prime] = curCount[prime]

    #The least common multiple (LCM) of all of the cycles is the product
    #of the most occurrances of each prime
    product = 1
    for p in factorCount.keys():
        product *= p**factorCount[p]
    return product


print("Year 2023, Day 8 solution part 1:", solution1())
print("Year 2023, Day 8 solution part 2:", solution2())