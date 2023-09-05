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
        print('Your health is now',self.health)

# Create a class for the player, inheriting from LivingThing
class Player(LivingThing):
    def __init__(self, name,):
        # Initialize player-specific attributes
        self.name = name
        self.health = 25
        self.status = 'regular'
        self.inventory = []
        self.equipped_weapon = ''
        self.room = ''
        self.rest_cooldown = 0
        self.gold = 0
        self.level = 1
        self.exp = 0
        self.score = 0

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
        # checks if the player is holding an item
        if self.equipped_weapon == '':
            print("You don't have anything equiped")
        else:
            print('You have', self.equipped_weapon.name,'equiped')
        print("You can't rest for",self.rest_cooldown,'turns')
        print('You are level',self.level)
        print('you have',self.exp,'exp')
        print('Your score is',self.score)

    def explore(self, monster):
        # has a chance to lower the players health
        # has a 1/3 chance of finding 1. a monster triggering a fight (if one is in the room) 
        # 2. a friendlynpc triggering an interaction (if one is in the room)
        # 3. a chance of finding an item (if one is in the room)
        self.rest_cooldown = self.rest_cooldown - 1
        self.tire()
        self.score += 50
        self.exp += 50
        diceroll = randint(0,2)
        if diceroll == 0:
            if self.room.monsters != '':
                # Player confronted a monster
                print('You have been confronted by',self.room.monsters.name)
                self.status = 'Confronted'
                input('Press Enter to continue\n>>')
            else:
                print("You couldn't find anything")
        elif diceroll == 1:
            if self.room.items != '':
                 # Player found an item while exploring
                print('You found a',self.room.items.name)
                hero.pick_up_item(self.room.items)
                self.room.items = ''
            else:
                print("You couldn't find anything")
        elif diceroll == 2:
            if self.room.npcs != '':
                # Player encountered a FriendlyNPC
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
            if self.equipped_weapon != '':
                attack = input(f'What action do you want to do?(slash,stab,use)\n>>')
                if attack == 'slash':
                    print(self.name,"slash's at the",monster.name)
                    dmg = randint(2,7) + self.equipped_weapon.modifier
                    print(self.name,'did',dmg,'damage')
                    monster.health -= dmg
                    print(monster.name,'health is now',monster.health)
                    input('Press Enter to continue\n>>')
                elif attack == 'stab':
                    print(self.name,"stab's at the",monster.name)
                    dmg = randint(3,5) + self.equipped_weapon.modifier
                    print(self.name,'did',dmg,'damage')
                    monster.health -= dmg
                    print(monster.name,'health is now',monster.health)
                    input('Press Enter to continue\n>>')
                elif attack == 'use':
                    self.use
                else:
                    print('Please input a real attack')
            else:
                print('you punch the',monster.name)
                monster.health -= randint(0,3)
                print(monster.name,'now has',monster.health,'health')
              
        if self.health > 0:
            print('Victory!\nYou defeated the', monster.name)
            print('your health is now',self.health)
            self.status = 'regular'
            self.room.monsters = ''
            self.score += 100
            self.exp += 100
        else:
            # checks if you are still alive
            print('You were Killed by the', monster.name)
            self.status = 'regular'

        def boss_fight(self,monster):
            pass
            
    def friendlyencounter(self,monster):
        # Allows the player to encounter friendlyNPC's
        print('Your options are \n>Leave (leave the Npc you encountered')
        print('Buy (allows you to buy items from npc)')
        option = input('Talk (allows the npc to say a line)\n>>')
        option = option.capitalize()
        while self.status == 'Encountered':
            if option == 'Leave':
                # leaves the interaction
                print(self.name,'walks away')
                self.status = 'regular'
                return
            elif option == 'Buy':
                # allows you to buy items from npc
                print('You can buy',self.room.npcs.items.name,'for',self.room.npcs.item_cost)
                option_2 = input('Do you want to buy this item? (yes/no)\n>>')
                if option_2 == 'yes':
                    if self.gold >= self.room.npcs.item_cost:
                        print('You bought',self.room.npcs.items.name,'for',self.room.npcs.item_cost)
                        self.pick_up_item(self.room.npcs.items)
                        return
                    else:
                        print("you don't have enough gold to buy", self.room.npcs.items.name)
                else:
                    return
            elif option == 'Talk':
                # allows the npc to say a line
                print(self.room.npcs.lines)
                input('Press Enter to continue\n>>')
                return
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
        # Allows the player to pick up 
        self.score += 10
        self.exp += 10
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
                    self.score += 10
                    self.exp += 10
                return
        print("You don't have that item in your inventory.")

    def equip(self, monster):
        # Allows the player to equip items they have in their inventory
        item_name = input('What do you want to equip?\n>> ')
        item_name = item_name.capitalize()
        for item in self.inventory:
            if item.name == item_name:
                self.score += 25
                self.exp += 25
                if isinstance(item, Weapon):
                    if self.equipped_weapon == '':
                        self.equipped_weapon = item
                        print(f'You equipped {item_name}')
                        self.rest_cooldown = self.rest_cooldown - 1
                        self.inventory.remove(self.equipped_weapon)
                        return  # Exit the function after equipping
                    else:
                        self.inventory.append(self.equipped_weapon)
                        self.equipped_weapon = item
                        print(f'You equipped {item_name}')
                        self.rest_cooldown = self.rest_cooldown - 1
                        return  # Exit the function after equipping
                else:
                    print('that is not a weapon and can not be equiped')
                    return # Exits function
        print("You can't equip that")

    def go(self,monster):
        # Allows the player to move between rooms 
        try:
            direction = input("Which direction do you want to go? (north/south/east/west)\n>> ")
            if self.room.monsters != '':
                # checks if their is still a monster in a room and if their is has a 1/2 chance of encountering it
                num = randint(1,2)
                if num == 1:
                    print('You have been confronted by',self.room.monsters.name)
                    input('Press Enter to continue\n>>')
                    self.status = 'Confronted'
                    monster = self.room.monsters
                    self.fight(monster)
            # checks if the direction that was inputed is an avaliable direction
            if direction in room_connections[self.room]:
                self.room = room_connections[self.room][direction]
                print(f'You went {direction}')
                print(f'you are now in the {self.room.name}')
                self.rest_cooldown = self.rest_cooldown - 1
                self.tire()
                self.score += 25
                self.exp += 25
            else:
                print("You can't go that way.")
        except KeyError:
            print("Invalid input or no valid connections from this room.")
            
    def die(self,monster):
        # Allows the player to die at will 
        self.health = 0
        print('せっぷく')

    def rest(self,monster):
        # allows the player to rest (gaining a small amount of health) resting can only happen once every couple of turns
        if self.rest_cooldown <= 0:
            self.heal()
            self.rest_cooldown = 5
            self.score += 10
            self.exp += 10
        else:
            print('your not tired enough to rest')

    def teleport(self,monster):
        pass

    def show_exits(self,monster):
        pass

    def god_mode(self,monster):
        self.health = 1000
        self.inventory.append(god_weapon)
        self.exp += 100000000

