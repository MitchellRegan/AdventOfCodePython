aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


class GameChar:
    def __init__(self, name_:str, hp_:int, dmg_:int, arm_:int):
        '''Initializes a game character with health, damage (attack power), and armor values.'''
        self.name = name_
        self.hp = hp_
        self.damage = dmg_
        self.armor = arm_
        
    def takeDamage(self, incommingDmg_:int)->bool:
        '''Applies incomming damage to this character. Returns True if still alive, and False if dead.'''
        totalDmg = incommingDmg_ - self.armor
        if totalDmg < 1:
            totalDmg = 1
        self.hp -= totalDmg
        testing and print("\t", self.name, "attacked for", incommingDmg_, "-", self.armor, "=", totalDmg, "    HP:", self.hp)
            
        return (self.hp > 0)
    

class Item:
    def __init__(self, name_:str, c_:int, d_:int, a_:int):
        '''Initializes this item with cost, damage boost, and armor boost values.'''
        self.name = name_
        self.cost = c_
        self.damage = d_
        self.armor = a_


def getInput():
    player = [100, 0, 0]
    boss = None

    with open(inFile, 'r') as f:
        bhp = None
        bdm = None
        bar = None
        for line in f:
            line = line.replace('\n', '').split(' ')
            if bhp is None:
                bhp = int(line[-1])
            elif bdm is None:
                bdm = int(line[-1])
            else:
                bar = int(line[-1])
        boss = [bhp, bdm, bar]

    return player, boss
            

def solution1():
    playerStats, bossStats = getInput()
    if testing:
        playerStats[0] = 8
        
    weapons = [
            Item("Dagger", 8, 4, 0),
            Item("Shortsword", 10, 5, 0),
            Item("Warhammer", 25, 6, 0),
            Item("Longsword", 40, 7, 0),
            Item("Greataxe", 74, 8, 0)
        ]
    armor = [
            Item("Leather", 13, 0, 1),
            Item("Chainmail", 31, 0, 2),
            Item("Splintmail", 53, 0, 3),
            Item("Bandedmail", 75, 0, 4),
            Item("Platemail", 102, 0, 5)
        ]
    rings = [
            Item("Damage +1", 25, 1, 0),
            Item("Damage +2", 50, 2, 0),
            Item("Damage +3", 100, 3, 0),
            Item("Defense +1", 20, 0, 1),
            Item("Defense +2", 40, 0, 2),
            Item("Defense +3", 80, 0, 3)
        ]
    
    def runCombat(p_:GameChar, b_:GameChar)->bool:
        '''Simulates combat between the given player and the boss. Returns True if player wins.'''
        while p_.hp > 0:
            b_.takeDamage(p_.damage)
            if b_.hp < 1:
                testing and print("\t\tPLAYER WINS!")
                return True
            p_.takeDamage(b_.damage)
            
        testing and print("\t\tPLAYER LOSES")
        return False

    
    def buyStuff(w_=None, a_=None, r1_=None, r2_=None):
        '''Recursive function to buy (or ignore) one item from each slot. After all items have been purchased,
        combat is run between the player and the boss. If the player wins, the gold cost of all items is returned.
        All parameters are index values for their respective item categories.'''
        leastGold = 999999
        #Buying a weapon (mandatory)
        if w_ is None:
            for i in range(len(weapons)):
                leastGold = min(leastGold, buyStuff(i))
            return leastGold
        #Buying at most 1 piece of armor
        if a_ is None:
            for i in range(-1, len(armor)):
                leastGold = min(leastGold, buyStuff(w_, i))
            return leastGold
        #Buying at most 1 ring for the first ring slot
        if r1_ is None:
            for i in range(-1, len(rings)):
                leastGold = min(leastGold, buyStuff(w_, a_, i))
            return leastGold
        #Buying at most 1 ring for the second ring slot if it's not the same as ring 1
        if r2_ is None:
            for i in range(-1, len(rings)):
                if i != r1_:
                    leastGold = min(leastGold, buyStuff(w_, a_, r1_, i))
            return leastGold
        
        #If all items have been chosen, we create the player and boss to initiate combat
        player = GameChar("Player", playerStats[0], playerStats[1] + weapons[w_].damage, playerStats[2])
        boss = GameChar("Boss", bossStats[0], bossStats[1], bossStats[2])
        gold = weapons[w_].cost
        testing and print("\tWeapon:", weapons[w_].name)
        if a_ != -1:
            testing and print("\tArmor:", armor[a_].name)
            player.armor += armor[a_].armor
            gold += armor[a_].cost
        if r1_ != -1:
            testing and print("\tRing 1:", rings[r1_].name)
            player.armor += rings[r1_].armor
            player.damage += rings[r1_].damage
            gold += rings[r1_].cost
        if r2_ != -1:
            testing and print("\tRing 2:", rings[r2_].name)
            player.armor += rings[r2_].armor
            player.damage += rings[r2_].damage
            gold += rings[r2_].cost
            
        if runCombat(player, boss):
            testing and print("\t\tGold used:", gold)
            return gold
        return leastGold
        

    return buyStuff()


