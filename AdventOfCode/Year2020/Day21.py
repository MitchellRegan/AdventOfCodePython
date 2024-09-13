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
            line = line.replace('\n', '')
            ingredients = line.split(' (')[0].split(' ')
            allergens = line[:-1].split(' (contains ')[1].split(', ')
            inpt.append([ingredients, allergens])
    return inpt
            

def solution1():
    inpt = getInput()
    
    #Getting dictionaries to locate all unique allergen names
    allAlr = {}
    
    #Finding the names of all unique allergens
    for line in range(0, len(inpt)):
        for alr in inpt[line][1]:
            if alr not in allAlr.keys():
                allAlr[alr] = [x for x in inpt[line][0]]
                testing and print(alr, "starting words:", allAlr[alr])
            else:
                allAlr[alr] = [x for x in allAlr[alr] if x in inpt[line][0]]
                testing and print("\t", alr, "reduced to", allAlr[alr])
    
    #Comparing every allergen against every other allergen
    allergenNames = [x for x in allAlr.keys()]
    while True:
        updated = False
        for i in range(len(allergenNames)-1):
            for j in range(i+1, len(allergenNames)):
                name1 = allergenNames[i]
                name2 = allergenNames[j]
                
                #If neither allergen has a known ingredient name, we move on
                if len(allAlr[name1]) > 1 and len(allAlr[name2]) > 1:
                    continue
                
                #If the first allergen has a known name, we remove it from the other allergen's possible names
                if len(allAlr[name1]) == 1 and allAlr[name1][0] in allAlr[name2]:
                    allAlr[name2].remove(allAlr[name1][0])
                    updated = True
                    
                #If the second allergen has a known name, we remove it from the first allergen's possible names
                elif len(allAlr[name2]) == 1 and allAlr[name2][0] in allAlr[name1]:
                    allAlr[name1].remove(allAlr[name2][0])
                    updated = True

        if not updated:
            break
            
    if testing:
        for a in allAlr.keys():
            print("\t", a, ":", allAlr[a])
        
    #Counting the number of total words that are not one of the known allergens
    ans = 0
    for line in inpt:
        for allergen in allAlr.keys():
            if allAlr[allergen][0] in line[0]:
                line[0].remove(allAlr[allergen][0])
        ans += len(line[0])

    return ans


def solution2():
    inpt = getInput()
    
    #Getting dictionaries to locate all unique allergen names
    allAlr = {}
    
    #Finding the names of all unique allergens
    for line in range(0, len(inpt)):
        for alr in inpt[line][1]:
            if alr not in allAlr.keys():
                allAlr[alr] = [x for x in inpt[line][0]]
                testing and print(alr, "starting words:", allAlr[alr])
            else:
                allAlr[alr] = [x for x in allAlr[alr] if x in inpt[line][0]]
                testing and print("\t", alr, "reduced to", allAlr[alr])
    
    #Comparing every allergen against every other allergen
    allergenNames = [x for x in allAlr.keys()]
    while True:
        updated = False
        for i in range(len(allergenNames)-1):
            for j in range(i+1, len(allergenNames)):
                name1 = allergenNames[i]
                name2 = allergenNames[j]
                
                #If neither allergen has a known ingredient name, we move on
                if len(allAlr[name1]) > 1 and len(allAlr[name2]) > 1:
                    continue
                
                #If the first allergen has a known name, we remove it from the other allergen's possible names
                if len(allAlr[name1]) == 1 and allAlr[name1][0] in allAlr[name2]:
                    allAlr[name2].remove(allAlr[name1][0])
                    updated = True
                    
                #If the second allergen has a known name, we remove it from the first allergen's possible names
                elif len(allAlr[name2]) == 1 and allAlr[name2][0] in allAlr[name1]:
                    allAlr[name1].remove(allAlr[name2][0])
                    updated = True

        if not updated:
            break
            
    dangerWord = []
    for a in allAlr.keys():
        testing and print("\t", a, ":", allAlr[a])
        dangerWord.append(a)
    dangerWord.sort()
    testing and print("All Danger Words:", dangerWord)
    for i in range(0, len(dangerWord)):
        dangerWord[i] = allAlr[dangerWord[i]][0]
    testing and print("All Danger Words:", dangerWord)
    
    return ','.join(dangerWord)


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())