from items import *
import random

enemy_rogue_knight = {
    "id": "knight",

    "name": "Rogue Knight",

    "weak": ["Fire", "Bludgeon"],

    "resist": ["Slash", "Stab"],

    "attack": random.randint(15, 30),

    "hp": 100,

    "temp_hp": 100,

    "drop": [item_bandage, item_upg_sword, item_mage_staff, item_restoration_potion]
    }

enemy_castle_mage = {
    "id": "mage",

    "name": "Castle Mage",

    "weak": ["Slash", "Stab", "Bludgeon"],

    "resist": ["Fire"],

    "attack": random.randint(20, 70),

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

    "attack": random.randint(20, 30),

    "hp": 40,

    "temp_hp": 40, 
    
    "drop": [item_upg_sword, item_bandage]

}
enemy_harambe_warrior = {
    "id": "warrior",

    "name": "Harambe's Warrior",

    "weak": ["Slash", "Stab", "Bludgeon"],

    "resist": ["Fire"],

    "attack": random.randint(5, 50),

    "hp": 40,

    "temp_hp": 40, 
    
    "drop": [item_upg_sword, item_bandage]

} 
enemy_harambe = {
    "id": "harambe",

    "name": "Harambe",

    "weak": [],

    "resist": [],

    "attack": random.randint(25, 50),

    "hp": 150,

    "temp_hp": 150, 
    
    "drop": [item_mage_staff, item_bandage]

} 

enemy_kirilla_clown = {
    "id": "clown",

    "name": "Kirilla Clown",

    "weak": ["Fire", "Slash"],

    "resist": ["Slash", "Bludgeon", "Gun"],

    "attack": random.randint(20, 40),

    "hp": 100,

    "temp_hp": 100,

    "drop": [item_buff_potion]
    }
