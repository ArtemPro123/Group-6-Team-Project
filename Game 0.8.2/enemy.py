from items import *

enemy_rogue_knight = {
    "id": "knight",

    "name": "Rogue Knight",

    "weak": ["Fire", "Bludgeon"],

    "resist": ["Slash", "Stab"],

    "attack": 45,

    "hp": 100,

    "temp_hp": 100,

    "drop": [item_bandage]
    }

enemy_castle_mage = {
    "id": "mage",

    "name": "Castle Mage",

    "weak": ["Slash", "Stab", "Bludgeon"],

    "resist": ["Fire"],

    "attack": 60,

    "hp": 30,

    "temp_hp": 30,

    "drop": [item_bandage, item_mage_staff]
    }
enemy_kobold = {
    "id": "kobold",

    "name": "Harambe's Kobold",

    "weak": ["Slash"],

    "resist": ["Fire"],

    "attack": 10,

    "hp": 30,

    "temp_hp": 30,

    "drop": [item_dagger]

} 
enemy_bandit = {
    "id": "bandit",

    "name": "Bandit",

    "weak": ["Fire"],

    "resist": ["Slash"],

    "attack": 30,

    "hp": 40,

    "temp_hp": 40, 
    
    "drop": [item_upg_sword, item_bandage]

} 
enemy_rufian = {
    "id": "rufian",

    "name": "Rufian",

    "weak": ["Fire"],

    "resist": ["Slash"],

    "attack": 30,

    "hp": 40,

    "temp_hp": 40, 
    
    "drop": [item_upg_sword, item_bandage]

}
enemy_harambe_warrior = {
    "id": "warrior",

    "name": "Harambe's Warrior",

    "weak": ["Fire"],

    "resist": ["Slash"],

    "attack": 30,

    "hp": 40,

    "temp_hp": 40, 
    
    "drop": [item_upg_sword, item_bandage]

} 
enemy_harambe = {
    "id": "harambe",

    "name": "Harambe",

    "weak": ["Fire"],

    "resist": ["Slash"],

    "attack": 50,

    "hp": 150,

    "temp_hp": 150, 
    
    "drop": [item_mage_staff, item_bandage]

} 
