import time
import csv

delay = float(0.5)

racefile = open('race.csv', 'r')
raceing = csv.DictReader(racefile)
raceList = []
raceATT = []
for col in raceing:
    raceList.append(col['raceName'])
    raceATT.append(col['SDV'])
print(raceATT)

class race:
  def __init__(self,stats):
    self.str = str(stats)[0]
    self.dex = str(stats)[1]
    self.vit = str(stats)[2]
#Todolist: Starting Weapons, Attribute assignment, make attributes leave this fuction

print(
    'You wake up in a cave, head throbbing. You look up up to see a hole. You decide that must be how you got here. You stand up and realize you can\'t remember anything.'
)
time.sleep(delay)
print('You look down at yourself and think "Oh I must be a..."')
time.sleep(delay)
stats = ''
while stats != 'chosen':
    race = str.lower(input('Choose your character: Elf, Dwarf, Human : '))
    if race in raceList:
        #aattributes to player.csv
        #starting weapon to player.csv
        stats = 'chosen'
    else:
        print('{0} is unacceptable'.format(race))
print('"I must be a {0}"'.format(race))
#strength = effectiveness of weapons
#dexterity = dodge chance and attack order in batle
#vitality = Max HP and 'regeneration' capabilities?
