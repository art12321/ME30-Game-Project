import classFramework as cf
import charCreate as cc
#Evan was thinking that this could be a list of rooms we can call from.

#roomNum/eventNum
#discriptionOfRoom (what does the room look like)
#descriptionOfEvent (enemy, pit, nothing,boss)
#example room

# I think this will be where we will store active player and enemy states
player1 = cc.charactercreation()
goblin1 = cc.baseGoblin
goblin2 = cc.baseGoblin
goblin3 = cc.baseGoblin
goblin4 = cc.baseGoblin
goblin5 = cc.baseGoblin
goblin6 = cc.baseGoblin
goblin7 = cc.baseGoblin
goblin8 = cc.baseGoblin
goblin9 = cc.baseGoblin
goblin10 = cc.baseGoblin
goblin11 = cc.baseGoblin
goblin12 = cc.baseGoblin
goblin13 = cc.baseGoblin
goblin14 = cc.baseGoblin
goblin15 = cc.baseGoblin
goblin16 = cc.baseGoblin
goblin17 = cc.baseGoblin
boss = cc.baseBoss


def R1(): #WormRoom
    #check room state
    roomNum = 1
    if encStateDic[roomNum] == 0: #This is a state check that looks if the room has been entered before.
      #Description
      print('The room you enter is dimly lit by a single torch. Through the edge of your vision, you see a humongous worm on the other side waiting to devour you.')
      #Event
      print('It takes one look at you, screams and then slithers away. You look around and found 20 gold coins!')
      #testFight
      print("testCode: (comment out to test other stuff.)")
      endstate = cf.battle(player1,goblin1)
      if endstate == 1:
        print("Congrats!")
        #encStateDic[roomNum] = 1
        return 1 #battle won
      elif endstate == 2:
        return 2 #flee
      else:
        return 3 #game over
    else: # this triggers if encStateDic[roomNum] != 0
      print("a dead goblin lies dead...")
    #Outcome
    player1.gold =+ 20


def R2(): #PitRoom
    roomNum = 2
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

def R3(): #GoblinRoom
    roomNum = 3
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

def R4(): #BanditRoom
    roomNum = 4
    #Description
    print('You hear voices in the next room. Slowly opening the door, you see it is a group of bandits, huddled around a fire.')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Intimidate. (Strength)')
    #
    #Choice 1 - Initiate Combat
    print('You unsheathe your weapon and prepare yourself for a fight.')
    #Choice 2 - Intimidate
    print('Strength check success! You grab a bandit in a chokehold, and command the rest to run away. The bandits all scatter, leaving behind 20 cold coins.')
    print('Strength check failed! You look at yourself, and realize that you are too weak to be taken seriously.')
    #Outcome
    global gold
    gold =+ 20

 
def R5(): #GasRoom
    roomNum = 5
    #Description
    print('You enter the next room, and are immediately hit with a strong odor. The room is filled with poisonous gas!')
    #Event
    #Choice 1 - Vitality Check
    print('Vitality check success! You manage to hold your breath long enough to escape the room without harm.')
    #Choice 2 - Bad End
    print('Vitality check failed! You suffer damage from the gas.')
    #Outcome


def R6(): #CultistRoom
    roomNum = 6
    #Description
    print('The room you enter has a strange hooded figure. He offers you safe passage in exchange for participating in his ritual.')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Participate in Ritual. (Vitality)')
    #Choice 1 - Initiate Combat
    #if userinput = "Initiate Combat":
    print('You unsheathe your weapon and prepare yourself for a fight.')
    #Choice 2 - Vitality Check
    #else:
    print('Vitality check success! You agree to the ritual, and make it through unscathed, albeit, disgusted.')
    #Outcome


def R7(): #Shop
    roomNum = 7
    import store as s
    #s.barkeeper()

def R8(): #OrcRoom
    roomNum = 8
    #Description
    print('The room you enter has a tough-looking orc guarding the next door.')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Evade Enemy. (Dexterity)')
    #Choice 1 - Initiate Combat
    #if userinput = "Initiate Combat":
    print('You unsheathe your weapon and prepare yourself for a fight.')
    #Choice 2 - Dexterity Check
    #else:
    print('Dexterity check success! You effortlessly dodge past the orc and run past him. He cant fit through the door. How unfortunate.')
    #Outcome  

