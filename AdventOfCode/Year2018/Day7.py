#https://adventofcode.com/2018/day/7
#https://adventofcode.com/2018/day/7#part2

inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2018\\InputTestFiles\\d7_test.txt"
#inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2018\\InputRealFiles\\d7_real.txt"

def solution1():
    allSteps = []
    parentSteps = {}
    order = ""

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            s1 = line.split(' ')[1]
            s2 = line.split(' ')[7]
            
            if s1 not in allSteps:
                allSteps.append(s1)
            if s2 not in allSteps:
                allSteps.append(s2)

            if s2 not in parentSteps.keys():
                parentSteps[s2] = s1
            else:
                parentSteps[s2] += s1

    #Finding all steps that have no prior requirement
    for s in allSteps:
        if s not in parentSteps.keys():
            order += s

    #If there's more than 1 starting step, we have to put them in order
    order = ''.join(sorted(order))
    si = 0
    while len(allSteps) > 0:
        #String to store all of the new steps that have become valid this loop
        validSteps = []
        #Looping through each step
        for k in parentSteps.keys():
            #If this step has a prerequisite step that is in the order string, we remove that prerequisite
            if order[si] in parentSteps[k]:
                parentSteps[k] = parentSteps[k].replace(order[si], '')
                #if there are no more prerequisites, this step becomes valid
                if parentSteps[k] == "":
                    validSteps.append(k)
                    parentSteps.pop(k)

        #after all of the loops are done, we pop the current step from the list of all steps
        allSteps.remove(order[si])
        si += 1
        order += ''.join(sorted(validSteps))

    return order


def solution2():
    
    return 0


print("Year 2018, Day 7 solution part 1:", solution1())
print("Year 2018, Day 7 solution part 2:", solution2())