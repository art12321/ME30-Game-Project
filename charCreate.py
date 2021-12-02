import time
import csv


delay = 0.5

racefile = open('race.csv', 'r')
raceing = csv.DictReader(racefile)
weaponfile = open('weapons.csv', 'r')
weaponing = csv.DictReader(weaponfile)
raceList = []
raceATT = []
weaponList = []
weaponATT = []

#appending csv files to lists to compare for potential choices and get sholder

for col in raceing:
    raceList.append(col['raceName'])
    raceATT.append(col['StrengthDexterityVitality'])
for col in weaponing:
    weaponList.append(col['weaponName'])
    weaponATT.append(col['stats'])

#making string to show all playable races and wholder
raceList.remove('finalboss')
raceList.remove('goblin')
weaponList.remove('weaponBase')
weaponList.remove('fist')
raceString = ', '.join(raceList)
weaponString = ', '.join(weaponList)


print(
    'You wake up in a cave with a throbbing headache. You look up up to see a hole. You decide that must be how you got here. After standing up, you realize that you can\'t remember anything.'
)
time.sleep(delay)
print('You look down at yourself and realize, "Oh I must be a..."')
time.sleep(delay)
sholder = ''
wholder = ''
while sholder != 'chosen':
    race = str.lower(input('Choose your type, {0}: '.format(raceString)))
    if race in raceList:
        poss = raceList.index(race)
        Stats = (raceATT[poss])
        sholder = 'chosen'
    else:
        print('{0} is unacceptable'.format(race))
print('"I must be a {0}"'.format(race))
time.sleep(delay)
print(
    "You see a stack of weapons on the ground next to you, but can\'t remember which one was yours."
)
time.sleep(delay)
while wholder != 'chosen':
    weapon = str.lower(input('Choose your weapon: {0}: '.format(weaponString)))
    if weapon in weaponList:
        posw = weaponList.index(weapon)
        wStats = (weaponATT[posw])
        wholder = 'chosen'
    else:
        print('{0} is not acceptable, please try again'.format(weapon))
print('"Ah yes, this one is mine" You say as you pick up your {0} from the pile.'.format(weapon))


str = Stats[0]
dex = Stats[1]
vit = Stats[2]


#strength = effectiveness of wholder
#dexterity = dodge chance and attack order in batle
#vitality = Max HP and 'regeneration' capabilities?
