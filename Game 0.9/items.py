import random

item_dagger = {
    "id": "dagger",

    "name": "Dagger",

    "description":
    """Stabby stab""",

    "type": "Stab",

    "attack": random.randint(15, 30),

    "crit": 8, 

    "cost": 20,

    "chance": 6 
    }

item_barman = {
    "id": "Duncan",

    "name": "Zoo manager duncan",

    "description":
    """The publicity manager at the zoo""",

    "type": "None",

    "cost": 0
}

item_helping_hand = {
    "id": "helping_hand",

    "name": "Helping Hand",

    "description":
    """ Use to get into areas you sometimes may not be ready for.""",

    "type": "None",

    "cost": 60, 

    "chance": 3
    }

item_mace = {
    "id": "mace",

    "name": "Mace",

    "description":
    """Used to blugeon enemies""",

    "type": "Bludgeon",

    "attack": random.randint(30,40),

    "crit": 4,

    "cost": 20, 

    "chance": 5 
    }
item_restoration_potion = {
    "id": "restore",

    "name": "Restoration Potion",

    "description":
    """Used to restore health""",

    "type": "Heal",

    "hp": 50,

    "cost": 30, 

    "chance": 4
    } 
item_isiah = {
    "id": "isiah",

    "name": "Isiah",

    "description":
    """A 4 year old lad from your village.""",

    "type": "None",

    "cost": 0 
    }

item_mage_staff = {
    "id": "staff",

    "name": "Mage Staff",

    "description":
    """ Your mage staff is infused with the power of the fire elements shooting out fire balls""",

    "type": "Fire",

    "attack": random.randint(40,65), 

    "crit": 3, 

    "cost": 200, 

    "chance": 3 
}

item_bandage = {
    "id": "bandage",

    "name": "Bandage",

    "description":
    """its a bandage""",

    "type": "Heal",

    "hp": 30,

    "cost": 30, 

    "chance": 8 

}

item_wood_block = {
    "id": "wood",

    "name": "Wood",

    "description":
    """ Wood blockade init fam""",

    "type": "None",
    
    "cost": 2 
    }
item_sword = {
    "id": "sword",

    "name": "Iron Sword",

    "description":
    """basic sword, everyone's got one of these lying around""",

    "type": "Slash",

    "attack": random.randint(20, 30),

    "crit": 4, 

    "cost": 20, 

    "chance": 4 

} 
item_upg_sword = {
    "id": "steelsword",

    "name": "Steel Sword",

    "description":
    """its a sword you twat""",

    "type": "Slash",

    "attack": random.randint(45, 55),

    "crit": 6, 
    
    "cost": 30,

    "chance": 3

    }
item_axe = {
    "id": "axe",

    "name": "Axe",

    "description":
    """Axe for wood chop chop""",

    "type": "Slash",

    "attack": random.randint(18,20),

    "crit": 4, 
    
    "cost": 30, 

    "chance": 4  
}
item_chainmail = {
    "id": "chainmail",

    "name": "Chainmail Armour",

    "description":
    """Armour fashioned from metal chains""",

    "type": "Armour",

    "hp": 50,

    "cost": 40, 

    "chance": 4  
}
item_potion = {
    "id": "potion",

    "name": "Potion",

    "description":
    """Its. A. Potion.""",

    "type": "Heal",

    "hp": 100, 

    "cost": 40, 

    "chance": 5 
}

item_knights_armour = {
    "id": "knightsArmour",

    "name": "Black Knights Armour",

    "decription": 
    """ The black knights armour is inbued with ancient magic increasing the HP of any wearer by a considerable amount! """,

    "type": "Armour",

    "hp": 150,

    "cost": 75,

}

item_hunting_rifle = {
    "id": "rifle",

    "name": "Hunting Rifle",

    "description":
    """Zoo Manager Duncans rifle. Looks pretty shabby but could cause some serious damage to the right enemies!""",

    "type": "Gun",

    "attack": random.randint(30, 40),

    "crit": 4, 

    "cost": 100, 

    "chance": 4 
}

item_buff_potion = {
    "id": "buff",

    "name": "Crit Potion",

    "description":
    """Crit chance increase!""",

    "type": "buff",

    "cost": 0, 

    "chance": 1000
    } 
