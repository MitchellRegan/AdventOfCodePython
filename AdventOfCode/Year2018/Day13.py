aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    rails = []
    cartState = {}

    with open(inFile, 'r') as f:
        row = 0
        for line in f:
            line = line.replace('\n', '')
            for col in range(0, len(line)):
                if line[col] == '>':
                    cartState[(row,col)] = ['>', 'L']
                elif line[col] == '<':
                    cartState[(row,col)] = ['<', 'L']
                elif line[col] == 'v':
                    cartState[(row,col)] = ['v', 'L']
                elif line[col] == '^':
                    cartState[(row,col)] = ['^', 'L']
            rails.append(line.replace('>', '-').replace('<', '-').replace('v', '|').replace('^', '|'))
            row += 1

    return rails, cartState
            

def solution1():
    rails, cartState = getInput()
    
    #Looping the carts along the rails until a crash happens
    while True:
        if testing:
            testRails = rails[:]
            for cart in cartState.keys():
                r,c = cart
                testRails[r] = testRails[r][:c] + cartState[cart][0] + testRails[r][c+1:]
            for line in testRails:
                print(line)
            print()

        nextState = {}
        #Sorting the carts to move in-turn based on y coord first, then x coord
        cartOrder = [x for x in cartState.keys()]
        cartOrder.sort(key=lambda c: [c[0], c[1]])
        for cart in cartOrder:
            r,c = cart
            direction, turn = cartState[cart]
            
            nextPos = (r,c)
            nextDir = direction
            nextTurn = turn
            
            #If the cart's current position is an intersection '+', we turn
            if rails[r][c] == '+':
                if direction == '>':
                    if turn == 'L': #Left
                        nextPos = (r-1,c)
                        nextDir = '^'
                        nextTurn = 'S'
                    elif turn == 'S': #Straight
                        nextPos = (r,c+1)
                        nextDir = '>'
                        nextTurn = 'R'
                    elif turn == 'R': #Right
                        nextPos = (r+1,c)
                        nextDir = 'v'
                        nextTurn = 'L'
                        
                elif direction == '<':
                    if turn == 'L': #Left
                        nextPos = (r+1,c)
                        nextDir = 'v'
                        nextTurn = 'S'
                    elif turn == 'S': #Straight
                        nextPos = (r,c-1)
                        nextDir = '<'
                        nextTurn = 'R'
                    elif turn == 'R': #Right
                        nextPos = (r-1,c)
                        nextDir = '^'
                        nextTurn = 'L'
                        
                elif direction == 'v':
                    if turn == 'L': #Left
                        nextPos = (r,c+1)
                        nextDir = '>'
                        nextTurn = 'S'
                    elif turn == 'S': #Straight
                        nextPos = (r+1,c)
                        nextDir = 'v'
                        nextTurn = 'R'
                    elif turn == 'R': #Right
                        nextPos = (r,c-1)
                        nextDir = '<'
                        nextTurn = 'L'
                    
                elif direction == '^':
                    if turn == 'L': #Left
                        nextPos = (r,c-1)
                        nextDir = '<'
                        nextTurn = 'S'
                    elif turn == 'S': #Straight
                        nextPos = (r-1,c)
                        nextDir = '^'
                        nextTurn = 'R'
                    elif turn == 'R': #Right
                        nextPos = (r,c+1)
                        nextDir = '>'
                        nextTurn = 'L'
            
            #If the cart hits a turn
            elif rails[r][c] in ['/','\\']:
                if direction == '>':
                    if rails[r][c] == '/':
                        nextPos = (r-1,c)
                        nextDir = '^'
                    else:
                        nextPos = (r+1,c)
                        nextDir = 'v'
                elif direction == '<':
                    if rails[r][c] == '/':
                        nextPos = (r+1,c)
                        nextDir = 'v'
                    else:
                        nextPos = (r-1,c)
                        nextDir = '^'
                elif direction == 'v':
                    if rails[r][c] == '/':
                        nextPos = (r,c-1)
                        nextDir = '<'
                    else:
                        nextPos = (r,c+1)
                        nextDir = '>'
                elif direction == '^':
                    if rails[r][c] == '/':
                        nextPos = (r,c+1)
                        nextDir = '>'
                    else:
                        nextPos = (r,c-1)
                        nextDir = '<'
                    
            #Otherwise it continues in it's given direction
            else:
                if direction == '>':
                    nextPos = (r,c+1)
                elif direction == '<':
                    nextPos = (r,c-1)
                elif direction == 'v':
                    nextPos = (r+1,c)
                elif direction == '^':
                    nextPos = (r-1,c)
                    
            #If the cart crashes into another cart that hasn't taken it's turn yet
            if nextPos in cartState.keys():
                if nextPos[0] > r or (nextPos[0] == r and nextPos[1] > c):
                    testing and print("Collision with cart that hasn't taken their turn")
                    return str(nextPos[1]) + ',' + str(nextPos[0])
            #If this position is already occupied by another cart for the next state, we have our first collision
            elif nextPos in nextState.keys():
                testing and print("Collision with cart that's already moved")
                return str(nextPos[1]) + ',' + str(nextPos[0])
            else:
                nextState[nextPos] = [nextDir, nextTurn]
        
        cartState = nextState
    return


