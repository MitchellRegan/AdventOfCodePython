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

    return ans, tsp


def solution2():
    inpt = getInput()
    #List of each ingredient name, because if we keep using inpt.keys() we're not guaranteed the same order each time
    ing = [x for x in inpt.keys()]

    def get_score_and_cal(tsp_:list)->list:
        '''Temp function to find the total score and calorie count from a list of ingredient teaspoons.'''
        cap = dur = flv = tex = cal = score = 0
        for i in range(len(tsp_)):
            cap += inpt[ing[i]][0] * tsp_[i]
            dur += inpt[ing[i]][1] * tsp_[i]
            flv += inpt[ing[i]][2] * tsp_[i]
            tex += inpt[ing[i]][3] * tsp_[i]
            cal += inpt[ing[i]][4] * tsp_[i]

        #Totals for each value can't be negative, so they're calculated at 0 instead (per the instructions on y2015d15)
        score = max(0,cap) * max(0,dur) * max(0,flv) * max(0,tex)
        return score, cal
    
    #Getting the score and teaspoon configuration for part 1's answer to use as a starting point
    p1_score, p1_tsp = solution1()
    p1_score, p1_cal = get_score_and_cal(p1_tsp)

    #Performing a BFS from our starting teaspoon configuration
    seen = {tuple(p1_tsp):tuple(get_score_and_cal(p1_tsp))}
    q = [tuple(p1_tsp)]
    ans = -1
    while len(q) > 0:
        tsp = q.pop(0)
        score, cal = seen[tsp]

        #Saving the best score where the ingredients have exactly 500 calories
        if cal == 500:
            if score > ans:
                ans = score
            continue
        else:
            #From the current configuration of teaspoons, we try shifting 1tsp from each group to every other group to see the result
            for i in range(len(tsp)):
                for j in range(len(tsp)):
                    if i == j:
                        continue
                    #Shifting 1tsp from the ingredient at index i to the ingredient at index j
                    new_tsp = [x for x in tsp]
                    new_tsp[i] -= 1
                    new_tsp[j] += 1
                    new_tsp = tuple(new_tsp)

                    if new_tsp not in seen.keys():
                        new_score, new_cal = get_score_and_cal(new_tsp)
                        #If the calorie count is higher than the answer from part 1, or the calorie is too far
                        #below the goal of 500, or this teaspoon combo gives a score too far below our current
                        #best answer, we don't add it to the que
                        if new_cal < p1_cal and new_cal > 485 and (ans == -1 or new_score > (0.75*ans)):
                            q.append(new_tsp)
                            seen[new_tsp] = tuple(get_score_and_cal(new_tsp))

    return ans
#not 17694720


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1()[0])
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())