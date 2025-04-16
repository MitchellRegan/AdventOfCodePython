aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = {}#Key = ingredient name, Value = [capacity, durability, flavor, texture, calories]

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').replace(',', '').split(' ')
            n = line[0][:-1]
            inpt[n] = [int(line[2]), int(line[4]), int(line[6]), int(line[8]), int(line[10])]

    return inpt
            

def solution1():
    inpt = getInput()
    
    #List of each ingredient name, because if we keep using inpt.keys() we're not guaranteed the same order each time
    ing = [x for x in inpt.keys()]
    #List of how many teaspoons of each ingredient is used
    tsp = [1] * len(ing)
    ans = 0

    #Looping 100 times, adding 1 teaspoon each time to the ingredient that gives the best overall score
    for x in range(len(ing), 100):
        #testing and print("Loop", x, "\n\tTeaspoons:", tsp, "\n\tScore:", ans)
        best_score = ans
        best_index = -1
        cap = dur = flv = tex = 0

        #Finding the current values of each property
        for i in range(len(ing)):
            cap += (inpt[ing[i]][0] * tsp[i])
            dur += (inpt[ing[i]][1] * tsp[i])
            flv += (inpt[ing[i]][2] * tsp[i])
            tex += (inpt[ing[i]][3] * tsp[i])
        #testing and print("\tCap:", cap, "Dur:", dur, "Flv:", flv, "Tex:", tex)

        #Simulating what the score would be if we added 1tsp of any single ingredient
        for i in range(len(ing)):
            temp_score = (cap + inpt[ing[i]][0]) * (dur + inpt[ing[i]][1]) * (flv + inpt[ing[i]][2]) * (tex + inpt[ing[i]][3])
            #testing and print("\t\tBest score with", ing[i], ":", temp_score)
            if temp_score > best_score:
                best_score = temp_score
                best_index = i

        if best_index == -1:
            return
        #testing and print("\tAdding 1tsp of", ing[best_index], "\n")
        ans = best_score
        tsp[best_index] = tsp[best_index]+1

    return ans


def solution2():
    inpt = getInput()
    #List of each ingredient name, because if we keep using inpt.keys() we're not guaranteed the same order each time
    ing = [x for x in inpt.keys()]

    start = tuple([0]*len(inpt))
    seen = {start:True} #dictionary where key is a tuple of ingredient teaspoons to track which combinations we've already seen
    q = [start]
    ans = 0

    #Performing what is essentially a BFS where we check all combinations that are 1 tsp removed from the current
    #combination until we find ones that have exactly 100 tsp and 500 cal
    while len(q) > 0:
        tsp = q.pop(0)

        cap = dur = flv = tex = cal = 0
        #Finding the current values of each property
        for i in range(len(ing)):
            cap += (inpt[ing[i]][0] * tsp[i])
            dur += (inpt[ing[i]][1] * tsp[i])
            flv += (inpt[ing[i]][2] * tsp[i])
            tex += (inpt[ing[i]][3] * tsp[i])
            cal += (inpt[ing[i]][4] * tsp[i])

        #Combinations with exactly 100 tsp of ingredients have their calorie count checked
        if sum(tsp) == 100:
            if cal == 500:
                score = cap * dur * flv * tex
                ans = max(ans, score)
        #Combinations that have less than 100 tsp of ingredients are iterated on
        else:
            for i in range(len(ing)):
                new_combo = [x for x in tsp]
                new_combo[i] += 1
                new_combo = tuple(new_combo)
                if new_combo not in seen.keys():
                    seen[new_combo] = True
                    q.append(new_combo)
    return ans
#not 17694720


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())