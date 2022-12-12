#https://adventofcode.com/2018/day/7
#https://adventofcode.com/2018/day/7#part2

from HelperFunctions import inputReaders as ir
import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d7_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d7_real.txt")

def solution1():
    order = ""
    #List to hold tasks that don't have any prerequisite tasks
    q = []
    #Getting the dictionary of tasks that DO have prerequisite tasks from the input file
    dict = ir.toDict1key1val(inFile, 7, 1)
    for k in dict.keys():
        #print(k,":", dict[k])
        #If any of the prerequisite tasks aren't keys (i.e. don't have prerequisites of their own) they're completed
        for i in dict[k]:
            if i not in dict.keys() and i not in q:
                q.append(i)

    q.sort()

    #Looping through every completed task in the que to check them off of other tasks' prerequisites
    while len(q) > 0:
        #Completed task at the head of the que to check off
        cur = q.pop(0)
        #List of tasks that are completed this loop
        newlyCompleted = []

        #If the current task is a prereque for one in the dictionary, we remove it
        for k in dict.keys():
            if cur in dict[k]:
                dict[k].remove(cur)
                #If there are no more prerequisites left, this task is complete
                if len(dict[k]) == 0:
                    newlyCompleted.append(k)

        #Removing the newly completed tasks from the dictionary to speed up future searches
        for n in newlyCompleted:
            dict.pop(n)

        #Adding the newly completed tasks to the que and sorting them in alphabetical order
        q.extend(newlyCompleted)
        q.sort()
        order += cur
        #print(cur)
        #print(" - Newly completed:", newlyCompleted)
        #print(" - Updated que:", q)

    return order


def solution2():
    #Number of workers going in parallel
    workers = 5
    #Offset for the amount removed from character ascii values
    asciiOffset = 4

    #List to hold tasks that don't have any prerequisite tasks
    q = []
    #Dictionary to hold the time duration for each running task
    taskTime = {}

    #Getting the dictionary of tasks that DO have prerequisite tasks from the input file
    dict = ir.toDict1key1val(inFile, 7, 1)
    for k in dict.keys():
        #If any of the prerequisite tasks aren't keys (i.e. don't have prerequisites of their own) they're completed
        for i in dict[k]:
            if i not in dict.keys() and i not in q:
                #getting the duration that this task takes to complete
                taskTime[i] = ord(i) - asciiOffset
                q.append(i)

    q.sort()

    #Looping through every completed task in the que to check them off of other tasks' prerequisites
    time = 0
    while len(q) > 0:
        time += 1
        #Completed task at the head of the que to check off
        cur = []

        #print("Second", time)
        for c in range(0, min(len(q), workers)):
            #print(" - Worker", c+1, "doing task", q[c], "- time remaining:", taskTime[q[c]])
            taskTime[q[c]] -= 1
            if taskTime[q[c]] == 0:
                cur.append(q[c])

        for c in cur:
            q.remove(c)
        if len(cur) > 0:
            cur.sort()
            #List of tasks that are completed this loop
            newlyCompleted = []
        
            #If the current task is a prereque for one in the dictionary, we remove it
            for k in dict.keys():
                for c in cur:
                    if c in dict[k]:
                        dict[k].remove(c)
                        #If there are no more prerequisites left, this task is complete
                        if len(dict[k]) == 0:
                            newlyCompleted.append(k)
                            taskTime[k] = ord(k) - asciiOffset

            #Removing the newly completed tasks from the dictionary to speed up future searches
            for n in newlyCompleted:
                dict.pop(n)

            #Adding the newly completed tasks to the que and sorting them in alphabetical order
            newlyCompleted.sort()
            q.extend(newlyCompleted)

    return time

print("Year 2018, Day 7 solution part 1:", solution1())
print("Year 2018, Day 7 solution part 2:", solution2())
#902 too low
#1177 too high