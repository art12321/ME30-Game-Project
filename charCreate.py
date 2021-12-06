import time
import csv
import classFramework as cf


delay = 0.5

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

#code for activating enemies 

goblinStats = raceATT[raceList.index('goblin')]
goblinWeapon = (weaponATT[weaponList.index('dagger')])
goblinWeaponName = "dagger"
bossStats = raceATT[raceList.index('finalboss')]
bossWeapon = (weaponATT[weaponList.index('dagger')])
bossWeaponName = "dagger"

#making strings to show all playable races and weapons
raceList.remove('finalboss')
raceList.remove('goblin')
weaponList.remove('weaponBase')
weaponList.remove('fist')
raceString = ', '.join(raceList)
weaponString = ', '.join(weaponList)

# where what you actually see in game starts

print(
    'You wake up in a cave with a throbbing headache. You look up up to see a hole. You decide that must be how you got here. After standing up, you realize that you can\'t remember anything. Even My Name...'
)
print()
time.sleep(delay)
playerName = input("I think my name is: ")
print()
time.sleep(delay)
print('You look down at yourself and realize, "Oh I must be a..."')
print()
time.sleep(delay)
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
time.sleep(delay)
print()
print(
    "You see a stack of weapons on the ground next to you, but can\'t remember which one was yours."
)
print()

time.sleep(delay)
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
weapName = wStats[0]

player1 = cf.state((player1Vit*10),player1Str*10,player1Vit,player1Dex,cf.position(0,0),0,weapon, playerName)
baseGoblin = cf.state((goblinStats[2]*5),goblinStats[0],goblinStats[2],goblinStats[1],cf.position(0,0),0,goblinWeaponName,"Goblin")
baseBoss = cf.state((bossStats[2]*5),bossStats[0],bossStats[2],bossStats[1],cf.position(0,0),0,goblinWeaponName,"Boss Man")

#strength = effectiveness of wholder
#dexterity = dodge chance and attack order in batle
#vitality = Max HP and 'regeneration' capabilities?