# Create a class for monsters, also inheriting from LivingThing
class Monster(LivingThing):
    def __init__(self, name, health, maxdamage,drops,gold_drops):
        # Initialize monster attributes
        self.name = name
        self.health = health
        self.maxdamage = maxdamage
        self.drops = drops
        self.gold_drops = gold_drops

# Create a class for humanoid monsters, inheriting from Monster
class Humanoid(Monster):
    def __init__(self, name, health, maxdamage, drops, gold_drops):
        # Initialize humanoid monsters attributes
        self.name = name
        self.health = health
        self.maxdamage = maxdamage
        self.drops = drops
        self.gold_drops = gold_drops
        self.actions = ['slash','stab']

# Create a class for beast monsters, inheriting from Monster
class Beast(Monster):
    def __init__(self, name, health, maxdamage, drops, gold_drops):
        self.name = name
        self.health = health
        self.maxdamage = maxdamage
        self.drops = drops
        self.gold_drops = gold_drops
        self.actions = ['slash','maul']

class Dragon(Monster):
    def __init__(self, name, health, maxdamage, drops, gold_drops):
        self.name = name
        self.health = health
        self.maxdamage = maxdamage
        self.drops = drops
        self.gold_drops = gold_drops
        self.actions = ['flamebreath','fireball']

# Create a class for friendly NPC's, also inheriting from LivingThing
class FriendlyNPC(LivingThing):
    def __init__(self,name,health,lines,items,item_cost):
        # Initialize friendly NPC attributes
        self.name = name
        self.health = health
        self.lines = lines
        self.items = items
        self.item_cost = item_cost

# Create a Class for Items
class Item():
    def __init__(self,name,description,attributes):
        # Initialize Items
        self.name = name 
        self.description = description
        self.attributes = attributes

# Create a class for Weapons, inheriting from Item
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
    print('Tester -- Gabriel Mesquita')

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
    'password': Player.god_mode
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
print('you are a travelar from a far of land')
print('you came to this land to find valour of die trying')
name = input('What is your name?\n>> ')
hero = Player(name)
difficulty = 2

