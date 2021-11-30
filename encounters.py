#Evan was thinking that this could be a list of rooms we can call from.

#roomNum/eventNum
#discriptionOfRoom (what does the room look like)
#descriptionOfEvent (enemy, pit, nothing,boss)
#example room
def encounters(num):
  if num == 1:
    print('room1')
    #state = 0
    #while state == 0:
      #print('You walk through the door to find a humongous worm on the other side waiting to devour you. It takes one look and screams and sliters away. You look around and spot 20 gold coins')
      #state = 1
      #return gold += 20
  elif num == 2:
    print('room2')
  elif num == 3:
    print('room3')
  elif num == 4:
    print('room4')
  elif num == 5:
    print('room5')
  elif num == 6:
    print('room6')
  elif num == 7:
    print('room7')
  elif num == 8:
    print('room8')
  elif num == 9:
    print('room9')
  elif num == 10:
    print('room10')
  elif num == 11:
    print('room11')
  elif num == 12:
    print('room12')
  elif num == 13:
    print('room13')







def Wormroom():
  state = 'incomplete'
  if state == 'incomplete':
    print('You walk through the door to find a humongous worm on the other side waiting to devour you.')
    print('It takes one look and screams and sliters away. You look around and spot 20 gold coins')
    global gold
    gold =+ 20