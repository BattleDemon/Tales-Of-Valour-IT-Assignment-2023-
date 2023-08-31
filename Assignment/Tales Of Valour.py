from random import randint, choice

# Create a base class representing a living thing
class LivingThing():
    def __init__(self):
        self.name = 'some name'
        self.health = 1
        
    def tire(self):
        # has the chance to deal 2 dmg to the livingthing
        diceroll = randint(0,1)
        if diceroll == 0:
            self.health = self.health - 2
            print('You have gotten tired, your health suffered')
            print('Your health is', hero.health)
        else:
            pass

    def heal(self):
        # adds up to 10 health to the livingthing
        self.health = self.health + 5
        self.health = self.health + randint(0,5)
        print('Your health is now',self.health)

    def mega_heal(self):
        # doubles the livingthings health
        self.health = self.health * 2

# Create a class for the player, inheriting from LivingThing
class Player(LivingThing):
    def __init__(self, name,):
        # Initialize player-specific attributes
        global starter_room
        self.name = name
        self.health = 25
        self.status = 'regular'
        self.inventory = []
        self.equipped_weapon = ''
        self.rest_cooldown = 0

    def help(self, monster):
        # Display available actions for the player
        print('Your choices are:')
        print('help : Shows you what you can do ')
        print("stats : Display's your stats")
        print("explore : Allows you to find items and friendly Npc's at the risk of encountering a monster")
        print('inventory : Allows you to view your inventory')
        print('use : Allows you to use items in your inventory') 
        print('equip : Allows you to equip weapons')
        print('go : Allows you to move between rooms')
        print('die : Used for testing and if you want to view credits')
        print('rest : Allows the player to gain health every 5 turns')

    def stats(self, monster):
        # Display player's stats
        print('You are', self.name)
        print('You have a health of', self.health)
        print('your status is', self.status)
        print('You are in', self.room.name)
        if self.equipped_weapon == '':
            print("You don't have anything equiped")
        else:
            print('You have', self.equipped_weapon.name,'equiped')
        print("You can't rest for",self.rest_cooldown,'turns')

    def explore(self, monster):
        # Increase player's health and possibly trigger a monster encounter
        self.rest_cooldown = self.rest_cooldown - 1
        self.tire()
        diceroll = randint(0,2)
        if diceroll == 0:
            if self.room.monsters != '':
                print('You have been confronted by',self.room.monsters.name)
                self.status = 'Confronted'
                input('Press Enter to continue\n>>')
            else:
                print("You couldn't find anything")
        elif diceroll == 1:
            # Player found an item while exploring
            if self.room.items != '':
                print('You found a',self.room.items.name)
                hero.pick_up_item(self.room.items)
                self.room.items = ''
                print(self.room.items)
            else:
                print("You couldn't find anything")
        elif diceroll == 2:
            # Player encountered an FriendlyNPC
            if self.room.npcs != '':
                print('You have Encountered the', self.room.npcs.name)
                self.status = 'Encountered'
                input('Press Enter to continue\n>>')
            else:
                print("You couldn't find anything")

    def fight(self, monster):
        # Engage in combat with a monster
        self.rest_cooldown = self.rest_cooldown - 1
        monster = self.room.monsters
        while self.health > 0 and monster.health > 0:
            # First deals Dmg to the monster then to the hero 
            monster.health = monster.health - randint(0,15)
            if self.equipped_weapon != '':
                monster.health = monster.health - self.equipped_weapon.modifier
            self.health = self.health - randint(0,monster.maxdamage)
            print(monster.name, 'attacks you')
            print('your health is now',self.health)
            print(monster.name,'health is now',monster.health)
            input('Press Enter to continue\n>>')

        if self.health <= 0:
            print('You were Killed by the', monster.name)
            self.status = 'regular'
        else:
            print('Victory!\nYou defeated the', monster.name)
            print('your health is now',self.health)
            self.status = 'regular'
            self.room.monsters = ''

        def boss_fight(self,monster):
            pass
            
    def friendlyencounter(self,monster):
        # Allows the player to encounter friendlyNPC's
        option = input('Your options are \n>Leave (leave the Npc you encountered)\n>Buy ()\n>Talk ()\n>>')
        option = option.capitalize()
        while self.status == 'Encountered':
            if option == 'Leave':
                print(self.name,'walks away')
                self.status = 'regular'
                return
            elif option == 'Buy':
                pass
            elif option == 'Talk':
                pass
            else:
                print(self.name,"doesn't understand this suggestion")

    def show_inventory(self, monster):
        # Allows the player to view their inventory
        if self.inventory:
            print('You have:')
            for item in self.inventory:
                print(f'{item.name}: {item.description}')
        else:
            print('Your inventory is empty.')
    
    def pick_up_item(self, item):
        # Allows the player to pick up items
        self.inventory.append(item)  # Add the item to the inventory list
        print(f'You picked up {item.name}.')

    def use(self, monster):
        # Allows the player to use item such as health potions
        item_name = input('What item do you want to use?\n>>')
        item_name = item_name.capitalize()
        for item in self.inventory:
            if item.name == item_name:
                if isinstance(item, Weapon):
                    print("You can't use a weapon in this way.")
                else:
                    item.attributes()  # Call the item's attributes method
                    self.inventory.remove(item)  # Remove the used item from inventory
                    self.rest_cooldown = self.rest_cooldown - 1
                return
        print("You don't have that item in your inventory.")

    def equip(self, monster):
        # Allows the player to equip items they have in their inventory
        item_name = input('What do you want to equip?\n>> ')
        item_name = item_name.capitalize()
        for item in self.inventory:
            if item.name == item_name:
                self.equipped_weapon = item
                print(f'You equipped {item_name}')
                self.rest_cooldown = self.rest_cooldown - 1
                return  # Exit the function after equipping
        print("You can't equip that")

    def go(self,monster):
        # Allows the player to move between rooms 
        try:
            direction = input("Which direction do you want to go? (forward/back/left/right)\n>> ")
            # checks if the direction that was inputed is an avaliable direction
            if direction in room_connections[self.room]:
                self.room = room_connections[self.room][direction]
                print(f'You went {direction}')
                print(f'you are now in the {self.room.name}')
                self.rest_cooldown = self.rest_cooldown - 1
                self.tire()
            else:
                print("You can't go that way.")
        except KeyError:
            print("Invalid input or no valid connections from this room.")
            
    def die(self,monster):
        # Allows the player to die at will 
        self.health = 0
        death_message = [
            'Commited せっぷく',
            'Disappeared',
            'Commited Self murder'
        ]
        death_message = choice(death_message)
        print(death_message)

    def rest(self,monster):
        # allows the player to rest (gaining a small amount of health) resting can only happen once every couple of turns
        if self.rest_cooldown <= 0:
            self.heal()
            print(f'Your health is now {self.health}')
            self.rest_cooldown = 5
        else:
            print('your not tired enough to rest')

    def egg(self,monster):
        print('This is an easter egg')


