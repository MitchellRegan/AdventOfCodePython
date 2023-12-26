#https://adventofcode.com/2023/day/20
#https://adventofcode.com/2023/day/20#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 1:
    inFile = os.path.join(inFileDir, "InputTestFiles/d20_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d20_real.txt")


def getInput():
    broadcast = []
    flipFlops = {}
    conjuctions = {}

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n','').split(' -> ')
            key = line[0]
            vals = line[1]
            while ' ' in vals:
                vals = vals.replace(' ', '')
            vals = vals.split(',')

            if key == "broadcaster":
                broadcast = vals
            elif key[0] == "%":
                flipFlops[key[1:]] = vals
            elif key[0] == "&":
                remember = []
                for x in vals:
                    remember.append([x, False])
                conjuctions[key[1:]] = remember

    #Dictionary for quickly finding out which flip-flop is connected to each conjunction
    modConj = {}
    for con in conjuctions.keys():
        for mod in conjuctions[con]:
            if mod[0] in modConj.keys():
                modConj[mod[0]].append(con)
            else:
                modConj[mod[0]] = [con]

    return broadcast, flipFlops, conjuctions, modConj


def solution1():
    broadcast, flipFlops, conjuctions, modConj = getInput()
    #Initializing all modules to the Low pulse state
    modState = {}
    for mod in flipFlops.keys():
        modState[mod] = False

    #Counts for how many Low/High pulses were sent
    lowCount = 0
    highCount = 0

    if True:
        print("Broadcaster:", broadcast)
        print("Flip-flops:")
        for ff in flipFlops.keys():
            print('\t', ff, "==>", flipFlops[ff], "\tState:", modState[ff])
            if ff in modConj.keys():
                print("\t\tBelongs to conjunction", modConj[ff])
        print("Conjuctions:")
        for c in conjuctions.keys():
            print("\t", c, "==>", conjuctions[c])
        print("============================================\n")

    for i in range(0, 1):
        print("Loop", i, "-----------------------------------------")
        #Handling broadcast signals to each module in the order in which they were sent
        #Each element is (ID of sender, ID of receiver, Signal Strength)
        q = []
        for x in broadcast:
            q.append(("broadcaster", False, x))
        while len(q) > 0:
            sender, sig, mod = q.pop(0)
            print('\t', sender, "---", sig, "-->", mod)

            if sig:
                highCount += 1
            else:
                lowCount += 1

            if mod in flipFlops.keys():
                #If the signal is Low, the flip-flop changes state and sends a signal to all of it's next modules
                if not sig:
                    modState[mod] = not modState[mod]
                    for nextMod in flipFlops[mod]:
                        q.append((mod, modState[mod], nextMod))
                
                    #Storing the signal this module sent for its associated conjunction
                    if mod in modConj.keys():
                        conList = modConj[mod]
                        for c in conList:
                            for mc in range(0, len(conjuctions[c])):
                                if conjuctions[c][mc][0] == mod:
                                    conjuctions[c][mc][1] = modState[mod]
                                    break
            elif mod in conjuctions.keys():
                allHigh = True
                for m in conjuctions[mod]:
                    if not m[1]:
                        allHigh = False
                        break

                #Sending signals to all next modules
                for m in conjuctions[mod]:
                    q.append((mod, allHigh, m[0]))

    print("\nHigh Pulses:", highCount, "\nLow Pulses: ", lowCount)
    return lowCount * highCount


def solution2():


    return


print("Year 2023, Day 20 solution part 1:", solution1())
print("Year 2023, Day 20 solution part 2:", solution2())