#https://adventofcode.com/2020/day/11
#https://adventofcode.com/2020/day/11#part2

# Real data
data = ['LLLLLLLLLLLL.LLLLLLL.LLLLLLL..LLLL.LLLLL.LLLLL.LLL..LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LLLLL.L.LLL.LLLLL.LLLL..LLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLL','LLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLL.L.LLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL..LLLLL.','L.LLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLL.LLLL.LLLLLLLL.LL.L.LLLLLLL.LLLL.LLLLLLLL.LLLLLLL','LLLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLL.LL.LLLL','LLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLL','LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LL.LLLLL.LLLL.LLLLLLLL.LLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLL','.L...LL.L.L.L....L..L......LL...L..L.L.LLL.....L...L..LLL.L.LL..LLL......L..L.LLLLL.....L..L...','LLLLL..LLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLL.LLLLLLLLLLLLLLLLLLLLL','LLL.LLLLLLLL..LLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLL.LLLL.L.LLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLL','LLLLL.L.LLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLL.LLLLL.LLLL.LLLLLLLLLLLL..LLLLLLL.LLLLLLLLLL.LL.LLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLL.LLLLLLL.LLL.LLLL.LLLLLLL','LLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLL...LLLLLL','LLL.LLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLL.LLLLLLLL','LLLLL.LLLLLLLLLLLLLLLL.LL.LL.LLLLL.LLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLL..LLLLLLLLLLLLL.LLLLL.L','L.LLLLLLLLLL.LLLLLLLLL.LLLLL.L.LLL.LLLLL.LLLLLLLLLL.LLLLLLLL.LLLL.LLLLL.L.LLLL.LLLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LL.LL.LLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLL.LLLL.L.LLLLLL.LLLLLLL','L...L.LL..L.L.LL.LL.L.....L..L.L.......L.L.LL...L....L......L.L.L.L.L..L....LL......L......L...','LLLL..LLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.L.LLLL.LLLL.LLLLL..LLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLL.LL.LL.LLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLL.','L..LL.LLLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLL.LLLLL.LL.L.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL..LLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLL','LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLL.LLLLL.L.LLLLL.LLLLLLL','LL.LL.LLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLLL.LLL.LLL','...............L.L..LL.....L.L..L...LL.......LL....L......L...L....L...............LLL...L.LLL.','LLLLLLLLLLL..LLLLLL.LLLLLLLL.LLLLL.LLLLL.LLLLLLLLLL..LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.L.LLLLL','LL.LL.LLLLLL.LLLLLLLLL.LLLLL.LLLL..LLLLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLL.LLL.LLLLLLLLL.LLLLLLL','.LLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLL.LLLLLLLLLLLLLLL.LLL.LLLLLLLLLLLL.LLLLL.LLLLLLLLLL','LLLLL.L.LLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLL.LLL..LLLLLLLLLLLLLLLL','LLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLL.LLLL.LLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLL','LLL.L.LLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLL','LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLL','....L..L..........L......L.LL..L.L..LL.......L.....LL..L..LL...L......L....L..L..L....L.......L','.L.LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLL.LLLLLL.LLLLLLLLLL.LL.LLLLLLLLLL.L.LLLL.LLLLLLLL.LLLLLLL','LLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLL','LLLLL.LLL.LL.LLL.LLLLL.LLLLLLLLLLL.LLLLL.LLLLL.LLLL.L.LLLLLLLLLL..LLLLLLLLLLLL.LLLLLLLL.LLLLLLL','LL.LL.LLLLLL.LLLL.LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLL.L.LLLLLLLL.LLLLLLLLLLLL.L.LL.LLLLLLLL.LLLLLLL','LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLL.LLLLLLL..LLLLLLL','.....L.L..LL.LLL.LL.L.L.....L..L.L......L......L.LL...L....LL..L.........L..L.....L.L....L..L..','LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLL','LLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLL.LLL..LLLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLLLLLLLLLLLLLL.L.LLL.LLLLL.LL.LL.LLLL.L.LLLLL...LLL.LLL.LLLLLLLL.LLLLLLLL.LLLLLLL','LLLLL.L.LLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLL','LLLLL.LLLLL..LLLLLLLLL.L.LLL.LLL.L.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLL.','LLLLLLLLLLLL.LLLLLLLL..LLLLLLLLLLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLLL.LLLL.LLLLL.LLLLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLL','...L..LL.L......L....LLL....L.L.LL..L.L..L.LL..L..L.L......L...L.L..L..LL....L..L..LL...LL.....','L..LL.LLLLLL.LLLLLLLLLL.LL.L.LLLLL.L.LLL.LLLLLL.LLL.LLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLLL..LL.LLLLLLLL.LLLLLLLL.LLLLLLL','LLLLLLLLLLLL.L.LLLLLLL.LLLLL.LLLLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLL','LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL..LLLLLLLLLLLLL.LLLLLLL','LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLL.LLLLLL.LLLL.L.LLL.LL.LLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLL','LLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLL..LLLLLLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLL.L.LLLL.LLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLL','LL..L.L.L.L..LL...LL....L.L..L..LLL..L.LL.L.LLLL..L.L.L..L...L.....L..LL........L...LL..L.L.LL.','LLLLL.LLLL.L.LL.LLLLLL.LLLLLLLLLLLLL.LLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.L.LLLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LLLLL.LLLLLL.LLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL','LLLLL.LLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LL.L.LLLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL','LLLLL.LLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLL..LLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLL','LL.L..L..L.....LL......L.......LLLLL..L.L.LL...L......L.L..L.L.L........L..L.L.L..LLLL....L....','LLL.L.LLLLLLLLLLL.LLLL.LLLLL..LLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLL.L.LLL.LLLLLLL.LLLLLLL','LLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLL.LLLL..LLL.LLLLLL.LLLLLLLL.LLLL.LL.LLLLLLLLLLLLLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLL..LLLLLLL.L.LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LL.LLLLL.LLLLLLL','LLLLL.L.LLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLL.LLLL.LL.LLLLL.LLLLLLL','LLLLL.LLLLLLLLLLLLLL.L.LLLLL.L.LLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL','LLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.LLLLL.LL.L.LLL.LLLLLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLL.','LLLLL.LLLLLLLLLLLL.LLL.LLL.L.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLL..LLLL.LLLLLLLL..LLLLLL','LL.LL..L......L...L.....LL...L......L..L..LL...LL..L.L.....L.L...L...........LL...L.L.L..L.L.L.','LLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLL.LLLL.LLL.LLLL.LLLLLLL','LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLL.L.LLL..L.LLLLL.LLLLLLLLLLLLL.LLLLLLL','LLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLL','LLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLL..LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLL..LLLLLLL.LLLLLLL','LLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLL.LL.LLLL','L....L..L..L...LL.L....L..LL.LL..L....L.L.....LL..........L...L...L..L.L.........L....L..L.....','LLLLL.LLLL.LLLLL.LLLLL..LLLL.LLLLL.LLLLLLLLLLLL.LLLLLLLLLLLL.LLLL.L.LLLLLLLLLL.LLLLLLLLLLL.LLLL','..LLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLL.LLLLLLL','LLL.L.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLL.L.LLLL.LLLLLLLLLLLLLLLL','L.........LL.L..L.L....L.LLLL...L.L.....LLLL.........LL..LL....L...L..L.L...LL..LL...L.L.L..L.L','LLLLL.LLLLLL..LLLLLLLL.LLL.L.LLLLL.LLL.L.LLLLL.L.LL.LLLLLLLL.LLLL.L.LLLLL...LL.LL.LLLLLLLLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLL','LLLLLLLLLL.L.LLLLLLLLL.LLLLL.LLL.L.LLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLL.LL.L.LLLLLLLL.L.LLLLL','LLLLL.LLLLLL.LLLLLLLLLLLLLL..LLLLL.LLLLL.LLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLL.LLLL.LLLL.LLL.LLLLLLL','LLLLLLLLLLL..LLLLLLLLL.LLLLL.LLLLLLLLLLL.L.LLL.LLLL.LLLLLLLL.LLLL.LLLL.LL.LLL.LLLLLLLLLLLLLLLLL','LLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLL.LLLLLLLLL..LLLLLLLL.LLLL.LLLLLLL.LLLL.LLLLLLLL.LLLLLLL','LLLLL.LLLLLL.LLLLLLLLL.LL.LLLLLLLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLL','.LLLL.LLLLLL.LLLLLLLLL.LLLLL.L.LLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LL.L.LLLLLLL','LLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.L.L..LLLLLLLLLLLLLLLL']
# Test data
#data = ['L.LL.LL.LL','LLLLLLL.LL','L.L.L..L..','LLLL.LL.LL','L.LL.LL.LL','L.LLLLL.LL','..L.L.....','LLLLLLLLLL','L.LLLLLL.L','L.LLLLL.LL']


