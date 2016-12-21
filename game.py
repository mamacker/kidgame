import random
import time
import re
import copy

class Player:
  name = "Kid"
  desc = "Scruffy looking boy with a wirey frame."
  stuff = []
  health = 10
  armor = 0
  currentRoom = None;

  def __init__(self):
    stuff = []
    health = 10

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

class Map:
  '''def __init__(self, name, desc, isWeapon, damage, points = 1, 
                health = 0, isEdible = False, isArmor = False):'''
  potentialStuff = [Stuff("knife", "rusty", True, 1),
                    Stuff("gold coin","shiny", False, .2),
                    Stuff("torch","Lasts about 1 hour", False, .5),
                    Stuff("sword","rusty", True, 4),
                    Stuff("staff","brutal", True, 3),
                    Stuff("sword","shiny", True, 6),
                    Stuff("broad sword","chipped", True, 5),
                    Stuff("broad sword","shiny", True, 7),
                    Stuff("dirt", "Smelly", False, .3),
                    Stuff("gauntlet", "rusty", False, 1, 1, 0, False, True),
                    Stuff("health potion","magic", False, .2, 5, 5, True),
                    Stuff("boots of butt kicking","spikey", True, 8),
                    ]
  potentialCreature = [Creature("skeleton", "Dangerous", 2, 2),
                        Creature("dragon", "Deadly", 7, 5),
                        Creature("lizard", "Small", 1, 1),
                        Creature("octopus", "slimy, creepy, crawly", 3, 15),
                        Creature("glob", "slimy, acid, teenage", 10, 10),
                        Creature("toad", "evil", 3, 10),
                        Creature("troll", "dumb", 3, 15),
                        Creature("dog", "vicious", 3, 3)
                        ]
  rooms = []

  def __init__(self):
    self.rooms = [Room() for i in range(200)];

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


map = None;

def buildMap():
  global map;
  map = Map()
  map.generateRooms();

def goLeft(kid):
  if kid.currentRoom.left != None:
    kid.currentRoom = kid.currentRoom.left
  else:
    return None
  return kid

def goRight(kid):
  if kid.currentRoom.right != None:
    kid.currentRoom = kid.currentRoom.right
  else:
    return None
  return kid

def goForward(kid):
  if kid.currentRoom.forward != None:
    kid.currentRoom = kid.currentRoom.forward
  else:
    return None
  return kid

def goBack(kid):
  if kid.currentRoom.back != None:
    kid.currentRoom = kid.currentRoom.back
  else:
    print "You can't go back!"
    return None
  return kid

def search(kid):
  room = kid.currentRoom;
  contents = room.contents
  stuffSeen = False
  if not len(contents) == 0:
    for thing in contents:
      stuffSeen = True
      print("This room has a " + thing.desc + " " + thing.name) 
      thing.visible = True
  if stuffSeen == False:
    print("There is nothing in this room.")
  return kid

def take(kid):
  room = kid.currentRoom;
  contents = kid.currentRoom.contents
  itemFound = False
  for item in contents:
    if item.visible == True:
      itemFound = True
      kid.stuff.append(item)
      kid.currentRoom.contents.remove(item)
      print("You took " + item.desc + " " + item.name);
      if item.isEdible and item.name == "health potion":
        print("It was a health potion!") 
        time.sleep(1)
        print("Glug")
        time.sleep(1)
        print("Glug")
        time.sleep(1)
        print("Glug")
        time.sleep(1)
        print("Buuuuuuuuuuurrrrrrrrrrpp!");
        time.sleep(1)
        print("You were healed " + str(item.health))
        kid.health = kid.health + item.health
      if item.isArmor:
        print("This has a little armor value! You now have " + str(item.damage) + " more armor pts.")
        kid.armor = kid.armor + item.damage
  
  if itemFound == False:
    print("There was nothing found!  Did you search the room?");

  return kid

