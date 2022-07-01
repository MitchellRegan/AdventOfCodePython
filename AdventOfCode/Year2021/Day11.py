#https://adventofcode.com/2021/day/11
#https://adventofcode.com/2021/day/11#part2

# Real data
data = [[7,2,2,2,2,2,1,2,7,1],[6,4,6,3,7,5,4,2,3,2],[3,3,7,3,4,8,4,6,8,4],[4,6,7,4,4,6,1,2,6,5],[1,1,8,7,8,3,4,7,8,8],[1,1,7,5,3,1,6,3,5,1],[8,2,1,1,4,1,1,8,4,6],[4,6,5,7,8,2,8,3,3,3],[5,2,8,6,3,2,5,3,3,7],[5,7,7,1,3,2,4,8,3,2]]
# Test data
#data = [[5,4,8,3,1,4,3,2,2,3],[2,7,4,5,8,5,4,7,1,1],[5,2,6,4,5,5,6,1,7,3],[6,1,4,1,3,3,6,1,4,6],[6,3,5,7,3,8,5,4,7,8],[4,1,6,7,5,2,4,6,4,5],[2,1,7,6,8,4,1,7,2,1],[6,8,8,2,8,8,1,1,3,4],[4,8,4,6,8,4,8,5,5,4],[5,2,8,3,7,5,1,5,2,6]]


def solution1():
    dataCopy = []
    for d in data:
        dataCopy.append(d.copy())

    # var to track the number of flashes that have happened
    totalFlashes = 0

    # Looping for 100 steps
    for s in range(0, 100):
        # Queue to track if a jelly coordinate has flashed in this step
        flashQ = []

        # Increase the light level of each jelly by 1
        for r in range(0, len(dataCopy)):
            for c in range(0, len(dataCopy[r])):
                dataCopy[r][c] += 1
                if dataCopy[r][c] > 9:
                    flashQ.append((r,c))

        # Iterating through each jelly that needs to flash and increasing the surrounding light levels
        while len(flashQ) > 0:
            # Popping the first jelly coordinate and increasing the number of total flashes
            r = flashQ[0][0]
            c = flashQ[0][1]
            flashQ.pop(0)
            totalFlashes += 1

            # U
            if r > 0:
                dataCopy[r-1][c] += 1
                if dataCopy[r-1][c] == 10:
                    flashQ.append((r-1, c))
            # UR
            if r > 0 and c < len(dataCopy[r])-1:
                dataCopy[r-1][c+1] += 1
                if dataCopy[r-1][c+1] == 10:
                    flashQ.append((r-1, c+1))
            # R
            if c < len(dataCopy[r])-1:
                dataCopy[r][c+1] += 1
                if dataCopy[r][c+1] == 10:
                    flashQ.append((r, c+1))
            # DR
            if r < len(dataCopy)-1 and c < len(dataCopy[r])-1:
                dataCopy[r+1][c+1] += 1
                if dataCopy[r+1][c+1] == 10:
                    flashQ.append((r+1, c+1))
            # D
            if r < len(dataCopy)-1:
                dataCopy[r+1][c] += 1
                if dataCopy[r+1][c] == 10:
                    flashQ.append((r+1, c))
            # DL
            if r < len(dataCopy)-1 and c > 0:
                dataCopy[r+1][c-1] += 1
                if dataCopy[r+1][c-1] == 10:
                    flashQ.append((r+1, c-1))
            # L
            if c > 0:
                dataCopy[r][c-1] += 1
                if dataCopy[r][c-1] == 10:
                    flashQ.append((r, c-1))
            # UL
            if r > 0 and c > 0:
                dataCopy[r-1][c-1] += 1
                if dataCopy[r-1][c-1] == 10:
                    flashQ.append((r-1, c-1))

        # Resetting each jelly's light level
        for r in range(0, len(dataCopy)):
            for c in range(0, len(dataCopy[r])):
                if dataCopy[r][c] > 9:
                    dataCopy[r][c] = 0

    print("Year 2021, Day 11 solution part 1:", totalFlashes)


def solution2():
    dataCopy = []
    for d in data:
        dataCopy.append(d.copy())

    # Looping for 100 steps
    s = 0
    while s < 100000:
        # var to track the number of flashes that have happened this stage
        totalFlashes = 0
        # Queue to track if a jelly coordinate has flashed in this step
        flashQ = []

        # Increase the light level of each jelly by 1
        for r in range(0, len(dataCopy)):
            for c in range(0, len(dataCopy[r])):
                dataCopy[r][c] += 1
                if dataCopy[r][c] > 9:
                    flashQ.append((r,c))

        # Iterating through each jelly that needs to flash and increasing the surrounding light levels
        while len(flashQ) > 0:
            # Popping the first jelly coordinate and increasing the number of total flashes
            r = flashQ[0][0]
            c = flashQ[0][1]
            flashQ.pop(0)
            totalFlashes += 1

            # U
            if r > 0:
                dataCopy[r-1][c] += 1
                if dataCopy[r-1][c] == 10:
                    flashQ.append((r-1, c))
            # UR
            if r > 0 and c < len(dataCopy[r])-1:
                dataCopy[r-1][c+1] += 1
                if dataCopy[r-1][c+1] == 10:
                    flashQ.append((r-1, c+1))
            # R
            if c < len(dataCopy[r])-1:
                dataCopy[r][c+1] += 1
                if dataCopy[r][c+1] == 10:
                    flashQ.append((r, c+1))
            # DR
            if r < len(dataCopy)-1 and c < len(dataCopy[r])-1:
                dataCopy[r+1][c+1] += 1
                if dataCopy[r+1][c+1] == 10:
                    flashQ.append((r+1, c+1))
            # D
            if r < len(dataCopy)-1:
                dataCopy[r+1][c] += 1
                if dataCopy[r+1][c] == 10:
                    flashQ.append((r+1, c))
            # DL
            if r < len(dataCopy)-1 and c > 0:
                dataCopy[r+1][c-1] += 1
                if dataCopy[r+1][c-1] == 10:
                    flashQ.append((r+1, c-1))
            # L
            if c > 0:
                dataCopy[r][c-1] += 1
                if dataCopy[r][c-1] == 10:
                    flashQ.append((r, c-1))
            # UL
            if r > 0 and c > 0:
                dataCopy[r-1][c-1] += 1
                if dataCopy[r-1][c-1] == 10:
                    flashQ.append((r-1, c-1))

        # If all jellies have flashed this phase, this is the first synchronization
        if totalFlashes == (len(dataCopy) * len(dataCopy[0])):
            print("Year 2021, Day 11 solution part 2:", s+1)
            return

        # Resetting each jelly's light level
        for r in range(0, len(dataCopy)):
            for c in range(0, len(dataCopy[r])):
                if dataCopy[r][c] > 9:
                    dataCopy[r][c] = 0

        # Incrementing the step counter if there was no synch
        s += 1


solution1()
solution2()