class Player:
  name = "Kid"
  desc = "Scruffy looking boy with a wirey frame."
  stuff = []
  health = 10
  armor = 0
  currentRoom = None;

  def getArmorTotal(self):
    total = 0
    for item in self.stuff:
      if item.isArmor:
        total = total + item.damage;
    return total
    
  def assignArmorDamage(self, howMuch):
    armorLeft = self.getArmorTotal();
    armorUsed = 0;
    for item in self.stuff:
      if item.isArmor:
        damageLeft = item.damage;
        if damageLeft > howMuch:
          item.damage = item.damage - howMuch;
          howMuch = 0
          armorUsed = armorUsed + howMuch
        else:
          howMuch = howMuch - damageLeft;
          armorUsed = armorUsed + damageLeft
          item.damage = 0
      
      if howMuch <= 0:
        break

    return howMuch, damageLeft
  
  def __init__(self):
    stuff = []
    health = 10

