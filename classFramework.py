

class map:
  """Map and position class"""
  def __init__(self):
    return
  def __str__():
    return

  def centerPos(mapName): #Works!
    """Function finds the center of a map grid if odd. Map x,y needs to be odd to allow for a zero value."""
    if len(mapName)/2 == int(len(mapName)/2):
        return "map size incorrect"
    else:
        centerPointY = len(mapName)//2
        centerPointX = len(mapName[len(mapName)//2])//2
    return position(centerPointX, centerPointY)
  
  def adjustMapPos(mapName): #Works!
    """Function that adjusts player starting position to origin of a cartesian coordinate system (0,0). Example: playerStartPos = (0,0); """
    newStartPosX = map.centerPos(mapName).x
    newStartPosY = map.centerPos(mapName).y
    newStartPos = position(newStartPosX,newStartPosY)
    newStartPos = newStartPos.dirMove()
    return newStartPos

class position: #Works!
  """Character Position Class"""
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __str__(self):
    return "(" + str(self.x) + "," + str(self.y) + ")"
    
  def addMove(self, changePos): #Works!
    """Return the move as the sum of two points, returning a new point. Example: Example:playerPos=(0,0); west=(-1,0); newPlayerPos = playerPos.addMove(west); output:newPlayerPos=(-1,0)"""
    return position(self.x + changePos.x, self.y + changePos.y)
    
  def dirMove(self): #Works!
    """Return the move as a teleport, returning a new point. Falls into a pit? Slides to the beginning. Example:playerPos=(0,0); newPlayerPos=(7,-5); playerPos=newPlayPos.dirMove()...might be redundant..."""
    return position(self.x, self.y)

class state:
  """current state of a charater and environment"""
  def __init__(self, health, attack, defense, speed, currentPos, goldValue, weapon, name):
    self.health = int(health) # health = vit*10 
    self.attack = int(attack) # attack = baseS + weapDMG + mods
    self.defense = int(defense) # def = 
    self.speed = int(speed) # speed = dex*mod
    self.currentPos = currentPos
    self.goldValue = int(goldValue)
    self.weapon = weapon
    self.name = name

  def __str__(self):
      return self
      #str(self.health) + " health points " + str(self.attack) + " attack points " + str(self.defense) + " defense points " + str(self.speed) + " speed points " + " and has gold " + str(self.goldValue)

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

class item:
  """Perhaps this could act as a global inventory system"""
  def __init__(self):
    return

  def item(self):
    #get item info, can be picked up?
    #ask for input, pickup... skip...
    #add to inventory and remove from world
    return


class encounterState:
  """Placehold for potential encounters class"""
  def __init__(self,encName,encState,encNumber):
    self.encName = encName
    self.encState = encState
    self.encNumber = encNumber
    
  def __str__(self):
    return "An Encounter is taking place!"
    
  def room(self):
    #get room info
    return

def battle(char1,char2): #these should be two state class objects, char1=player?
  """Takes the input from the state class object and reduces it down to comparisons. initates a pokemon style battle, gives player choices.  [Not sure if this needs to be a class yet, probably only needs to be a function.]"""
  #maybe a print statement with enemy(char2) info
  endstate = 0
  while endstate == 0: #while endstate == 0, the battle will continue.
    #maybe a print statement with stats
    print("What do you want to do? (Attack is the only option.)")
    userinput = input("input:") #asks for input, implement lower()
    if userinput == "attack":
      currentDamage12 = stateDif(char1.attack,char2.defense)
      if currentDamage12 <= 0:
        currentDamage12 = 0
      print('{0} swings their {1} and does {2} Damage to {3}'.format(char1.name,char1.weapon,currentDamage12, char2.name))
      char2.health -= currentDamage12
      if char2.health <= 0:
        print()
        print(char2.name + " has been killed. Moving on...")
        endstate += 1
        return
      currentDamage21 = stateDif(char2.attack,char1.defense)
      if currentDamage21 <= 0:
        currentDamage21 = 0
      print('{0} swings their {1} and does {2} Damage to {3}'.format(str(char2.name),char2.weapon,currentDamage21, str(char1.name)))
      char1.health -= currentDamage21
      if char1.health <= 0:
        print()
        print(char1.name + " has been killed. GAME OVER!")
        endstate += 1
        return
      #When the returned value is negative, the enemy is given "health". Print("looks like that did nothing...im screwed.")" 
    #if userinput == "flee":#placeholder
     # return
    #if userinput == "items": #placeholder
     # return

#Command initialize
west = position(0,-1)
east = position(0,1)
north = position(-1,0)
south = position(1,0)
playerStartPos_x = 0
playerStartPos_y = 0

map1 = ([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], #testmap
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

map3 = ([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], #testmap
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

map2 = ([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], #largermap Placehold
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

"""
#initialize variables
west = (-1,0)
east = (1,0)
north = (0,1)
south = (0,-1)
west = position(-1,0)
east = position(1,0)
north = position(0,1)
south = position(0,-1)
m = "m"
b = "b"
i = "i"
playerStartPos_x = 0
playerStartPos_y = 0
playerPos = position(playerStartPos_x,playerStartPos_y)

map1 = ([0,0,0,0,0,0,0,0,B,0,0], #does work because odd # of rows and columns
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,2,0,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0])
map2 = ([0,0,0,0,0,0,0,0,0,0], #does not work because even # of rows and columns
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0])

#testcode
print(len(map1)) #result: 11
print(len(map1)/2) #result: 5.5
print((len(map2)/2)// 1) #result: 5.0 
print(round(len(map1)/2)) #in this case map 1 would work with the position adjust function because it is odd.
print(len(map2)) #result: 10
print(len(map2)/2)  #result: 5.0
print((len(map2)/2)// 1)  #result: 5.0
print(round(len(map2)/2)) #in this case map 2 would not work with the position adjust function because it needs to be odd.
cmap1 = map.centerPos(map1)
print(cmap1) #result: (5,5)
print(map1[5]) #result: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
print(map1[5][5]) #result: 1
playerCenterStartPosition = map.adjustMapPos(map1)
print(playerCenterStartPosition) 

playerPos = map.adjustMapPos(map1)
print(playerPos)
print("RoomValue = " + str(map1[playerPos.x][playerPos.y]))
playerPos = playerPos.addMove(west)
print(playerPos)

"""