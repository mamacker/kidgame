import random
import time
import re
import copy
import stuff
import player
import creature
import room
import map
import os

Stuff = stuff.Stuff
Player = player.Player
Creature = creature.Creature
Room = room.Room
Map = map.Map

map = None;

def buildMap():
  global map;
  map = Map()
  map.generateRooms();

def clearScreen():
  os.system('cls')
  os.system('clear')


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
        print("This has armor value! You now have " + str(item.damage) + " more armor pts.")
  
  if itemFound == False:
    print("There was nothing found!  Did you search the room?");

  return kid

def fight(kid, monster):
  alive = True;
  monsterAlive = True;

  #pick the strongest weapon on the kid, start with fists
  weapon = Stuff("fists","bare", True, 1)

  for item in kid.stuff:
    if item.isWeapon:
      if item.damage > weapon.damage:
        weapon = item;

  print("You decide to fight with " + weapon.desc + " " + weapon.name);
  print("You have " + str(kid.health) + " health. And " + str(kid.getArmorTotal()) + " armor pts.")

  while alive and monsterAlive:
    print "You swing with " + weapon.name;
    time.sleep(2)
    
    if random.randint(0,10) >= monster.dexterity:
      print " and hit!"
      monster.health = monster.health - random.randint(1, weapon.damage);
    else:
      print " and, ooooh noooo, miss!"

    time.sleep(2)
    print "The " + monster.name +" has " + str(monster.health) + " health left!";
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
        if kid.getArmorTotal() > 0:
          damage, taken = kid.assignArmorDamage(damage)
          if damage < 0:
            damage = 0
          print("Your armor takes " + str(taken) + " of it. You take " + str(damage) + " damage.")
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
    print "The " + monster.name + " has killed you.  So, very, very sad..."
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
    if monster.art != None:
      print monster.art
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
  
    clearScreen()
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

  #try:
  while not kid.currentRoom.name == "End":
    kid = chooseRoom(kid)

  playAgain = raw_input('Do you want to play again? (yes or no)\r\n');
  #except:
  #  playAgain = "no"
    

print ("\n\nGoodbye!");
