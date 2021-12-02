import time
import classFramework as cf
from random import randint
import charCreate

delay = charCreate.delay

pStr = charCreate.str
pDex = charCreate.dex
pVit = charCreate.vit
player1 = cf.state(1,1,1,1,1,1,1)


#(health,attack,defen,speed,currentpos,gold,weapon)

import charCreate
import encounters as ec


gold = 0

print('After remembering yourself, you look around the cave and realize there are two paths you could choose.')
direction = 'still'
while direction != 'cont':
  direction = str.lower(input('Would you like to go left (l) or right (r)? '))
  if direction=="l" or "left":
    #ec.encounters()
    direction = 'cont'
  elif direction=='r' or "right":
    print('Right')
    direction = 'cont'
  else:
    print('You try to go in the {0} direction but then realize that your face hit a wall because {0} is not a choice.'.format(direction))

#halfway point
import store

print('As you reach the end of the cave, you look over your remaining loot. It looks like you escaped with {0} gold.'.format(player1.goldValue))