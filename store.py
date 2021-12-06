import time
import classFramework as cf
import charCreate as cc


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
    #weapon change
    return (print('goblin'))


def wizard():
    #stat change
    return (print('wizard'))


shoppos = 0  # counter of where in the shop code we are

print(
    'As you enter this room you look around and see paneling and chairs. As you walk further, you start to hear music and then it dawns on you, you\'re in some sort of underground tavern. You decide to step in to take a break from everything else and maybe get a drink. You sit down at the bar and strike up a conversation with the bartender.')
barkeeper()

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
print('Since you\'ve decided to leave the tavern you must continue back into the dark dingy cave to find your way out. ')