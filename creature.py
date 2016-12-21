import stuff
import copy
import random

Stuff = stuff.Stuff

class Creature:
  name = ""
  desc = ""
  damage = 1
  visible = True
  treasure = None

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

  def __init__(self, name, desc, damage, health = 0):
    self.name = name
    self.desc = desc
    self.damage = damage
    self.health = health
    self.treasure = copy.deepcopy(self.potentialTreasure[random.randint(0,len(self.potentialTreasure) - 1)])

