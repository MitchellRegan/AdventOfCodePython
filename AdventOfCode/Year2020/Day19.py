aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    rules = {}
    messages = []

    with open(inFile, 'r') as f:
        readingRules = True
        for line in f:
            line = line.replace('\n', '')
            if len(line) == 0:
                readingRules = False
                continue

            if readingRules:
                ruleNum = int(line.split(':')[0])
                line = line.split(': ')[1].split(' ')
                if len(line) == 1:
                    line = line[0][1]
                else:
                    for x in range(0, len(line)):
                        if line[x] is not '|':
                            line[x] = int(line[x])
                rules[ruleNum] = line
            else:
                messages.append(line)

    return rules, messages
            

def solution1():
    rules, messages = getInput()
    
    if testing:
        print("Rules")
        for r in rules.keys():
            print("\t", r, ":", rules[r])
        print("\nMessages")
        for m in messages:
            print("\t", m)
        print("Updating rules")
            
    #Simplifying the rules a bit more
    while True:
        updatedRules = False
        
        for r in rules.keys():
            testing and print("\tChecking to update rule", r, ":", rules[r])
            numChar = 0
            for i in range(0, len(rules[r])):
                rn = rules[r][i]
                if rn is not '|' and type(rn) is int:
                    testing and print("\t\t", rn, "is int to check")
                    if len (rules[rn]) == 1:
                        testing and print("\t\t\tSub-rule is", rules[rn])
                        rules[r][i] = rules[rn]
                        updatedRules = True
                        numChar += 1
                elif type(rn) is str:
                    numChar += 1
            if numChar > 1 and numChar == len(rules[r]) and '|' in rules[r]:
                testing and print("\t\tAll values in", rules[r], "are chars")
                lineIndex = rules[r].index('|')
                rules[r] = [''.join(rules[r][0:lineIndex]), '|', ''.join(rules[r][lineIndex+1:])]
        #If an entire loop of checking the rules resulted in no changes, we're as simplified as possible
        if not updatedRules:
            break
        
    if True:
        print("Updated Rules")
        for r in rules.keys():
            print("\t", r, ":", rules[r])
            
    def ruleChecker(message_:str, r_:int=0, ptr_:int=0)->int:
        testing and print("Rule Checker Sub-Function. Message:", message_, "  Rule:", r_, ":", rules[r_], "  Ptr:", ptr_)
        #Only 1 element in the rule array means it's just checking a single string
        if len(rules[r_]) == 1:
            rc = rules[r_][0][1]
            testing and print("Matching char", rc, "with", message_[ptr_])
            if rc == message_[ptr_:ptr_+len(rc)]:
                return 1
            else:
                return 0
            
        #Comparing different sets of rules
        elif '|' in rules[r_]:
            lineIndex = rules[r_].index('|')
            subRules1 = rules[r_][:lineIndex]
            subRules2 = rules[r_][lineIndex+1:]
            
        #Going rule-by-rule
        else:
            for i in range(0, len(rules[r_])):
                ptrOffset = 0
                #If it's a single string, we compare with the current 
                if type(rules[r_][i]) is str:
                    if rules[r_][i] == message_[ptr_:ptr_+len(rules[r_][i])]:
                        ptr_ += 1
                    else:
                        return 0
                #If it's another rule, we do a recursive call with the rule at the current pointer index
                else:
                    result = ruleChecker(message_, rules[r_][i], ptr_)
                    #If the result is 0, none of the recursive sub-rules matched the string
                    if result == 0:
                        return 0
                    #If the result is greater than 0, we move the pointer index by that much
                    else:
                        ptr_ += result
            #If we go through the entire list of rules, we return our current 

    matchZero = 0
    for m in messages:
        result = ruleChecker(m, 0)
        matchZero += ruleChecker(m, 4)

    return matchZero


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())