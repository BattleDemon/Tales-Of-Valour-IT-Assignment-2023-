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
        heal_amount = randint(0,5) + 5
        self.health += heal_amount
        print('You gained',heal_amount,'health')
        print('Your health is now',self.health)

    def mega_heal(self):
        # doubles the livingthings health
        self.health = self.health + 20
        print('You gained 20 health')
        print('Your health is now',self.health)

    def nothing(self):
        pass

# Create a class for the player, inheriting from LivingThing
class Player(LivingThing):
    def __init__(self, name,):
        # Initialize player-specific attributes c
        self.name = name
        self.health = 25
        self.status = 'regular'
        self.inventory = []
        self.equipped_weapon = ''
        self.equipped_armour = ''
        self.room = ''
        self.rest_cooldown = 0
        self.gold = 0
        self.level = 1
        self.exp = 0
        self.score = 0
        self.dev = False

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
        print('quit : allows you to quit the game')
        print('rest : Allows the player to gain health every 5 turns')

    def stats(self, monster):
        # Display player's stats
        print('You are', self.name)
        print('You have a health of', self.health)
        print('your status is', self.status)
        print('You are in', self.room.name)
        # checks if the player is holding a weapon
        if self.equipped_weapon == '':
            print("You don't have any weapon equiped")
        else:
            print('You have', self.equipped_weapon.name,'equiped')
            print(self.equipped_weapon.name,'Increases damage by',self.equipped_weapon.modifier)
        # checks if the player is wearing armour
        if self.equipped_armour == '':
            print("You don't have any armour equiped")
        else:
            print('You have', self.equipped_armour.name,'equiped')
            print(self.equipped_armour.name,'Reduces damage taken by',self.equipped_armour.modifier)
        print("You can't rest for",self.rest_cooldown,'turns')
        print('you have',self.gold,'gold')
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
        diceroll = randint(0,2)
        if diceroll == 0:
            if self.room.monsters != '':
                # Player confronted a monster
                print('You have been confronted by',self.room.monsters.name)
                self.status = 'Confronted'
                self.score += 50
                self.exp += 50
                input('Press Enter to continue\n>>')
                monster = self.room.monsters
                return monster
            else:
                print("You couldn't find anything")
        elif diceroll == 1:
            if self.room.items != '':
                 # Player found an item while exploring
                print('You found a',self.room.items.name)
                hero.pick_up_item(self.room.items)
                self.room.items = ''
                self.score += 50
                self.exp += 50
            else:
                print("You couldn't find anything")
        elif diceroll == 2:
            if self.room.npcs != '':
                # Player encountered a FriendlyNPC
                print('You have Encountered the', self.room.npcs.name)
                self.status = 'Encountered'
                self.score += 50
                self.exp += 50
                input('Press Enter to continue\n>>')
            else:
                print("You couldn't find anything")

    def use(self, monster):
        # Allows the player to use item such as health potions
        item_name = input('What item do you want to use?\n>>')
        item_name = item_name.capitalize()
        for item in self.inventory:
            if item.name == item_name:
                if isinstance(item, Weapon):
                    print("You can't use a weapon in this way.")
                elif isinstance(item, Armour):
                    print("You can't use armour in this way.")
                elif item_name == 'Key':
                    if locket in self.inventory:
                        print('you notice the key matches the lock on the locket')
                        print('you turn the key')
                        print('after you hear the click of the lock the locket disapears')
                        print('you gain 500 xp')
                        self.inventory.remove(locket)
                        self.exp += 500
                        self.score += 500
                elif item_name == 'Locket':
                    if key in self.inventory:
                        print('you notice the lock on the locket matches the shape of the key ')
                        print('you turn the key')
                        print('after you hear the click of the lock the locket disapears')
                        print('you gain 500 xp')
                        self.inventory.remove(locket)
                        self.exp += 500
                        self.score += 500
                else:
                    item.attributes()  # Call the item's attributes method
                    self.inventory.remove(item)  # Remove the used item from inventory
                    self.rest_cooldown = self.rest_cooldown - 1
                    self.score += 10
                    self.exp += 10
                return
        print("You don't have that item in your inventory.")

    def fight(self, monster):
        # Engage in combat with a monster
        self.rest_cooldown = self.rest_cooldown - 1
        while self.health > 0 and monster.health > 0:
            # First deals Dmg to the monster then to the hero 
            non_comabat_action = False
            if self.equipped_weapon != '':
                attack = input(f'What action do you want to do?(slash,stab,use,inv)\n>>')
                if attack == 'slash':
                    print(self.name,"slash's at the",monster.name)
                    dmg = randint(2,9) + self.equipped_weapon.modifier
                    print(self.name,'did',dmg,'damage')
                    monster.health -= dmg
                    print(monster.name,'health is now',monster.health)
                    input('Press Enter to continue\n>>')
                elif attack == 'stab':
                    print(self.name,"stab's at the",monster.name)
                    dmg = randint(3,6) + self.equipped_weapon.modifier
                    print(self.name,'did',dmg,'damage')
                    monster.health -= dmg
                    print(monster.name,'health is now',monster.health)
                    input('Press Enter to continue\n>>')
                elif attack == 'use':
                    self.use(monster)
                    non_comabat_action = True
                    input('Press Enter to continue\n>>')
                elif attack == 'inv':
                    self.show_inventory(monster)
                    non_comabat_action = True
                else:
                    print('Please input a real attack')
                    non_comabat_action = True
            else:
                attack = input('What action do you want to do?(punch,use,inv)\n>>')
                if attack == 'punch':
                    dmg = randint(0,5)
                    print('you punch the',monster.name,'for',dmg,'damage')
                    monster.health -= dmg
                    print(monster.name,'now has',monster.health,'health')
                    input('Press Enter to continue\n>>')
                elif attack == 'use':
                    self.use(monster)
                    non_comabat_action = True
                    input('Press Enter to continue\n>>')
                elif attack == 'inv':
                    self.show_inventory(monster)
                    non_comabat_action = True
                else:
                    print('Please input a real attack')
                    non_comabat_action = True
            if monster.health > 0:
                if non_comabat_action == True:
                    pass
                else:
                    mindamage = round(monster.maxdamage/3)
                    dmg = randint(mindamage,monster.maxdamage)
                    if self.equipped_armour != '':
                        dmg -= self.equipped_armour.modifier
                    print('The',monster.name,choice(monster.actions),'you for',dmg,'damage')
                    self.health -= dmg
                    print('Your health is now',self.health)
                    input('Press Enter to continue\n>>')
              
        if self.health > 0:
            print('Victory!\nYou defeated the', monster.name)
            print('your health is now',self.health)
            self.status = 'regular'
            self.room.monsters = ''
            self.score += 100
            self.exp += 100
            if monster.drops != '':
                self.inventory.append(monster.drops)
                print('you picked up',monster.drops.name,'from',monster.name)
            self.gold += monster.gold_drops
            print('you picked up',monster.gold_drops,'gold')
            input('Press Enter to continue\n>>')
        else:
            # checks if you are still alive
            print('You were Killed by the', monster.name)
            self.status = 'regular'

    def boss_fight(self,monster):
        global fight_stage
        if fight_stage == 1:
            print(boss.name,': Petty mortal')
            print('you have entered my realm ')
            print('Yet you still are not worthy to challenge me')
            print('you need to prove that you are worth my time')
            print(self.name,'you see a gate open behind you and a goblin brute enters')
            monster = goblin_brute_2
            self.fight(monster)
            fight_stage += 1
        elif fight_stage == 2:
            print(boss.name,': hmmn')
            print('well done mortal')
            print('NOW YOU CHALLENGE ME')
            print('YOU CANT TURN BACK NOW')
            print('LETS SEE HOW LONG YOU CAN LIVE')
            input('Press Enter to continue\n>>')
            fight_stage += 1
        elif fight_stage == 3:
            first_round = True
            while self.health > 0 and monster.health > 0:
                # First deals Dmg to the monster then to the hero 
                non_comabat_action = False
                if first_round == True:
                    first_round = False
                else:
                    if self.equipped_weapon != '':
                        attack = input(f'What action do you want to do?(slash,stab,use,inv)\n>>')
                        if attack == 'slash':
                            print(self.name,"slash's at the",boss.name)
                            dmg = randint(2,9) + self.equipped_weapon.modifier
                            print(self.name,'did',dmg,'damage')
                            boss.health -= dmg
                            print(boss.name,'health is now',boss.health)
                            input('Press Enter to continue\n>>')
                        elif attack == 'stab':
                            print(self.name,"stab's at the",boss.name)
                            dmg = randint(3,6) + self.equipped_weapon.modifier
                            print(self.name,'did',dmg,'damage')
                            boss.health -= dmg
                            print(boss.name,'health is now',boss.health)
                            input('Press Enter to continue\n>>')
                        elif attack == 'use':
                            self.use(boss)
                            non_comabat_action = True
                            input('Press Enter to continue\n>>')
                        elif attack == 'inv':
                            self.show_inventory(boss)
                            non_comabat_action = True
                        else:
                            print('Please input a real attack')
                            non_comabat_action = True
                    else:
                        attack = input('What action do you want to do?(punch,use,inv)\n>>')
                        if attack == 'punch':
                            dmg = randint(0,5)
                            print('you punch the',boss.name,'for',dmg,'damage')
                            boss.health -= dmg
                            print(boss.name,'now has',boss.health,'health')
                            input('Press Enter to continue\n>>')
                        elif attack == 'use':
                            self.use(boss)
                            non_comabat_action = True
                            input('Press Enter to continue\n>>')
                        elif attack == 'inv':
                            self.show_inventory(boss)
                            non_comabat_action = True
                        else:
                            print('Please input a real attack')
                            non_comabat_action = True
                if boss.health >= 0:
                    if non_comabat_action == True:
                        pass
                    else:
                        mindamage = round(boss.maxdamage/3)
                        dmg = randint(mindamage,boss.maxdamage)
                        if self.equipped_armour != '':
                            dmg -= self.equipped_armour.modifier
                        print('The',boss.name,choice(boss.actions),'you for',dmg,'damage')
                        self.health -= dmg
                        print('Your health is now',self.health)
                        input('Press Enter to continue\n>>')
            if self.health > 0:
                # checks if you are still alive
                print('Victory!\nYou defeated the', boss.name)
                self.room.monsters = ''
                input('Press Enter to continue\n>>')
            else:
                print('You were Killed by', boss.name)

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
                if self.room.npcs.items != '':
                    print('you have',self.gold,'gold')
                    print('You can buy',self.room.npcs.items.name,'for',self.room.npcs.item_cost)
                    option_2 = input('Do you want to buy this item? (yes/no)\n>>')
                    if option_2 == 'yes':
                        if self.gold >= self.room.npcs.item_cost:
                            print('You bought',self.room.npcs.items.name,'for',self.room.npcs.item_cost)
                            self.pick_up_item(self.room.npcs.items)
                            self.gold -= self.room.npcs.item_cost
                            return
                        else:
                            print("you don't have enough gold to buy", self.room.npcs.items.name)
                    else:
                        return
                else:
                    print("this Npc doesn't have an item to sell")
                    input('Press Enter to continue\n>>')
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
                        self.inventory.remove(item)
                        print(f'You equipped {item_name}')
                        self.rest_cooldown = self.rest_cooldown - 1
                        return  # Exit the function after equipping
                elif isinstance(item, Armour):
                    if self.equipped_armour == '':
                        self.equipped_armour = item
                        print(f'You equipped {item_name}')
                        self.rest_cooldown = self.rest_cooldown - 1
                        self.inventory.remove(self.equipped_armour)
                        return  # Exit the function after equipping
                    else:
                        self.inventory.append(self.equipped_armour)
                        self.equipped_armour = item
                        self.inventory.remove(item)
                        print(f'You equipped {item_name}')
                        self.rest_cooldown = self.rest_cooldown - 1
                        return  # Exit the function after equipping
                else:
                    print('that is not a weapon or armour and can not be equiped')
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
            
    def quit(self,monster):
        # Allows the player to quit the game 
        self.health = 0                            

    def rest(self,monster):
        # allows the player to rest (gaining a small amount of health) resting can only happen once every couple of turns
        if self.rest_cooldown <= 0:
            self.heal()
            self.rest_cooldown = 5
            self.score += 10
            self.exp += 10
        else:
            print('your not tired enough to rest')

    def show_exits(self,monster):
        pass

    def dev_mode(self,monster):
        # allows the player to activate dev mode making them over powered 
        self.health = 1000
        self.equipped_weapon = god_weapon
        self.exp += 100000000
        self.gold += 100000
        Commands.popitem()
        self.dev = True

    def save(self,monster):
        # Allows the player to save the game
        pass

    def load(self,monster):
        # Allow the player to load a saved game
        pass

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

