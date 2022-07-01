#https://adventofcode.com/2021/day/6
#https://adventofcode.com/2021/day/6#part2

data = [3,5,2,5,4,3,2,2,3,5,2,3,2,2,2,2,3,5,3,5,5,2,2,3,4,2,3,5,5,3,3,5,2,4,5,4,3,5,3,2,5,4,1,1,1,5,1,4,1,4,3,5,2,3,2,2,2,5,2,1,2,2,2,2,3,4,5,2,5,4,1,3,1,5,5,5,3,5,3,1,5,4,2,5,3,3,5,5,5,3,2,2,1,1,3,2,1,2,2,4,3,4,1,3,4,1,2,2,4,1,3,1,4,3,3,1,2,3,1,3,4,1,1,2,5,1,2,1,2,4,1,3,2,1,1,2,4,3,5,1,3,2,1,3,2,3,4,5,5,4,1,3,4,1,2,3,5,2,3,5,2,1,1,5,5,4,4,4,5,3,3,2,5,4,4,1,5,1,5,5,5,2,2,1,2,4,5,1,2,1,4,5,4,2,4,3,2,5,2,2,1,4,3,5,4,2,1,1,5,1,4,5,1,2,5,5,1,4,1,1,4,5,2,5,3,1,4,5,2,1,3,1,3,3,5,5,1,4,1,3,2,2,3,5,4,3,2,5,1,1,1,2,2,5,3,4,2,1,3,2,5,3,2,2,3,5,2,1,4,5,4,4,5,5,3,3,5,4,5,5,4,3,5,3,5,3,1,3,2,2,1,4,4,5,2,2,4,2,1,4]
#data = [3,4,3,1,2]

def solution(days_):
    # Creating an array of ints where the index represents the number of days left until reproduction, and the value at that index represents the quantity at that stage
    arr = [0] * 9

    # Looping through the data to get the quantity of each fish in each stage
    for stage in data:
        arr[stage] += 1
    
    # Looping a number of days to simulate growth
    for day in range(0, days_):
        # All fish who were at stage 0 reproduce
        reproduce = arr[0]

        # Shifting each fish down one stage
        for stage in range(0, len(arr) - 1):
            arr[stage] = arr[stage + 1]

        # Clearing the last stage of fish unless more are reproduced
        arr[len(arr)-1] = 0

        # Fish that reproduce are reset back to stage 6
        arr[6] += reproduce
        # Newly created fish have a starting stage of 8
        arr[8] += reproduce

    # Getting the total number of fish in all stages
    sum = 0
    for fish in arr:
        sum += fish
    return sum


print("Year 2021, Day 6 solution part 1:", solution(80))
print("Year 2021, Day 6 solution part 2:", solution(256))