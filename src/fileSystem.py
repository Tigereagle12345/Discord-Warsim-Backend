### The name says it all
import os
import math
import random
import warsim
import sqlite3
from base64 import b64encode, b64decode
from misc import *

def newUser(id : str):
    userDatabase = sqlite3.connect('users.db')
    userDatabase.row_factory = sqlite3.Row
    userCursor = userDatabase.cursor()
    userCursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users';''')
    if not userCursor.fetchone()[0]==1:
        userCursor.execute('CREATE TABLE users (id int, gold int, level int, xp int)')
    gold = random.randrange(1000,25000)
    insert = id + ',' + str(gold) + ',0,0);'
    userCursor.execute('INSERT INTO users (id,gold,level,xp) VALUES (' + insert)
    userCursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='land';''')
    if not userCursor.fetchone()[0]==1:
        userCursor.execute('CREATE TABLE land (ownerid int, barren bool, population int, infected int, type int, plague text)')