# Create a class for armour, inheriting from weapon
class Armour(Item):
    def __init__(self,name,description,modifier):
        # initialize Armour
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
    print('Tester -- Samson Droney') 
    print('Tester -- Will Garner')
    print('Tester -- Dexter Hart')
    print('Tester -- Gabriel Mesquita')
    print('Tester -- Joss Ormes')

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
    'quit': Player.quit,
    'rest': Player.rest,
    'i am a dev': Player.dev_mode
}

# Dictionary of Difficultys 
Difficulty = {
    'Easy': 1,
    'Normal': 2,
    'Hard': 3,
    '1' : 1,
    '2' : 2,
    '3' : 3
}

difficulty = ''

# get difficulty
def get_difficulty():
    global difficulty
    while difficulty == '':
        difficulty = input("Please select a difficulty:\nEasy (1),\nNormal (2),\nHard (3)\n>>")
        if difficulty in Difficulty.keys():
            difficulty = Difficulty[difficulty]
        else:
            print('!!Please select a real difficulty!!')
            difficulty = ''
    return difficulty

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
print('you are a travelar from a far off land')
print('you came to this land to find valour or die trying')
name = input('What is your name?\n>> ')
hero = Player(name)
get_difficulty()

try:
    # get high score 
    file = open("highscore.txt",'r')
    high_score = int(file.read())
    file.close()

    # get player with high score
    file = open('highscoreholder.txt','r')
    high_score_holder = file.read()
    file.close()

    # tell player high score and its holder
    print('the current highscore holder is',high_score_holder,'with a score of',high_score)
    print('')
