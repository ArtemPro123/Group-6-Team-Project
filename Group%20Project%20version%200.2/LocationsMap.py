from items import *

location_village = {
    "name": "the hometown village",

    "description":
    """To be added.""",

    "exits": {"west": "Shop", "east": "Bar", "north": "Forest"},

    "items": #This needs adding after items module has been done. [item_biscuits, item_handbook]
}

location_shop = {
    "name": "the local arms dealer",

    "description":
    """To be added.""",

    "exits":  {"north": "River", "east": "Village"},

    "items": [item_axe, item_shield, item_food]
}

location_river = {
    "name": "river",

    "description":
    """To be added.""",

    "exits": {"north": "Castle", "south": "Shop"},

    "items": []
}

location_castle = {
    "name": "castle",         

    "description":
    """Too be added.""",

    "exits": {"north": "Enclosure", "south": "River"},

    "items": []
}

location_bar= {
    "name": "the local bar",

    "description":
    """To be added.""",

    "exits": {"west": "Village", "north": "Camp"},

    "items": [item_beer]
}

location_camp = {
    "name": "abandoned war camp",

    "description":
    """Too be added.""",

    "exits": {"west": "Forest", "north": "Enclosure"},

    "items": [item_2handedsword]
}

location_forest = {
    "name": "deep dark forest",

    "description":
    """Too be added.""",

    "exits": {"south": "Village", "east": "Camp"},

    "items": []
}

location_enclosure = {
    "name": "enclosure",

    "description":
    """Too be added.""",

    "exits": {},

    "items": []
}

locations = {
    "Village": location_village,
    "Shop": location_shop,
    "River": location_river,
    "Castle": location_castle,
    "Forest": location_forest,
    "Bar": location_bar,
    "Camp": location_camp,
    "Enclosure": location_enclosure
}
