import time
import classFramework as cf
import charCreate
import encountersystem as ecs
#import store

#delay = charCreate.delay
#player1 = charCreate.player1
#print(player1)

#state class = (health,attack,defen,speed,currentpos,gold,weapon)

#map1 solution = n*3,w*2,s*1,w*1,s*1,w*1,s*2,e*2

print("you enter a room and the door behind closes(startNav)")
playerPos = cf.position(cf.playerStartPos_x,cf.playerStartPos_y)
playerPos = cf.map.adjustMapPos(cf.map1)
directionSelectionMode = 1
while directionSelectionMode == 1:
  playerInput = str.lower(input("which direction do you want to go...? "))
  if playerInput == "west" or playerInput == "w":
    playerPos = playerPos.addMove(cf.west)
    if cf.map1[playerPos.x][playerPos.y] == -1:
      print("Theres a wall to the west. Turning around...")
      playerPos = playerPos.addMove(cf.east)
    print("testcode: currentPos= " + str(playerPos) + str(cf.map1[playerPos.x][playerPos.y]))
    ecs.encDic[int(cf.map1[playerPos.x][playerPos.y])]()
    print()
    print()

  elif playerInput == "east" or playerInput == "e":
    playerPos = playerPos.addMove(cf.east)
    if cf.map1[playerPos.x][playerPos.y] == -1:
      print("Theres a wall to the east. Turning around...")
      playerPos = playerPos.addMove(cf.west)
    print("testcode: currentPos= " + str(playerPos) + str(cf.map1[playerPos.x][playerPos.y]))
    ecs.encDic[int(cf.map1[playerPos.x][playerPos.y])]()
    print()
    print()

  elif playerInput == "north" or playerInput == "n":
    playerPos = playerPos.addMove(cf.north)
    if cf.map1[playerPos.x][playerPos.y] == -1:
      print("Theres a wall to the north. Turning around...")
      playerPos = playerPos.addMove(cf.south)
    print("testcode: currentPos= " + str(playerPos) + str(cf.map1[playerPos.x][playerPos.y]))
    ecs.encDic[int(cf.map1[playerPos.x][playerPos.y])]()
    print()
    print()

  elif playerInput == "south" or playerInput == "s":
    playerPos = playerPos.addMove(cf.south)
    if cf.map1[playerPos.x][playerPos.y] == -1:
      print("Theres a wall to the south. Turning around...")
      playerPos = playerPos.addMove(cf.north)
    print("testcode: currentPos= " + str(playerPos) + str(cf.map1[playerPos.x][playerPos.y]))
    ecs.encDic[int(cf.map1[playerPos.x][playerPos.y])]()
    print()
    print()
  else:
    print('not valid movement')
  
#halfway point
import store


print('As you reach the end of the cave, you look over your remaining loot. It looks like you escaped with {0} gold.'.format(player1.goldValue))