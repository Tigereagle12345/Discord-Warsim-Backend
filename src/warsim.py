### A core module so to speak of the game itself,
### Will handle all ingame functions, and also be largly intertwined with the saving and loading processes
class user:
    def __init__(self, ID, GOLD, LAND, ESOLDIER, SOLDIER, PSOLDIER, TECH, LEVEL, XP, PLAGUE, RESEARCH, OP):
        self.id = int(ID)
        self.gold = int(GOLD)
        self.land = int(LAND)
        self.elite = int(ESOLDIER)
        self.troop = int(SOLDIER)
        self.peasant = int(PSOLDIER)
        self.men = self.elite + self.troop + self.peasant
        self.tech = int(TECH)
        self.level = int(LEVEL)
        self.xp = int(XP)
        self.plague = PLAGUE
        self.research = int(RESEARCH)
        self.publicOp = OP
    def Gold(self, mod : int):
        self.gold += mod
        return self.gold
    def XP(self, mod : int):
        self.xp += mod
        return self.xp
    def income(self, pop, land):
        income = int(((float(pop[0]) * 50)/8 * float(land[0]))/10)
        income += int(((float(pop[1]) * 30)/8 * float(land[1]))/10)
        income += int(((float(pop[2]) * 30)/8 * float(land[2]))/10)
        income = int(float(income) * float(self.publicOp)/40)
        if self.plague.severe <= 10:
            income *= 1
        elif self.plague.severe <= 20:
            income = int(float(income) * .9)
        elif self.plague.severe <= 30:
            income = int(float(income) * .7)
        elif self.plague.severe <= 40:
            income = int(float(income) * .6)
        elif self.plague.severe <= 50:
            income = int(float(income) * .5)
        elif self.plague.severe <= 60:
            income = int(float(income) * .4)
        elif self.plague.severe <= 70:
            income = int(float(income) * .3)
        elif self.plague.severe <= 80:
            income = int(float(income) * .2)
        else:
            income = int(float(income) * .1)
        self.gold += income
        return income
class plague:
    def __init__(self, ID, EXISTS, SEV, LETH, INF, IU, IC, IT):
        self.id = ID
        if EXISTS == 'Existant':
            self.exists = True
        else:
            self.exists = False
        self.severe = int(SEV)
        self.lethal = int(LETH)
        self.infective = int(INF)
        self.infectedurban = int(IU)
        self.infectedcountry = int(IC)
        self.infectedtowns = int(IT)
class items:
    ### Purchase item data shall be formated as such
    ### <--- START ITEM --->
    ###     ID={ID}
    ###     NAME={NAME}
    ###     DESCRIPTION="{DESCRIPTION}"
    ###     COST={COST}
    ###     MAINTANCE={MAINTANCE_COST}
    ###     ...ETC...
    ###     <--- START PROPERTIES --->
    ###         {EFFECT_ID}={EFFECT}
    ###         ...ETC...
    ###     <--- END PROPERTIES --->
    ### <--- END ITEM --->
    ###
    ### I would recomend formatting it like this, as it is more python-friendly
    ### iten_name = {
    ###     "id": ID,
    ###     "name": NAME,
    ###     "decription": DESCRIPTION,
    ###     "cost": COST,
    ###     "maintance": MAINTANCE_COST,
    ###     ...ETC...
    ###     "properties": {
    ###         "effect_id": EFFECT,
    ###         ...ECT...
    ###     }
    ### }
    def __init__(self):
        itemList = open('config/items.txt', 'r')
        self.itemList = itemList.read()     
class land:
    def __init__(self, urban, town, rural):
        self.urban = urban
        self.town = town
        self.rural = rural
