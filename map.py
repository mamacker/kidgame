import copy
import time
import random
import stuff
import creature
import player
import room

Stuff = stuff.Stuff
Creature = creature.Creature
Room = room.Room
Player = player.Player

class Map:
  '''def __init__(self, name, desc, isWeapon, damage, points = 1, 
                health = 0, isEdible = False, isArmor = False):'''
  rooms = []

  def __init__(self):
    self.rooms = [Room() for i in range(300)];

  def checkMap(self):
    for room in rooms:
      if not room.name == "start":
        if room.back == None:
          return False;
    return True

  def buildRoom(self, previous):
    room = Room();
    if random.randint(0,100) > 70:
      room.contents = [Stuff.getRandomStuff()]
    if random.randint(0,100) > 70:
      if len(room.contents) == 0:
        room.contents = []
      room.contents.append(Creature.getRandomCreature())

    room.back = previous
    return room;

  def generateRooms(self):
    potentialDescriptions = [
      "a dungeon.  Its a dirty, cold and dark room",
      "a kitchen. Its a stinky and dusty room",
      "a bathroom. It has a broken toilet.  You really don't like this room",
      "a bedroom.  There is a shattered bed.  Its a scary room",
      "the kings room.  There is a destroyed chest.  The throne is broken",
      "another dungeon.  This one has a skeleton on the wall",
      "weapon room.  Broken weapons lay strewn about.",
      "a mud room.  There is no floor.  Its a gross room",
      "a closet.  There is a hidden door broken open.  Its a small room",
    ]
    roomCt = 0;
    for i in range(0, 100):
      if i == 0:
        self.rooms[0] = Room();
        self.rooms[0].name = "start"
        self.rooms[0].desc = potentialDescriptions[random.randint(0, len(potentialDescriptions) -1)]
        self.rooms[0].contents = [Stuff.getRandomStuff()];
        room = self.rooms[0]
      else:
        self.rooms[i] = self.buildRoom(self.rooms[i-1])
        self.rooms[i].desc = potentialDescriptions[random.randint(0, len(potentialDescriptions) -1)]
        self.rooms[i-1].forward = self.rooms[i];
        room = self.rooms[i]
      roomCt += 1

    #Build side rooms
    for i in range(0,50):
      roomIndex = random.randint(0, roomCt - 1);
      if self.rooms[roomIndex].left == None:
        self.rooms[roomIndex].left = self.buildRoom(self.rooms[roomIndex])
        self.rooms[roomCt] = self.rooms[roomIndex].left;
      if self.rooms[roomIndex].right == None:
        self.rooms[roomIndex].right = self.buildRoom(self.rooms[roomIndex])
        self.rooms[roomCt] = self.rooms[roomIndex].right;
      roomCt += 1;

    self.rooms[roomCt - 1].name = "End";

    print("There are now: " + str(roomCt) + " rooms.");