# Create a class for monsters, also inheriting from LivingThing
class Monster(LivingThing):
    def __init__(self, name, health, maxdamage):
        # Initialize monster attributes
        self.name = name
        self.health = health
        self.maxdamage = maxdamage


# Create a class for friendly NPC's, also inheriting from LivingThing
class FriendlyNPC(LivingThing):
    def __init__(self,name,health,lines,items):
        # Initialize friendly NPC attributes
        self.name = name
        self.health = health
        self.lines = lines
        self.items = items


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
    def __init__(self,name ,description, monsters, npcs, items):
        # Initialize Rooms
        self.name = name
        self.description = description
        self.monsters = monsters
        self.npcs = npcs
        self.items = items
        

# function to roll credits
def credits():
    input('Press Enter to continue\n>>')
    print('\n\n\n')
    print('░▀█▀░█░█░█▀█░█▀█░█░█░█▀▀░░░█▀▀░█▀█░█▀▄░░░█▀█░█░░░█▀█░█░█░▀█▀░█▀█░█▀▀\n'
          '░░█░░█▀█░█▀█░█░█░█▀▄░▀▀█░░░█▀▀░█░█░█▀▄░░░█▀▀░█░░░█▀█░░█░░░█░░█░█░█░█\n'
          '░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀')
    print('Lead Design -- Dexter Hart')
    print('Lead Artist -- Dexter Hart')
    print('Lead Programmer -- Dexter Hart')
    print('Lead Level Designer -- Dexter Hart')
    print('Tester -- Dexter Hart')
    print('Tester -- Joss Ormes')
    print('Tester -- Samson Droney')
    print('Tester -- ')

