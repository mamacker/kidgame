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
  roomDrawGrid = []

  def checkMap(self):
    for room in self.rooms:
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
    for i in range(0, 50):
      if i == 0:
        self.rooms.append(Room());
        firstRoom = self.rooms[0];
        firstRoom.name = "start"
        firstRoom.desc = potentialDescriptions[random.randint(0, len(potentialDescriptions) -1)]
        firstRoom.contents = [Stuff.potentialStuff[0]];
        firstRoom.height = 4;
        firstRoom.depth = 0;
        room = firstRoom;
      else:
        curRoom = Room.buildRoom(self.rooms[i-1]);
        self.rooms.append(curRoom)
        curRoom.desc = potentialDescriptions[random.randint(0, len(potentialDescriptions) -1)]
        self.rooms[i-1].forward = curRoom
        curRoom.depth = roomCt;
        room = curRoom
      roomCt += 1

    lastRoom = self.rooms[roomCt-1];
    lastRoom.name = "End";
    lastRoom.contents.append(Creature.getRandomCreature())

    #Build side rooms
    for i in range(0,25):
      roomIndex = random.randint(0, roomCt - 1);
      if self.rooms[roomIndex].left == None:
        self.rooms[roomIndex].left = Room.buildRoom(self.rooms[roomIndex])
        self.rooms[roomIndex].left.depth = self.rooms[roomIndex].depth;
        self.rooms.append(self.rooms[roomIndex].left);
      if self.rooms[roomIndex].right == None:
        self.rooms[roomIndex].right = Room.buildRoom(self.rooms[roomIndex])
        self.rooms[roomIndex].right.depth = self.rooms[roomIndex].depth;
        self.rooms.append(self.rooms[roomIndex].right);
        
      roomCt += 1;

    self.walkMap(self.rooms[0]);
    self.drawMap();

  def updateVisited(self, kid):
    kid.currentRoom.visited = True

  def walkMap(self, room):
    room.drawn = True;
    if room.left:
      room.left.height = room.height - 2;
      room.left.depth = room.depth + 1;
      self.walkMap(room.left);

    if room.forward:
      room.forward.depth = room.depth + 2;
      room.forward.height = room.height;
      self.walkMap(room.forward)

    if room.right:
      room.right.height = room.height + 1;
      room.right.depth = room.depth + 1;
      self.walkMap(room.right)
  
  def drawMap(self, kid = None):
    maxDepth = 0
    for room in self.rooms:
      if maxDepth < room.depth:
        maxDepth = room.depth

    maxHeight = 0
    minHeight = 15
    for room in self.rooms:
      if maxHeight < room.height:
        maxHeight = room.height
      if room.height != 0 and room.height < minHeight:
        minHeight = room.height;

    for y in range(0, maxHeight + 1):
      print('');
      for x in range(0, maxDepth + 1):
        foundOne = False
        for room in self.rooms:
          if room.height == y and room.depth == x:
            if room.visited:
              foundOne = True
              if kid.currentRoom == room:
                print('P', end="")
              else: 
                print('*', end="")
        if not foundOne:
          print(' ', end="")
    return 

  def updateMap(self, kid):
    self.updateVisited(kid);
    room = self.rooms[0]
    self.drawMap(kid);

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
      print("You can't go back!")
      returnVal = None
    self.updateMap(kid);
    return returnVal

