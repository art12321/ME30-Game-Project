import classFramework as cf
import charCreate as cc

# Stores active player and enemy states
player1 = cc.charactercreation()
goblin1 = cc.baseGoblin
goblin2 = cc.baseGoblin
goblin3 = cc.baseGoblin
goblin4 = cc.baseBandit
goblin5 = cc.baseGoblin
goblin6 = cc.baseCultist
goblin7 = cc.baseGoblin
goblin8 = cc.baseOrc
goblin9 = cc.baseGoblin
goblin10 = cc.baseGoblin
goblin11 = cc.baseMage
goblin12 = cc.baseDemon
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
      while encStateDic[roomNum] == 0:
        #Description
        cc.delay()
        print('The room you enter is dimly lit by a single torch. Through the edge of your vision, you see a humongous worm on the other side waiting to devour you.')
        #Event
        cc.delay()
        print('It takes one look at you, screams and then slithers away. You look around and find 20 gold coins!')
        player1.goldValue+=20
        #testFight
        cc.delay()
        encStateDic[roomNum] = 1
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")
 


def R2(): #PitRoom
    roomNum = 2
    if encStateDic[roomNum] == 0:
    #Description
      print('You open the door, and instinctively take a step forward, and feel nothing underneath you.')
      print('Your dexterity is: '+ player1.speed + '/4')
      #Event
      if player1.speed >=4:
        #Choice 1 - Dexterity Check
        print('Dexterity check success! You quickly grab onto the doorframe and and then carefully work your way around the pit.')
        encStateDic[roomNum] = 1
        return 1 #Encounter passed.
      else:
        #Choice 2 - Bad End
        print('Dexterity check failed! You fall into the pit and die. Mistakes were made.')
        return 3 #Game over.
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R3(): #GoblinRoom
    roomNum = 3
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:
        #Description
        print('As you enter into the next room, you see small figures darting around in the dark. You have been ambushed by goblins!')
        #Event
        print(str(player1.goldValue) + '/20')
        userinput = input('What would you like to do? 1. Initiate Combat, 2. Bribe. - Current Gold: ').lower()
        print("You decide to: " + userinput) 
        #Choice 1 - Initiate Combat
        if userinput == "Initiate Combat" or userinput == "1": 
          print('You unsheathe your weapon and prepare yourself for a fight.')
          endstate = cf.battle(player1,goblin3)
          if endstate == 1:
            print("Room cleared!")
            #encStateDic[roomNum] = 1
            encStateDic[roomNum] = 1
            return 1 #battle won
          elif endstate == 2:
            return 2 #flee
          else:
            return 3 #game over
        #Choice 2 - Bribe
        elif userinput == "Bribe" or userinput == "2" and player1.goldValue >= 20:
          print('You throw money at the goblins, which distracts them for a split second; just enough to get away!')
          player1.gold =- 20
          encStateDic[roomNum] = 1
          return 1
        else:
          print('Please input a valid command.')
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R4(): #BanditRoom
    roomNum = 4
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:    
        #Description
        print('You hear voices in the next room. Slowly opening the door, you see it is a group of bandits, huddled around a fire.')
        #Event
        userinput = input('What would you like to do?').lower()
        print('1. Initiate Combat, 2. Intimidate. - Strength: '+ str(player1.strength) + '/4')
        print("You decide to: "+ userinput)
        #Choice 1 - Initiate Combat
        if userinput == "Initiate Combat" or userinput == "1":
          print('You unsheathe your weapon and prepare yourself for a fight.')
          endstate = cf.battle(player1,goblin4)
          if endstate == 1:
            print("Room cleared!")
            encStateDic[roomNum] = 1
            return 1 #battle won
          elif endstate == 2:
            return 2 #flee
          else:
            return 3 #game over
        #Choice 2 - Intimidate
        elif userinput == "Intimidate" or userinput == "2" and player1.strength >=4:
          print('Strength check success! You grab a bandit in a chokehold, and command the rest to run away. The bandits all scatter.')
          encStateDic[roomNum] = 1
          return 1 #Encounter passed.
        else:
          print('Please input a valid command.')
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R5(): #GasRoom
    roomNum = 5
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:
        #Description
        print('You enter the next room, and are immediately hit with a strong odor. The room is filled with poisonous gas!')
        #Event
        print('Your vitality is: '+ str(player1.defense) + '/4')
        if player1.defense >= 4:
          #Choice 1 - Vitality Check
          print('Vitality check success! You manage to hold your breath long enough to escape the room without harm.')
          encStateDic[roomNum] = 1
          return 1 #Encounter passed.
        else:
          #Choice 2 - Bad End
          print('Vitality check failed! You suffer damage from the gas.')
          player1.health -= 10
          print(player1.health)
          if player1.health <= 0:
            return 3
          encStateDic[roomNum] = 1
          return 1
          
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R6(): #CultistRoom
    roomNum = 6
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:
        #Description
        print('The room you enter has a strange hooded figure. He offers you safe passage in exchange for participating in his ritual.')
        #Event
        userinput = input('What would you like to do?').lower()
        print('1. Initiate Combat, 2. Participate in Ritual. - Vitality: ' + str(player1.defense) + '/4')
        print("You decide to: "+ userinput)
        #Choice 1 - Initiate Combat
        if userinput == "Initiate Combat" or userinput == "1":
          print('You unsheathe your weapon and prepare yourself for a fight.')
          endstate = cf.battle(player1,goblin6)
          if endstate == 1:
            print("Room cleared!")
            #encStateDic[roomNum] = 1
            return 1 #battle won
          elif endstate == 2:
            return 2 #flee
          else:
            return 3 #game over
        #Choice 2 - Vitality Check
        #else:
        elif (userinput == "Participate in Ritual" or userinput == "2") and player1.defense >= 4:
          print('Vitality check success! You agree to the ritual, and make it through unscathed, albeit, disgusted.')
          encStateDic[roomNum] = 1
          return 1 #Encounter passed.
        else:
          print('Please input a valid command.')
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R7(): #Shop
    roomNum = 7
    import store as s
    #s.barkeeper()