# Dictionary of commands mapped to player methods
Commands = {
    'help': Player.help,
    'stats': Player.stats,
    'explore': Player.explore,
    'inventory': Player.show_inventory,
    'inv': Player.show_inventory,
    'use' : Player.use,
    'equip': Player.equip,
    'go' : Player.go,
    'die': Player.die,
    'rest': Player.rest,
    '': Player.egg
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

# Title
print(
    "_________ _______  _        _______  _______        _______  _______               _______  _        _______           _______ \n"
    "\__   __/(  ___  )( \      (  ____ \(  ____ \      (  ___  )(  ____ \    |\     /|(  ___  )( \      (  ___  )|\     /|(  ____ )\n"
    "   ) (   | (   ) || (      | (    \/| (    \/      | (   ) || (    \/    | )   ( || (   ) || (      | (   ) || )   ( || (    )|\n"
    "   | |   | (___) || |      | (__    | (_____       | |   | || (__        | |   | || (___) || |      | |   | || |   | || (____)|\n"
    "   | |   |  ___  || |      |  __)   (_____  )      | |   | ||  __)       ( (   ) )|  ___  || |      | |   | || |   | ||     __)\n"
    "   | |   | (   ) || |      | (            ) |      | |   | || (           \ \_/ / | (   ) || |      | |   | || |   | || (\ (   \n"
    "   | |   | )   ( || (____/\| (____/\/\____) |      | (___) || )            \   /  | )   ( || (____/\| (___) || (___) || ) \ \__\n"
    "   )_(   |/     \|(_______/(_______/\_______)      (_______)|/              \_/   |/     \|(_______/(_______)(_______)|/   \__/\n"
)
input('Press Enter to continue\n>>')

# Get the player's name
print('Welcome hero')
name = input('What is your name?\n\n>> ')
hero = Player(name)
difficulty = ''

# Get difficulty function
def get_difficulty():
    global difficulty
    while difficulty == '':
        difficulty = input('Please select a difficulty\nReally Easy <1>\nEasy <2>\n'
                           'Normal <3>\nHard <4>\nExtra Hard <5>\nExtreme <6>\n>>  ')
        if difficulty in Difficulty.keys():
            difficulty = Difficulty[difficulty]
        else:
            print('!!Please select a real difficulty!!')
            difficulty = ''
    return difficulty

# get difficulty
get_difficulty()

# Create Item instances
health_potion = Item('Health potion','Restores some health points.',hero.heal)
health_potion_2 = Item('Health potion','Restores some health points.',hero.heal)
health_potion_3 = Item('Health potion','Restores some health points.',hero.heal)
health_potion_4 = Item('Health potion','Restores some health points.',hero.heal)
mega_health_potion = Item('Mega health potion','Restores many health points.',hero.mega_heal)
teleport = Item('Teloport stone','Teleports user to any* room','') # Add fuc to teleport

magic_sword = Weapon('Magic Sword','Increase damage by 15',15)
pitch_folk = Weapon('Pitch Folk','Increase damage by 6',6)
sword = Weapon("Sword",'Increase damage by 4',4)
axe = Weapon('Axe','Increase damage by 2',2)

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

# Create friendly NPC instances
villiger = FriendlyNPC('Villiger',5,"PLACE HOLDER",'')
traveler = FriendlyNPC('Traveler',10,"PLACE HOLDER",health_potion_4)
hermit = FriendlyNPC('Hermit',15,'Place Holder','')

# Create monster instances
goblin = Monster('Goblin', round(15*difficulty),5*difficulty)
wolf = Monster('Wolf',round(10*difficulty),5*difficulty)
bear = Monster('Bear Cub',round(15*difficulty),7*difficulty)
goblin_2 = Monster('Goblin',round(5*difficulty),7*difficulty)


# Create Boss instance
dragon = Monster('Red Dragon',round(25*difficulty),12*difficulty)

# list of Monsters
monsters = [
    goblin,
    wolf,
    bear,
    goblin_2
]

# Create Rooms
starter_room = Room('Forest Clearing','in a forest clearing','','',health_potion) # room with health potion
forest = Room('Forest','you leave the clearing and venture into the forest',wolf,'',axe) # room with wolf and axe
path_in_forest = Room('Path in forest','you find a path in the forest','',traveler,'') # room with traveler
cave_entrance = Room('Cave entrance','as you wonder through the forest you come to a cave entrance',goblin,'','') # room with goblin
cave_cavern = Room('Cave Cavern','you continue deeper into the cave and find a large open cavern',goblin_2,'',sword) # room with goblin and sword
along_path = Room('Path in forest','you follow the path deeper into the forest',bear,'','') # room with bear
hut_along_path = Room('Hut along path','while following the path you come to a hut in the forest. the path splits','',hermit,'') # room with hermit
village = Room('Village','after following the path you come to a village','',villiger,pitch_folk) # room with villiger and pitch folk
other_cave_entrance = Room('Cave entrance','you follow one of the paths to an entrance to a cave','','','')
boss_room = Room('Deep Dark Cave','as you explore the cavern the ground seems to move suddenly a large creature rises from the deeps',dragon,'',teleport) # boss room with dragon and teleporter

# Room connections dictionarys
room_connections = {
    starter_room : {'forward':forest},
    forest : {'back':starter_room , 'left':cave_entrance , 'right':path_in_forest},
    path_in_forest : {'back':forest , 'forward':along_path},
    cave_entrance : {'back':forest , 'forward':cave_entrance},
    along_path : {'back':path_in_forest , 'forward':hut_along_path},
    hut_along_path : {'back':along_path , 'left':other_cave_entrance , 'right':village},
    villiger : {'back':hut_along_path},
    other_cave_entrance : {'back':hut_along_path , 'forward':cave_cavern},
    cave_cavern : {'right':cave_entrance , 'left':other_cave_entrance , 'forward':boss_room},
    boss_room : {'back':cave_cavern}
}

hero.inventory = [sword] # remove
hero.inventory.append(health_potion) # remove 
boss = dragon
monster = ''
# Main game loop function
def Main_loop():
    # Start Story
    hero.room = starter_room
    print('(type help to get a list of actions) ')
    print(hero.name, 'Your story begins' ,hero.room.description)
    # Game loop
    while hero.health > 0 and boss.health > 0:
        if hero.status == 'Confronted':
            # Force fight
            hero.fight(monster)
        elif hero.status == 'Encountered':
            # Force encounter with FriendlyNPC's
            hero.friendlyencounter(hero.room.npcs)
        else:
            # User inputs
            print('Your',hero.room.description)
            line = input('What do you want to do \n>> ')
            if hero.rest_cooldown < 0:
                hero.rest_cooldown = 0
            if line in Commands.keys():
                Commands[line](hero, monster)
            else:
                print(hero.name, 'does not understand this suggestion.')

# Run main loop
Main_loop()

# Ending options
if hero.health > 0:
    print('You Win! Game Over')
else:
    print('Game Over. you lost :(')

# roll credits 
credits()