except FileNotFoundError:
    high_score = 0
    pass

# Create Item instances
health_potion = Item('Health potion','Restores some health points.',hero.heal) # Start with
health_potion_2 = Item('Health potion','Restores some health points.',hero.heal) # drops from goblin scout
health_potion_3 = Item('Health potion','Restores some health points.',hero.heal) # drops from goblin scout
health_potion_4 = Item('Health potion','Restores some health points.',hero.heal) # drops from goblin outcast
health_potion_5 = Item('Health potion','Restores some health points.',hero.heal) # found in forest
health_potion_6 = Item('Health potion','Restores some health points.',hero.heal) # found along path
health_potion_7 = Item('Health potion','Restores some health points.',hero.heal) # found in tall ridge
mega_health_potion = Item('Mega health potion','Restores many health points.',hero.mega_heal) # buy from hermit for 200 gold
mega_health_potion_2 = Item('Mega health potion','Restores many health points.',hero.mega_heal) # found in deep forest
mega_health_potion_3 = Item('Mega health potion','Restores many health points.',hero.mega_heal) # found in cave cavern
seedling = Item('Seedling','This item serves no purpose',hero.nothing) # found in forest grove
key = Item('Key','This is a key to something i dont know what','') # found in dungeon
crown = Item('Old Crown','This crown used to belong to a old king',hero.nothing) # found in old vault
locket = Item('Old Locket','This locket seems locked maybe a key will unlock it','') # buy from goblin adventurer

