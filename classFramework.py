class map:
  """Map class? map selection?"""
  def _init_(self):
    return
  def centerPos(self): #Works!
    """Function finds the center of a map grid if odd. Map x,y needs to be odd to allow for a zero value."""
    if len(self)/2 == int(len(self)/2):
        return "map size incorrect"
    else:
        centerPointY = len(self)//2
        centerPointX = len(self[len(self)//2])//2
    return position(centerPointX, centerPointY)
  
  def adjustMapPos(self):
    """Function that adjusts player starting position to origin of a cartesian coordinate system (0,0). Example: playerStartPos = (0,0); """
    newStartPos = map.centerPos(self)
    return print(newStartPos)

class position:
  """Character Position Class"""
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __str__(self):
    return "(" + str(self.x) + "," + str(self.y) + ")"
    
  def addMove(self, changePos):
    """Return the move as the sum of two points, returning a new point."""
    return position(self.x + changePos.x, self.y + changePos.y)
    
  def dirMove(self, newPos):
    """Return the move as a teleport, returning a new point. Falls into a pit? Slides to the beginning."""
    return position(newPos.x, newPos.y)

class state:
  """current state of a charater and environment"""
  def __init__(self, health, attack, defense, speed, currentPos, goldValue):
    self.health = health
    self.attack = attack
    self.defense = defense
    self.speed = speed
    self.currentPos = currentPos
    self.goldValue = goldValue

  def __str__(self):
      return str(self.health) + " health points " + str(self.attack) + " attack points " + str(self.defense) + " defense points " + str(self.speed) + " speed points " + " is at position " + str(self.curPos) + " and has gold " + str(self.goldValue)

  def stateCompare(self, stateType):
    """This is a comparison tool for battles, compare speed"""
    value1 = self.char1Values.stateType #get char1 value for stateType
    value2 = self.char2Values.stateType #get char2 value for stateType
    if value1 > value2: #assign turns based
      order = (self.char1Values, self.char2Values)
    else: 
      order = (self.char2Values,self.char1Values)
    return order #returns order somehow

class battle:
  """Takes the input from the state class object and reduces it down to comparisons. initates a pokemon style battle, gives player choices.  [Not sure if this needs to be a class yet, probably only needs to be a function.]"""
  def __init__(self, char1Values, char2Values):
    self.char1Values = char1Values #get char1 values for attack, defense, speed
    self.char2Values = char2Values #get char2 values for attack, defense, speed

  def __str__(self):
    return "A Battle is taking place!"
    
  def speedCompare(self): #added a general compare function in the state class, may not use this...
    """This is called by the fight function to calculate turn order."""
    speed1 = self.char1Values.speed #get char1 value for speed
    speed2 = self.char2Values.speed #get char2 value for speed
    if speed1 > speed2: #assign turns based
      order = self.char1Values, self.char2Values
    else: 
      order = self.char2Values,self.char1Values
    return order

  def attackdefend(self):
    """This is called by the fight function to do math for attack defend."""
    
    #do math to get values
    return

  def fight(self):
    print("What do you want to do? (Type help for examples)")
    userinput = input("input:") #ask for input
    if userinput == "attack":
      battle.attackdefend()   
    #create end condition
    return

    
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
  def __init__(self,enVal):
    self.enVal = enVal
    
  def __str__(self):
    return "An Encounter is taking place!"
    
  def room(self):
    #get room info
    return
  
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

"""