import time
import csv

delay = float(0.5)

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
#Todolist: Starting Weapons, Attribute assignment, make attributes leave this fuction


#making string to show all potential choices for race
raceList.remove('finalboss')
raceString = ', '.join(raceList)


print(
    'You wake up in a cave, head throbbing. You look up up to see a hole. You decide that must be how you got here. You stand up and realize you can\'t remember anything.'
)
time.sleep(delay)
print('You look down at yourself and think "Oh I must be a..."')
time.sleep(delay)
stats = ''
while stats != 'chosen':
    race = str.lower(input('Choose your type, : '))
    if race in raceList:
        #aattributes to main to be in player class
        #starting weapon to player.csv
        stats = 'chosen'
    else:
        print('{0} is unacceptable'.format(race))
print('"I must be a {0}"'.format(race))
#strength = effectiveness of weapons
#dexterity = dodge chance and attack order in batle
#vitality = Max HP and 'regeneration' capabilities?