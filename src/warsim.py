### A core module so to speak of the game itself,
### Will handle all ingame functions, and also be largly intertwined with the saving and loading processes
class user:
    def __init__(self, ID, GOLD, LAND, ESOLDIER, SOLDIER, PSOLDIER, TECH, LEVEL, XP, PLAGUE):
        self.id = ID
        self.gold = GOLD
        self.land = LAND
        self.elite = ESOLDIER
        self.troop = SOLDIER
        self.peasant = PSOLDIER
        self.men = self.elite + self.troop + self.peasant
        self.tech = TECH
        self.level = LEVEL
        self.xp = XP
        self.plague = PLAGUE
class plague:
    def __init__(self, ID, EXISTS, SEV, LETH, INF, IU, IC, IT):
        self.id = ID
        if EXISTS == 'Existant':
            self.exists = True
        else:
            self.exists = False
        self.severe = SEV
        self.lethal = LETH
        self.infective = INF
        self.infectedurban = IU
        self.infectedcountry = IC
        self.infectedtowns = IT
class purchases:
    ### Purchase item data shall be formated as such
    ### <--- START ITEM --->
    ###     ID={ID}
    ###     NAME={NAME}
    ###     COST={COST}
    ###     MAINTANCE={MAINTANCE_COST}
    ###     ...ETC...
    ###     <--- START PROPERTIES --->
    ###         WARSCORE={WARSCORE}
    ###         ...ETC...
    ###     <--- END PROPERTIES --->
    ### <--- END ITEM --->
    def __init__(self):
        purchaseList = open('config/purchases.sdc')
        self.purchaseList = purchaseList.read