# Create Weapon instances
magic_sword = Weapon('Magic Sword','Increase damage by 15',15) # Drops from dragon
pitch_fork = Weapon('Pitch fork','Increase damage by 6',6) # found in village
sword = Weapon("Sword",'Increase damage by 4',4) # found in deeper forest
axe = Weapon('Axe','Increase damage by 2',2) # found on path in forest
village_guard_sword = Weapon('Guard sword','Increase damage by 10',10) # buy from villager for 300 gold
sharp_stick = Weapon('Sharp stick','Increases damage by 1',1) # found in forest
lords_sword = Weapon('Lords sword','Increase damage by 12',12) # found in keep
god_weapon = Weapon('Gods sword','Increase damage by 100',100) # if player uses god_mode func
rusted_sword = Weapon('Rusted sword','Increase damage by 3',3) # drops from bandit
goblin_scimatar = Weapon('Goblin scimatar','Increases damage by 13',13) # drops from goblin brute

# Create armour instances
traveler_armour = Armour('Travelers armour','Reduces damage taken by 2',2) #
village_armour = Armour('Village armour','Reduces damage by 4',4) #
troll_armour = Armour('Troll armour','Reduces damage by 6',6) #

# Create friendly NPC instances
villiger = FriendlyNPC('Villiger',5,"I have heard storys of the horrors out side the village",'','') # found in village
traveler = FriendlyNPC('Traveler',10,"I just got robbed on the trail i suggest you turn back now",traveler_armour,50) # found along path
hermit = FriendlyNPC('Hermit Samson',15,'Those village folk are always scared of what is out of their village',mega_health_potion,200) # found in hut along path
lord = FriendlyNPC('Lord Joss',20,'Have you heard of the goblins to the north, they send war partys to our lands','','') # found in keep
shepherd = FriendlyNPC('Humble Gabe',10,'I am but a humble shepherd, but i have heard rumors of the goblins to the north','','') # found in meadow
prisoner = FriendlyNPC('Prisoner',2,'','','') # found in cave entrance 2
prisoner_2 = FriendlyNPC('Prisoner',2,'','','') # found in deep cave
village_scout = FriendlyNPC('Zen the scout',10,'','','') # found on path in meadow
satyr = FriendlyNPC('Friendly satyr',10,'This grove has been guarded by my kind for centuries we dont bother our selves with the outside world','','') # found in forest grove
prison_guard = FriendlyNPC('Prison guard',10,'i am the guard of this here prison we have never had an excepee','','') # found in dungeon
goblin_adventurer = FriendlyNPC('Goblin Adventurer',10,'gih fuu feufeueu ueu gfeufg eug eu yeuhgewufiw whfyyw ygvu fhvw',locket,20) # found in old vault