def numEmptySeats(r_, c_, data_):
    numEmpty = 0
    
    if r_ > 0: # Up
       if data_[r_-1][c_] is not '#':
            numEmpty += 1
    else:
        numEmpty += 1

    if r_ < len(data_)-1: # Down
       if data_[r_+1][c_] is not '#':
            numEmpty += 1
    else:
        numEmpty += 1

    if c_ > 0:
       if data_[r_][c_-1] is not '#': # Left
            numEmpty += 1
    else:
        numEmpty += 1

    if c_ < len(data_[0])-1:
       if data_[r_][c_+1] is not '#': # Right
            numEmpty += 1
    else:
        numEmpty += 1

    if r_ > 0 and c_ > 0:
       if data_[r_-1][c_-1] is not '#': # Up-Left
        numEmpty += 1
    else:
        numEmpty += 1

    if r_ < len(data_)-1 and c_ > 0:
       if data_[r_+1][c_-1] is not '#': # Down-Left
            numEmpty += 1
    else:
        numEmpty += 1

    if r_ > 0 and c_ < len(data_[0])-1:
       if data_[r_-1][c_+1] is not '#': # Up-Right
            numEmpty += 1
    else:
        numEmpty += 1

    if r_ < len(data_)-1 and c_ < len(data_[0])-1:
       if data_[r_+1][c_+1] is not '#': # Down-Right
        numEmpty += 1
    else:
        numEmpty += 1

    return numEmpty


