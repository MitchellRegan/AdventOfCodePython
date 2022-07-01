#https://adventofcode.com/2021/day/14
#https://adventofcode.com/2021/day/14#part2

start = "VCOPVNKPFOOVPVSBKCOF"
data = {'NO':'K','PO':'B','HS':'B','FP':'V','KN':'S','HV':'S','KC':'S','CS':'B','KB':'V','OB':'V','HN':'S','OK':'N','PC':'H','OO':'P','HF':'S','CB':'C','SB':'V','FN':'B','PH':'K','KH':'P','NB':'F','KF':'P','FK':'N','FB':'P','FO':'H','CV':'V','CN':'P','BN':'N','SC':'N','PB':'K','VS':'N','BP':'P','CK':'O','PS':'N','PF':'H','HB':'S','VN':'V','OS':'V','OC':'O','BB':'F','SK':'S','NF':'F','FS':'S','SN':'N','FC':'S','BH':'N','HP':'C','VK':'F','CC':'N','SV':'H','SO':'F','HH':'C','PK':'P','NV':'B','KS':'H','NP':'H','VO':'C','BK':'V','VV':'P','HK':'B','CF':'B','BF':'O','OV':'B','OH':'C','PP':'S','SP':'S','CH':'B','OF':'F','NK':'F','FV':'F','KP':'O','OP':'O','SS':'P','CP':'H','BO':'O','KK':'F','HC':'N','KO':'V','CO':'F','NC':'P','ON':'P','KV':'C','BV':'K','HO':'F','PV':'H','VC':'O','NH':'B','PN':'H','VP':'O','NS':'N','NN':'S','BS':'H','SH':'P','VB':'V','VH':'O','FH':'K','FF':'H','SF':'N','BC':'H','VF':'P'}
#start = "NNCB"
#data = {'CH':'B','HH':'N','CB':'H','NH':'C','HB':'C','HC':'B','HN':'C','NN':'C','BH':'H','NC':'B','NB':'B','BN':'B','BB':'N','BC':'B','CC':'N','CN':'C'}


def solution(iterations_):
    # Breaking down the initial polymer into each pair and storing the pair values in a dictionary
    pairs = {}
    for p in range(0, len(start)-1):
        chemPair = '' + start[p] + start[p+1]
        if chemPair not in pairs.keys():
            pairs[chemPair] = 1
        else:
            pairs[chemPair] += 1

    # Counting up all of the chars in the original string
    charCount = {}
    for c in start:
        # Adding the count for the left char
        if c not in charCount.keys():
            charCount[c] = 1
        else:
            charCount[c] += 1

    # Looping as many times as we're given
    for t in range(0, iterations_):
        # Creating a dictionary of each pair to add at the end of this loop
        loopPairs = {}

        # Looping through each existing pair in the pairs dictionary to find which new ones to add
        for k in pairs.keys():
            if k in data.keys():
                p1 = '' + k[0] + data[k]
                if p1 not in loopPairs:
                    loopPairs[p1] = pairs[k]
                else:
                    loopPairs[p1] += pairs[k]

                p2 = '' + data[k] + k[1]
                if p2 not in loopPairs:
                    loopPairs[p2] = pairs[k]
                else:
                    loopPairs[p2] += pairs[k]

                # Keeping track of the char count for the added char
                if data[k] not in charCount.keys():
                    charCount[data[k]] = pairs[k]
                else:
                    charCount[data[k]] += pairs[k]

                # Removing all of the pairs of type k from the pairs dictionary
                pairs[k] = 0

        # Now that we have all of the new pairs, we can add them into the keys dictionary
        for lp in loopPairs.keys():
            if lp not in pairs.keys():
                pairs[lp] = loopPairs[lp]
            else:
                pairs[lp] += loopPairs[lp]

    # Finding the difference between the most common element and the least common element
    return max(charCount.values()) - min(charCount.values())


print("Year 2021, Day 14 solution part 1:", solution(10))
print("Year 2021, Day 14 solution part 2:", solution(40))