def solution2():
    rails, cartState = getInput()
    
    #Looping the carts along the rails until a crash happens
    while True:
        if testing:
            testRails = rails[:]
            for cart in cartState.keys():
                r,c = cart
                testRails[r] = testRails[r][:c] + cartState[cart][0] + testRails[r][c+1:]
            for line in testRails:
                print(line)
            print()

        nextState = {}
        removedCarts = []
        #Sorting the carts to move in-turn based on y coord first, then x coord
        cartOrder = [x for x in cartState.keys()]
        cartOrder.sort(key=lambda c: [c[0], c[1]])
        for cart in cartOrder:
            #If this cart was run into before it could move, we ignore it's movement
            if cart in removedCarts:
                continue
            #If all other remaining carts have been removed, this cart's position is the final one
            elif len(nextState.keys()) == 0:
                lastCart = True
                for i in range(cartOrder.index(cart)+1, len(cartOrder)):
                    if cartOrder[i] not in removedCarts:
                        lastCart = False
                        break
                if lastCart:
                    testing and print("Last cart remaining hasn't moved yet.")
                    return str(cart[1]) + ',' + str(cart[0])
            r,c = cart
            direction, turn = cartState[cart]
            
            nextPos = (r,c)
            nextDir = direction
            nextTurn = turn
            
            #If the cart's current position is an intersection '+', we turn
            if rails[r][c] == '+':
                if direction == '>':
                    if turn == 'L': #Left
                        nextPos = (r-1,c)
                        nextDir = '^'
                        nextTurn = 'S'
                    elif turn == 'S': #Straight
                        nextPos = (r,c+1)
                        nextDir = '>'
                        nextTurn = 'R'
                    elif turn == 'R': #Right
                        nextPos = (r+1,c)
                        nextDir = 'v'
                        nextTurn = 'L'
                        
                elif direction == '<':
                    if turn == 'L': #Left
                        nextPos = (r+1,c)
                        nextDir = 'v'
                        nextTurn = 'S'
                    elif turn == 'S': #Straight
                        nextPos = (r,c-1)
                        nextDir = '<'
                        nextTurn = 'R'
                    elif turn == 'R': #Right
                        nextPos = (r-1,c)
                        nextDir = '^'
                        nextTurn = 'L'
                        
                elif direction == 'v':
                    if turn == 'L': #Left
                        nextPos = (r,c+1)
                        nextDir = '>'
                        nextTurn = 'S'
                    elif turn == 'S': #Straight
                        nextPos = (r+1,c)
                        nextDir = 'v'
                        nextTurn = 'R'
                    elif turn == 'R': #Right
                        nextPos = (r,c-1)
                        nextDir = '<'
                        nextTurn = 'L'
                    
                elif direction == '^':
                    if turn == 'L': #Left
                        nextPos = (r,c-1)
                        nextDir = '<'
                        nextTurn = 'S'
                    elif turn == 'S': #Straight
                        nextPos = (r-1,c)
                        nextDir = '^'
                        nextTurn = 'R'
                    elif turn == 'R': #Right
                        nextPos = (r,c+1)
                        nextDir = '>'
                        nextTurn = 'L'
            
            #If the cart hits a turn
            elif rails[r][c] in ['/','\\']:
                if direction == '>':
                    if rails[r][c] == '/':
                        nextPos = (r-1,c)
                        nextDir = '^'
                    else:
                        nextPos = (r+1,c)
                        nextDir = 'v'
                elif direction == '<':
                    if rails[r][c] == '/':
                        nextPos = (r+1,c)
                        nextDir = 'v'
                    else:
                        nextPos = (r-1,c)
                        nextDir = '^'
                elif direction == 'v':
                    if rails[r][c] == '/':
                        nextPos = (r,c-1)
                        nextDir = '<'
                    else:
                        nextPos = (r,c+1)
                        nextDir = '>'
                elif direction == '^':
                    if rails[r][c] == '/':
                        nextPos = (r,c+1)
                        nextDir = '>'
                    else:
                        nextPos = (r,c-1)
                        nextDir = '<'
                    
            #Otherwise it continues in it's given direction
            else:
                if direction == '>':
                    nextPos = (r,c+1)
                elif direction == '<':
                    nextPos = (r,c-1)
                elif direction == 'v':
                    nextPos = (r+1,c)
                elif direction == '^':
                    nextPos = (r-1,c)
                    
            #If the cart crashes into another cart that hasn't taken it's turn yet
            if nextPos in cartState.keys():
                if nextPos[0] > r or (nextPos[0] == r and nextPos[1] > c):
                    testing and print("Collision with cart that hasn't taken their turn at", nextPos[1], nextPos[0])
                    #Ignoring this cart's next position and removing the collided cart before it can move
                    removedCarts.append(nextPos)
                    if len(removedCarts) + len(nextState.keys()) == len(cartState.keys())-1:
                        print("======= ONE CART REMAINS")
            #If this position is already occupied by another cart for the next state, we have our first collision
            elif nextPos in nextState.keys():
                testing and print("Collision with cart that's already moved at", nextPos[1], nextPos[0])
                #Ignoring this cart's next position and removing the cart it collided with
                nextState.pop(nextPos)
            else:
                nextState[nextPos] = [nextDir, nextTurn]
        
        cartState = nextState
        if len(cartState.keys()) == 1:
            for k in cartState.keys():
                return str(nextPos[1]) + ',' + str(nextPos[0])
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())
#92,87 incorrect