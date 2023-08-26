from random import randint, choice

# Create a base class representing a living thing
class LivingThing():
    def __init__(self):
        self.name = 'some name'
        self.health = 1
        
    def tire(self):
        self.health = self.health - 2

    def hurt(self):
        self.health = self.health - randint(0, self.health)

    def heal(self):
        self.health = self.health + 5

    def mega_heal(self):
        self.health = self.health * 2


# Create a class for the player, inheriting from LivingThing
class Player(LivingThing):
    def __init__(self, name):
        # Initialize player-specific attributes
        self.name = name
        self.health = 25
        self.status = 'regular'
        self.inventory = {}

    def help(self, monster):
        # Display available actions for the player
        print('Your choices are:')
        for key in Commands.keys():
            print(key)

    def stats(self, monster):
        # Display player's and monster's stats
        print('You are', self.name)
        print('with health of', self.health)
        print('your status is', self.status)
        print(monster.name, 'health is', monster.health)

    def explore(self, monster):
        # Increase player's health and possibly trigger a monster encounter
        self.heal()
        print('Your health is now', self.health)
        if randint(0, 1) == 1:
            print(monster.name, 'confronts you')
            self.status = 'Confronted'
        else:
            # Player found an item while exploring
            random_item = choice(items)
            hero.pick_up_item(random_item)

    def run(self, monster):
        # Decide whether the player successfully runs from a monster
        if randint(0, self.health) < randint(0, monster.health):
            print('A monster has appeared')
            self.status = 'Confronted'
            self.fight(monster)
        else:
            self.tire()
            monster.heal()
            print('Your health suffered by running')
            print('Your health is now', self.health)

    def fight(self, monster):
        # Engage in combat with a monster
        if self.status == 'Confronted':
            self.hurt()
            monster.hurt()
            print(monster.name, 'attacks you')
            if self.health <= 0:
                print('You were Killed by the', monster.name)
            elif monster.health > 0:
                print('You survived the', monster.name)
                print('Your health is now', self.health)
            else:
                print('Victory!\nYou defeated the', monster.name)
        else:
            print('You are safe. Not a monster in sight anywhere!')

    def inventory(self, monster):
        # Displays the player's inventory
        if self.inventory:
            print('You have:')
            for item_name, item in self.inventory.items():
                print(f'{item_name}:{item.description}')
        else:
            print('Your inventory is empty.')
    
    def pick_up_item(self, item):
        # Allows the player to pick up items
        self.inventory[item.name] = item
        print(f'You picked up {item.name}.')

    def use(self, item, monster):
        pass

    def equip(self, weapon):
        pass


# Create a class for monsters, also inheriting from LivingThing
class Monster(LivingThing):
    def __init__(self, name, health):
        # Initialize monster attributes
        self.name = name
        self.health = health


# Create a class for boss's, inheriting from Monster
class Boss(Monster):
    def __init__(self,name,health,level):
        self.name = name 
        self.health = health
        self.level = level 


# Create a class for friendly NPC's, also inheriting from LivingThing
class FriendlyNPC(LivingThing):
    def __init__(self,name,health,lines):
        # Initialize friendly NPC attributes
        self.name = name
        self.health = health
        self.lines = lines


# Create a Class for Items
class Item():
    def __init__(self,name,description,attributes):
        # Initialize Items
        self.name = name 
        self.description = description
        self.attributes = attributes


# Create a class for Weapons, inheriting from Items
class Weapon(Item):
    def __init__(self,name,description,modifier):
        # Initialize Weapons
        self.name = name
        self.description = description
        self.modifier = modifier


# Create a class for Rooms
class Room():
    def __init__(self, description, monsters, npcs, items):
        # Initialize Rooms
        self.description = description
        self.monsters = monsters
        self.npcs = npcs
        self.items = items
        

# function to roll credits
def credits():
    print('\n\n\n')
    print('░▀█▀░█░█░█▀█░█▀█░█░█░█▀▀░░░█▀▀░█▀█░█▀▄░░░█▀█░█░░░█▀█░█░█░▀█▀░█▀█░█▀▀\n'
          '░░█░░█▀█░█▀█░█░█░█▀▄░▀▀█░░░█▀▀░█░█░█▀▄░░░█▀▀░█░░░█▀█░░█░░░█░░█░█░█░█\n'
          '░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀')
    print('Lead Design -- Dexter Hart')
    print('Lead Artist -- Dexter Hart')
    print('Lead Programmer -- Dexter Hart')
    print('Lead Level Designer -- Dexter Hart')
    print('Tester -- Dexter Hart')
    print('Tester -- ')
    print('Tester -- ')
    print('')

