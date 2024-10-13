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
            line = line.replace('\n', '').split(' ')
            p1 = line[0][0]
            p2 = line[-1][0]
            h = int(line[3])
            if line[2] == "lose":
                h *= -1
            if p1 in inpt.keys():
                inpt[p1].append((p2,h))
            else:
                inpt[p1] = [(p2,h)]

    return inpt
            

def solution1():
    inpt = getInput()
    
    def getPermHappiness(perm_:list)->int:
        '''Recursively creates all permutations of seating arrangements for people and returns the total happiness.'''
        if len(perm_) == len(inpt.keys()):
            testing and print(perm_)
            h = 0
            for i in range(len(perm_)):
                n = i+1
                if i == len(perm_)-1:
                    n = 0
                p = i - 1
                if i == 0:
                    p = len(perm_)-1
                testing and print("\t", perm_[p], "--", perm_[i], "--", perm_[n])
                h += sum([y for (x,y) in inpt[perm_[i]] if x in [perm_[n], perm_[p]]])
            testing and print("\tTotal:", h)
            return h
        
        h = 0
        for n in [x for x in inpt.keys() if x not in perm_]:
            nextPerm = perm_[:]
            nextPerm.append(n)
            h = max(h, getPermHappiness(nextPerm))
        return h

    ans = 0
    for k in inpt.keys():
        #testing and print('\t', k, ':', inpt[k])
        ans = max(ans, getPermHappiness([k]))

    return ans


def solution2():
    inpt = getInput()
    
    newRow = []
    for k in inpt.keys():
        inpt[k].append(('Z',0))
        testing and print(k, ":", inpt[k])
        newRow.append((k,0))
    inpt['Z'] = newRow
    testing and print("Z :", inpt['Z'])
    
    def getPermHappiness(perm_:list)->int:
        '''Recursively creates all permutations of seating arrangements for people and returns the total happiness.'''
        if len(perm_) == len(inpt.keys()):
            testing and print(perm_)
            h = 0
            for i in range(len(perm_)):
                n = i+1
                if i == len(perm_)-1:
                    n = 0
                p = i - 1
                if i == 0:
                    p = len(perm_)-1
                testing and print("\t", perm_[p], "--", perm_[i], "--", perm_[n])
                h += sum([y for (x,y) in inpt[perm_[i]] if x in [perm_[n], perm_[p]]])
            testing and print("\tTotal:", h)
            return h
        
        h = 0
        for n in [x for x in inpt.keys() if x not in perm_]:
            nextPerm = perm_[:]
            nextPerm.append(n)
            h = max(h, getPermHappiness(nextPerm))
        return h

    ans = 0
    for k in inpt.keys():
        #testing and print('\t', k, ':', inpt[k])
        ans = max(ans, getPermHappiness([k]))

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())