class warscore:
    def __init__(self, elite, peasant, soldier, unit):
        self.elite = elite
        self.peasant = peasant
        self.soldier = soldier
        self.unit = unit
        self.eliteCount = elite
        self.peasantCount = peasant
        self.soldierCount = soldier
        self.calculate()
    perMan : int
    perUnit : int
    perForce : int
    perSoldier = 45
    perElite = 150
    perPeasant = 25
    def calculate(self):
        self.elite *= self.perMan
        self.peasant *= self.perMan
        self.soldier *= self.perMan
        self.elite += self.eliteCount * self.perElite
        self.soldier += self.soldierCount * self.perSoldier
        self.peasant += self.peasantCount * self.perPeasant
        for i in range(len(self.unit)):
            self.unitElite = self.unit[i][0] * self.perMan + self.eliteCount * self.perElite + self.perUnit
            self.unitSoldier = self.unit[i][1] * self.perMan + self.soldierCount * self.perSoldier + self.perUnit
            self.unitPeasant = self.unit[i][2] * self.perMan + self.peasantCount * self.perPeasant + self.perUnit
            self.elite = self.elite - self.unit[i][0] * self.perMan + self.eliteCount * self.perElite + self.unitElite
            self.soldier = self.soldier - self.unit[i][1] * self.perMan + self.soldierCount * self.perSoldier + self.unitSoldier
            self.peasant = self.peasant - self.unit[i][2] * self.perMan + self.peasantCount * self.perPeasant + self.unitPeasant
        del self.unitElite
        del self.unitPeasant
        del self.unitSoldier
        self.elite += self.perForce
        self.soldier += self.perForce
        self.peasant += self.perForce
        self.eliteRatio = float(self.elite)/float(self.eliteCount)
        self.soldierRatio = float(self.soldier)/float(self.soldierCount)
        self.peasantRatio = float(self.peasant)/float(self.peasantCount)
class levels:
    def __init__(self, xp):
        self.xp = xp
    def levelCalc(self, max = 300):
        self.levels = [1000]
        self.max = max
        for i in range(max):
            self.levels.append(self.levels[i] * 2)
        for i in range(len(self.levels)):
            if self.xp >= self.levels[i]:
                if not i + 1 == len(self.levels) and self.xp < self.levels[i + 1]:
                    break
                elif i + 1 == len(self.levels):
                    break
                else:
                    pass
            elif i == 0:
                break
        self.level = i + 1
        return self.level