# Create Item instances
health_potion = Item('Health potion','Restores some health points.',hero.heal) # found in starter room
health_potion_2 = Item('Health potion','Restores some health points.',hero.heal) # found in
health_potion_3 = Item('Health potion','Restores some health points.',hero.heal) # found in
health_potion_4 = Item('Health potion','Restores some health points.',hero.heal) # found in
health_potion_5 = Item('Health potion','Restores some health points.',hero.heal) # found in
health_potion_6 = Item('Health potion','Restores some health points.',hero.heal) # found in
health_potion_7 = Item('Health potion','Restores some health points.',hero.heal) # found in
mega_health_potion = Item('Mega health potion','Restores many health points.',hero.mega_heal) # drops from 
mega_health_potion_2 = Item('Mega health potion','Restores many health points.',hero.mega_heal) # buy from hermit for 200 gold
teleport = Item('Teloport stone','Teleports user to any* room','') # Add fuc to teleport/ found in boss room

# Create Weapon instances
magic_sword = Weapon('Magic Sword','Increase damage by 15',15) # Drops from dragon
pitch_folk = Weapon('Pitch Folk','Increase damage by 6',6) # found in village
sword = Weapon("Sword",'Increase damage by 4',4) # found in 
axe = Weapon('Axe','Increase damage by 2',2) # found on path in forest
traveler_sword = Weapon('Traveler sword','Increase damage by 8',8) # buy from travelar for 250 gold
village_guard_sword = Weapon('Guard sword','Increase damage by 10',10) # buy from villager for 300 gold
sharp_stick = Weapon('Sharp stick','Increases damage by 1',1) # found in forest
lords_sword = Weapon('Lords Sword','Increase damage by 12',12) # found in keep
god_weapon = Weapon('Gods sword','Increase damage by 100',100) # if player uses god_mode func

# list of Items
items = [
    health_potion,
    health_potion_2,
    health_potion_3,
    health_potion_4,
    health_potion_5,
    health_potion_6,
    health_potion_7,
    mega_health_potion,
    mega_health_potion_2,
    teleport,
    sword,
    axe,
    pitch_folk,
    traveler_sword,
    magic_sword,
    village_guard_sword,
    sharp_stick,
    lords_sword
]

# Create friendly NPC instances
villiger = FriendlyNPC('Villiger',5,"I have heard storys of the horrors out side the village",'','')
traveler = FriendlyNPC('Traveler',10,"I just got robbed on the trail i suggest you turn back now",traveler_sword,250)
hermit = FriendlyNPC('Hermit Samson',15,'Those village folk are always scared of what is out of their village',mega_health_potion,200)
lord = FriendlyNPC('Lord Joss',20,'Have you heard of the goblins to the north, they send war partys to are lands','','')

# Create monster instances
wolf = Beast('Wolf',round(10*difficulty),5*difficulty,'',20)
wolf_2 = Beast('Wolf',round(10*difficulty),5*difficulty,'',20)
bear = Beast('Bear Cub',round(15*difficulty),7*difficulty,'',30)
spider = Beast('Giant Spider',round(15*difficulty),7*difficulty,'',30)
goblin_scout = Humanoid('Goblin Scout',round(5*difficulty),5*difficulty,'',50)
bandit = Humanoid('Bandit',round(25*difficulty),7*difficulty,'',100)
thug = Humanoid('Thug',round(15*difficulty),7*difficulty,'',100)
goblin = Humanoid('Goblin', round(15*difficulty),5*difficulty,'',50)
goblin_scout_2 = Humanoid('Goblin Scout',round(5*difficulty),5*difficulty,'',50)
goblin_scout_3 = Humanoid('Goblin Scout',round(5*difficulty),5*difficulty,'',50)
goblin_runt = Humanoid('Goblin Runt',round(2*difficulty),3*difficulty,'',30)
goblin_brute = Humanoid('Goblin Brute',round(20*difficulty),9*difficulty,'',100)
troll = Humanoid('Troll',round(20*difficulty),9*difficulty,'',100)

# Create Boss instance
dragon = Dragon('Red Dragon',round(25*difficulty),12*difficulty,magic_sword,400)

