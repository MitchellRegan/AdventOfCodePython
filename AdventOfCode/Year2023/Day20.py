#https://adventofcode.com/2023/day/20
#https://adventofcode.com/2023/day/20#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d20_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d20_real.txt")


def getInput():
    #Key is the module's name. Val is [type, pulse state, list of destinations]
    modules = {}

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n','').replace(' ', '').split('->')
            mod = line[0]
            destinations = line[1].split(',')

            if mod == "broadcaster":
                modules[mod] = ['bc', False, destinations]
            elif mod[0] == "%":
                modules[mod[1:]] = ['ff', False, destinations]
            elif mod[0] == "&":
                modules[mod[1:]] = ['cj', False, destinations]

    #Key is the conjunction module's name. Val is [list of module names that output to the conjunction module]
    conjunctionInputs = {}
    for outMod in modules.keys():
        for inMod in modules[outMod][2]:
            if inMod in modules.keys() and modules[inMod][0] == 'cj':
                if inMod not in conjunctionInputs.keys():
                    conjunctionInputs[inMod] = [outMod]
                else:
                    conjunctionInputs[inMod].append(outMod)

    return modules, conjunctionInputs


def solution1():
    modules, conjunctionMemory = getInput()

    #Counts for how many Low/High pulses were sent
    lowCount = 0
    highCount = 0

    for i in range(0, 1000):
        #queue of tuples where each one contains a pulse and the mod that the pulse is going to
        q = [("button", False, "broadcaster")]

        while len(q) > 0:
            fromMod, pulse, toMod = q.pop(0)

            if pulse:
                highCount += 1
            else:
                lowCount += 1

            if toMod not in modules.keys():
                continue

            #Determining how the mod should handle the incoming signal
            if modules[toMod][0] == "bc": #broadcaster
                for d in modules[toMod][2]:
                    q.append((toMod, pulse, d))
                modules[toMod][1] = pulse
            elif modules[toMod][0] == "ff": #flip-flop
                if pulse:
                    continue
                else:
                    modules[toMod][1] = not modules[toMod][1]
                    for d in modules[toMod][2]:
                        q.append((toMod, modules[toMod][1], d))
            elif modules[toMod][0] == "cj": #conjunction
                newPulse = False
                for inputMod in conjunctionMemory[toMod]:
                    if not modules[inputMod][1]:
                        newPulse = True
                        break
                for d in modules[toMod][2]:
                    q.append((toMod, newPulse, d))
                modules[toMod][1] = newPulse

    #print("\nHigh Pulses:", highCount, "\nLow Pulses: ", lowCount)
    return lowCount * highCount


def solution2():
    modules, conjunctionMemory = getInput()

    #Count for how many times a 'True' signal is sent to the 'rx' mod
    rxTrueCount = 0
    #prevCount = 0
    buttonPresses = 0

    while True:
        #queue of tuples where each one contains a pulse and the mod that the pulse is going to
        q = [("button", False, "broadcaster")]
        buttonPresses += 1

        while len(q) > 0:
            fromMod, pulse, toMod = q.pop(0)

            if toMod == 'rx':
                if pulse:
                    rxTrueCount += 1
                else:
                    rxFalseCount += 1

            if toMod not in modules.keys():
                continue

            #Determining how the mod should handle the incoming signal
            if modules[toMod][0] == "bc": #broadcaster
                for d in modules[toMod][2]:
                    q.append((toMod, pulse, d))
                modules[toMod][1] = pulse
            elif modules[toMod][0] == "ff": #flip-flop
                if pulse:
                    continue
                else:
                    modules[toMod][1] = not modules[toMod][1]
                    for d in modules[toMod][2]:
                        q.append((toMod, modules[toMod][1], d))
            elif modules[toMod][0] == "cj": #conjunction
                newPulse = False
                for inputMod in conjunctionMemory[toMod]:
                    if not modules[inputMod][1]:
                        newPulse = True
                        break
                for d in modules[toMod][2]:
                    q.append((toMod, newPulse, d))
                modules[toMod][1] = newPulse

        
        #print("Button:", buttonPresses, "-->", rxTrueCount)
        if rxTrueCount == 1:
            break
        #prevCount = rxTrueCount
        rxTrueCount = 0

    return buttonPresses


#print("Year 2023, Day 20 solution part 1:", solution1())
print("Year 2023, Day 20 solution part 2:", solution2())