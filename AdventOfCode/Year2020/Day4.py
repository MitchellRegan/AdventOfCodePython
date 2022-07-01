#https://adventofcode.com/2020/day/4
#https://adventofcode.com/2020/day/4#part2


def checkPassport(ps_):
    delStr = ps_.split(' ')
    ecl = False
    pid = False
    eyr = False
    hcl = False
    byr = False
    iyr = False
    hgt = False

    for p in delStr:
        entry = p[:3]

        if entry == "ecl":
            ecl = True
        elif entry == "pid":
            pid = True
        elif entry == "eyr":
            eyr = True
        elif entry == "hcl":
            hcl = True
        elif entry == "byr":
            byr = True
        elif entry == "iyr":
            iyr = True
        elif entry == "hgt":
            hgt = True

    return (ecl and pid and eyr and hcl and byr and iyr and hgt)


def checkPassport2(ps_):
    ps_ = ps_.replace('\n', ' ')
    delStr = ps_.split(' ')
    ecl = False
    pid = False
    eyr = False
    hcl = False
    byr = False
    iyr = False
    hgt = False

    for p in delStr:
        entry = p[:3]
        data = p[4:]

        if entry == "ecl":
            if data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                ecl = True
        elif entry == "pid":
            if len(data) == 9:
                try:
                    pidNum = int(data)
                    pid = True
                except:
                    pid = False
        elif entry == "eyr":
            try:
                year = int(data)
                if year >= 2020 and year <= 2030:
                    eyr = True
            except:
                eyr = False
        elif entry == "hcl":
            if len(data) == 7:
                hcl = True
                hex = "0123456789abcdefABCDEF"
                for c in range(1, len(data)):
                    if hex.count(data[c]) < 1:
                        hcl = False
                        break
        elif entry == "byr":
            try:
                year = int(data)
                if year >= 1920 and year <= 2002:
                    byr = True
            except:
                byr = False
        elif entry == "iyr":
            try:
                year = int(data)
                if year >= 2010 and year <= 2020:
                    iyr = True
            except:
                iyr = False
        elif entry == "hgt":
            type = data[len(data)-2:]
            try:
                height = int(data[:len(data)-2])
                if type == "cm":
                    if height >= 150 and height <= 193:
                        hgt = True
                elif type == "in":
                    if height >= 59 and height <= 76:
                        hgt = True
            except:
                hgt = False

    return (ecl and pid and eyr and hcl and byr and iyr and hgt)


def solution1():
    file = open(".\\Year2020\\dataFiles\\day4_Input.txt", "r")
    #file = open(".\\Year2020\\dataFiles\\day4_Input_Test.txt", "r")

    valid = 0
    passport = ""
    for line in file:
        if line == "\n":
            if checkPassport(passport):
                valid += 1
            passport = ""
        else:
            passport += line[:len(line)-1] + " "

    if passport != "":
        if checkPassport(passport):
            valid += 1

    file.close()
    return valid


def solution2():
    file = open(".\\Year2020\\dataFiles\\day4_Input.txt", "r")
    #file = open(".\\Year2020\\dataFiles\\day4_Input_Test.txt", "r")

    valid = 0
    passport = ""
    for line in file:
        if line == "\n":
            if checkPassport2(passport):
                valid += 1
            passport = ""
        else:
            passport += line

    if passport != "":
        if checkPassport2(passport):
            valid += 1

    file.close()
    return valid

    
print("Year 2020, Day 4 solution part 1:", solution1())
print("Year 2020, Day 4 solution part 2:", solution2())

