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
    #Choice 1 - Dexterity Check
    print('Dexterity check success! You quickly grab onto the doorframe and and then carefully work your way around the pit.')
    #Choice 2 - Bad End
    print('Dexterity check failed! You fall into the pit and die. Mistakes were made.')
    #Outcome
    global gold
    gold =+ 20

def GoblinRoom2_1():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('As you enter into the next room, you see small figures darting around in the dark. You have been ambushed by goblins!')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Bribe Enemy. (20 Gold)')    
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and prepare yourself for a fight.')
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
    print('You unsheathe your weapon and prepare yourself for a fight.')
    #Choice 2 - Intimidate
    print('Strength check success! You grab a bandit in a chokehold, and command the rest to run away. The bandits all scatter, leaving behind 20 cold coins.')
    print('Strength check failed! You look at yourself, and realize that you are too weak to be taken seriously.')
    #Outcome
    global gold
    gold =+ 20
def PoisonRoom2_2():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('You enter the next room, and are immediately hit with a strong odor. The room is filled with poisonous gas!)
    #Event
    #Choice 1 - Vitality Check
    print('Vitality check success! You manage to hold your breath long enough to escape the room without harm.')
    #Choice 2 - Bad End
    print('Vitality check failed! You suffer damage from the gas.')
    #Outcome

def CultistRoom3_1():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('The room you enter has a strange hooded figure. He offers you safe passage in exchange for participating in his ritual.)
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Participate in Ritual. (Vitality)')
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and prepare yourself for a fight.')
    #Choice 2 - Vitality Check
    print('Vitality check success! You agree to the ritual, and make it through unscathed, albeit, disgusted.')
    #Outcome

def MerchantRoom3_2():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('The room you enter has a strange hooded figure. He appears to be a traveling merchant, offering you his wares.')
    #Event
    print('What would you like to do? 1. Initiate Trade, 2. Attempt Pickpocket. (Dexterity)')
    #Choice 1 - Initiate Trade
    print('You take a seat and browse his wares.')
    #Choice 2 - Dexterity Check
    print('Dexterity check success! You manage to steal 20 gold coins from the merchant.')
    #Outcome  
    
def OrcRoom4_1():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('The room you enter has a tough-looking orc guarding the next door.')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Evade Enemy. (Dexterity)')
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and prepare yourself for a fight.')
    #Choice 2 - Dexterity Check
    print('Dexterity check success! You effortlessly dodge past the orc and run past him. He cant fit through the door. How unfortunate.')
    #Outcome  
  
def BoulderRoom4_2():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('You open the door and are immediately greeted with a massive boulder blocking your way!')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Punch Boulder. (Strength)')
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and prepare to attack the boulder. I guess this counts as a fight.')
    #Choice 2 - Strength Check
    print('Strength check success! You punch the boulder and it breaks into pieces. Totally realistic.')
    #Outcome  

def TreasureRoom5_1():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('You enter a large room filled with gold and treasure, a menacing fire dragon sleeps atop his trove.')
    #Event
    print('What would you like to do? 1. Initiate Combat (Bad Idea), 2. Steal Tresaure. (Dexterity)')
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and the dragon immediately burns you alive. Did you think that was a good idea?')
    #Choice 2 - Dexterity Check
    print('Dexterity check success! You manage to steal some treasure and get away without waking up the dragon!')
    #Outcome  

def MageRoom5_2():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('You open the door, and surprise a mage conducting a ritual. She immediately readies herself for combat.')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Bribe Enemy. (40 Gold)')
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and prepare yourself for a fight.')
    #Choice 2 - Bribe
    print('You jingle a bag of coin in front of her, convincing her to let you past.')
    #Outcome  

def DemonRoom6_1():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('You enter a pitch black room, you hear strange whispering around you. You have been ambushed by a demon!')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Excorcise. (Vitality)')
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and prepare yourself for a fight.')
    #Choice 2 - Vitality Check
    print('Vitality check success!. You perform an excorcism ritual, leaving you drained, but alive.')
    #Outcome  

def LavaRoom6_2():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('You enter the room, and the floor is literally lava!')
    #Event
    #Choice 1 - Vitality Check
    print('Strength check success! You avoid the lava by climbing along the walls!')
    #Choice 2 - Bad End
    print('Strength check failed! You slip and burn yourself on the edge of the lava.)
    #Outcome  

def BossRoom():
  state = 'incomplete'
  if state == 'incomplete':
    #Description
    print('You enter the final room to face your sworn enemy: a giant rat. INCOMPLETE, NEED TO FINISH')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Bribe Enemy. (40 Gold)')
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and prepare yourself for the final battle.')
    #Choice 2 - Bribe
    print('You jingle a bag of coin in front of her, convincing her to let you past.')
    #Outcome  