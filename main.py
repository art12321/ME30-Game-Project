import time
import charCreate
import encounters as ec
from random import randint

gold = 0

print('After remembering yourself you look around the cave and realize there are two paths you could choose.')
direction = 'still'
while direction != 'cont':
  direction = str.lower(input('Would you like to go left(l) or right(r) '))
  if direction=="l" or "left":
    ec.encounters()
    direction = 'cont'
  elif direction=='r' or "right":
    print('Right')
    direction = 'cont'
  else:
    print('You try to go in the {0} direction but then realize that your face hit a wall because {0} is not a choice.'.format(direction))

print('As you reach the end of the cave, you look over your remaining loot. It looks like you escaped with is {0} gold'.format(gold))