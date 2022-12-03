#https://adventofcode.com/2019/day/2
#https://adventofcode.com/2019/day/2#part2

# Real data
data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,1,6,23,27,2,27,9,31,2,6,31,35,1,5,35,39,1,10,39,43,1,43,13,47,1,47,9,51,1,51,9,55,1,55,9,59,2,9,59,63,2,9,63,67,1,5,67,71,2,13,71,75,1,6,75,79,1,10,79,83,2,6,83,87,1,87,5,91,1,91,9,95,1,95,10,99,2,9,99,103,1,5,103,107,1,5,107,111,2,111,10,115,1,6,115,119,2,10,119,123,1,6,123,127,1,127,5,131,2,9,131,135,1,5,135,139,1,139,10,143,1,143,2,147,1,147,5,0,99,2,0,14,0]
# Test data
#data = [1,9,10,3,2,3,11,0,99,30,40,50]


def solution1():
    # Creating a deep copy of the data since we need to modify it
    dataCopy = [x for x in data]

    # Making the index changes designated in the question
    dataCopy[1] = 12
    dataCopy[2] = 2

    # Looping through each opcode in our data
    opIndex = 0
    while opIndex < len(dataCopy):
        # doing the specified opcode commands at the current index
        if dataCopy[opIndex] == 1: #add
            #print("Index %d: Add %d + %d and store at index %d" %(opIndex, dataCopy[dataCopy[opIndex + 1]], dataCopy[dataCopy[opIndex + 2]], dataCopy[dataCopy[opIndex + 3]]))
            changedIndex = dataCopy[opIndex + 3]
            firstValIndex = dataCopy[opIndex + 1]
            secondValIndex = dataCopy[opIndex + 2]
            dataCopy[changedIndex] = dataCopy[firstValIndex] + dataCopy[secondValIndex]
            opIndex += 4
        elif dataCopy[opIndex] == 2: #multiply
            #print("Index %d: Multiply %d x %d and store at index %d" %(opIndex, dataCopy[dataCopy[opIndex + 1]], dataCopy[dataCopy[opIndex + 2]], dataCopy[dataCopy[opIndex + 3]]))
            changedIndex = dataCopy[opIndex + 3]
            firstValIndex = dataCopy[opIndex + 1]
            secondValIndex = dataCopy[opIndex + 2]
            dataCopy[changedIndex] = dataCopy[firstValIndex] * dataCopy[secondValIndex]
            opIndex += 4
        elif dataCopy[opIndex] == 99: #terminate
            #print("Index %d: Terminate" %(opIndex))
            break
        else:
            print("Invalid opcode %d at index %d" %(dataCopy[opIndex], opIndex))
            break

    # returning the value stored at index 0
    return dataCopy[0]


def solution2():
    #Looping through all available values for the 'noun'
    for n in range(0,100):
        # Looping through all available values for the 'verb'
        for v in range(0,100):
            # Initializing the memory array to the correct starting position with the given noun and verb
            dataCopy = [x for x in data]
            dataCopy[1] = n
            dataCopy[2] = v

            # Running through this memory iteration
            ip = 0
            while ip < len(dataCopy):
                # doing the specified opcode commands at the current index pointer
                if dataCopy[ip] == 1: #add
                    changedIndex = dataCopy[ip + 3]
                    firstValIndex = dataCopy[ip + 1]
                    secondValIndex = dataCopy[ip + 2]
                    dataCopy[changedIndex] = dataCopy[firstValIndex] + dataCopy[secondValIndex]
                    ip += 4
                elif dataCopy[ip] == 2: #multiply
                    changedIndex = dataCopy[ip + 3]
                    firstValIndex = dataCopy[ip + 1]
                    secondValIndex = dataCopy[ip + 2]
                    dataCopy[changedIndex] = dataCopy[firstValIndex] * dataCopy[secondValIndex]
                    ip += 4
                elif dataCopy[ip] == 99: #terminate
                    break
                else: #error
                    break

            # If the value at index 0 is 19690720, we found the correct noun/verb combo
            if dataCopy[0] == 19690720:
                return (100 * n) + v

    # If for some reason we make it here, we return an error value
    return -1

    
print("Year 2019, Day 2 solution part 1:", solution1())
print("Year 2019, Day 2 solution part 2:", solution2())