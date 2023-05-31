#https://adventofcode.com/2021/day/16
#https://adventofcode.com/2021/day/16#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d16_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d16_real.txt")


def getInput():
    inputString = ""
    with open(inFile, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            inputString = line
            break
    return inputString


def hexToBin(c_):
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


def solution1():
    inputStr = getInput()
    #print("Input string:", inputStr)

    # Converting the string to binary
    str = ""
    for c in inputStr:
        str += hexToBin(c)
    #print("Input to binary:", str)

    #Using the recursive packet parser function to find the sum of all version numbers
    return packetParser1(str)


def solution2():

    return 0


print("Year 2021, Day 16 solution part 1:", solution1())
print("Year 2021, Day 16 solution part 2:", solution2())