import random
import copy
import creature
import stuff

Stuff = stuff.Stuff
Creature = creature.Creature

class Room:
  name = "standard"
  desc = """long, cold and dark """
  contents = []
  people = []
  treasure = None
  doors = 0
  left = None
  right = None
  forward = None
  back = None

  @staticmethod
  def buildRoom(previous):
    room = Room();
    if random.randint(0,100) > 70:
      room.contents = [Stuff.getRandomStuff()]
    if random.randint(0,100) > 70:
      if len(room.contents) == 0:
        room.contents = []
      room.contents.append(Creature.getRandomCreature())

    room.back = previous
    return room;

  def createRoom(self, desc, contents, left, right, forward, back):
    self.desc = desc
    self.contents = contents
    self.left = left
    self.right = right
    self.forward = forward
    return self

  def ctDoors(self):
    ct = 0;
    if (self.left): ct += 1
    if (self.right): ct += 1
    if (self.forward): ct += 1
    return ct

  def hasMonster(self):
    for item in self.contents:
      if isinstance(item, Creature):
        return True
    return False

  def handleMonster(self, kid):
    monster = None
    for item in self.contents:
      if isinstance(item, Creature):
        monster = item
    if not monster == None:
      print("Oh no!  There is a: " + monster.desc + " " + monster.name)
      return (kid, monster)
    return kid, None
