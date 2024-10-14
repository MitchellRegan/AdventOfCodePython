aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = None

    with open(inFile, 'r') as f:
        for line in f:
            inpt = int(line.replace('\n', ''))

    return inpt
            

def solution1():
    inpt = getInput()
    
    i = 1
    while True:
        #testing and print("House", i)
        #Getting all divisors of the current value of i
        #divs = []
        score = 10 + (10 * i)
        #testing and print("\tSquare Root:", int(i**0.5))
        for d in range(2, int(i**0.5)+1):
            if i % d == 0:
                #divs.append(d)
                score += (10 * d)
                if i//d != d:
                    #divs.append(i//d)
                    score += (10 * (i//d))
        #testing and print("\tScore:", score)
        if score >= inpt:
            return i
        i += 1

    return


def solution2():
    inpt = getInput()
    seen = {}#Key = int for divisor value, Value = number of times the divisor has been seen
    
    i = 1
    while True:
        #Getting all divisors of the current value of i
        score = 0
        for d in range(1, int(i**0.5)+1):
            if i % d == 0:
                if d not in seen.keys():
                    seen[d] = 0
                seen[d] += 1
                if seen[d] <= 50:
                    score += (11 * d)
                    
                o = i//d
                if o != d:
                    if o not in seen.keys():
                        seen[o] = 0
                    seen[o] += 1
                    if seen[o] <= 50:
                        score += (11 * o)
                        
        if score >= inpt:
            return i
        i += 1

    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())