def fight(kid, monster):
  alive = True;
  monsterAlive = True;

  #pick the strongest weapon on the kid, start with fists
  weapon = Stuff("fists","bare", True, .1)

  for item in kid.stuff:
    if item.isWeapon:
      if item.damage > weapon.damage:
        weapon = item;

  print("You decide to fight with " + weapon.desc + " " + weapon.name);
  print("You have " + str(kid.health) + " health. And " + str(kid.armor) + " armor pts.")

  while alive and monsterAlive:
    print "You swing with " + weapon.name;
    time.sleep(2)
    
    if random.randint(0,1) == 1:
      print " and hit!"
      monster.health = monster.health - random.randint(1,weapon.damage);
    else:
      print " and, ooooh noooo, miss!"

    time.sleep(2)
    print "The monster has " + str(monster.health) + " health left!";
    time.sleep(2)
    if monster.health < 1:
      monsterAlive = False;
    else:
      print("The monster attacks! His hits could do " + str(monster.damage) + " damage!")
      time.sleep(2)
      print("The monster swings...");
      time.sleep(2)
      if random.randint(0,1) == 1:
        damage = random.randint(1, monster.damage);
        print("and hits for " + str(damage) + "!!!")
        if kid.armor > 0:
          damage = damage - kid.armor;
          print("Your armor takes " + str(kid.armor) + " of it. You take " + str(damage) + " damage.")
        kid.health = kid.health - damage;
      else:
        print("and missed!!!")

      time.sleep(2)
      if kid.health <= 0:
        print "XXXXXXXXXXXXXXXXXXXXXXXXXXX :( XXXXXXXXXXXXXXXXXXXXXXXXXX"
        print "Oh no!!!";
        time.sleep(2)
        print "You died!!!"
        alive = False;
      else:
        print "You lived!!!"
        print("You have " + str(kid.health) + " health left.")

    time.sleep(2)

  if alive:
    print "!!!!!!!!!!!!!!!!!!!!!! Yay! !!!!!!!!!!!!!!!!!!!!!!!!!"
    print "You have defeated the " + monster.name
    kid.currentRoom.contents.append(monster.treasure);
    kid.currentRoom.contents.remove(monster)
    print "You should probably search the room!";
  else:
    print "The monster has killed you.  So, very, very sad..."
    points = 0;
    for item in kid.stuff:
      if item.points:
        print "You had a " + item.name;
        points = points + item.points
    print "But... you got " + str(points) + " points!!! Well done!"
    kid.currentRoom.name = "End"
  
  return kid;

def runAway(kid, monster):
  print "You try..."
  time.sleep(2)
  print "You made it!!!"
  kid.currentRoom = kid.currentRoom.back;
  return kid;

def handleMonsterAction(kid, monster):
  print "<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>";
  print "The monster wont let you pass!!!"
  func = None
  while func == None:
    print "You can try to run - but the monster might kill you."
    print "You can try to fight - but the battle will be gruelling."
    print "What do you want to do?"
    action = str(raw_input("(fight or run)> "))
    
    def f(x):
      return {
        'fight': fight,
        'f': fight,
        'run': runAway,
        'r': runAway 
      }.get(x, None)

    func = f(action);

    if func == None:
      print("I don't know what you mean.")

  result = func(kid,monster)
  return result;

def actionPrompt(kid):
  print('\n--------------------------------------------------');
  print('You are in ' + kid.currentRoom.desc + '.  It has ' + str(kid.currentRoom.ctDoors()) + " exits.");
  print('You can search the room.');

  if (kid.currentRoom.hasMonster() == True):
    kid, monster = kid.currentRoom.handleMonster(kid);
    kid = handleMonsterAction(kid, monster);

    if kid.currentRoom.name == "End":
      return kid
    
  if (kid.currentRoom.left != None): print('You can go left.')
  if (kid.currentRoom.right != None): print('You can go right.')
  if (kid.currentRoom.forward != None): print('You can go forward.')
  if (kid.currentRoom.back != None): print('Or you can go back.')
  for thing in kid.currentRoom.contents:
    if not isinstance(thing, Creature) and thing.visible == True:
      print("You can take " + thing.desc + " " + thing.name);
  action = str(raw_input("> "))
  return action

def inventory(kid):
  stuffFound = False
  if len(kid.stuff) == 0:
    print("You don't have anything.")
  else:
    for item in kid.stuff:
      print("You have a " + item.desc + " " + item.name);

def health(kid):
  print("You have " + str(kid.health) + " health.");

def chooseRoom(kid):
  result = None
  while result == None:
    action = actionPrompt(kid);

    if kid.currentRoom.name == "End":
      result = kid
      break

    print "---------------------------------------------------------------"
    print "\nYou entered: " + action

    if re.match(r'take', action, re.I):
      action = "take"

    def quit(kid):
      points = 0;
      for item in kid.stuff:
        if item.points:
          print "You had a " + item.name;
          points = points + item.points
      print "You got " + str(points) + " points!!! Well done!"
      raise

    def f(x):
      return {
        'left': goLeft,
        'l': goLeft,
        'go left': goLeft,
        'right': goRight,
        'r': goRight,
        'go right': goRight,
        'forward': goForward,
        'go forward': goForward,
        'f': goForward,
        'back': goBack,
        'go back': goBack,
        'b': goBack,
        'search': search,
        's': search,
        'search the room': search,
        'search room': search,
        'take': take,
        't': take,
        'inventory': inventory,
        'i': inventory,
        'inv': inventory,
        'health': health,
        'h':health,
        'quit': quit,
        'q': quit
      }.get(x, None)
    func = f(action);
    if func == None:
      print("I don't know what you mean.")
      result = None
    else:
      result = f(action)(kid)
  return result

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
  buildMap();
  kid = Player();
  kid.stuff = []
  kid.currentRoom = map.rooms[0];

  try:
    while not kid.currentRoom.name == "End":
      kid = chooseRoom(kid)

    playAgain = raw_input('Do you want to play again? (yes or no)\r\n');
  except:
    playAgain = "no"
    

print ("\n\nGoodbye!");