def numEmptySeats_v2(r_, c_, data_):
    numEmpty = 0
    
    # Checking up
    oob = True
    for i in range(r_-1, -1, -1):
        if data_[i][c_] is not '.':
            if data_[i][c_] is 'L':
                numEmpty += 1
            oob = False
            break
    if oob:
        numEmpty += 1
    
    # Checking down
    oob = True
    for i in range(r_+1, len(data_)):
        if data_[i][c_] is not '.':
            if data_[i][c_] is 'L':
                numEmpty += 1
            oob = False
            break
    if oob:
        numEmpty += 1
    
    # Checking left
    oob = True
    for i in range(c_-1, -1, -1):
        if data_[r_][i] is not '.':
            if data_[r_][i] is 'L':
                numEmpty += 1
            oob = False
            break
    if oob:
        numEmpty += 1
    
    # Checking right
    oob = True
    for i in range(c_+1, len(data_[r_])):
        if data_[r_][i] is not '.':
            if data_[r_][i] is 'L':
                numEmpty += 1
            oob = False
            break
    if oob:
        numEmpty += 1

    # Checking Up-left
    oob = True
    i = r_ - 1
    j = c_ - 1
    while i > -1 and j > -1:
        if data_[i][j] is not '.':
            if data_[i][j] is 'L':
                numEmpty += 1
            oob = False
            break
        i -= 1
        j -= 1
    if oob:
        numEmpty += 1

    # Checking Up-right
    oob = True
    i = r_ - 1
    j = c_ + 1
    while i > -1 and j < len(data_[0]):
        if data_[i][j] is not '.':
            if data_[i][j] is 'L':
                numEmpty += 1
            oob = False
            break
        i -= 1
        j += 1
    if oob:
        numEmpty += 1

    # Checking Down-left
    oob = True
    i = r_ + 1
    j = c_ - 1
    while i < len(data_) and j > -1:
        if data_[i][j] is not '.':
            if data_[i][j] is 'L':
                numEmpty += 1
            oob = False
            break
        i += 1
        j -= 1
    if oob:
        numEmpty += 1

    # Checking Down-right
    oob = True
    i = r_ + 1
    j = c_ + 1
    while i < len(data_) and j < len(data_[0]):
        if data_[i][j] is not '.':
            if data_[i][j] is 'L':
                numEmpty += 1
            oob = False
            break
        i += 1
        j += 1
    if oob:
        numEmpty += 1

    return numEmpty


