aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            if line[0] == "swap" and line[1] == "position":
                inpt.append(('sp', int(line[2]), int(line[-1])))
                
            elif line[0] == "swap" and line[1] == "letter":
                inpt.append(('sl', line[2], line[-1]))
                
            elif line[0] == "reverse":
                inpt.append(('rv', int(line[2]), int(line[-1])))
                
            elif line[0] == "rotate":
                if line[1] == "based":
                    inpt.append(('rp', line[-1]))
                else:
                    steps = int(line[2])
                    if line[1] != "left":
                        steps *= -1
                    inpt.append(('rd', steps))
                
            elif line[0] == "move":
                inpt.append(('m', int(line[2]), int(line[-1])))

    return inpt
            

def solution1():
    inpt = getInput()
    ans = [x for x in "abcdefgh"]
    if testing:
        ans = [x for x in "abcde"]
    
    for i in inpt:
        testing and print(i)
        if i[0] == "sp": #Swap position
            ph = ans[i[1]]
            ans[i[1]] = ans[i[2]]
            ans[i[2]] = ph
        elif i[0] == "sl": #Swap letters
            i1 = ans.index(i[1])
            i2 = ans.index(i[2])
            ph = ans[i1]
            ans[i1] = ans[i2]
            ans[i2] = ph
        elif i[0] == "rv": #Reverse
            s = i[1]
            e = i[2]
            while s < e:
                ph = ans[s]
                ans[s] = ans[e]
                ans[e] = ph
                s += 1
                e -= 1
        elif i[0] == "rp": #Rotate based on pos
            steps = -ans.index(i[1]) - 1
            if ans.index(i[1]) > 3:
                steps -= 1
            steps = steps % len(ans)
            testing and print("\tRotating", steps, "from index", ans.index(i[1]))
            left = ans[steps:]
            right = ans[:steps]
            ans = left + right
        elif i[0] == "rd": #Rotate direction
            left = ans[i[1]:]
            right = ans[:i[1]]
            ans = left + right
        else: #Move
            ph = ans.pop(i[1])
            ans.insert(i[2], ph)

        testing and print("\t", ''.join(ans))

    return ''.join(ans)


def solution2():
    inpt = getInput()
    inpt.reverse()
    ans = [x for x in "fbgdceah"]
    
    for i in inpt:
        if i[0] == "sp": #Swap position
            ph = ans[i[1]]
            ans[i[1]] = ans[i[2]]
            ans[i[2]] = ph
        elif i[0] == "sl": #Swap letters
            i1 = ans.index(i[1])
            i2 = ans.index(i[2])
            ph = ans[i1]
            ans[i1] = ans[i2]
            ans[i2] = ph
        elif i[0] == "rv": #Reverse
            s = i[1]
            e = i[2]
            while s < e:
                ph = ans[s]
                ans[s] = ans[e]
                ans[e] = ph
                s += 1
                e -= 1
        elif i[0] == "rp": #Rotate based on pos
            steps = -ans.index(i[1]) - 1
            if ans.index(i[1]) > 3:
                steps -= 1
            steps = steps % len(ans)
            left = ans[-steps:]
            right = ans[:-steps]
            ans = left + right
        elif i[0] == "rd": #Rotate direction
            left = ans[-i[1]:]
            right = ans[:-i[1]]
            ans = left + right
        else: #Move
            ph = ans.pop(i[2])
            ans.insert(i[1], ph)

    return ''.join(ans)


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())
#cegahdbf not it