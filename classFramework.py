class map:
  """Map and position class"""

  def centerPos(mapName): 
    """Function finds the center of a map grid if odd. Map x,y needs to be odd to allow for a zero value."""
    if len(mapName)/2 == int(len(mapName)/2):
        return "map size incorrect"
    else:
        centerPointY = len(mapName)//2
        centerPointX = len(mapName[len(mapName)//2])//2
    return position(centerPointX, centerPointY)
  
  def adjustMapPos(mapName): 
    """Function that adjusts player starting position to origin of a cartesian coordinate system (0,0). Example: playerStartPos = (0,0); """
    newStartPosX = map.centerPos(mapName).x
    newStartPosY = map.centerPos(mapName).y
    newStartPos = position(newStartPosX,newStartPosY)
    newStartPos = newStartPos.dirMove()
    return newStartPos

class position: 
  """Character Position Class"""
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __str__(self):
    return "(" + str(self.x) + "," + str(self.y) + ")"
    
  def addMove(self, changePos): 
    """Return the move as the sum of two points, returning a new point. Example: Example:playerPos=(0,0); west=(-1,0); newPlayerPos = playerPos.addMove(west); output:newPlayerPos=(-1,0)"""
    return position(self.x + changePos.x, self.y + changePos.y)
    
  def dirMove(self): 
    """Return the move as a teleport, returning a new point. Falls into a pit? Slides to the beginning. Example:playerPos=(0,0); newPlayerPos=(7,-5); playerPos=newPlayPos.dirMove()...might be redundant..."""
    return position(self.x, self.y)

class state:
  """current state of a charater and environment"""
  def __init__(self, health, strength, defense, speed, currentPos, goldValue, weaponName, name,weaponMulti):
    self.health = float(health) # health = vit*10 
    self.attack = float(float(weaponMulti)*float(strength)) # attack = baseS + weapDMG + mods
    self.strength = float(strength)
    self.defense = float(defense) # def = 
    self.speed = int(speed) # speed = dex*mod
    self.currentPos = currentPos
    self.goldValue = int(goldValue)
    self.weaponName = weaponName
    self.name = name
    self.weaponMulti = float(weaponMulti)

  def __str__(self):
      return '{0} has {1} health points, a modified attack of {2}, defense of {3}, speed of {4}, {5} gold pieces. {0}\'s weapon, a {6}, has a multiplier of {7}'.format(str(self.name),str(self.health),str(self.attack),str(self.defense),str(self.speed),str(self.goldValue),str(self.weaponName),str(self.weaponMulti))

  def stateCompare(self, stateType): #needs a pointer to which Characters its using.
    """This is a comparison tool for battles, compare speed"""
    value1 = self.char1Values.stateType #get char1 value for stateType
    value2 = self.char2Values.stateType #get char2 value for stateType
    if value1 > value2: #assign turns based
      order = (self.char1Values, self.char2Values)
    else: 
      order = (self.char2Values,self.char1Values)
    return order #returns order somehow

def stateDif(stateType1, stateType2): #This works but is outside of the state class. involves 
  """This is a comparison tool for battles, diff math, Damage = attack - defense. Example: player1 = state(100,7,5,3,5,4,4);enemy = state(100,10,10,10,10,10,10),print(stateDif(player1.attack,enemy.defense));output = -3"""
  value1 = int(stateType1) #get char1 value for stateType
  value2 = int(stateType2) #get char2 value for stateType
  damage = value1 - value2 
  return  damage #returns damage somehow


def battle(char1,char2): #these should be two state class objects, char1=player?
  """Takes the input from the state class object and reduces it down to comparisons. initates a pokemon style battle, gives player choices.  [Not sure if this needs to be a class yet, probably only needs to be a function.]"""
  #maybe a print statement with enemy(char2) info
  endstate = 0
  while endstate == 0: #while endstate == 0, the battle will continue.
    #maybe a print statement with stats
    print("What do you want to do? (Attack and Flee are the only options.)")
    userinput = input("input:") #asks for input, implement lower()
    if userinput == "attack" or userinput == "a":
      print('{0}\'s health is: {1}'.format(char1.name,char1.health,char2.name,char2.health))
      print('{0}\'s health is: {1}'.format(char2.name,char2.health))
      currentDamage12 = stateDif(char1.attack,char2.defense)
      if currentDamage12 <= 0: #When the returned value is negative, the enemy is given "health"." 
        currentDamage12 = 0
      print('{0} swings their {1} and does {2} Damage to {3}'.format(char1.name,char1.weaponName,currentDamage12, char2.name))
      char2.health -= currentDamage12
      if char2.health <= 0:
        print()
        print(char2.name + " has been killed. Moving on...")
        endstate += 1
        return 1
      currentDamage21 = stateDif(char2.attack,char1.defense)
      if currentDamage21 <= 0:
        currentDamage21 = 0
      print('{0} swings their {1} and does {2} Damage to {3}'.format(str(char2.name),char2.weaponName,currentDamage21, str(char1.name)))
      if currentDamage21 == 0:
        print('{0} says: Looks like that did nothing...im screwed.'.format(char2.name))
      char1.health -= currentDamage21
      if char1.health <= 0:
        print()
        print(char1.name + " has been killed. GAME OVER!") 
        endstate += 1
        return 3
    if userinput == "flee":
      print('{0} runs away because they are scared...'.format(char1.name))
      print("You head back the way you came in.")
      endstate += 2
      return 2
    #if userinput == "items": #placeholder
     # return

#Command initialize
#Binds movement options.
west = position(0,-1)
east = position(0,1)
north = position(-1,0)
south = position(1,0)
#Sets start position for the player.
playerStartPos_x = 0
playerStartPos_y = 0

map1 = ([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], #Current map in use.
        [-1,-1,-1,"8","7","7",-1,-1,0,0,-1],
        [-1,-1,"10","9","5","6",-1,0,0,0,-1],
        [-1,"12","11",-1,"3","4",-1,0,0,0,-1],
        [-1,"13",-1,-1,-1,"1","2",-1,0,0,-1],
        [-1,"14","15","17",-1,"0",-1,0,0,0,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])

map3 = ([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], #Test Map 1
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,2,0,0,0,0,0,-1],
        [-1,0,8,4,2,"S",0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])

map2 = ([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], #Test Map 2
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,2,0,0,0,0,0,-1],
        [-1,0,8,4,2,"S",0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])