class warscore:
    perMan : int
    perUnit : int
    perForce : int
    perSoldier : int
    perElite : int
    perPeasant : int
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
