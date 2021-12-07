import time
import classFramework as cf
import charCreate as cc
import encountersystem as ecs
#import store

#player1 = cc.player1
#goblin = cc.baseGoblin
#boss = cc.baseBoss
#print(player1)

#state class = (health,attack,defen,speed,currentpos,gold,weapon)

#map1 solution = n*3,w*2,s*1,w*1,s*1,w*1,s*2,e*2

print("You enter a room and the door behind closes")
playerPos = cf.position(cf.playerStartPos_x,cf.playerStartPos_y)  #initiallized players current position
playerPos = cf.map.adjustMapPos(cf.map1) #moves player to center of map
directionSelectionMode = 1
while directionSelectionMode == 1:
  if cf.map1[playerPos.x][playerPos.y] == "17": #Triggers end of game
    directionSelectionMode = 0
  playerInput = str.lower(input("which direction do you want to go...? (North, East, South, West) ")) #Asks for player input
  if playerInput == "west" or playerInput == "w": 
    playerPos = playerPos.addMove(cf.west)
    if cf.map1[playerPos.x][playerPos.y] == -1:
      print("Theres a wall to the west. Turning around...")
      playerPos = playerPos.addMove(cf.east)
    print("testcode: currentPos= " + str(playerPos) + str(cf.map1[playerPos.x][playerPos.y]))
    battlestate = ecs.encDic[int(cf.map1[playerPos.x][playerPos.y])]() #runs the battle() command
    if battlestate == 1:
      ecs.encStateDic[int(cf.map1[playerPos.x][playerPos.y])] = 1
    if battlestate == 2:
      playerPos = playerPos.addMove(cf.east)
    if battlestate == 3:
      print("you have died")
      print()
      print()
      directionSelectionMode = 0

  elif playerInput == "east" or playerInput == "e":
    playerPos = playerPos.addMove(cf.east)
    if cf.map1[playerPos.x][playerPos.y] == -1:
      print("Theres a wall to the east. Turning around...")
      playerPos = playerPos.addMove(cf.west)
    print("testcode: currentPos= " + str(playerPos) + str(cf.map1[playerPos.x][playerPos.y]))
    battlestate = ecs.encDic[int(cf.map1[playerPos.x][playerPos.y])]()  #runs the battle() command
    if battlestate == 1:
      ecs.encStateDic[int(cf.map1[playerPos.x][playerPos.y])] = 1
    if battlestate == 2:
      playerPos = playerPos.addMove(cf.west)
    if battlestate == 3:  #Triggers end of game
      print("you have died")
      print()
      print()
      directionSelectionMode = 0

  elif playerInput == "north" or playerInput == "n":
    playerPos = playerPos.addMove(cf.north)
    if cf.map1[playerPos.x][playerPos.y] == -1:
      print("Theres a wall to the north. Turning around...")
      playerPos = playerPos.addMove(cf.south)
    print("testcode: currentPos= " + str(playerPos) + str(cf.map1[playerPos.x][playerPos.y]))
    battlestate = ecs.encDic[int(cf.map1[playerPos.x][playerPos.y])]() #runs the battle() command
    if battlestate == 1:
      ecs.encStateDic[int(cf.map1[playerPos.x][playerPos.y])] = 1
    if battlestate == 2:
      playerPos = playerPos.addMove(cf.south)
    if battlestate == 3:  #Triggers end of game
      print("you have died")
      print()
      print()
      directionSelectionMode = 0

  elif playerInput == "south" or playerInput == "s":
    playerPos = playerPos.addMove(cf.south)
    if cf.map1[playerPos.x][playerPos.y] == -1:
      print("Theres a wall to the south. Turning around...")
      playerPos = playerPos.addMove(cf.north)
    print("testcode: currentPos= " + str(playerPos) + str(cf.map1[playerPos.x][playerPos.y]))
    battlestate = ecs.encDic[int(cf.map1[playerPos.x][playerPos.y])]()  #runs the battle() command
    if battlestate == 1:
      ecs.encStateDic[int(cf.map1[playerPos.x][playerPos.y])] = 1
    if battlestate == 2:
      playerPos = playerPos.addMove(cf.north)
    if battlestate == 3:  #Triggers end of game
      print("you have died")
      print()
      print()
      directionSelectionMode = 0
  else:
    print('not valid movement')
  
#halfway point
#import store

print()
print('As you reach the end of the cave, you look over your remaining loot. It looks like you escaped with {0} gold.'.format(ecs.player1.goldValue))