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
        gold = randStr(7500,15001)
        tech = randStr(3,8)
        xp = randStr(0, 250)
        soldier = randStr(1000, 5000)
        peasant = randStr(1500, 7500)
        elite = randStr(50, 500)
