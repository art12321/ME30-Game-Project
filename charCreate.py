import time
import csv
import classFramework as cf


def delay():
  time.sleep(0.5)

racefile = open('race.csv', 'r')
raceing = csv.DictReader(racefile)
weaponfile = open('weapons.csv', 'r')
weaponing = csv.DictReader(weaponfile)
raceList = []
raceATT = []
weaponList = []
weaponATT = []

#appending csv files to lists to compare for potential choices and get stats

for col in raceing:
    raceList.append(col['raceName'])
    raceATT.append(col['StrengthDexterityVitality'])
for col in weaponing:
    weaponList.append(col['weaponName'])
    weaponATT.append(col['stats'])

#code for activating enemies states 

goblinStats = raceATT[raceList.index('goblin')]
goblinWeapon = (weaponATT[weaponList.index('dagger')])
goblinWeaponName = "dagger"
bossStats = raceATT[raceList.index('finalboss')]
bossWeapon = (weaponATT[weaponList.index('longsword')])
bossWeaponName = "longsword"

#making strings to show all playable races and weapons
raceList.remove('finalboss')
raceList.remove('goblin')
weaponList.remove('weaponBase')
weaponList.remove('fist')
raceString = ', '.join(raceList)
weaponString = ', '.join(weaponList)

def charactercreation():

  print(
      'You wake up in a cave with a throbbing headache. You look up up to see a hole. You decide that must be how you got here.\nAfter standing up, you realize that you can\'t remember anything. \nEven your own name... \nSuddenly, it comes to you.'
  )
  print()
  delay()
  playerName = input("Thats right, my name is: ")
  print()
  delay()
  print('You take a second to recuperate and examine yourself. Even though you can\'t remember what you are, you look down and, based off what you see, say, "Oh I must be a..."')
  print()
  delay()
  
  #placeholders for breaking character and weapon selection loops
  sholder = '' 
  wholder = ''

  #race selection loop
  while sholder != 'chosen':
      race = str.lower(input('Choose your type, {0}: '.format(raceString)))
      if race in raceList:
          poss = raceList.index(race)
          Stats = (raceATT[poss])
          sholder = 'chosen'
      else:
          print('{0} is unacceptable'.format(race))
  print('"I must be a {0}"'.format(race))
  delay()
  print()
  print(
      "You see a stack of weapons on the ground next to you, but can\'t remember which one was yours."
  )
  print()

  delay()
  #weapon selection loop
  while wholder != 'chosen':
      weapon = str.lower(input('Choose your weapon: {0}: '.format(weaponString)))
      if weapon in weaponList:
          posw = weaponList.index(weapon)
          wStats = (weaponATT[posw])
          wholder = 'chosen'
      else:
          print('{0} is not acceptable, please try again'.format(weapon))
  print('"Ah yes, this one is mine" You say as you pick up your {0} from the pile.'.format(weapon))
  print()
  player1Str = Stats[0]
  player1Dex = Stats[1]
  player1Vit = Stats[2]
  player1 = cf.state(int(player1Vit)*10,player1Str,player1Vit,player1Dex,cf.position(0,0),0,weapon, playerName, 1.5)
  return player1



#Enemy Archtypes
baseGoblin = cf.state(int(goblinStats[2]),goblinStats[0],goblinStats[2],goblinStats[1],cf.position(0,0),0,goblinWeaponName,"Goblin",1.5)
baseBandit = cf.state(int(goblinStats[2]),goblinStats[0],goblinStats[2],goblinStats[1],cf.position(0,0),0,goblinWeaponName,"Bandits",1.5)
baseCultist = cf.state(int(goblinStats[2]),goblinStats[0],goblinStats[2],goblinStats[1],cf.position(0,0),0,goblinWeaponName,"Cultist",1.5)
baseOrc = cf.state(int(goblinStats[2]),goblinStats[0],goblinStats[2],goblinStats[1],cf.position(0,0),0,goblinWeaponName,"Orc",1.5)
baseMage = cf.state(int(goblinStats[2]),goblinStats[0],goblinStats[2],goblinStats[1],cf.position(0,0),0,goblinWeaponName,"Mage",1.5)
baseDemon = cf.state(int(goblinStats[2]),goblinStats[0],goblinStats[2],goblinStats[1],cf.position(0,0),0,goblinWeaponName,"Demon",1.5)
baseBoss = cf.state(int(bossStats[2])*5,bossStats[0],bossStats[2],bossStats[1],cf.position(0,0),0,goblinWeaponName,"Boss Man",1.5)

#strength = effectiveness of wholder
#dexterity = dodge chance and attack order in batle
#vitality = Max HP and 'regeneration' capabilities?
