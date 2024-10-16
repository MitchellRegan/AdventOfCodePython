aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').replace(' ', '')
            inpt.append(line)

    return inpt
            

def solution1():
    inpt = getInput()
    
    def evaluateStr(evs:str):
        '''Recursive method that traverses the given string and returns the final result.'''
        testing and print("Evaluating:", evs)
        seq = []
        i = 0
        while i < len(evs):
            if evs[i].isdigit():
                seq.append(int(evs[i]))
                i += 1
            elif evs[i] != '(':
                seq.append(evs[i])
                i += 1
            else:
                paren = 1
                for j in range(i+1, len(evs)):
                    if evs[j] == '(':
                        paren += 1
                    elif evs[j] == ')':
                        paren -= 1
                        if paren == 0:
                            testing and print("\tSubstring found:", evs[i:j+1])
                            seq.append(evaluateStr(evs[i+1:j]))
                            i = j+1
                            break
        testing and print("\tStack:", seq)
        res = seq[0]
        for x in range(1, len(seq), 2):
            testing and print("\t\t", res, seq[x], seq[x+1])
            if seq[x] == '+':
                res += seq[x+1]
            elif seq[x] == '*':
                res *= seq[x+1]
            testing and print("\t\t\t=", res)
        return res
    
    ans = 0
    for line in inpt:
        testing and print(line)
        ans += evaluateStr(line)

    return ans


def solution2():
    inpt = getInput()
    
    def evaluateStr(evs:str):
        '''Recursive method that traverses the given string and returns the final result.'''
        testing and print("Evaluating:", evs)
        seq = []
        i = 0
        while i < len(evs):
            if evs[i].isdigit():
                seq.append(int(evs[i]))
                i += 1
            elif evs[i] != '(':
                seq.append(evs[i])
                i += 1
            else:
                paren = 1
                for j in range(i+1, len(evs)):
                    if evs[j] == '(':
                        paren += 1
                    elif evs[j] == ')':
                        paren -= 1
                        if paren == 0:
                            seq.append(evaluateStr(evs[i+1:j]))
                            i = j+1
                            break
        testing and print("\tStack:", seq)
        while '+' in seq:
            plusInd = seq.index('+')
            newVal = seq[plusInd-1] + seq[plusInd+1]
            seq.pop(plusInd-1)
            seq.pop(plusInd-1)
            seq[plusInd-1] = newVal
            testing and print("\t\tRemoved Plus. New Stack:", seq)
        res = seq[0]
        for x in range(1, len(seq), 2):
            testing and print("\t\t", res, seq[x], seq[x+1])
            if seq[x] == '+':
                res += seq[x+1]
            elif seq[x] == '*':
                res *= seq[x+1]
            testing and print("\t\t\t=", res)
        return res
    
    ans = 0
    for line in inpt:
        testing and print(line)
        ans += evaluateStr(line)

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())