# Create monster instances
wolf = Beast('Wolf',7*difficulty,5*difficulty,'',20) # found in forest
wolf_2 = Beast('Wolf',7*difficulty,5*difficulty,'',20) # found in deeper forest
goblin_outcast = Humanoid('Goblin Outcast',7*difficulty,4*difficulty,health_potion_4,20) # found in path in forest
bear = Beast('Bear Cub',9*difficulty,7*difficulty,'',30) # found along path
trapper = Humanoid('Trapper',10*difficulty,7*difficulty,'',40) # found in hut in forest
spider = Beast('Giant Spider',10*difficulty,7*difficulty,'',30) # found in deep forest
goblin_scout = Humanoid('Goblin Scout',13*difficulty,5*difficulty,health_potion_2,50) # found in meadow
bandit = Humanoid('Bandit',4*difficulty,7*difficulty,rusted_sword,100) # found on cross roads
thug = Humanoid('Thug',8*difficulty,7*difficulty,'',100) # found in village
goblin = Humanoid('Goblin', 15*difficulty,13*difficulty,'',50) # found along ridge
goblin_scout_2 = Humanoid('Goblin Scout',13*difficulty,5*difficulty,health_potion_3,50) # found on tall ridge
goblin_scout_3 = Humanoid('Goblin Scout',13*difficulty,5*difficulty,'',50) # found on path in meadow
goblin_runt = Humanoid('Goblin Runt',7*difficulty,3*difficulty,'',30) # found in cave entrance 2
goblin_brute = Humanoid('Goblin Brute',20*difficulty,9*difficulty,goblin_scimatar,100) # found in cave entrance 
troll = Humanoid('Troll',20*difficulty,9*difficulty,troll_armour,100) # found in cave cavern
excaped_prisoner = Humanoid('Excaped prisoner',3*difficulty,2*difficulty,'','') # found in dungeon

# Create Boss instance
dragon = Dragon('Timόtheos',45*difficulty,15*difficulty,'',400) # found in boss room
goblin_brute_2 = Humanoid('Goblin Brute',20*difficulty,9*difficulty,'',100)

# Create Rooms
forest_clearing = Room('Forest Clearing','you are in a forest clearing','','',sharp_stick)
forest = Room('Forest','you are in a forest',wolf,'',health_potion_5)
path_in_forest = Room('Path in Forest','you find a path in the forest',goblin_outcast,'',axe)
deeper_in_forest = Room('Deeper in Forest','you are deeper in the forest',wolf_2,'',sword)
along_forest = Room('Along Path','You are following a path',bear,traveler,health_potion_6)
deep_forest = Room('Deep Dark Forest','You are in a deep dark forest',spider,'',mega_health_potion_2)
hut_in_forest = Room('Hut in Forest','you are on a hut along the path',trapper,hermit,'')
meadow = Room('meadow','You are in a wide open meadow',goblin_scout,shepherd,'')
cross_road = Room('Cross Roads','You are at a cross roads their is a sign pointing west it says village of lord joss',bandit,'','')
village = Room('The village','You are in a village',thug,villiger,pitch_fork)
along_ridge = Room('Along the Ridge','You are along a ridge',goblin,'','')
tall_ridge = Room('Tall Ridge','You are at a tall ridge',goblin_scout_2,'',health_potion_7)
path_in_meadow = Room('Path Along Meadow','you are on a path in a meadow',goblin_scout_3,village_scout,'')
keep = Room('The Keep','you are in the keep of lord joss','',lord,lords_sword)
cave_entrance_2 = Room('Cave Entrance','You are in a cave entrance',goblin_runt,prisoner,'')
cave_entrance = Room('Cave Entrance','You are in a cave entrance',goblin_brute,'','')
deep_cave = Room('Deeper in cave','You are in a deep cave','',prisoner_2,'')
cave_cavern = Room('Cave Cavern','You are in a large open cavern',troll,'',mega_health_potion_3)
Boss_Room = Room('Open Cavern','',dragon,'','')

