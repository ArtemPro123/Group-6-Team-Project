from items import *
import random

enemy_rogue_knight = {
    "id": "knight",

    "name": "Rogue Knight",

    "weak": ["Fire", "Bludgeon"],

    "resist": ["Slash", "Stab"],

    "attack": random.randint(30, 50),

    "hp": 100,

    "temp_hp": 100,

    "drop": [item_bandage]
    }

enemy_castle_mage = {
    "id": "mage",

    "name": "Castle Mage",

    "weak": ["Slash", "Stab", "Bludgeon"],

    "resist": ["Fire"],

    "attack": random.randint(50, 70),

    "hp": 30,

    "temp_hp": 30,

    "drop": [item_bandage, item_mage_staff]
    }
enemy_kobold = {
    "id": "kobold",

    "name": "Harambe's Kobold",

    "weak": ["Slash, Stab, Bludgeon"],

    "resist": ["Fire"],

    "attack": random.randint(5, 15),

    "hp": 30,

    "temp_hp": 30,

    "drop": [item_dagger]

} 
enemy_bandit = {
    "id": "bandit",

    "name": "Bandit",

    "weak": ["Fire"],

    "resist": ["Slash"],

    "attack": random.randint(20,40),

    "hp": 40,

    "temp_hp": 40, 
    
    "drop": [item_upg_sword, item_bandage]

} 
enemy_rufian = {
    "id": "rufian",

    "name": "Rufian",

    "weak": ["Fire"],

    "resist": ["Slash"],

    "attack": random.randint(20, 35),

    "hp": 40,

    "temp_hp": 40, 
    
    "drop": [item_upg_sword, item_bandage]

}
enemy_harambe_warrior = {
    "id": "warrior",

    "name": "Harambe's Warrior",

    "weak": ["Slash", "Stab", "Bludgeon"],

    "resist": ["Fire"],

    "attack": random.randint(20,40),

    "hp": 40,

    "temp_hp": 40, 
    
    "drop": [item_upg_sword, item_bandage]

} 
enemy_harambe = {
    "id": "harambe",

    "name": "Harambe",

    "weak": [],

    "resist": [],

    "attack": random.randint(30, 70),

    "hp": 150,

    "temp_hp": 150, 
    
    "drop": [item_mage_staff, item_bandage]

} 
