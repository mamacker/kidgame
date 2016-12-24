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
  potentialStuff = [Stuff("knife", "rusty", True, 2),
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
  potentialCreature = [Creature("skeleton", "Dangerous", 2, 2, 5, Creature.creatureArt["skeleton"]),
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
      room.contents = [copy.deepcopy(self.potentialStuff[random.randint(0,len(self.potentialStuff) - 1)])]
    if random.randint(0,100) > 70:
      if len(room.contents) == 0:
        room.contents = []
      room.contents.append(copy.deepcopy(self.potentialCreature[random.randint(0,len(self.potentialCreature) - 1)]))

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
        self.rooms[0].contents = [copy.deepcopy(self.potentialStuff[0])];
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

