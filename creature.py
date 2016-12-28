import stuff
import copy
import random

Stuff = stuff.Stuff

""" This is the file to edit if you'd like to add a monster, or a potential bit of treassure! """

class Creature:
  creatureArt = {
    "gnat": """
   \__/
   (oo)
  //||\\\\""",
    "octopus": """
   ,---.
  ( @ @ )
   ).-.(
  '/|||\`
    '|`  
  """,
    "lizard": """
              ___   
       )/_  ,@  /   
       |(_,' _@/    
       |    /       
  \\)/ /    (_)/     
  ((_/   ,----~     
   \\    (_)/        
   / ,-----~        
  (('  _,-.         
   \\\\=//   
  """,
    "cat": """
  /\\___/\\
  \\ -.- /
  `-.^.-'
  """,
    "dragon": """
    .     _///_,
   .      / ` ' '>
     )   o'  __/_'>
    (   /  _/  )_\\'>
     ' "__/   /_/\\_>
         ____/_/_/_/
        /,---, _/ /
       ""  /_/_/_/
          /_(_(_(_                 \\
         (   \\_\\_\\\\_               )\\
          \\'__\\_\\_\\_\\__            ).\\
          //____|___\\__)           )_/
          |  _  \\'___'_(           /'
           \\_ (-'\\'___'_\\      __,'_'
           __) \\  \\\\___(_   __/.__,'
        ,((,-,__\\  '", __\\_/. __,'
                     '"./_._._-'
  """,
    "goat": """
(_(
/_/'_____/)
"  |      |
   |\"\"\"\"\"\"| 
  """,
    "skeleton": """
     .-.
    (o.o)
    |=|
    __|__
  //.=|=.\\\\
 // .=|=. \\\\
 \\\\ .=|=. //
  \\\\(_=_)//
   (:| |:)
    || ||
    () ()
    || ||
    || ||
   ==' '==
    """,
    "toad": """
     @..@        
    (\\--/)      
   (.>__<.)               
   ^^^  ^^^
    """,};
  name = ""
  desc = ""
  damage = 1
  visible = True
  treasure = None
  dexterity = 5
  art = None

  potentialTreasure = [
    Stuff("gold coin","shiny", False, .2, 1),
    Stuff("gold ring","shiny", False, .2, 2),
    Stuff("gold idol","shiny", False, .2, 3),
    Stuff("gold shoe","shiny", False, .2, 1),
    Stuff("gold pacifier","shiny", False, .2, 2),
    Stuff("sword","curved arabian", True, 6, 3),
    Stuff("helmet","rusty", False, 2, 3, 9, False, True),
    Stuff("chest plate","rusty", False, 4, 3, 0, False, True),
    Stuff("gauntlet", "rusty", False, 1, 1, 0, False, True),
    Stuff("gold tooth","shiny", False, .2, 1),
    Stuff("golden crown","busted", False, .2, 5),
    Stuff("health potion","magic", False, .2, 5, 5, True)
  ]

  potentialCreature = []

  @staticmethod
  def getRandomCreature():
    return copy.deepcopy(Creature.potentialCreature[random.randint(0,len(Creature.potentialCreature) - 1)])

  def __init__(self, name, desc, damage, health = 0, dexterity = 5, art = None):
    self.name = name
    self.desc = desc
    self.damage = damage
    self.health = health
    self.art = art
    self.treasure = copy.deepcopy(self.potentialTreasure[random.randint(0,len(self.potentialTreasure) - 1)])


""" Name and description of the creature are show when a battle starts. """
""" Desc is the description. """
""" Damage - is the max amount of potential damage a monster can do. """
""" Health - is how many hits of damage the creature can take before dying. """
""" Dexterity - controls how hard it is to hit a creature. 5 is average, higher numbers are more difficult to hit. """
""" Art - the ascii art that will be drawn when the battle starts! """
"""name, desc, damage, health = 0, dexterity = 5, art = None """
Creature.potentialCreature = [
  Creature("skeleton", "Dangerous", 2, 2, 5, Creature.creatureArt["skeleton"]),
  Creature("dragon", "Deadly", 7, 5, 7, Creature.creatureArt["dragon"]),
  Creature("lizard", "Small", 1, 1, 5, Creature.creatureArt["lizard"]),
  Creature("octopus", "slimy, creepy, crawly", 3, 15, 5, Creature.creatureArt["octopus"]),
  Creature("glob", "slimy, acid, teenage", 10, 10),
  Creature("toad", "evil", 3, 10, 4, Creature.creatureArt["toad"]),
  Creature("troll", "dumb", 3, 15, 3),
  Creature("pumpkin", "grinning", 3, 5),
  Creature("dog", "vicious", 3, 3, 6),
  Creature("gnat", "tiny", 3, 1, 8, Creature.creatureArt["gnat"]),
  Creature("gnat", "medium", 3, 2, 8, Creature.creatureArt["gnat"]),
  Creature("gnat", "collosal", 4, 2, 8, Creature.creatureArt["gnat"]),
  Creature("goat", "psyco", 3, 2, 10, Creature.creatureArt["goat"]),
  Creature("kitten", "kuddle", 1, 20, 5, Creature.creatureArt["cat"]),
]
