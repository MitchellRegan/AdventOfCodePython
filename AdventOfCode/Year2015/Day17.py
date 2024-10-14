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
            inpt.append(int(line))

    return inpt
            

def solution1():
    inpt = getInput()
    goal = 150
    if testing:
        goal = 25
    
    def combosToGoal(i_:int, total_:int)->int:
        '''Finds all combinations of values in the input whose sum exactly equals the goal.
        
        Perameters
        ----------
            i_: Index of the input list that's being evaluated.
            total_: Current sum of this recursion's input values.
            
        Returns
        ----------
            Int for how many combination sums exactly match the goal.
        '''
        testing and print("Index", i_, "Current total:", total_)
        if total_ == goal:
            testing and print("\t========== Goal Reached!")
            return 1
        if total_ > goal:
            testing and print("\tOver the goal")
            return 0
        if i_ >= len(inpt):
            testing and print("\tOut of Bounds")
            return 0
        #Doing 2 further recursions: one with the value at this index, one without
        return combosToGoal(i_+1, total_+inpt[i_]) + combosToGoal(i_+1, total_)

    return combosToGoal(0, 0)


def solution2():
    inpt = getInput()
    goal = 150
    if testing:
        goal = 25
    
    def fewestContainers(i_:int, total_:int=0, numContainer_:int=0)->int:
        '''Finds the fewest number of containers used that reaches the goal.
        
        Perameters
        ----------
            i_: Index of the input list that's being evaluated.
            total_: Current sum of this recursion's input values.
            numContainer_: The current number of containers used.
            
        Returns
        ----------
            Int for how many containers are used when the goal is reached.
        '''
        
        #testing and print("Index", i_, "Current total:", total_)
        if total_ == goal:
            #testing and print("\t========== Goal Reached!")
            return numContainer_
        if total_ > goal:
            #testing and print("\tOver the goal")
            return goal
        if i_ >= len(inpt):
            #testing and print("\tOut of Bounds")
            return goal
        
        #Doing 2 further recursions: one with the value at this index, one without
        return min(fewestContainers(i_+1, total_+inpt[i_], numContainer_+1), fewestContainers(i_+1, total_, numContainer_))

    fc = fewestContainers(0, 0, 0)
    
    def combosToGoal(i_:int, total_:int, numContainer_:int=0)->int:
        '''Finds all combinations of values in the input whose sum exactly equals the goal.
        
        Perameters
        ----------
            i_: Index of the input list that's being evaluated.
            total_: Current sum of this recursion's input values.
            numContainer_: The current number of containers used.
            
        Returns
        ----------
            Int for how many combination sums exactly match the goal.
        '''
        
        if total_ == goal:
            if numContainer_ == fc:
                return 1
            return 0
        if total_ > goal:
            return 0
        if i_ >= len(inpt):
            return 0
        #Doing 2 further recursions: one with the value at this index, one without
        return combosToGoal(i_+1, total_+inpt[i_], numContainer_+1) + combosToGoal(i_+1, total_, numContainer_)
    
    testing and print("Fewest containers needed:", fc)
    return combosToGoal(0, 0, 0)


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())