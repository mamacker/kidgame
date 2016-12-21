class Stuff:
  name = ""
  desc = ""
  isWeapon = False
  damage = 1
  visible = False
  points = 0
  isEdible= False
  isArmor = False

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
