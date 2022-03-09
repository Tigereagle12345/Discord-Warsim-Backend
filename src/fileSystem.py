### The name says it all
import os
import random
import time
import warsim
from misc import *

def newUser(id : int, choice : int):
    ### New user join process
    ### User Files will be structured like:
    ### <--- START USER --->
    ###     ID={ID}
    ###     LAND={LAND}
    ###     GOLD={GOLD}
    ###     TECH={TECH}
    ###     ...ETC...
    ###     <--- START MILILITARY --->
    ###         {MILITARY_COMPONENT} = {COUNT}
    ###     <--- END MILILITARY --->
    ###     <--- START PURCHASES --->
    ###         {PURCHASE_ID} = {STATUS}
    ###     <--- END PURCHASES --->
    ###     <--- START ALLIES --->
    ###         {ALLY's ID}
    ###     <--- END ALLIES --->
    ###     ...ETC...
    ### <--- END USER --->
    ### ETC
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
            ### 
            s = random.randrange(100)
            ### You are really fucked, Black Death level fucked
            if s >= 99:
                severity = randStr(random.randrange(9,11) * 10, 101)
                lethality = randStr(random.randrange(8,10) * 10, 101)
                while int(lethality) >= 100:
                    lethality = str(int(lethality) - 1)
                infectivity = randStr(random.randrange(8,10) * 10, 101)
                while int(infectivity) >= 100:
                    infectivity = str(int(infectivity) - 1)
                
        else:
            ### Congratulations! You don't currently suffer from a plague
            plague = ['Non-existant', '0 :: No severity', '0 :: No lethality', '0 :: No infectivity', '0 :: None infected']
