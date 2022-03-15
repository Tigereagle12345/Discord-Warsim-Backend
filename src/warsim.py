### A core module so to speak of the game itself,
### Will handle all ingame functions, and also be largly intertwined with the saving and loading processes
class user:
    def __init__(self, ID, GOLD, LAND, ESOLDIER, SOLDIER, PSOLDIER, TECH, LEVEL, XP, PLAGUE, RESEARCH):
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
    def Gold(self, mod : int):
        self.gold += mod
        return self.gold
    def XP(self, mod : int):
        self.xp += mod
        return self.xp
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
class purchases:
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
    def __init__(self):
        purchaseList = open('config/purchases.txt', 'r')
        self.purchaseList = purchaseList.read()     