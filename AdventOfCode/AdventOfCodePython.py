import os

def main():
    print(" Advent of Code Solutions")
    y = input(" - Select a year or press enter to run tests: ")

    if y == '2015':
        import Year2015
    elif y == '2016':
        import Year2016
    elif y == '2017':
        import Year2017
    elif y == '2018':
        import Year2018
    elif y == '2019':
        import Year2019
    elif y == '2020':
        import Year2020
    elif y == '2021':
        import Year2021
    elif y == '2022':
        import Year2022
    elif y == '2023':
        import Year2023
    elif y == '0':
        createNewYear()
    else:
        from HelperFunctions import testing


def createNewYear():
    print("\tSet-up for creating a new AoC year folder")

    year = ''
    while True:
        year = int(input("\t\tEnter the year to set up a project for: "))
        if year < 2015 or year > 2030:
            print("\t\t=== INVALID YEAR ===")
        else:
            print("You entered year", year, "  Is this correct? [Y]: ", end='')
            sure = input()
            if sure is not 'y' and sure is not 'Y':
                print("Validation not given. Closing program...")
                return
            break

    folderName = os.path.join(os.path.dirname(__file__), "Year" + str(year))
    realFolder = os.path.join(folderName, "InputRealFiles")
    testFolder = os.path.join(folderName, "InputTestFiles")

    print("Creating folder at path", folderName)
    if not os.path.exists(folderName):
        os.mkdir(folderName)

    if not os.path.exists(realFolder):
        print("\tCreating real input file folder...")
        os.mkdir(realFolder)
    else:
        print("\tInputRealFiles already exists")

    if not os.path.exists(testFolder):
        print("\tCreating test input file folder...")
        os.mkdir(testFolder)
    else:
        print("\tInputTestFiles already exists")

    if not os.path.exists(os.path.join(folderName, "__init__.py")):
        print("\tCreating __init__.py...")
        #open(os.path.join(folderName, "__init__.py"), 'a').close()
    else:
        print("\t__init__.py already exists")


    print("COMPLETE! Don't forget to go to the solution explorer and add the new folder to the project.")


main()