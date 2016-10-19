from items import *
from enemy import * 
room_home = {
    "name": "Home",

    "description":
    """You reside by your small home town, everything seems familiar, apart from one thing.
There is a new notice on the billboard that outlines:
The Ancient Cinncinati Legend has rampaged the area north of the castle and has had
his goons take a young lad by name of Isiah and locked him in the castle, he must be stopped!
A plentiful sum will be offered.
Signed - KS.""",

    "exits": {"west": "General Store", "east": "Bar","north": "Forest"},

    "items": [],

    "market": [],

    "combat": False, 
    
    "enemy": [],

    "max enemy": 0,

    "min enemy": 0,

    "check_item": [],

    "activity": [],

    "ascii":"""
         
                +++?7++    
                ?+++++?
                $I$7Z++     II
                7+++Z++    IIII
                +++++I.. ?IIII?O .  
                ++7I?++:8IIIIIIIII8...                                       @@@@    @   @ @  @ @ @ 
                +?++8I?IIIIIIIIIIIIIZ .                               @ @ @ @   @    @    @    @ @ 
                I7+OIIIIIIIIIIIIIIIIIIIZ                           @ @ @ @ @   @ @ @ @ @   @ @    @  
               .7IIIIIIIIII?IIIIIIIIIIII7....                         @ @@ @    @ @   @   @ @ @  @ @  @
    .        .~IIIIIIIIIII$,,,,,$?IIIIIIIIII~.                      @ @ @ @ @@@ @ @ @    @ @@ @     @ @ 
            $IIIIIIIIIIIZ,,,,::,,,ZIIIIIIIIIII7.                  @ @ @ @ @ @ @@ @ @ @ @    @ @ @ @ @ @ @ 
         .8IIIIIIIIIII=,,,,:ZZZ8:,,,~7IIIIIIIIII8..                 @@  @@ @  @    @@ @ @    @ @@ @   @ @ @
       ,IIIIIIIIIII7,,,,,,ZZ....OD,,,,,7IIIIIIIIIII,              @ @ @ @@ @ @   @ @ @ @ @   @ @ @@ @ @ @ @ 
    .8IIIIIIIIIII+,,,,,~ZZ...D:...$Z,,,,,,IIIIIIIIIII8.           @ @@ @ @  @  @  @@ @    @ @ @@ @ @ @  @
  .IIIIIIIIIII?,,,,,,,+==============+,,,,,,IIIIIIIIIIII.            @ @ @ @ @ @@@ @ @ @ @ @ @ @ @ @ 
~IIIIIIIIIIIZ:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:$IIIIIIIIIII:.            @  @ @   @ @ @ @@@ @ @ @
IIIIIIIIII7,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,IIIIIIIIIII:              @  @@ @  @    @@ @
IIIIIII7=,,,,,,,,,,,,,,,,,,,~=:,,,,,,,,,,,,,,,,,,,,7IIIIIIIO                  @@        @@@   @@@
7IIII$,,,,,,,,,,,,,,,,,,,D$$ZOZZZ$,,,,,,,,,,,,,,,,,,,ZIIIII.                  @#       #@   @  # @
 :Z=.8,,O888888888888,,,$$:,,,,,?ZO,,D888888888888D,,..?Z:                     @#      @#    #  @ @
    .8,,$.....$.....Z,,~$,,,,,:,,~Z:,D.....O:....88,,.                          #@#  @##   #   @  
   ..8,,$     Z.    Z,,~O,,?$ ,I,,Z:,D.    O:    88,,.                           @## @##  #
    .8,,$     Z.    Z,,~O,,I   =,,Z:,D.    O:    88,,.                           @## @#  #
    .8,,$.....Z ....$,,:O,,:,=++,,Z:,D.....8:....D8,,.                           @#233@ #
    .8,,$77777Z77777$,,~O,,,,,,,,,Z:,D$7777O$777788,,.                           @#@#@##
    .8,,$     $.    Z,,~O,,,,,,,,,Z:,D.    O:    88,,.                           @###@#
    .8,,$     $.    Z,,:O,.=,,,,,,Z:,D.    O:    88,,.                           @#@##
    .8,,$     Z.    Z,,~O,:,,,,,,,Z:,D.    O:    88,,.                           @##@@#
    .8,,$ZZZZZZZZZZZZ,,~O,,,,,,,,,Z::D$ZZZZ$$ZZZZ$8,,.                           @@#@#@
    .8,$$$$$$$$$$$$$$Z,~O,,,,,,,,,Z:OZ$$$$$$$$$$$$$,,.                           @!!@@@
    .8,IIIIIIIIIIIIIII,~O,,,,,,,,,Z:IIIIIIIIIIIIIII,,.                          @@%@%@%@
 .OO8OZ8Z,,,,,,,,,,,,,,:O,,,,,,,,,Z:,,,:7$?,,,$$::,,,78OZ                       ZZZZZZ65
 OOOOOOOOO7OOOODOOOOO,,~O,,,,,,,,,Z:,,OOOOOOOOOOOOOIDOOOOO                      #0)#)#)#3
""" 
}