# bonus rooms
forest_grove = Room('Forest Grove','you are in a forest grove','',satyr,seedling)
dungeon = Room('Dungeon','you are in a dungeon',excaped_prisoner,prison_guard,key)
old_vault = Room('Old Vault','You are in an old vault','',crown,goblin_adventurer)

# Room connections dict
room_connections = {
    forest_clearing : {'north' : forest},
    forest : {'north' : deeper_in_forest, 'west' : path_in_forest, 'south' : forest_clearing},
    deeper_in_forest : {'north' : deep_forest, 'west' : along_forest, 'south' : forest, 'east' : forest_grove},
    path_in_forest : {'north': along_forest, 'east' : forest },
    along_forest : {'north' : hut_in_forest, 'east' : deeper_in_forest, 'south' : path_in_forest},
    deep_forest : {'north' : meadow, 'south' : deeper_in_forest},
    hut_in_forest : {'north' : cross_road, 'south' : along_forest},
    meadow : {'north' : tall_ridge, 'south' : deep_forest},
    cross_road : {'north' : path_in_meadow, 'west' : village, 'south' : hut_in_forest},
    village : {'north' : keep, 'east' : cross_road},
    along_ridge : {'north' : cave_entrance_2, 'west' : tall_ridge, 'south' : old_vault },
    tall_ridge : {'north' : cave_entrance, 'east' : along_ridge, 'west' : path_in_meadow, 'south' : meadow},
    path_in_meadow : {'east' : along_ridge, 'west' : keep, 'south' : cross_road},
    keep : {'east' : path_in_meadow, 'south' : village, 'north' : dungeon},
    cave_entrance_2 : {'north' : deep_cave, 'south' : along_ridge},
    cave_entrance : {'north' : cave_cavern, 'south' : tall_ridge},
    deep_cave : {'west' : cave_cavern, 'south' : cave_entrance_2},
    cave_cavern : {'east' : deep_cave, 'east' : Boss_Room, 'south' : cave_entrance},
    Boss_Room : {'east' : cave_cavern},
    forest_grove : {'west' : deeper_in_forest},
    dungeon : {'south' : keep},
    old_vault : {'north' : along_ridge}
}

boss = dragon
fight_stage = 1
monster = ''
hero.room = forest_clearing
hero.inventory.append(health_potion)
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
            hero.health += 10
            print('You leveled up!!')
            print('You are now level',hero.level)
            print('You health is now',hero.health)
            hero.exp -= exp_to_next_level
            exp_to_next_level += exp_to_next_level
            input('Press Enter to continue\n>>')
        elif hero.room == Boss_Room:
            if fight_stage == 1:
                option = input('are you sure you want to enter the boss room this will trigger the boss fight (yes/no)\n>>')
                if option == 'no':
                    print('you turn back')
                    hero.room = cave_cavern
                else:
                    print('you enter the room and see a towering figure')
                    hero.status = 'Boss fight'
                    hero.boss_fight(boss)
            else:

                hero.status = 'Boss fight'
                hero.boss_fight(boss)
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

# checks if the player has activated dev mode
if hero.dev == True:
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

else:
    # Ending options
    if hero.health > 0:
        print('You Win! Game Over')
        hero.score += 1000
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
    print('You were',hero.level)
    print('you had',hero.exp,'exp')
    print('Your score is',hero.score)

    if high_score < hero.score:
        file = open('highscore.txt','w')
        file.write(str(hero.score))
        file.close()
        print('you set a new high score')
        file = open('highscoreholder.txt','w')
        file.write(hero.name)
        file.close()

# roll credits 
credits()
