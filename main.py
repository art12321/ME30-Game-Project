import time
import charCreate

gold = 0


def Wormroom():
  state = 'incomplete'
  if state == 'incomplete':
    print('You walk through the door to find a humongous worm on the other side waiting to devour you.')
    print('It takes one look and screams and sliters away. You look around and spot 20 gold coins')
    global gold
    gold =+ 20


print('After remembering yourself you look around the cave and realize there are two paths you could choose.')
direction = 'still'
while direction != 'cont':
  direction = str.lower(input('Would you like to go left(l) or right(r) '))
  if direction=="l" or "left":
    Wormroom()
    direction = 'cont'
  elif direction=='r' or "right":
    print('Right')
    direction = 'cont'
  else:
    print('You try to go in the {0} direction but then realize that your face hit a wall because {0} is not a choice.'.format(direction))

print('As you reach the end of the cave, you look over your remaining loot. It looks like you escaped with is {0} gold'.format(gold))