def R8(): #OrcRoom
    roomNum = 8
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:
        #Description
        print('The room you enter has a tough-looking orc guarding the next door.')
        #Event
        print(str(player1.speed) +"/4")
        userinput = input('What would you like to do? 1. Initiate Combat, 2. Evade Enemy. - Dexterity:').lower()
        print("You decide to: "+ userinput)
        #Choice 1 - Initiate Combat
        if userinput == "Initiate Combat" or userinput == "1":
          print('You unsheathe your weapon and prepare yourself for a fight.')
          endstate = cf.battle(player1,goblin8)
          if endstate == 1:
            print("Room cleared!")
            encStateDic[roomNum] = 1
            return 1 #battle won
          elif endstate == 2:
            return 2 #flee
          else:
            return 3 #game over
        #Choice 2 - Dexterity Check
        elif (userinput == "Evade Enemy" or userinput == "2") and player1.defense >= 4:
          print('Dexterity check success! You effortlessly dodge past the orc and run past him. He cant fit through the door. How unfortunate.')
          return 1 #Encounter passed.
        else:
          print('Please input a valid command.')
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R9(): #BoulderRoom
    roomNum = 9
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:
        #Description
        print('You open the door and are immediately greeted with a massive boulder blocking your way!')
        #Event
        print(str(player1.strength) +"/4")
        userinput = input('What would you like to do? 1. Initiate Combat, 2. Punch Boulder. - Strength').lower()
        print("You decide to: "+ userinput)
        if (userinput == "Initiate Combat" or userinput == "1"):
          #Choice 1 - Initiate Combat
          print('You unsheathe your weapon and prepare to attack the boulder. You hurt yourself trying to provoke the boulder into a fight.')
          player1.health -= 10
          print(player1.health)
          if player1.health <= 0:
            return 3
            encStateDic[roomNum] = 1
            return 1
        if (userinput == "Punch Boulder" or userinput == "2") and player1.strength <=4:   
          #Choice 2 - Strength Check
          print('Strength check success! You punch the boulder and it breaks into pieces. Totally realistic.')
          encStateDic[roomNum] = 1
          return 1
        else:
          print('Please input a valid command.')
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R10(): #TreasureRoom
    roomNum = 10
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:
        #Description
        print('You enter a large room filled with gold and treasure, a menacing fire dragon sleeps atop his trove.')
        #Event
        print(str(player1.speed) +"/4")        
        userinput = input('What would you like to do? 1. Initiate Combat (Bad Idea), 2. Steal Treasure. - Dexterity').lower()
        print("You decide to: "+ userinput)
        #Choice 1 - Initiate Combat
        if userinput == "Initiate Combat" or userinput == "1":
          print('You unsheathe your weapon and the dragon immediately burns you alive. Did you think that was a good idea?')
          return 3 #game over
        #Choice 2 - Dexterity Check
        if (userinput == "Steal Treasure" or userinput == "2") and player1.speed >= 4:   
          print('Dexterity check success! You manage to steal some treasure and get away without waking up the dragon!')
          encStateDic[roomNum] = 1
          return 1 #Encounter passed.
        else:
          print('Please input a valid command.')
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R11(): #MageRoom
    roomNum = 11
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:
        #Description
        print('You open the door, and surprise a mage conducting a ritual. She immediately readies herself for combat.')
        #Event
        print(str(player1.goldValue) +"/40")        
        userinput = input('What would you like to do? 1. Initiate Combat, 2. Bribe').lower()
        print("You decide to: "+ userinput)
        #Choice 1 - Initiate Combat
        if userinput == "Initiate Combat" or userinput == "1":
          print('You unsheathe your weapon and prepare yourself for a fight.')
          endstate = cf.battle(player1,goblin11)
          if endstate == 1:
            print("Room cleared!")
            #encStateDic[roomNum] = 1
            return 1 #battle won
          elif endstate == 2:
            return 2 #flee
          else:
            return 3 #game over
        #Choice 2 - Bribe
        elif (userinput == "Bribe" or userinput == "2") and player1.goldValue >= 40:
          print('You attempt to bribe your way past, convincing her to let you past.')
          player1.gold =- 40
          encStateDic[roomNum] = 1
          return 1 #Encounter passed.
        else:
          print('Please input a valid command.')
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R12(): #DemonRoom
    roomNum = 12
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:
        #Description
        print('You enter a pitch black room, you hear strange whispering around you. You have been ambushed by a demon!')
        #Event
        print(str(player1.defense) +"/4")          
        userinput = input('What would you like to do? 1. Initiate Combat, 2. Excorcise. - Vitality').lower()
        print("You decide to: "+ userinput)
        #Choice 1 - Initiate Combat
        if userinput == "Initiate Combat" or userinput == "1":
          print('You unsheathe your weapon and prepare yourself for a fight.')
          endstate = cf.battle(player1,goblin12)
          if endstate == 1:
            print("Room cleared!")
            encStateDic[roomNum] = 1
            return 1 #battle won
          elif endstate == 2:
            return 2 #flee
          else:
            return 3 #game over
        #Choice 2 - Vitality Check
        elif (userinput == "Excorcise" or userinput == "2") and player1.defense >= 4:
          print('Vitality check success!. You perform an excorcism ritual, leaving you drained, but unharmed.')
          encStateDic[roomNum] = 1
          return 1 #Encounter passed.
        else:
          print('Please input a valid command.')
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R13(): #LavaRoom
    roomNum = 13
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:    
        #Description
        print('You enter the room, and the floor is literally lava!')
        #Event
        print('Your strength is: '+ str(player1.strength) + '/4')
        if player1.strength >=4:
          #Choice 1 - Vitality Check
          print('Strength check success! You avoid the lava by climbing along the walls!')
          encStateDic[roomNum] = 1
          return 1 #Encounter passed.
        else:
          #Choice 2 - Bad End
          print('Strength check failed! You slip and burn yourself on the edge of the lava.') 
          player1.health -= 10
          print(player1.health)
          if player1.health <= 0:
            return 3
          encStateDic[roomNum] = 1
          return 1
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R14(): #WaterRoom
    roomNum = 14
    if encStateDic[roomNum] == 0:   
      while encStateDic[roomNum] == 0: 
        #Description
        print('You enter the room, filled with muddy water. Beneath the surface, you see a 50 foot catfish, who seems to be waiting for you to enter the water.')
        #Event
        print('Your dexterity is: '+ str(player1.speed) + '/4')
        if player1.defense >=4:
          #Choice 1 - Vitality Check
          print('Vitality check success! You manage to hold your breath long enough to escape the room without harm.')
          encStateDic[roomNum] = 1
          return 1 #Encounter passed.
        else:
          #Choice 2 - Bad End
          print('Vitality check failed! You suffer take drowning damage before you manage to reach ashore.')
          if player1.health <= 0:
            return 3
          encStateDic[roomNum] = 1
          return 1
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R15(): #SnakeRoom
    roomNum = 15
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:    
        #Description
        print('You look into the room, and it is full of SNAKES! The top 10 most venomous snakes mixed together floor to ceiling. One senses you and slithers towards you. The rest all begin to look towards you.')
        print('Your dexterity is: '+ str(player1.speed) + '/4')
        if player1.speed >=4:
          #Event
          #Choice 1 - Dexterity Check
          print('Dexterity check success! You put them into a trance and they are all dancing. You can escape this time.')
          encStateDic[roomNum] = 1
          return 1 #Encounter passed.
        else:
          #Choice 2 - Bad End
          print('Dexterity check failed! The snakes bite you, and deals some damage.')
          if player1.health <= 0:
            return 3
          encStateDic[roomNum] = 1
          return 1
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def R16(): #BounceRoom
    roomNum = 16
    if encStateDic[roomNum] == 0:
      while encStateDic[roomNum] == 0:
        #Description
        print('You step into the room and are launched headfirst into a wall.')
        #Event
        print('Your vitality is: '+ str(player1.defense) + '/4')
        if player1.defense >= 4:
          #Choice 1 - Vitality Check
          print('Vitality check success! You put on a helmet survive unscathed.')
          encStateDic[roomNum] = 1
          return 1 #Encounter passed.
        else:
          #Choice 2 - Bad End
          print('Vitality check failed! You hit your head. Ouch!')
          player1.health -= 10
          print(player1.health)
          if player1.health <= 0:
            return 3
          encStateDic[roomNum] = 1
          return 1
    else: # this triggers if encStateDic[roomNum] != 0
      print("You have already cleared this room.")

def B1():
    roomNum = 17
    if encStateDic[roomNum] == 0: 
      #Description
      print('You enter the final room to face your sworn enemy: a giant rat!')
      #Event
      print('You unsheathe your weapon and prepare yourself for the final battle.')
      endstate = cf.battle(player1,boss)
      if endstate == 1:
        print("Room cleared!")
        #encStateDic[roomNum] = 1
        print("You have beaten the game, congratulations!")
        encStateDic[roomNum] = 1
        return 1 #battle won
      elif endstate == 3:
        return 3 #flee
      else:
        return 3 #game over
      #Triggers game over prompt.
      directionSelectionMode = 0
      return directionSelectionMode

def startRoom():
  return print("Welcome Back, you are back where you started. How did that happen?")

#Converts the room strings to integers that can be used on our map.
encStateDic = {0:0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17:0}

encDic = {1: R1, 2: R2, 3: R3, 4: R4, 5: R5, 6: R6, 7: R7, 8: R8, 9: R9, 10: R10, 11: R11, 12: R12, 13: R13, 14: R14, 15: R15, 16: R16, 17 : B1,0: startRoom} #-1: W1