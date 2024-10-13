aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    dists = {}#Key = (min(city1, city2), max(city1, city2)), Value = distance int
    cities = {}#Key = city name, Value = [list of connected cities]

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            c1 = line[0]
            c2 = line[2]
            d = int(line[-1])
            
            if c1 not in cities.keys():
                cities[c1] = [c2]
            else:
                cities[c1].append(c2)
            if c2 not in cities.keys():
                cities[c2] = [c1]
            else:
                cities[c2].append(c1)
                
            dists[(min(c1,c2), max(c1,c2))] = d

    return cities,dists
            

def solution1():
    cities,dists = getInput()
    
    if testing:
        print("Cities:")
        for c in cities.keys():
            print("\t", c, ":", cities[c])
        print("Distances:")
        for d in dists.keys():
            print("\t", d, ":", dists[d])
            
    def getTotalDist(seen_:list)->int:
        testing and print(seen_)
        #If we've seen every city, we get the total travel distance in the order traveled
        if len(seen_) == len(cities.keys()):
            d = 0
            for i in range(len(seen_)-1):
                d += dists[(min(seen_[i], seen_[i+1]), max(seen_[i], seen_[i+1]))]
            testing and print("\tTotal Distance:", d)
            return d
        
        #Otherwise we get the next location
        best = None
        for n in [c for c in cities.keys() if c not in seen_]:
            newSeen = [x for x in seen_]
            newSeen.append(n)
            d = getTotalDist(newSeen)
            if best is None or d < best:
                best = d
        return best

    ans = None
    for c in cities.keys():
        d = getTotalDist([c])
        testing and print("====================================== Found distance:", d, "    Current answer:", ans)
        if ans is None or d < ans:
            ans = d
            testing and print("---------------------------- New final answer:", ans)

    return ans


def solution2():
    cities,dists = getInput()
    
    def getTotalDist(seen_:list)->int:
        #If we've seen every city, we get the total travel distance in the order traveled
        if len(seen_) == len(cities.keys()):
            d = 0
            for i in range(len(seen_)-1):
                d += dists[(min(seen_[i], seen_[i+1]), max(seen_[i], seen_[i+1]))]
            return d
        
        #Otherwise we get the next location
        best = 0
        for n in [c for c in cities.keys() if c not in seen_]:
            newSeen = [x for x in seen_]
            newSeen.append(n)
            d = getTotalDist(newSeen)
            best = max(best, d)
        return best

    ans = 0
    for c in cities.keys():
        d = getTotalDist([c])
        ans = max(ans, d)

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())