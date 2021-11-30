#Evan was thinking that this could be a list of rooms we can call from.

#roomNum/eventNum
#discriptionOfRoom (what does the room look like)
#descriptionOfEvent (enemy, pit, nothing,boss)
#example room
def encounters(num):
  if num == 1:
    print('room1')
    state = 0
    while state == 0:
      print(
      'You walk through the door to find a humongous worm on the other side waiting to devour you. It takes one look and screams and sliters away. You look around and spot 20 gold coins'
      )
      state = 1
      return gold =+ 20
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







def WormRoom1_1():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('The room you enter is dimly lit by a single torch. Through the edge of your vision, you see a humongous worm on the other side waiting to devour you.')
    #Event
    print('It takes one look at you, screams and then slithers away. You look around and found 20 gold coins!')
    #Outcome
    global gold
    gold =+ 20

def PitRoom1_2():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('You open the door, and instinctively take a step forward, and feel nothing underneath you.')
    #Event
    #Choice 1 - Agility Check
    print('Dexterity check success! You quickly grab onto the doorframe and and then carefully work your way around the pit.')
    #Choice 2 - Bad End
    print('Dexterity check failed! You fall into the pit and die. Bad end. GGWP.')
    #Outcome
    global gold
    gold =+ 20

def GoblinRoom2_1():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('As you enter into the next room, you see small figures darting around in the dark. You have been ambushed by goblins!')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Bribe. (20 Gold)')    
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and prepare yourself for a fight')
    #Choice 2 - Bribe
    print('You throw money at the goblins, which distracts them for a split second; just enough to get away!')
    print('You are too poor to bribe them!')
    #Outcome
    global gold
    gold =- 20

def BanditRoom2_2():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('You hear voices in the next room. Slowly opening the door, you see it is a group of bandits, huddled around a fire.)
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Intimidate. (Strength)')
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and prepare yourself for a fight')
    #Choice 2 - Intimidate
    print('Strength check success! You grab a bandit in a chokehold, and command the rest to run away. The bandits all scatter, leaving behind 20 cold coins.')
    print('Strength check failed! You look at yourself, and realize that you are too weak to be taken seriously.')
    #Outcome
    global gold
    gold =+ 20
def GoblinRoom2_2():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('You hear voices in the next room. Slowly opening the door, you see it is a group of bandits, huddled around a fire.)
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Intimidate. (Strength)')
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and prepare yourself for a fight')
    #Choice 2 - Intimidate
    print('You ')
    #Outcome
