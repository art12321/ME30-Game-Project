import time
import classFramework as cf
import charCreate as cc

def shoprunthrough():
  print('After finishing up at the bar, you decide to take some time and look around. There are crowded tables with lots going on around them. You see two other notable characters in the crowd, a goblin trader and a wizard')
  shopstate = 0
  while shopstate == 0:
    currentshop = str.lower(input('Would you like to visit the Goblin Trader, Wizard, Barkeeper or continue on: '))
    if currentshop =='goblin trader' or currentshop == 'goblin' or currentshop =='g':
      goblintrader()
    elif currentshop == 'wizard' or currentshop =='w':
      wizard()
    elif currentshop == 'barkeeper' or currentshop =='barkeep':
      barkeeper()
    elif currentshop == 'continue' or currentshop =='leave' or currentshop =='continue on':
      print('Since you\'ve decided to leave the tavern you must continue back into the dark dingy cave to find your way out. ')
      shopstate = 1
    else:
      print('You can\'t go to {0}'.format(currentshop))

def barkeeper():
  #modifies health
  print('The barkeeper offers you some ale for 10 gold coins. It looks really appealing and almost heartwarming.')
  keepstatus = 0
  keeper = str.lower(input('Do you take it? (y/n): '))
  while keepstatus == 0:  
    if keeper == 'y':
      print('You take the ale and start to sip on it.')
      #player1.health += 20
      print('While you sip it, you notice it feels extremely revitalizing, almost like 20 health points returned to you. Interesting...')
      keepstatus = 1
    elif keeper == 'n':
      print('You turn down the ale and decide to keep your gold. "Maybe I\'ll talk to someone else" you think')
      keepstatus = 1
    else:
      print('The barkeeper doesn\'t take {0} for an answer'.format(keeper))


def goblintrader():
  #weapon change store
    print('You approach the goblin and he says...')
    #not enough time to implement weapon change
    #str.lower(input('"Welcome... I have plenty of wares for you to choose from. Would you like to choose a new weapon?"'))
    print('I normally would have some new weapons for you but since my shipment has been delayed it would appear I have nothing to offer \n You walk away sadly.')
    return


def wizard():
  #print('You sit down in front of the wizard and he says \n "You have come to the right place. For a price I can make you faster, stronger or healthier "')
  #yeanay = str.lower(input('Do you want to change your stats?(y/n)'))
  #if yeanay == 'y' or yeanay == 'yes':
  print('As you walk up the wizard says to you "I have not been feeling very magical lately. I seem to have no powers so I must send you somewhere else"')
  return

storestate = 0
if storestate == 0:
  print(
      'As you enter this room you look around and see paneling and chairs. As you walk further, you start to hear music and then it dawns on you, you\'re in some sort of underground tavern. You decide to step in to take a break from everything else and maybe get a drink. You sit down at the bar and strike up a conversation with the bartender.')
  barkeeper()
  print('After finishing up at the bar, you decide to take some time and look around. There are crowded tables with lots going on around them. You see two other notable characters in the crowd, a goblin trader and a wizard')
  sstate = 0
  while sstate == 0:
    loc = str.lower(input('Who would you like to talk to, the Goblin Trader or the Wizard: '))
    if loc == 'wizard' or loc == 'w':
      wizard()
      sstate = 1
    elif loc == 'goblin trader' or loc == 'goblin' or loc == 'g':
      goblintrader()
      sstate = 1
    else:
      print('You take one look at {0} and decide to go back on your decision. You decide to choose a different person'.format(loc))
    shoprunthrough()
  

    

#implemet after the runthrogh
# print('After finishing up at the bar, you decide to take some time and look around. There are crowded tables with lots going on around them. You see two other notable characters in the crowd, a goblin trader and a wizard')
#  var = str.lower(input('You decide to visit the '))
#  if var == 'wizard':
#      wizard()
#  elif var == 'goblin' or 'goblin trader' or 'goblintrader' or 'trader':
#      goblintrader()
#  else:
#      print("You can't go to the {0}".format(var))
#  shop_pos = 1
#  while shop_pos == 1:
#      var1 = int(
#          input(
#              'Where would you like to go now? Barkeeper(1) Wizard(2) Goblin Trader(3) or Continue(4): '
#         ))
#     if var1 == 1:
#         barkeeper()
#     elif var1 == 2:
#         wizard()
#     elif var1 == 3:
#         goblintrader()
#     elif var1 == 4:
#         shop_pos = 2
#     else:
#         print('Thats not a place you silly goose! Try again.')


#leaving the store