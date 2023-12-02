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
elif y == 'wordle':
    from HelperFunctions import wordle
    wordle.solver()
else:
    from HelperFunctions import testing