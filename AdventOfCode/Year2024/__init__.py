print("===================== Year 2024 =====================")
while True:
    i = input(" - What day: ")
    
    try:
        if i == '1':
            from Year2024 import Day1
        elif i == '2':
            from Year2024 import Day2
        elif i == '3':
            from Year2024 import Day3
        elif i == '4':
            from Year2024 import Day4
        elif i == '5':
            from Year2024 import Day5
        elif i == '6':
            from Year2024 import Day6
        elif i == '7':
            from Year2024 import Day7
        elif i == '8':
            from Year2024 import Day8
        elif i == '9':
            from Year2024 import Day9
        elif i == '10':
            from Year2024 import Day10
        elif i == '11':
            from Year2024 import Day11
        elif i == '12':
            from Year2024 import Day12
        elif i == '13':
            from Year2024 import Day13
        elif i == '14':
            from Year2024 import Day14
        elif i == '15':
            from Year2024 import Day15
        elif i == '16':
            from Year2024 import Day16
        elif i == '17':
            from Year2024 import Day17
        elif i == '18':
            from Year2024 import Day18
        elif i == '19':
            from Year2024 import Day19
        elif i == '20':
            from Year2024 import Day20
        elif i == '21':
            from Year2024 import Day21
        elif i == '22':
            from Year2024 import Day22
        elif i == '23':
            from Year2024 import Day23
        elif i == '24':
            from Year2024 import Day24
        elif i == '25':
            from Year2024 import Day25
        else:
            print("Done")
            break
    except Exception as e:
        print("Day", i, "has no solution currently. Try again.")
        print("ERROR:", e)