#https://adventofcode.com/2021/day/16
#https://adventofcode.com/2021/day/16#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = os.path.join(inFileDir, "InputTestFiles/d16_test.txt")
#inFile = os.path.join(inFileDir, "InputRealFiles/d16_real.txt")


def getInput():
    inputStrings = []
    with open(inFile, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            inputStrings.append(line)

    return inputStrings


def hexToBin(c_):
    '''Utility function to convert a hexadecimal character to it's binary string value.
    '''
    c_ = c_.lower()

    if c_ == '0':
        return "0000"
    elif c_ == '1':
        return "0001"
    elif c_ == '2':
        return "0010"
    elif c_ == '3':
        return "0011"
    elif c_ == '4':
        return "0100"
    elif c_ == '5':
        return "0101"
    elif c_ == '6':
        return "0110"
    elif c_ == '7':
        return "0111"
    elif c_ == '8':
        return "1000"
    elif c_ == '9':
        return "1001"
    elif c_ == 'a':
        return "1010"
    elif c_ == 'b':
        return "1011"
    elif c_ == 'c':
        return "1100"
    elif c_ == 'd':
        return "1101"
    elif c_ == 'e':
        return "1110"
    elif c_ == 'f':
        return "1111"
    else:
        return "----"


def binToDec(b_):
    '''Utility function to convert a binary value into it's decimal value.
    '''
    val = 0

    exp = 0
    for c in range(len(b_)-1, -1, -1):
        if b_[c] == '1':
            val += 2**exp
        exp += 1

    return val


def packetParser1(pkt_, debug_=False):
    '''Recursive function to find the version sum of the given packet and all sub-packets it may contain.
    returns: Int for the sum of all packet/sub-packet version numbers.
    '''
    versionSum = 0
    #If the packet has a length less than 11, we can't do anything with it
    while len(pkt_) > 10:
        # Getting the packet version from the first 3 bits
        version = pkt_[:3]
        versionVal = binToDec(version)
        versionSum += versionVal

        # Getting the packet ID from the next 3 bits
        id = '' + pkt_[3] + pkt_[4] + pkt_[5]
        idVal = binToDec(id)
        pkt_ = pkt_[6:]
        
        if debug_:
            print("-------------------------------------------------")
            print(pkt_)
            print("VVVTTT")
            print("Version:", version, "=", versionVal)
            print("Type ID:", id, "=", idVal)
            print("Remainder:", pkt_)

        # If the ID is 4, it's a literal
        if idVal == 4:
            if debug_:
                print("\tLiteral:")
            # String to hold the binary value for the literal
            binary = ''

            while True:
                if debug_:
                    print("\t\t -", pkt_)
                # if the first bit of this segment is a 0, that means it's the end of the packet
                if pkt_[0] is '0':
                    if debug_:
                        print("\t\t - - End of packet. Segment:", pkt_[0] + pkt_[1] + pkt_[2] + pkt_[3] + pkt_[4])
                    binary += pkt_[1] + pkt_[2] + pkt_[3] + pkt_[4]
                    pkt_ = pkt_[5:]
                    break
                # If the first bit of this segment is a 1, that means the following 4 bits should be used for the binary literal
                else:
                    if debug_:
                        print("\t\t - - Leading 1. Segment:", pkt_[0] + pkt_[1] + pkt_[2] + pkt_[3] + pkt_[4])
                    binary += pkt_[1] + pkt_[2] + pkt_[3] + pkt_[4]
                    pkt_ = pkt_[5:]

            # If there's a required length
            if debug_:
                print("\t\t - Binary:", binary, "=", binToDec(binary))
        # Otherwise it's an operator
        else:
            if debug_:
                print("\tOperation")
            #If the first bit of this segment is 0, that means the next 15 bits represent the length of bits in this sub-packet
            if pkt_[0] is '0':
                binary = ''.join(pkt_[1:16])
                binVal = binToDec(binary)
                if debug_:
                    print(" - - - Leading 0. Determining size of sub-packets using next 15 bits")
                    print(" - - Binary:", binary, "=", binVal)
                pkt_ = pkt_[16:]
                versionSum += packetParser1(pkt_[:binVal], debug_)
                pkt_ = pkt_[binVal:]
            else:
                binary = ''.join(pkt_[1:12])
                binVal = binToDec(binary)
                if debug_:
                    print(" - - - Leading 1. Determining number of sub-packets using next 11 bits")
                    print(" - - Binary:", binary, "=", binVal)
                pkt_ = pkt_[12:]

    return versionSum


def packetParser2(pkt_, debug_=False):
    '''Recursive function to find the plain-text values of the given packet and all sub-packets it may contain.
    returns: List of all plain-text values in the given packet.
    '''
    #List for values to return
    values = []
    #List to keep track of how many packets are within a given set of parentheses
    parenCount = []

    #If the packet has a length less than 11, we can't do anything with it
    while len(pkt_) > 10:
        # Getting the packet version from the first 3 bits
        version = pkt_[:3]
        versionVal = binToDec(version)

        # Getting the packet ID from the next 3 bits
        id = '' + pkt_[3] + pkt_[4] + pkt_[5]
        idVal = binToDec(id)
        pkt_ = pkt_[6:]
        
        if debug_:
            print("-------------------------------------------------")
            print(pkt_)
            print("VVVTTT")
            print("Version:", version, "=", versionVal)
            print("Type ID:", id, "=", idVal)
            print("Remainder:", pkt_)

        #Depending on the ID value, we indicate an operation (except for ID 4 which is just a literal number)
        if idVal != 4:
            opCodes = ["+", "x", "min", "max", "#", ">", "<", "="]
            values.append(opCodes[idVal])

        # If the ID is 4, it's a literal
        if idVal == 4:
            if debug_:
                print("\tLiteral:")
            # String to hold the binary value for the literal
            binary = ''

            while True:
                if debug_:
                    print("\t\t -", pkt_)
                # if the first bit of this segment is a 0, that means it's the end of the packet
                if pkt_[0] is '0':
                    if debug_:
                        print("\t\t - - End of packet. Segment:", pkt_[0] + pkt_[1] + pkt_[2] + pkt_[3] + pkt_[4])
                    binary += pkt_[1] + pkt_[2] + pkt_[3] + pkt_[4]
                    pkt_ = pkt_[5:]
                    break
                # If the first bit of this segment is a 1, that means the following 4 bits should be used for the binary literal
                else:
                    if debug_:
                        print("\t\t - - Leading 1. Segment:", pkt_[0] + pkt_[1] + pkt_[2] + pkt_[3] + pkt_[4])
                    binary += pkt_[1] + pkt_[2] + pkt_[3] + pkt_[4]
                    pkt_ = pkt_[5:]

            # If there's a required length
            if debug_:
                print("\t\t - Binary:", binary, "=", binToDec(binary))
            values.append(binToDec(binary))
        # Otherwise it's an operator
        else:
            if debug_:
                print("\tOperation")
            #If the first bit of this segment is 0, that means the next 15 bits represent the length of bits in this sub-packet
            if pkt_[0] is '0':
                binary = ''.join(pkt_[1:16])
                binVal = binToDec(binary)
                if debug_:
                    print(" - - - Leading 0. Determining size of sub-packets using next 15 bits")
                    print(" - - Binary:", binary, "=", binVal)
                pkt_ = pkt_[16:]
                values.append("(")
                values.extend(packetParser2(pkt_[:binVal], debug_))
                values.append(")")
                pkt_ = pkt_[binVal:]
            else:
                binary = ''.join(pkt_[1:12])
                binVal = binToDec(binary)
                if debug_:
                    print(" - - - Leading 1. Determining number of sub-packets using next 11 bits")
                    print(" - - Binary:", binary, "=", binVal)
                values.append("(")
                parenCount.append(binVal+1)
                pkt_ = pkt_[12:]

        #Once we're done with the current packet, we check if there are any closing parentheses to add
        if len(parenCount) > 0:
            p = 0
            while p < len(parenCount):
                parenCount[p] -= 1
                if parenCount[p] == 0:
                    values.append(")")
                    parenCount.pop(p)
                else:
                    p += 1

    return values


def stackPreFixSolver(stack_):
    '''Function to find the single numerical result from a given stack in pre-fix notation.
    '''
    i = 0
    while i < len(stack_) and len(stack_) > 0:
        if stack_[i] == '+':
            #If the next 2 items in the stack are numbers, we can safely add them
            if isinstance(stack_[i+1], int) and isinstance(stack_[i+2], int):
                print("\tAdding", stack_[i+1], "and", stack_[i+2])
                stack_[i] = stack_[i+1] + stack_[i+2]
                stack_.pop(i+1)
                stack_.pop(i+1)
                i -= 2
                print("\t\t", stack_)
        elif stack_[i] == 'x':
            #If the next 2 items in the stack are numbers, we can safely multiply them
            if isinstance(stack_[i+1], int) and isinstance(stack_[i+2], int):
                stack_[i] = stack_[i+1] * stack_[i+2]
                stack_.pop(i+1)
                stack_.pop(i+1)
                i -= 2
                print("\t\t", stack_)
        elif stack_[i] == 'min':
            #Making sure we have at least one int value to take the minimum of
            if isinstance(stack_[i+1], int):
                #Looping through the remaining values of the list until we go out of bounds or hit a non-int value
                j = i + 1
                while j < len(stack_) and isinstance(stack_[j], int):
                    j += 1
                stack_[i] = min(stack_[i+1:j])
                print("\tMinimum of", stack_[i+1:j])
                while j > i+1:
                    stack_.pop(i+1)
                    j -= 1
                i -= 2
                print("\t\t", stack_)
        elif stack_[i] == 'max':
            #Making sure we have at least one int value to take the minimum of
            if isinstance(stack_[i+1], int):
                #Looping through the remaining values of the list until we go out of bounds or hit a non-int value
                j = i + 1
                while j < len(stack_) and isinstance(stack_[j], int):
                    j += 1
                stack_[i] = max(stack_[i+1:j])
                print("\Maximum of", stack_[i+1:j])
                while j > i+1:
                    stack_.pop(i+1)
                    j -= 1
                i -= 2
                print("\t\t", stack_)
        elif stack_[i] == '>':
            #If the next 2 items in the stack are numbers, we can safely check if the left value is larger
            if isinstance(stack_[i+1], int) and isinstance(stack_[i+2], int):
                if stack_[i+1] > stack_[i+2]:
                    stack_[i] = 1
                else:
                    stack_[i] = 0
                print("\t", stack_[i+1], "larger than", stack_[i+2])
                stack_.pop(i+1)
                stack_.pop(i+1)
                i -= 2
                print("\t\t", stack_)
        elif stack_[i] == '<':
            #If the next 2 items in the stack are numbers, we can safely check if the left value is smaller
            if isinstance(stack_[i+1], int) and isinstance(stack_[i+2], int):
                if stack_[i+1] < stack_[i+2]:
                    stack_[i] = 1
                else:
                    stack_[i] = 0
                print("\t", stack_[i+1], "smaller than", stack_[i+2])
                stack_.pop(i+1)
                stack_.pop(i+1)
                i -= 2
                print("\t\t", stack_)
        elif stack_[i] == '=':
            #If the next 2 items in the stack are numbers, we can safely check if they're equal
            if isinstance(stack_[i+1], int) and isinstance(stack_[i+2], int):
                if stack_[i+1] == stack_[i+2]:
                    stack_[i] = 1
                else:
                    stack_[i] = 0
                print("\t", stack_[i+1], "equal to", stack_[i+2])
                stack_.pop(i+1)
                stack_.pop(i+1)
                i -= 2
                print("\t\t", stack_)

        #Incrementing the index by 1
        i += 1
        if i >= len(stack_) and len(stack_) > 1:
            i = 0
    #Returning the last remaining value as the numerical result
    return stack_[0]


def solution1():
    inputStr = getInput()

    for x in inputStr:
        # Converting the string to binary
        str = ""
        for c in x:
            str += hexToBin(c)

        #Using the recursive packet parser function to find the sum of all version numbers
        return packetParser1(str)


def solution2():
    inputStr = getInput()

    for x in inputStr:
        # Converting the string to binary
        str = ""
        for c in x:
            str += hexToBin(c)

        #Using the recursive packet parser function to find the list of values and operators given from the input
        print(x)
        stack = packetParser2(str, False)
        print("\t", stack)
        print("\t =", stackPreFixSolver(stack))


print("Year 2021, Day 16 solution part 1:", solution1())
print("Year 2021, Day 16 solution part 2:", solution2())