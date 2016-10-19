from items import *
from map import rooms

warrior = {
    "inventory": [item_sword],
    #"gold": int(50),
    "hp": int(200),
    "temp_hp": int(200)
    }
mage = {
    "inventory": [item_mage_staff],
    #"gold" = int(50),
    "hp": int(150),
    "temp_hp": int(150)
    }
rogue = { 
    "inventory": [item_dagger, item_helping_hand],
    #"gold" = int(50),
    "hp": int(100),
    "temp_hp": int(100)
    } 
cleric = { 
    "inventory":[item_mace, item_restoration_potion],
    #"gold" = int(50),
    "hp": int(130),
    "temp_hp": int(130)
    } 

current_room = rooms["Home"]
gold = int(50) 
    

