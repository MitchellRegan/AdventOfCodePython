aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    pageOrder = {}
    updates = []

    with open(inFile, 'r') as f:
        onPageOrder = True
        for line in f:
            line = line.replace('\n', '')
            if line == '':
                onPageOrder = False
            elif onPageOrder:
                line = [int(x) for x in line.split('|')]
                if line[0] in pageOrder.keys():
                    pageOrder[line[0]].append(line[1])
                else:
                    pageOrder[line[0]] = [line[1]]
            else:
                line = [int(x) for x in line.split(',')]
                updates.append(line)

    return pageOrder, updates
            

def solution1():
    pageOrder, updates = getInput()
    
    ans = 0
    for line in updates:
        isValid = True

        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if line[i] in pageOrder.keys() and line[j] not in pageOrder[line[i]]:
                    isValid = False
                    break

                if line[j] in pageOrder.keys() and line[i] in pageOrder[line[j]]:
                    isValid = False
                    break
            if not isValid:
                break

        if isValid:
            ans += line[len(line)//2]

    return ans


def solution2():
    pageOrder, updates = getInput()

    ans = 0
    for line in updates:
        testing and print("Checking", line)
        isValid = True

        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if line[i] in pageOrder.keys() and line[j] not in pageOrder[line[i]]:
                    isValid = False
                    break

                if line[j] in pageOrder.keys() and line[i] in pageOrder[line[j]]:
                    isValid = False
                    break
            if not isValid:
                break

        if not isValid:
            testing and print("\tINVALID")
            newOrder = []
            for i in range(len(line)):
                inFront = 0
                for j in range(len(line)):
                    if i == j:
                        continue
                    if line[j] in pageOrder.keys() and line[i] in pageOrder[line[j]]:
                        inFront += 1
                testing and print("\t\t", line[i], "has", inFront, "in front")
                newOrder.append((line[i], inFront))

            newOrder.sort(key=lambda x:x[1])
            testing and print(newOrder)
            newOrder = [x[0] for x in newOrder]
            testing and print("\t\tFixed order:", newOrder)
            ans += newOrder[len(newOrder)//2]

    return ans

    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())