def R9(): #BoulderRoom
    roomNum = 9
    #Description
    print('You open the door and are immediately greeted with a massive boulder blocking your way!')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Punch Boulder. (Strength)')
    #Choice 1 - Initiate Combat
    #if userinput = "Initiate Combat":
    print('You unsheathe your weapon and prepare to attack the boulder. I guess this counts as a fight.')
    #Choice 2 - Strength Check
    print('Strength check success! You punch the boulder and it breaks into pieces. Totally realistic.')
    #Outcome  

def R10(): #TreasureRoom
    roomNum = 10
    #Description
    print('You enter a large room filled with gold and treasure, a menacing fire dragon sleeps atop his trove.')
    #Event
    print('What would you like to do? 1. Initiate Combat (Bad Idea), 2. Steal Treasure. (Dexterity)')
    #Choice 1 - Initiate Combat
    #if userinput = "Initiate Combat":
    print('You unsheathe your weapon and the dragon immediately burns you alive. Did you think that was a good idea?')
    #Choice 2 - Dexterity Check
    print('Dexterity check success! You manage to steal some treasure and get away without waking up the dragon!')
    #Outcome
  
def R11(): #MageRoom
    roomNum = 11
    #Description
    print('You open the door, and surprise a mage conducting a ritual. She immediately readies herself for combat.')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Bribe Enemy. (40 Gold)')
    #Choice 1 - Initiate Combat
    #if userinput = "Initiate Combat":
    print('You unsheathe your weapon and prepare yourself for a fight.')
    #Choice 2 - Bribe
    print('You attempt to bribe your way past, convincing her to let you past.')
    #Outcome  

def R12(): #DemonRoom
    roomNum = 12
    #Description
    print('You enter a pitch black room, you hear strange whispering around you. You have been ambushed by a demon!')
    #Event
    print('What would you like to do? 1. Initiate Combat, 2. Excorcise. (Vitality)')
    #Choice 1 - Initiate Combat
    #if userinput = "Initiate Combat":
    print('You unsheathe your weapon and prepare yourself for a fight.')
    #Choice 2 - Vitality Check
    print('Vitality check success!. You perform an excorcism ritual, leaving you drained, but unharmed.')
    #Outcome  

def R13(): #LavaRoom
    roomNum = 13
    #Description
    print('You enter the room, and the floor is literally lava!')
    #Event
    #Choice 1 - Vitality Check
    print('Strength check success! You avoid the lava by climbing along the walls!')
    #Choice 2 - Bad End
    print('Strength check failed! You slip and burn yourself on the edge of the lava.')
    #Outcome  

def R14(): #WaterRoom
    roomNum = 14
    #Description
    print('You enter the room, filled with muddy water. Beneath the surface, you see a 50 foot catfish, who seems to be waiting for you to enter the water.')
    #Event
    #Choice 1 - Vitality Check
    print('Vitality check success! You manage to hold your breath long enough to escape the room without harm.')
    #Choice 2 - Bad End
    print('Vitality check failed! You suffer take drowning damage before you manage to reach ashore.')
    #Outcome

def R15(): #SnakeRoom
    roomNum = 15
    #Description
    print('You look into the room, and it is full of SNAKES! The top 10 most venomous snakes mixed together floor to ceiling. One senses you and slithers towards you. The rest all begin to look towards you.')
    #Event
    #Choice 1 - Dexterity Check
    print('Dexterity check success! You put them into a trance and they are all dancing. You can escape this time.')
    #Choice 2 - Bad End
    print('Dexterity check failed! The snakes bite you, and deals some damage.')
    #Outcome

def R16(): #BounceRoom
    roomNum = 16
    #Description
    print('You step into the room and are launched head first into a wall.')
    #Event
    #Choice 1 - Vitality Check
    print('Vitality check success! You put on a helmet and survived.')
    #Choice 2 - Bad End
    print('Vitality check failed! You hit your head. Ouch!')
    #Outcome

def B1():
    roomNum = 17
    #Description
    print('You enter the final room to face your sworn enemy: a giant rat!')
    #Event
    print('You unsheathe your weapon and prepare yourself for the final battle.')
    #Outcome  
    directionSelectionMode = 0
    return directionSelectionMode

#def W1():
#  pass
  #wallOfShame
#  import main.prevPlayerPos as prevPos
#  newPos = prevPos
#  return newPos

def startRoom():
  return print("Welcome Back, you are back where you started. How did that happen?")

encStateDic = {0:0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17:0}

encDic = {1: R1, 2: R2, 3: R3, 4: R4, 5: R5, 6: R6, 7: R7, 8: R8, 9: R9, 10: R10, 11: R11, 12: R12, 13: R13, 14: R14, 15: R15, 16: R16, 17 : B1,0: startRoom} #-1: W1