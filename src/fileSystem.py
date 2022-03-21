### The name says it all
import os
import math
import random
import warsim
import sqlite3
from base64 import b64encode, b64decode
from misc import *

def newUser(id : str, choice : int):
    userDatabase = sqlite3.connect('users.db')
    userCursor = userDatabase.cursor()
