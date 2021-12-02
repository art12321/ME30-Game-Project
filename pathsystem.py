####NOT USED 
#maybe this is the nav system?
#maybe use a list like from the classwork:
# ([0,0,0,0,0],
#  [0,1,1,1,1],
#  [0,1,0,0,E],
#  [0,1,1,0,0],
#  [0,0,S,0,0])
#Compass? North, south, east, west?

class map: #moved to classFramework
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
    return "(" + str(centerPointX) + "," + str(centerPointY) + ")"

  def adjustPos(self):
    """Function that adjusts player starting position to origin of a cartesian coordinate system (0,0). Example: playerStartPos = (0,0); """
    newStartPos = map.centerPos(self)
    return newStartPos

    

map1 = ([0,0,0,0,0,0,0,0,0,0,0], #does work because odd # of rows and columns
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
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
        

"""
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
"""