# Dictionary of commands mapped to player methods
Commands = {
    'help': Player.help,
    'stats': Player.stats,
    'explore': Player.explore,
    'run': Player.run,
    'fight': Player.fight,
    'inventory': Player.inventory,
    'inv': Player.inventory
}

# Dictionary of Difficultys 
Difficulty = {
    'Really Easy': 1,
    'Easy': 2,
    'Normal': 3,
    'Hard': 4,
    'Extra Hard': 5,
    'Extreme': 6,
    'really easy': 1,
    'easy': 2,
    'normal': 3,
    'hard': 4,
    'extra hard': 5,
    'extreme': 6,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6
}

# Get the player's name
name = input('What is your name?\n>> ')
hero = Player(name)
difficulty = ''

# Get difficulty function
def get_difficulty():
    global difficulty
    while difficulty == '':
        difficulty = input('Please select a difficulty\nReally Easy <1>\nEasy <2>\nNormal <3>\nHard <4>\nExtra Hard <5>\nExtreme <6>\n>>  ')
        if difficulty in Difficulty.keys():
            difficulty = Difficulty[difficulty]
        else:
            print('!!Please select a real difficulty!!')
            difficulty = ''
    return difficulty

# get difficulty
get_difficulty()

# Create friendly NPC instances
villiger = FriendlyNPC('Villiger',5,"PLACE HOLDER")
traveler = FriendlyNPC('Traveler',10,"PLACE HOLDER")
hermit = FriendlyNPC('Hermit',15,'Place Holder')

# Create monster instances
goblin = Monster('Goblin', round(15*difficulty))
wolf = Monster('Wolf',round(10*difficulty))
bear = Monster('Bear Cub',round(15*difficulty))
goblin_2 = Monster('Goblin',round(5*difficulty))

# list of Monsters
monsters = [
    goblin,
    wolf,
    bear,
    goblin_2
]

# Choose a random monster to face
monster = choice(monsters)

# Create Boss instance
dragon = Boss('Red Dragon',round(25*difficulty),difficulty)

# Create Item instances
health_potion = Item('Health Potion','Restores some health points.',hero.heal())
sword = Weapon("Sword",'Increase damage by 4','') # Add Atribute Later
axe = Weapon('Axe','Increase damage by 2','')
health_potion_2 = Item('Health Potion','Restores some health points.',hero.heal)
health_potion_3 = Item('Health Potion','Restores some health points.',hero.heal)
health_potion_4 = Item('Health Potion','Restores some health points.',hero.heal)
mega_health_potion = Item('Mega Health Potion','Restores many health points.',hero.mega_heal)
magic_sword = Weapon('Magic Sword')
pitch_folk = Weapon('Pitch Folk')
teleport = Item('Teloport Stone','Teleports user to any* room',)


# list of Items
items = [
    health_potion,
    sword,
    axe,
    pitch_folk,
    teleport,
    mega_health_potion,
    magic_sword,
    health_potion_2,
    health_potion_3,
    health_potion_4
]

# Create Rooms
starter_room = Room('You find your self in a forest clearing','','',health_potion)
forest = Room('You are in a large forest',wolf,'',axe)
path_in_forest = Room('You find a path in the forest','','','')
cave_entrance = Room('you find an entrance to a cave','','','')
cave = Room('you continue down the cave','','','')
cave_cavern = Room('you come to a large cavern','','','')
along_path = Room('you follow the path through the forest','','','')
hut_along_path = Room('you find a small hut along the path','','','')
village = Room('You come across a village','','','')
other_cave_entrance = Room('you found an entrance to a cave','','','')
boss_room = Room('you find your self in a large room but their is, their is something in the room','','','')

# Room connections dictionarys
room_dictionary = {
starter_room : [forest],
forest : [starter_room,cave_entrance,path_in_forest],
path_in_forest : [forest,along_path],
along_path : [path_in_forest,hut_along_path],
hut_along_path : [along_path,other_cave_entrance,village],
villiger : [hut_along_path],
other_cave_entrance : [hut_along_path,cave_cavern],
cave_cavern : [cave,other_cave_entrance,boss_room],
boss_room : [cave_cavern]
}


# Start Story
print('(type help to get a list of actions) ')
print(hero.name, 'Enters a dark cave, searching for adventure. You will soon face the', monster.name)

# Main game loop function
def Main_loop():
    while hero.health > 0 and monster.health > 0:
        line = input('What do you want to do \n>> ')
        if line in Commands.keys():
            Commands[line](hero, monster)
        else:
            print(hero.name, 'does not understand this suggestion.')

    # Ending options
    if hero.health > 0:
        print('You Win! Game Over')
    else:
        print('Game Over. you lost :(')

# Run main loop
Main_loop()

# roll credits 
credits()