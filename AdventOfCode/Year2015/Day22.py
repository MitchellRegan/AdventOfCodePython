aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
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
        
    def takeDamage(self, incommingDmg_:int)->bool:
        '''Applies incomming damage to this character. Returns True if still alive, and False if dead.'''
        totalDmg = incommingDmg_ - self.armor
        if totalDmg < 1:
            totalDmg = 1
        self.hp -= totalDmg
        testing and print("\t", self.name, "attacked for", incommingDmg_, "-", self.armor, "=", totalDmg, "    HP:", self.hp)
            
        return (self.hp > 0)
 

def getInput():
    player = [50, 500]
    boss = [0,0]

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            if boss[0] == 0:
                boss[0] = int(line[-1])
            else:
                boss[1] = int(line[-1])

    return player, boss
            

def solution1():
    ps, bs = getInput()
    if testing:
        ps = [10, 250]
        
    spells = [("Magic Missile", 53), ("Drain", 73), ("Shield", 113), ("Poison", 173), ("Recharge", 229)]
    
    print("Player HP:", ps[0], "    Mana:  ", ps[1], "\nBoss   HP:", bs[0], "    Damage:", bs[1])
    def runCombat(hp_:int, mana_:int, manaUsed_:int, bossHp_:int, bossDmg_:int, shieldTime_:int=0, poisonTime_:int=0, rechargeTime_:int=0)->int:
        '''Recursive method to run each round of combat, simulating the results of every different spell choice.'''
        
        #Taking care of effects first
        if shieldTime_ > 0:
            shieldTime_ -= 1
        if poisonTime_ > 0:
            poisonTime_ -= 1
            bossHp_ -= 3
        if rechargeTime_ > 0:
            rechargeTime_ -= 1
            mana_ += 101
            
        #If the player can't afford even the most inexpensive spell, they lose
        if mana_ < spells[0][1]:
            return manaUsed_
        #Iterating through every spell option the player can cast
        #for spell in spells:
            #if spell[1] <= mana_:
            #    if spell[0] == "Magic Missile":
            #        
            ##    elif spell[0] == "Drain":
            #        
            #    elif spell[0] == "Shield":
            #        
            #    elif spell[0] == "Poison":
            #        
            #    elif spell[0] == "Recharge":

    return runCombat()


def solution2():
    playerStats, bossStats = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())