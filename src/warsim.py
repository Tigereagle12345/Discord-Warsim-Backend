### A core module so to speak of the game itself,
### Will handle all ingame functions, and also be largly intertwined with the saving and loading processes
class user:
    def __init__(self, ID, GOLD, LAND, ESOLDIER, SOLDIER, PSOLDIER, TECH, WAR, ISPLY, NAME, LEVEL, XP):
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
