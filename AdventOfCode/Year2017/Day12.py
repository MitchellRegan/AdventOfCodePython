aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = {}

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(" <-> ")
            num1 = int(line[0])
            cncts = [int(x) for x in line[1].split(', ')]
            for c in cncts:
                if num1 not in inpt.keys():
                    inpt[num1] = [c]
                elif c not in inpt[num1]:
                    inpt[num1].append(c)
                if c not in inpt.keys():
                    inpt[c] = [num1]
                elif num1 not in inpt[c]:
                    inpt[c].append(num1)

    return inpt
            

def solution1():
    inpt = getInput()
    
    seen = {0:True}
    q = [0]
    while len(q) > 0:
        head = q.pop(0)
        for adj in inpt[head]:
            if adj not in seen.keys():
                seen[adj] = True
                q.append(adj)

    return len(seen.keys())


def solution2():
    inpt = getInput()
    nodes = [x for x in inpt.keys()]
    groups = []
    
    while len(nodes) > 0:
        seen = {nodes[0]:True}
        q = [nodes.pop(0)]
        while len(q) > 0:
            head = q.pop(0)
            for adj in inpt[head]:
                if adj not in seen.keys():
                    seen[adj] = True
                    q.append(adj)
                    nodes.remove(adj)
        groups.append([x for x in seen.keys()])

    return len(groups)


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())