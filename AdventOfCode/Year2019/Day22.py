#https://adventofcode.com/2019/day/22
#https://adventofcode.com/2019/day/22#part2

import os
import itertools
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 0

deckSize = 0
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d22_test.txt")
    deckSize = 10
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d22_real.txt")
    deckSize = 10007


def getInput():
    instructions = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            
            #Replacing the 'cut', 'new', and 'deal' instructions with enums 0, 1, 2 for slightly faster checking
            if line[0] == 'cut':
                instructions.append((0, int(line[1])))
            elif line[0] == 'deal' and line[1] == 'into':
                instructions.append((1, 0))
            else:
                instructions.append((2, int(line[3])))

    return instructions
            

def shuffleDeck(instructions_:list, deck_:list)->list:
    cards = [x for x in deck_]
    
    for i in instructions_:
        #Dealing to new deck just reverses the current deck's order
        if i[0] == 1:
            cards.reverse()
            
        #Cutting 'n' takes n-cards from the top of the deck and puts them on the bottom
        elif i[0] == 0:
            if i[1] >= 0:
                cards.extend(cards[0 : i[1]])
                cards = cards[i[1] :]
            else:
                cutLen = len(cards) + i[1]
                cards.extend(cards[0 : cutLen])
                cards = cards[cutLen :]
            
        #Dealing 'n'
        elif i[0] == 2:
            newDeck = [-1 for x in cards]
            ptr = 0
            
            while len(cards) > 0:
                if ptr >= len(newDeck):
                    ptr -= len(newDeck)
                else:
                    if newDeck[ptr] == -1:
                        newDeck[ptr] = cards.pop(0)
                    else:
                        #Putting the new card in front of the card that was there previously, and then removing the next empty (-1) slot
                        newDeck.insert(cards.pop(0), ptr)
                        removeSlot = -1
                        for slot in range(ptr+2, len(newDeck)):
                            if newDeck[slot] == -1:
                                removeSlot = slot
                                break
                        if removeSlot == -1:
                            for slot in range(ptr-1, -1, -1):
                                if newDeck[slot] == -1:
                                    removeSlot = slot
                                    break
                        if removeSlot == -1:
                            print("ERROR: No empty slot found after inserting card at index", ptr)
                            return None
                        else:
                            newDeck.pop(removeSlot)
                    ptr += i[1]
                    
            cards = newDeck
            
    return cards


def solution1():
    instructions = getInput()
    deck = [x for x in range(deckSize)]
    
    testing and print(deck, "        INITIAL STATE")
    
    deck = shuffleDeck(instructions, deck)
    
    testing and print("\nFinal Deck Configuration:\n", deck)
    return deck.index(2019)


def solution2():
    instructions = getInput()
    
    #Deck size is [0, 119315717514047)
    #Shuffle it 101741582076661 times
    
    
    #Run tests to see how long it takes for different sizes of decks to end back up in their starting state
    for size in range(10007, 10010):
        deck = [x for x in range(size)]
        valAt2020 = deck[2020]
        statesFound = {2020:valAt2020}
        print("Initial value at index 2020:", deck[2020])

        #Looping until an identical state is found
        numShuffles = 1
        while True:
            #print(deck, "     shuffle", numShuffles)
            deck = shuffleDeck(instructions, deck)
            newIndex = deck.index(valAt2020)
            
            if newIndex in statesFound.keys():
                print("Deck size", size, "loops after", numShuffles, "shuffles\n\t", newIndex)
                break
            else:
                statesFound[newIndex] = valAt2020
                numShuffles += 1
                print(newIndex)
    return


print("Year 2019, Day 22 solution part 1:", solution1())
print("Year 2019, Day 22 solution part 2:", solution2())