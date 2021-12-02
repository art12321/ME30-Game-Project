import time
import charCreate
def barkeeper():
  #health help
  return(print('barkeep'))
def goblintrader():
  #weapon change
  return(print('goblin'))
def wizard():
  #stat change
  return(print('wizard'))


shoppos = 0


print(
    'As you enter this room you look around and see paneling and chairs. As you walk further, you start to hear music and then it dawns on you, you\'re in a tavern. You decide to step in to take a break from everything else and maybe get a drink. You sit down at the bar and strike up a conversation with the bartender.'
)
time.sleep(charCreate.delay)
barkeeper()
print('After finishing up at the bar, you decide to take some time and look around. There are crowded tables with lots going on around them. You see two other notable characters in the crowd, a goblin trader and a wizard')
var = str.lower(input('You decide to visit the '))
if var == 'wizard':
  wizard()
elif var == 'goblin' or 'goblin trader' or 'goblintrader' or 'trader':
  goblintrader()
else:
  print("You can't go to the {0}".format(var))
shop_pos = 1
var1 = int(input('Where would you like to go now? 1. Barkeep 2. Wizard 3. Goblin Trader: '))
while shop_pos == 1:
  if var1 == 1:
    barkeeper()
  elif var1 == 2:
    wizard()
  elif var1 == 3:
    goblintrader()
  elif var1 == 4:
    shop_pos = 2
    print(shop_pos)
  else:
    print('Thats not a place you silly goose!')