import time
#This runs at the start of the game to create a char. build...
delay = float(0.5)
#Strength
#Dexterity
#Vitality
#Startingweapon?

print('You wake up in a cave, head throbbing. You look up up to see a hole. You decide that must be how you got here. You stand up and realize you can\'t remember anything.')
time.sleep(delay)
print('You look down at yourself and think "Oh I must be a..."')
time.sleep(delay)
stats = 'choosing'
while stats == 'choosing':
  race = str.lower(input('Choose your race: Elf, Dwarf, or Human: '))#we should add more races
#weapon select(NYI) and attribute assignment (attributes out of 10)
  if race == 'human':
    strenght = 6
    dexterity = 6
    vitality = 5
    stats = 'chosen'
  elif race == 'elf':
    strength = 4
    dexterity = 8
    vitality = 6
    stats = 'chosen'
  elif race == 'dwarf':
    strength = 7
    dexterity = 3
    vitality = 7
    stats = 'chosen'
  else:
    print('{0} is unacceptable'.format(race))

print('"I must be a {0}"'.format(race))
#strength = effectiveness of weapons
#dexterity = dodge chance and attack order in batle
#vitality = Max HP and 'regeneration' capabilities?