# Create Rooms
forest_clearing = Room('Forest Clearing','you are in a forest clearing','','',health_potion)
forest = Room('Forest','you are in a forest',wolf,'',sharp_stick)
path_in_forest = Room('Path in Forest','you find a path in the forest','','',axe)
deeper_in_forest = Room('Deeper in Forest','you are deeper in the forest',wolf_2,'','')
along_forest = Room('Along Path','You are following a path',bear,traveler,'')
deep_forest = Room('Deep Dark Forest','You are in a deep dark forest',spider,'','')
hut_in_forest = Room('Hut in Forest','you are on a hut along the path','',hermit,'')
meadow = Room('meadow','You are in a wide open meadow',goblin_scout,'','')
cross_road = Room('Cross Roads','You are at a cross roads their is a sign pointing west it says village of {}',bandit,'','')
village = Room('The village','You are in a village',thug,villiger,pitch_folk)
along_ridge = Room('Along the Ridge','You are along a ridge',goblin,'','')
tall_ridge = Room('Tall Ridge','You are at a tall ridge',goblin_scout_2,'','')
path_in_meadow = Room('Path Along Meadow','you are on a path in a meadow',goblin_scout_3,'','')
keep = Room('The Keep','you are in the keep of lord joss','',lord,lords_sword)
cave_entrance_2 = Room('Cave Entrance','You are in a cave entrance',goblin_runt,'','')
cave_entrance = Room('Cave Entrance','You are in a cave entrance',goblin_brute,'','')
deep_cave = Room('Deeper in cave','You are in a deep cave',troll,'','')
cave_cavern = Room('Cave Cavern','You are in a large open cavern','','','')
Boss_Room = Room('Open Cavern','',dragon,'',magic_sword)

# Room connections dict
room_connections = {
    forest_clearing : {'north' : forest},
    forest : {'north' : deeper_in_forest, 'west' : path_in_forest, 'south' : forest_clearing},
    deeper_in_forest : {'north' : deep_forest, 'west' : along_forest, 'south' : forest},
    along_forest : {'north' : hut_in_forest, 'east' : deeper_in_forest, 'south' : path_in_forest},
    deep_forest : {'north' : meadow, 'south' : deeper_in_forest},
    hut_in_forest : {'north' : cross_road, 'south' : along_forest},
    meadow : {'north' : tall_ridge, 'south' : deep_forest},
    cross_road : {'north' : path_in_meadow, 'west' : village, 'south' : hut_in_forest},
    village : {'north' : keep, 'east' : cross_road},
    along_ridge : {'north' : cave_entrance_2, 'west' : tall_ridge},
    tall_ridge : {'north' : cave_entrance, 'east' : along_ridge, 'west' : path_in_meadow, 'south' : meadow},
    path_in_meadow : {'east' : along_ridge, 'west' : keep, 'south' : cross_road},
    keep : {'east' : path_in_meadow, 'south' : village},
    cave_entrance_2 : {'north' : deep_cave, 'south' : along_ridge},
    cave_entrance : {'north' : cave_cavern, 'south' : tall_ridge},
    deep_cave : {'west' : cave_cavern, 'south' : cave_entrance_2},
    cave_cavern : {'east' : deep_cave, 'east' : Boss_Room, 'south' : cave_entrance},
    Boss_Room : {'east' : cave_cavern}
}

hero.inventory = [sword] # remove
hero.inventory.append(health_potion) # remove 
boss = dragon
forest_clearing.npcs = hermit # remove
hero.gold = 10000000 # remove
monster = ''
exp_to_next_level = 100
hero.room = forest_clearing
# Main game loop function
def Main_loop():
    # Start Storys
    print('(type help to get a list of actions) ')
    print(hero.name, 'Your story begins' ,hero.room.description)
    exp_to_next_level = 100
    # Game loop
    while hero.health > 0 and boss.health > 0:
        if hero.status == 'Confronted':
            # Force fight
            hero.fight(monster)
        elif hero.status == 'Encountered':
            # Force encounter with FriendlyNPC's
            hero.friendlyencounter(hero.room.npcs)
        elif hero.exp >= exp_to_next_level:
            # levels the player up
            hero.level += 1
            hero.health += 15
            print('You leveled up!!')
            print('You are now level',hero.level)
            print('You now have',hero.health,'health')
            hero.exp -= exp_to_next_level
            exp_to_next_level += exp_to_next_level
            input('Press Enter to continue\n>>')
        else:
            # User inputs
            print(hero.room.description)
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
input('Press Enter to continue\n>>')

# shows the player their inventory 
if hero.inventory:
    print('You had:')
    for item in hero.inventory:
        print(f'{item.name}: {item.description}')
else:
    print('Your inventory was empty.')

# Shows the player their important stats
input('Press Enter to continue\n>>')
print('You are level',hero.level)
print('you have',hero.exp,'exp')
print('Your score is',hero.score)

# roll credits 
credits()