def solution1():
    # Creating a copy of the data to modify
    cpy = data.copy()

    while True:
        # Creating a list of coordinates that need to be changed
        changes = []

        # Iterating through each seat
        for r in range(0, len(cpy)):
            for c in range(0, len(cpy[r])):
                # If the seat is empty (L)
                if cpy[r][c] is 'L':
                    numEmpty = 8 - numEmptySeats(r, c, cpy)
                    # If there are no filled seats, this one becomes occupied
                    if numEmpty == 0:
                        changes.append([r,c,'#'])
                # If the seat is occupied (#)
                elif cpy[r][c] is '#':
                    numEmpty = 8 - numEmptySeats(r,c, cpy)
                    # If there are 4 or more occupied seats, it becomes empty
                    if numEmpty >= 4:
                        changes.append([r,c,'L'])
        
        # If there are no changes left, we break the loop
        if len(changes) == 0:
            break
        # Otherwise, once all of the changes have been identified, we changed them all at once
        for i in changes:
            r = i[0]
            c = i[1]
            seat = i[2]
            newStr = cpy[r][:c] + seat + cpy[r][c+1:]
            cpy[r] = newStr

    # Once the seat changing has stablized, we count the number of occupied seats
    occSeats = 0
    for line in cpy:
        for c in line:
            if c is '#':
                occSeats += 1
    return occSeats


def solution2():
    # Creating a copy of the data to modify
    cpy = data.copy()

    while True:
        # Creating a list of coordinates that need to be changed
        changes = []

        # Iterating through each seat
        for r in range(0, len(cpy)):
            for c in range(0, len(cpy[r])):
                # If the seat is empty (L)
                if cpy[r][c] is 'L':
                    numEmpty = 8 - numEmptySeats_v2(r, c, cpy)
                    # If there are no filled seats, this one becomes occupied
                    if numEmpty == 0:
                        changes.append([r,c,'#'])
                # If the seat is occupied (#)
                elif cpy[r][c] is '#':
                    numEmpty = 8 - numEmptySeats_v2(r,c, cpy)
                    # If there are 4 or more occupied seats, it becomes empty
                    if numEmpty >= 5:
                        changes.append([r,c,'L'])
        
        # If there are no changes left, we break the loop
        if len(changes) == 0:
            break
        # Otherwise, once all of the changes have been identified, we changed them all at once
        for i in changes:
            r = i[0]
            c = i[1]
            seat = i[2]
            newStr = cpy[r][:c] + seat + cpy[r][c+1:]
            cpy[r] = newStr

    # Once the seat changing has stablized, we count the number of occupied seats
    occSeats = 0
    for line in cpy:
        for c in line:
            if c is '#':
                occSeats += 1
    return occSeats

    
print("Year 2020, Day 11 solution part 1:", solution1())
print("Year 2020, Day 11 solution part 2:", solution2())

