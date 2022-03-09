### The name says it all
import os
import random
import time
import warsim
from base64 import b64encode, b64decode
from misc import *

def newUser(id : str, choice : int):
    ### New user join process
    ### User Files will be structured like:
    ### <--- START USER --->
    ###     ID={ID}
    ###     LAND={LAND}
    ###     GOLD={GOLD}
    ###     TECH={TECH}
    ###     ...ETC...
    ###     <--- START MILILITARY --->
    ###         {MILITARY_COMPONENT}={COUNT}
    ###     <--- END MILILITARY --->
    ###     <--- START PURCHASES --->
    ###         {PURCHASE_ID}={STATUS}
    ###     <--- END PURCHASES --->
    ###     <--- START ALLIES --->
    ###         {ALLY's ID}
    ###     <--- END ALLIES --->
    ###     ...ETC...
    ### <--- END USER --->
    ### ETC
    ### TODO: Add choices
    ### Choices will be:
    ### 1. Standard-No risk, no reward
    ### 2. Russian roulette-High risk, high reward
    ### 3. Selling your soul to the devil-Extrodinarily high risk, extrodinaryily high reward
    if choice == 1:
        land = randStr(3,11)
        gold = randStr(7500,15001)
        tech = randStr(3,8)
        xp = randStr(250)
        soldier = randStr(1000, 5000)
        peasant = randStr(1500, 7500)
        elite = randStr(50, 500)
        urban = int(land/10) + 1
        if urban <= 0:
            urban = 1
        country = int(land - 1/3)
        towns = int(land) - urban - country
        urbanPop = urban * random.randrange(1000, 200000)
        countryPop = country * random.randrange(50, 5000)
        townsPop = towns * random.randrange(250, 15000)
        ### Plague time!
        rnd = random.randrange(100)
        if rnd >= 75:
            ### Congratulations! You have a plague!
            plague = ['Existant']
            s = random.randrange(100)
            if s >= 99:
                ### You are really fucked, Black Death level fucked
                severity = randStr(random.randrange(9,11) * 10, 101)
                lethality = randStr(random.randrange(8,10) * 10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(random.randrange(8,10) * 10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                plague.append(severity)
                plague.append(lethality)
                plague.append(infectivity)
                infectedUrban = int(float(urbanPop) * (float(infectivity)/float(100)))
                infectedCountry = int(float(countryPop) * (float(infectivity)/float(150)))
                infectedTowns = int(float(townsPop) * (float(infectivity)/float(125)))
                plague.append(str(infectedUrban))
                plague.append(str(infectedCountry))
                plague.append(str(infectedTowns))
            elif s >= 90:
                ### Shit's bad man, real bad
                severity = randStr(random.randrange(8,10) * 10, 101)
                lethality = randStr(random.randrange(7,10) * 10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(random.randrange(7,10) * 10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                plague.append(severity)
                plague.append(lethality)
                plague.append(infectivity)
                infectedUrban = int(float(urbanPop) * (float(infectivity)/float(100)))
                infectedCountry = int(float(countryPop) * (float(infectivity)/float(150)))
                infectedTowns = int(float(townsPop) * (float(infectivity)/float(125)))
                plague.append(str(infectedUrban))
                plague.append(str(infectedCountry))
                plague.append(str(infectedTowns))
            elif s >= 80:
                ### Good luck cleaning all the bodies off the streets
                severity = randStr(random.randrange(7,10) * 10, 101)
                lethality = randStr(random.randrange(6,10) * 10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(random.randrange(5,10) * 10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                plague.append(severity)
                plague.append(lethality)
                plague.append(infectivity)
                infectedUrban = int(float(urbanPop) * (float(infectivity)/float(100)))
                infectedCountry = int(float(countryPop) * (float(infectivity)/float(150)))
                infectedTowns = int(float(townsPop) * (float(infectivity)/float(125)))
                plague.append(str(infectedUrban))
                plague.append(str(infectedCountry))
                plague.append(str(infectedTowns))
            elif s >= 70:
                ### Many will die
                severity = randStr(random.randrange(6,10) * 10, 101)
                lethality = randStr(random.randrange(6,9) * 10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(random.randrange(5,8) * 10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                plague.append(severity)
                plague.append(lethality)
                plague.append(infectivity)
                infectedUrban = int(float(urbanPop) * (float(infectivity)/float(100)))
                infectedCountry = int(float(countryPop) * (float(infectivity)/float(150)))
                infectedTowns = int(float(townsPop) * (float(infectivity)/float(125)))
                plague.append(str(infectedUrban))
                plague.append(str(infectedCountry))
                plague.append(str(infectedTowns))
            elif s >= 60:
                severity = randStr(random.randrange(4,10) * 10, 101)
                lethality = randStr(random.randrange(5,9) * 10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(random.randrange(5,9) * 10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                plague.append(severity)
                plague.append(lethality)
                plague.append(infectivity)
                infectedUrban = int(float(urbanPop) * (float(infectivity)/float(100)))
                infectedCountry = int(float(countryPop) * (float(infectivity)/float(150)))
                infectedTowns = int(float(townsPop) * (float(infectivity)/float(125)))
                plague.append(str(infectedUrban))
                plague.append(str(infectedCountry))
                plague.append(str(infectedTowns))
            elif s >= 50:
                severity = randStr(random.randrange(4,9) * 10, 101)
                lethality = randStr(random.randrange(4,9) * 10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(random.randrange(3,8) * 10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                plague.append(severity)
                plague.append(lethality)
                plague.append(infectivity)
                infectedUrban = int(float(urbanPop) * (float(infectivity)/float(100)))
                infectedCountry = int(float(countryPop) * (float(infectivity)/float(150)))
                infectedTowns = int(float(townsPop) * (float(infectivity)/float(125)))
                plague.append(str(infectedUrban))
                plague.append(str(infectedCountry))
                plague.append(str(infectedTowns))
            elif s >= 40:
                severity = randStr(random.randrange(4,8) * 10, 101)
                lethality = randStr(random.randrange(3,7) * 10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(random.randrange(2,8) * 10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                plague.append(severity)
                plague.append(lethality)
                plague.append(infectivity)
                infectedUrban = int(float(urbanPop) * (float(infectivity)/float(100)))
                infectedCountry = int(float(countryPop) * (float(infectivity)/float(150)))
                infectedTowns = int(float(townsPop) * (float(infectivity)/float(125)))
                plague.append(str(infectedUrban))
                plague.append(str(infectedCountry))
                plague.append(str(infectedTowns))
            elif s >= 30:
                ### Many shall suffer, few shall die
                severity = randStr(random.randrange(7) * 10, 101)
                lethality = randStr(random.randrange(5) * 10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(random.randrange(7) * 10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                plague.append(severity)
                plague.append(lethality)
                plague.append(infectivity)
                infectedUrban = int(float(urbanPop) * (float(infectivity)/float(100)))
                infectedCountry = int(float(countryPop) * (float(infectivity)/float(150)))
                infectedTowns = int(float(townsPop) * (float(infectivity)/float(125)))
                plague.append(str(infectedUrban))
                plague.append(str(infectedCountry))
                plague.append(str(infectedTowns))
            elif s >= 20:
                severity = randStr(random.randrange(3) * 10, 101)
                lethality = randStr(random.randrange(3) * 10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(random.randrange(3) * 10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                plague.append(severity)
                plague.append(lethality)
                plague.append(infectivity)
                infectedUrban = int(float(urbanPop) * (float(infectivity)/float(100)))
                infectedCountry = int(float(countryPop) * (float(infectivity)/float(150)))
                infectedTowns = int(float(townsPop) * (float(infectivity)/float(125)))
                plague.append(str(infectedUrban))
                plague.append(str(infectedCountry))
                plague.append(str(infectedTowns))
            elif s >= 10:
                severity = randStr(random.randrange(2) * 10, 101)
                lethality = randStr(random.randrange(2) * 10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(random.randrange(2) * 10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                plague.append(severity)
                plague.append(lethality)
                plague.append(infectivity)
                infectedUrban = int(float(urbanPop) * (float(infectivity)/float(100)))
                infectedCountry = int(float(countryPop) * (float(infectivity)/float(150)))
                infectedTowns = int(float(townsPop) * (float(infectivity)/float(125)))
                plague.append(str(infectedUrban))
                plague.append(str(infectedCountry))
                plague.append(str(infectedTowns))
            else:
                severity = randStr(10, 101)
                lethality = randStr(10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                plague.append(severity)
                plague.append(lethality)
                plague.append(infectivity)
                infectedUrban = int(float(urbanPop) * (float(infectivity)/float(100)))
                infectedCountry = int(float(countryPop) * (float(infectivity)/float(150)))
                infectedTowns = int(float(townsPop) * (float(infectivity)/float(125)))
                plague.append(str(infectedUrban))
                plague.append(str(infectedCountry))
                plague.append(str(infectedTowns))
        else:
            ### Congratulations! You don't currently suffer from a plague!
            plague = ['Non-existant', '0 :: No severity', '0 :: No lethality', '0 :: No infectivity', '0 :: None infected','0 :: None infected','0 :: None infected',]
    file = open(id + '.wdf', 'x')
    file.write('<--- START USER --->\n')
    file.write('\t<--- START GENERIC --->\n')
    file.write('\t\tID=' + id + '\n')
    file.write('\t\tLAND=' + land + '\n')
    file.write('\t\tGOLD=' + gold + '\n')
    file.write('\t\tTECH=' + tech + '\n')
    file.write('\t\tLEVEL=1\n')
    file.write('\t\tXP=' + xp + '\n')
    file.write('\t<--- END GENERIC --->\n')
    file.write('\t<--- START LAND --->\n')
    file.write('\t\tURBAN=' + urban + '\n')
    file.write('\t\tRURAL=' + country + '\n')
    file.write('\t\tTOWN=' + towns + '\n')
    file.write('\t<--- END LAND --->\n')
    file.write('\t<--- START POPULATION --->\n')
    file.write('\t\tURBAN=' + urbanPop + '\n')
    file.write('\t\tRURAL=' + countryPop + '\n')
    file.write('\t\tTOWN=' + townsPop + '\n')
    file.write('\t<--- END POPULATION --->\n')
    file.write('\t<--- START PLAGUE --->\n')
    for i in plague:
        file.write('\t\t' + i + '\n')
    file.write('\t<--- END PLAGUE --->\n')
    file.write('\t<--- START MILITARY --->\n')
    file.write('\t\tELITE=' + elite + '\n')
    file.write('\t\tSOLDIER=' + soldier + '\n')
    file.write('\t\tPEASANT=' + peasant + '\n')
    file.write('\t<--- END MILITARY --->\n')
    ### TODO: Add purchases
    file.write('\t<--- START PURCHASES --->\n')
    file.write('\t<--- END PURCHASES --->\n')
    file.write('\t<--- START ALLIES --->\n')
    file.write('\t\t :: New users don\'t have allies, stupid')
    file.write('\t<--- END ALLIES --->\n')
    file.write('<--- END USER --->\n')
    file.close()
    del file
    file = open(id + '.wdf', 'r')
    File = file.read()
    file.close()
    del file
    os.remove(id + '.wdf')
    file = open(id + '.wdf', 'xb')
    file.write(b64encode(File.encode('unicode-escape')))
    file.close()
    del file
    file = open(id + '.bak.wdf', 'xb')
    file.write(b64encode(File.encode('unicode-escape')))
    file.close()
    del file
class savefile:
    def __init__(self, id : str):
        self.id = id
        tmp = open(id + '.wdf', 'r+b')
        self.filedata = b64decode(tmp.read()).decode('unicode-ecape')
        tmp.close()
        self.landdata = partition(self.filedata, '\t<--- START LAND --->\n', '\t<--- END LAND --->\n')
        self.populationdata = partition(self.filedata, '\t<--- START POPULATION --->\n', '\t<--- END POPULATION --->\n')
        self.militarydata = partition(self.filedata, '\t<--- START MILITARY --->\n', '\t<--- END MILITARY --->\n')
        self.purchasedata = partition(self.filedata, '\t<--- START PURCHASES --->\n', '\t<--- END PURCHASES --->\n')
        self.plaguedata = partition(self.filedata, '\t<--- START PLAGUE --->\n', '\t<--- END PLAGUE --->\n')
        self.allydata = partition(self.filedata, '\t<--- START ALLIES --->\n', '\t<--- END ALLIES --->\n')
        self.genericdata = partition(self.filedata, '\t<--- START GENERIC --->\n', '\t<--- END GENERIC --->\n')
    def removeComments(self,replaceInFile : bool):
        tempFileData = self.filedata.partition('\n')[0]
        for i in self.filedata:
            if i == tempFileData:
                pass
            elif '::' in i:
                tempFileData += i.partition('::')[0]
            else:
                tempFileData += i
        if replaceInFile == True:
            os.remove(id + '.bak.wdf')
            tmp = open(id + '.bak.wdf', 'xb')
            tmp.write(b64encode(self.filedata.encode('unicode-escape')))
            tmp.close()
            del tmp
            tmp = open(id + '.wdf', 'w+b')
            tmp.write(b64encode(tempFileData.encode('unicode-escape')))
            tmp.close()
            del tmp
            self.filedata = tempFileData
        else:
            self.filedata = tempFileData
    def repartition(self):
        self.landdata = partition(self.filedata, '\t<--- START LAND --->\n', '\t<--- END LAND --->\n')
        self.populationdata = partition(self.filedata, '\t<--- START POPULATION --->\n', '\t<--- END POPULATION --->\n')
        self.militarydata = partition(self.filedata, '\t<--- START MILITARY --->\n', '\t<--- END MILITARY --->\n')
        self.purchasedata = partition(self.filedata, '\t<--- START PURCHASES --->\n', '\t<--- END PURCHASES --->\n')
        self.plaguedata = partition(self.filedata, '\t<--- START PLAGUE --->\n', '\t<--- END PLAGUE --->\n')
        self.allydata = partition(self.filedata, '\t<--- START ALLIES --->\n', '\t<--- END ALLIES --->\n')
        self.genericdata = partition(self.filedata, '\t<--- START GENERIC --->\n', '\t<--- END GENERIC --->\n')
    def redef(self):
        tmp = open(id + '.wdf', 'r+b')
        self.filedata = b64decode(tmp.read()).decode('unicode-ecape')
        tmp.close()
        self.repartition()
    def plague(self):
        plagueData = list(self.plaguedata)
        for i in range(len(plagueData)):
            plagueData[i] = plagueData[i].strip()
            if not i == 0:
                plagueData[i] = int(plagueData)
        plague = warsim.plague(self.id, plagueData[0], plagueData[1], plagueData[2], plagueData[3], plagueData[4], plagueData[5], plagueData[6])
        return plague
