import copy
import random

class Stuff:
  name = ""
  desc = ""
  isWeapon = False
  damage = 1
  visible = False
  points = 0
  isEdible= False
  isArmor = False

  potentialStuff = []  
  
  @staticmethod
  def getRandomStuff():
    return copy.deepcopy(Stuff.potentialStuff[random.randint(0,len(Stuff.potentialStuff) - 1)])


  def __init__(self, name, desc, isWeapon, damage, points = 1, 
                health = 0, isEdible= False, isArmor = False):
    self.name = name
    self.desc = desc
    self.isWeapon = isWeapon
    self.damage = damage
    self.points = points
    self.isEdible= isEdible
    self.health = health
    self.isArmor = isArmor


Stuff.potentialStuff = [
  Stuff("knife", "rusty", True, 2),
  Stuff("gold coin","shiny", False, .2),
  Stuff("torch","Lasts about 1 hour", False, .5),
  Stuff("sword","rusty", True, 4),
  Stuff("staff","brutal", True, 4),
  Stuff("sword","shiny", True, 6),
  Stuff("broad sword","chipped", True, 5),
  Stuff("broad sword","shiny", True, 7),
  Stuff("dirt", "Smelly", False, .3),
  Stuff("gauntlet", "rusty", False, 1, 1, 0, False, True),
  Stuff("chestplate", "rusty", False, 3,2, 0, False, True),
  Stuff("wood board", "rotten", True, 3, 1, 0, False, False),
  Stuff("health potion","magic", False, .2, 5, 5, True),
  Stuff("boots of butt kicking","spikey", True, 8),
  Stuff("lance of light","glowing", True, 8),
  Stuff("bucket","stupid", True, 1),
  Stuff("toothbrush of doom","scary", True, 5),
  Stuff("glove","the slapping", True, 2),
]

