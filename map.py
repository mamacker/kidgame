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
  rooms = []
  maxRoomWidth = 0

  def __init__(self):
    self.rooms = [Room() for i in range(300)];

  def checkMap(self):
    for room in rooms:
      if not room.name == "start":
        if room.back == None:
          return False;
    return True


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
        self.rooms[i] = Room.buildRoom(self.rooms[i-1])
        self.rooms[i].desc = potentialDescriptions[random.randint(0, len(potentialDescriptions) -1)]
        self.rooms[i-1].forward = self.rooms[i];
        room = self.rooms[i]
      roomCt += 1

    #Build side rooms
    for i in range(0,50):
      roomIndex = random.randint(0, roomCt - 1);
      if self.rooms[roomIndex].left == None:
        self.rooms[roomIndex].left = Room.buildRoom(self.rooms[roomIndex])
        self.rooms[roomCt] = self.rooms[roomIndex].left;
      if self.rooms[roomIndex].right == None:
        self.rooms[roomIndex].right = Room.buildRoom(self.rooms[roomIndex])
        self.rooms[roomCt] = self.rooms[roomIndex].right;
      roomCt += 1;

    self.rooms[roomCt - 1].name = "End";

    print("There are now: " + str(roomCt) + " rooms.");

  def updateVisited(self, kid):
    kid.currentRoom.visited = True

  def walkMap(self, room):
    if room.left:
      print("/")
      room.left.distFromCenterHall = room.distFromCenterHall + 1;
      if abs(maxRoomWidth) < abs(room.left.distFromCenterHall):
        maxRoomWidth = abs(room.left.distFromCenterHall)
      self.walkMap(room.left);

    print("-")

    if room.right:
      print("\\")
      room.right.distFromCenterHall = room.distFromCenterHall + 1;
      if abs(maxRoomWidth) < abs(room.right.distFromCenterHall):
        maxRoomWidth = abs(room.right.distFromCenterHall)
      self.walkMap(room.right)
  
  def updateMap(self, kid):
    self.updateVisited(kid);
    room = self.rooms[0]
    self.walkMap(room);

  def goLeft(self, kid):
    returnVal = kid;
    if kid.currentRoom.left != None:
      kid.currentRoom = kid.currentRoom.left
    else:
      returnVal = None

    self.updateMap(kid);
    return returnVal

  def goRight(self, kid):
    returnVal = kid;
    if kid.currentRoom.right != None:
      kid.currentRoom = kid.currentRoom.right
    else:
      returnVal = None
    self.updateMap(kid);
    return returnVal

  def goForward(self, kid):
    returnVal = kid;
    if kid.currentRoom.forward != None:
      kid.currentRoom = kid.currentRoom.forward
    else:
      returnVal = None
    self.updateMap(kid);
    return returnVal

  def goBack(self, kid):
    returnVal = kid;
    if kid.currentRoom.back != None:
      kid.currentRoom = kid.currentRoom.back
    else:
      print "You can't go back!"
      returnVal = None
    self.updateMap(kid);
    return returnVal