room_bar = {
    "name": "Bar",

    "description":
    """As you approach the bar you notice a rotten old sign hanging just above the door. You can faintly make out the words \'Liquor in the Front, Poker in the Back\'.
    You step over a drunken reveler to enter the bar and as you enter you're taken back by the smell and the noise of men singing and playing games.""",

    "exits": {"north": "Camp", "west": "Home"},

    "items": [],

    "market": [],

    "combat": False,

    "enemy": [],

    "max enemy": 0,

    "min enemy": 0,

    "check_item": [],

    "activity": "hi",

    "ascii":"""
                                                                                             
                                                                                                   
                                     #######(                                                      
                                     #######(                                                      
                                     #######(                                                      
                              (###########################################################*        
                             /#############################################################/       
                            (###############################################################,      
                           *#################################################################*     
                          (###################################################################,    
                         /#####################################################################*   
                        (#############################/¯¯¯¯¯¯¯¯¯¯¯¯\############################.  
                       *#############################|     BAR      |############################. 
                       ,,,,,,,/////////////////////// \____________/ //////////////////////*,,,,,,, 
                              ,,*,,,,,,,,,,,,,,,,,,**,,,,,,*,,,,,,,,,,,*,,,,,,,,,,,,,,,,,,,        
                              ,,,/,    ,    ,%,,,,,#,       .        %*,,,#.    .    ,**,,,        
                              ,,*/.    ,    .%,,,,,#*       .        %*,,,#.    .    ,*,,,,        
                              ,,,/.    ,    .%,,,,,#*       .        %*,,,#.    .    ,*,,,,        
       .######################,*,/.    ,    .%,,,,,#*       .        %*,,,#.    .    ,*,,,,        
       #######################,,*/.    ,    .%,,,,,#*       .        %*,,,#.    .    ,*,,,,        
      (#######################,,*/.    ,    .%,,,,,#*       .        %*,,,#.    .    ,*,,,,        
     #########################,*,*///////////**,,,,*******************,,*,************,,,,,        
    (#########################,,**%%%%%%%%%%%#,,,,,*//////////////////,,,,#%%%%%%%%%%%**,,,        
   ###########################,*,/,    ,    .%,,,,,/#################(,*,,#.    ,    ,*,,,,        
    .*************************,,*/.    ,    .%,,,,,/########%########(,,,,#.    .    ,*,,,,        
     *,,,#########%########/,,,,,/*....*....*%,,,,,/########%########(,,,,%,....*....**,,,,        
     ,,,,#########%########/,,,*,/.    ,    .%,,,,,/#####/*(%#(*(####(,,,,#.    .    ,*,,,,       (@##@)
     ,,,,#########%########/,,,*,/.    ,    .%,,,,,/######(####(#####(,,,,#.    .    ,*,,,,      (@@##@%)
     ,,,,#########%########/,,,*,//****/****/%,,,,,/#################(,,,,%*****/****(*,,,,      (@#@##@)
     ,,,,#########%########/,,,*,,,,,,,,,,,,,,,,,,,/########%########(,,,,,,,,,,,,,,,**,,,,      (#%@%##) 
     ....******************,.......................,///////*/*///////*.....................      (@####@)     
                                                                                                  (####)
""" 
    }

room_shop = {
    "name": "General Store",

    "description":
    """As you walk in, you hear the ting of the bell go off, you're in your local
store, it sells everything a regular person would need. The shopkeep grumbles and
raises his brow at you. "What you want?" """,

    "exits": {"north": "Bridge", "east": "Home"},

    "items": [],
    
    "market": [item_upg_sword, item_axe, item_chainmail, item_potion],

    "combat": False,

    "enemy": [],

    "max enemy": 0,

    "min enemy": 0,

    "check_item": [],

    "activity": [],

    "ascii":"""
                                                                  
______________________________________________________________________________________________
###############################################################################################
############################################/\#################################################
##########################################//   \\##############################################
########################################//      \\#############################################
######################################//           \\###########################################
####################################//               \\#########################################
##################################//                   \\#######################################
################################//                       \\#####################################
_______________________________|| ======================= ||____________________________________
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII||   |                      ||IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIII     ,    IIIIIIIIIIII||   |                     ||IIIIIIIIIIIII     ,     IIIIIIIIIIII
IIIIIIIII     ,    IIIIIIIIIIII||    _________            ||IIIIIIIIIIIII     ,     IIIIIIIIIIII
IIIIIIIII     ,    IIIIIIIIIIII||    |       |            ||IIIIIIIIIIIII     ,     IIIIIIIIIIII
IIIIIIIII     ,    IIIIIIIIIIII||    |       |            ||IIIIIIIIIIIII     ,     IIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII||    |       |            ||IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII||    |       |            ||IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
==============================//__________________________\\====================================
==============================||___________________________||===================================
=============================//_____________________________\\==================================
============================||_______________________________||=================================
===========================//_________________________________\\================================
==========================||___________________________________||===============================
                      
                                                                                                                                         
           
""" 
    }