def solution2():
    playerStats, bossStats = getInput()
        
    weapons = [
            Item("Dagger", 8, 4, 0),
            Item("Shortsword", 10, 5, 0),
            Item("Warhammer", 25, 6, 0),
            Item("Longsword", 40, 7, 0),
            Item("Greataxe", 74, 8, 0)
        ]
    armor = [
            Item("Leather", 13, 0, 1),
            Item("Chainmail", 31, 0, 2),
            Item("Splintmail", 53, 0, 3),
            Item("Bandedmail", 75, 0, 4),
            Item("Platemail", 102, 0, 5)
        ]
    rings = [
            Item("Damage +1", 25, 1, 0),
            Item("Damage +2", 50, 2, 0),
            Item("Damage +3", 100, 3, 0),
            Item("Defense +1", 20, 0, 1),
            Item("Defense +2", 40, 0, 2),
            Item("Defense +3", 80, 0, 3)
        ]
    
    def runCombat(p_:GameChar, b_:GameChar)->bool:
        '''Simulates combat between the given player and the boss. Returns True if player wins.'''
        while p_.hp > 0:
            b_.takeDamage(p_.damage)
            if b_.hp < 1:
                return True
            p_.takeDamage(b_.damage)
            
        return False

    
    def buyStuff(w_=None, a_=None, r1_=None, r2_=None):
        '''Recursive function to buy (or ignore) one item from each slot. After all items have been purchased,
        combat is run between the player and the boss. If the player wins, the gold cost of all items is returned.
        All parameters are index values for their respective item categories.'''
        leastGold = 0
        #Buying a weapon (mandatory)
        if w_ is None:
            for i in range(len(weapons)):
                leastGold = max(leastGold, buyStuff(i))
            return leastGold
        #Buying at most 1 piece of armor
        if a_ is None:
            for i in range(-1, len(armor)):
                leastGold = max(leastGold, buyStuff(w_, i))
            return leastGold
        #Buying at most 1 ring for the first ring slot
        if r1_ is None:
            for i in range(-1, len(rings)):
                leastGold = max(leastGold, buyStuff(w_, a_, i))
            return leastGold
        #Buying at most 1 ring for the second ring slot if it's not the same as ring 1
        if r2_ is None:
            for i in range(-1, len(rings)):
                if i != r1_:
                    leastGold = max(leastGold, buyStuff(w_, a_, r1_, i))
            return leastGold
        
        #If all items have been chosen, we create the player and boss to initiate combat
        player = GameChar("Player", playerStats[0], playerStats[1] + weapons[w_].damage, playerStats[2])
        boss = GameChar("Boss", bossStats[0], bossStats[1], bossStats[2])
        gold = weapons[w_].cost
        
        if a_ != -1:
            player.armor += armor[a_].armor
            gold += armor[a_].cost
        if r1_ != -1:
            player.armor += rings[r1_].armor
            player.damage += rings[r1_].damage
            gold += rings[r1_].cost
        if r2_ != -1:
            player.armor += rings[r2_].armor
            player.damage += rings[r2_].damage
            gold += rings[r2_].cost
            
        if not runCombat(player, boss):
            return gold
        return leastGold
        

    return buyStuff()


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())