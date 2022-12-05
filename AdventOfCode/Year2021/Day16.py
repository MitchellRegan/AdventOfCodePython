#https://adventofcode.com/2021/day/16
#https://adventofcode.com/2021/day/16#part2

# Real data
#data = "220D69802BE00A0803711E1441B1006E39C318A12730C200DCE66D2CCE360FA0055652CD32966E3004677EDF600B0803B1361741510076254138D8A00E4FFF3E3393ABE4FC7AC10410010799D2A4430003764DBE281802F3102CA00D4840198430EE0E00021D04E3F41F84AE0154DFDE65A17CCBFAFA14ADA56854FE5E3FD5BCC53B0D2598027A00848C63F2B918C7E513DEC3290051B3867E009CCC5FE46BD520007FE5E8AD344B37583D0803E40085475887144C01A8C10FE2B9803B0720D45A3004652FD8FA05F80122CAF91E5F50E66BEF8AB000BB0F4802039C20917B920B9221200ABF0017B9C92CCDC76BD3A8C4012CCB13CB22CDB243E9C3D2002067440400D9BE62DAC4D2DC0249BF76B6F72BE459B279F759AE7BE42E0058801CC059B08018A0070012CEC045BA01006C03A8000D46C02FA000A8EA007200800E00618018E00410034220061801D36BF178C01796FC52B4017100763547E86000084C7E8910AC0027E9B029FE2F4952F96D81B34C8400C24AA8CDAF4F1E98027C00FACDE3BA86982570D13AA640195CD67B046F004662711E989C468C01F1007A10C4C8320008742287117C401A8C715A3FC2C8EB3777540048272DFE7DE1C0149AC8BC9E79D63200B674013978E8BE5E3A2E9AA3CCDD538C01193CFAB0A146006AA00087C3E88B130401D8E304A239802F39FAC922C0169EA3248DF2D600247C89BCDFE9CA7FFD8BB49686236C9FF9795D80C0139BEC4D6C017978CF78C5EB981FCE7D4D801FA9FB63B14789534584010B5802F3467346D2C1D1E080355B00424FC99290C7E5D729586504803A2D005E677F868C271AA479CEEB131592EE5450043A932697E6A92C6E164991EFC4268F25A294600B5002A3393B31CC834B972804D2F3A4FD72B928E59219C9C771EC3DC89D1802135C9806802729694A6E723FD6134C0129A019E600"
# Test data
#data = "D2FE28"
data = "38006F45291200"


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


def courseOfAction(str, bitsToAnalyze = -1):
    return 0


def parseLiteral(str):
    # String to hold the binary value for the literal
    binary = ''

    while True:
        print(" - -", str)
        # if the first bit of this segment is a 0, that means it's the end of the packet
        if str[0] is '0':
            print(" - - - End of packet. Segment:", str[0] + str[1] + str[2] + str[3] + str[4])
            binary += str[1] + str[2] + str[3] + str[4]
            str = str[5:]
            break
        # If the first bit of this segment is a 1, that means the following 4 bits should be used for the binary literal
        else:
            print(" - - - Leading 1. Segment:", str[0] + str[1] + str[2] + str[3] + str[4])
            binary += str[1] + str[2] + str[3] + str[4]
            str = str[5:]

    # If there's a required length
    print(" - - Binary:", binary, "=", binToDec(binary))


def parseOperator(str):
    #If the first bit of this segment is 0, that means the next 15 bits represent the length of bits in this sub-packet
    if str[0] is '0':
        print(" - - - Leading 0. Determining size of sub-packets using next 15 bits")
        binary = ''.join(str[1:16])
        print(" - - Binary:", binary, "=", binToDec(binary))
        str = str[16:]
    else:
        print(" - - - Leading 1. Determining size of sub-packets using next 11 bits")
        binary = ''.join(str[1:12])
        print(" - - Binary:", binary, "=", binToDec(binary))
        str = str[12:]


def solution1():
    versionSum = 0

    # Converting the string to binary
    str = ""
    for c in data:
        str += hexToBin(c)
    print(str)

    while len(str) > 10:
        # Getting the packet version from the first 3 bits
        version = str[:3]
        versionVal = binToDec(version)
        versionSum += versionVal

        # Getting the packet ID from the next 3 bits
        print(str)
        id = '' + str[3] + str[4] + str[5]
        idVal = binToDec(id)
        str = str[6:]

        print("Version:", version, "=", versionVal)
        print("ID:", id, "=", idVal)
        print("Remainder:", str)

        # If the ID is 4, it's a literal
        if idVal == 4:
            print(" - Literal:")
            parseLiteral(str)
        # Otherwise it's an operator
        else:
            print(" - Operation")
            parseOperator(str)

    return versionSum


def solution2():

    return 0


print("Year 2021, Day 16 solution part 1:", solution1())
print("Year 2021, Day 16 solution part 2:", solution2())