room_bridge = {
        "name": "Bridge",

        "description":
        """You come across a path, with beaten roads and snapped branches. You notice a raging river ahead and an old broken up bridge.
        Nothing you can't fix with the right materials, even a 5 year old engineer could do it! Looking past the bridge you see the castle past the river and hear the faint crys of Isiah.""",


        "exits": {"south": "General Store", "north": "Castle"},

        "items": [],

        "market": [],

        "combat": True,

        "enemy": [enemy_kobold, enemy_bandit],

        "max enemy": 2,

        "min enemy": 1,

        "check_item": item_wood_block,

        "enemy_present": [],

        "activity": [],

        "ascii": """"""

}
room_castle = {
        "name": "Castle",

        "description":
        """As you enter the castle, you can see a set of armour scattered across the floor, chipped stone
on the walls and bloody arrows everywhere. There's clearly been a battle here.""",

        "exits": {"south": "Bridge", "north": "Cinncinati Zoo"},

        "items": [item_isiah],

        "market": [],

        "combat": True,

        "enemy": [enemy_bandit, enemy_rufian, enemy_rogue_knight, enemy_castle_mage],

        "max enemy": 4,

        "min enemy": 3,

        "check_item": [],

        "enemy_present": [],

        "activity": [],

        "ascii": """"""

        }

room_zoo = {
        "name": "Cinncinati Zoo",

        "description":
        """You've entered the entrance to the Zoo, you can sense your close to the source of the peril that
has purged your lands. All of the signs have been bent, written over and there seems to be recurring phrase
amongst the graffiti: "Dicks Out!". What this means is unknown to you.""",

        "exits": {"south": "Castle", "north": "Harambe's Pen"},

        "items": [],

        "market": [],

        "combat": True,

        "enemy": [enemy_kobold],

        "max enemy": 2,

        "min enemy": 1,

        "check_item": [], 

        "enemy_present": [],

        "activity": [], 

        "ascii": """"""  

        }

room_harambe = {
        "name": "Harambe's Pen",

        "description":
        """As you enter you can hear the snorts coming from who is known as Harambe. He sits in wait for challengers
on his thrown, the anarchy of the situation is clear, with blood and corpsers of previous challengers laiden on the ground.
There are cages to the left and right of him, with children caged up inside. It is no fake warlord you are fighting here.""",

        "exits": {"south": "Cinncinati Zoo"},

        "items": [],

        "market": [],

        "combat": True,

        "enemy": [enemy_harambe],

        "max enemy": 2,

        "min enemy": 1,

        "check_item": [], 

        "enemy_present": [],

        "activity": [], 

        "ascii": """"""  
}

room_forest = {
        "name": "Forest",

        "description":
        """This forest has a weird tinge to it, mist covers the ground, the trees bare no leaves
there is no life here. It feels cold and eary, once inside, escaping will be difficult.""",

        "exits": {"south": "Home", "east": "Camp"},

        "items": [item_wood_block],

        "market": [],

        "combat": True,

        "enemy": [enemy_kobold, enemy_harambe_warrior],

        "max enemy": 3,

        "min enemy": 2,

        "check_item": item_axe,

        "enemy_present": [],

        "activity": [], 

        "ascii": """"""

    }

room_camp = {
        "name": "Camp",

        "description":
        """The camp has been burnt to a crisp but you can still spot remnants of salvagable gear. Along with
some shady members.""",

        "exits": {"west": "Clearing", "north": "Clearing2", "south": "Bar"},

        "items": [item_sword],

        "market": [],

        "combat": True,

        "enemy": [enemy_bandit, enemy_kobold, enemy_rufian, enemy_harambe_warrior],

        "max enemy": 5,

        "min enemy": 2,

        "check_item": [],

        "enemy_present": [],

        "activity": [], 

        "ascii": """"""
}
room_festival_grounds = {
        "name": "Festival Grounds",

        "description":
        """clearing""",

        "exits": {"south": "Camp","west": "Cinncinati Zoo"},

        "items": [],

        "market":[],

        "combat": False,

        "enemy": [],

        "max enemy": 0,

        "min enemy": 0,

        "check_item": item_isiah,

        "activity": [], 

        "ascii": """"""
}
room_clearing = {
        "name": "Clearing",

        "description":
        """ clearing""",

        "exits": {"west": "Forest", "east": "Camp"},

        "items": [],

        "market": [],

        "combat": False,

        "enemy": [],

        "max enemy": 0,

        "min enemy": 0,

        "check_item": [],

        "activity": [], 

        "ascii": """"""
}

rooms = {
        "Home": room_home,
        "Bar": room_bar,
        "General Store": room_shop,
        "Bridge": room_bridge,
        "Castle": room_castle,
        "Cinncinati Zoo": room_zoo,
        "Harambe's Pen": room_harambe,
        "Forest": room_forest,
        "Camp": room_camp,
        "Clearing": room_clearing,
        "Clearing2": room_festival_grounds
}
