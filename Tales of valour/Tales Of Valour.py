# Imports randint and choice from random so they can be used in the code
from random import randint, choice
from LivingThingSubclasses.PlayerClass import Player
from LivingThingSubclasses.PlayerSubclasses.PlayerSubclassTraveler import Traveler
from LivingThingSubclasses.PlayerSubclasses.PlayerSubclassWilder import Wilder
from LivingThingSubclasses.PlayerSubclasses.PlayerSubclassRanger import Ranger
from LivingThingSubclasses.PlayerSubclasses.PlayerSubclassShaman import Shaman
from LivingThingSubclasses.MonsterSubclasses.MonsterSubclassHumanoid import Humanoid
from LivingThingSubclasses.MonsterSubclasses.MonsterSubclassBeast import Beast
from LivingThingSubclasses.MonsterSubclasses.MonsterSubclassDragon import Dragon
from LivingThingSubclasses.FriendlyNPCClass import FriendlyNPC
from NonLivingThingClasses.ItemClass import Item
from ItemSubclasses.ItemSubclassConsumables import Consumables
from ItemSubclasses.ItemSubclassWeapon import Weapon
from ItemSubclasses.ItemSubclassArmour import Armour
from NonLivingThingClasses.RoomClass import Room

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
        # allows the player to select a difficulty
        difficulty = input("Please select a difficulty:\nEasy (1),\nNormal (2),\nHard (3)\n>> ")
        if difficulty in Difficulty.keys():
            difficulty = Difficulty[difficulty]

        else:
            # if the player inputed something other than a difficulty
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
input('Press Enter to continue\n>> ')

# Get the player's class and name
print('Welcome hero')
while True:
    option = input('are you a traveler\na wilder\na ranger\nor a shaman\n>>')
    option = option.lower()
    if option == 'traveler':
        print('You are a Traveler from a far off land')
        print('You came to this land to find valour or die')
        
        name = input("What is your name?\n>> ")
        if len(name) > 15:
            # limits the number of characters the players name can have
            print ("Please keep the name below 15 characters!")
        hero = Traveler(name)
        break

    elif option == 'wilder':
        print('You have been wondering this lard for awhile')
        print('as a wild man you are out seeking valour')
        
        name = input("What is your name?\n>> ")
        if len(name) > 15:
            # limits the number of characters the players name can have
            print ("Please keep the name below 15 characters!")

        hero = Wilder(name)
        break

    elif option == 'ranger':
        print('You are a ranger from a far off land')
        print('you have come to this land to find valour or die')
        
        name = input("What is your name?\n>> ")
        if len(name) > 15:
            # limits the number of characters the players name can have
            print ("Please keep the name below 15 characters!")

        hero = Ranger(name)
        break

    elif option == 'shaman':
        print('you are a shaman from a far off land ')
        print('you have come to this land to find valour or die')
        
        name = input("What is your name?\n>> ")
        if len(name) > 15:
            # limits the number of characters the players name can have
            print ("Please keep the name below 15 characters!")

        hero = Shaman(name)
        break

    else:
        print('please make sure you spelt that right')

# Get difficulty
get_difficulty()

# attemps to get a high score and high score holder
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
    print('the current high score holder is',high_score_holder,'with a score of',high_score)
    print('')

except FileNotFoundError:
    # Allows the player to pick if they want to use my score or start from 0
    want_dev_score = input('Do you want to go up against Dexters high score of 6050:(y/n)\n>> ')
    if want_dev_score == 'y':
        # Sets the high score and high score holder to 'Dexter' and 6050 respectively 
        high_score_holder = 'Dexter'
        high_score = 6050
        print('the current high score holder is',high_score_holder,'with a score of',high_score)
        pass

    else:
        # If one doesn't exist it sets high score to 0
        print('currently there is no high score')
        high_score = 0
        pass

# Create Item instances
health_potion = Consumables('Health potion','Restores some health points.',hero.heal) # Start with
health_potion_2 = Consumables('Health potion','Restores some health points.',hero.heal) # drops from goblin scout
health_potion_3 = Consumables('Health potion','Restores some health points.',hero.heal) # drops from goblin scout
health_potion_4 = Consumables('Health potion','Restores some health points.',hero.heal) # drops from goblin outcast
health_potion_5 = Consumables('Health potion','Restores some health points.',hero.heal) # found in forest
health_potion_6 = Consumables('Health potion','Restores some health points.',hero.heal) # found along path
health_potion_7 = Consumables('Health potion','Restores some health points.',hero.heal) # found in tall ridge
mega_health_potion = Consumables('Mega health potion','Restores many health points.',hero.mega_heal) # buy from hermit for 200 gold
mega_health_potion_2 = Consumables('Mega health potion','Restores many health points.',hero.mega_heal) # found in deep forest
mega_health_potion_3 = Consumables('Mega health potion','Restores many health points.',hero.mega_heal) # found in cave cavern
seedling = Item('Seedling','This item is a seedling from the grove') # found in forest grove
key = Consumables('Key','This is a key to something i dont know what','') # found in dungeon
crown = Item('Old Crown','This crown used to belong to a old king') # found in old vault
locket = Consumables('Locket','This locket seems locked maybe a key will unlock it','') # buy from goblin adventurer

# Create Weapon instances
sharp_stick = Weapon('Sharp stick','Increases damage by 1',1) # found in forest
axe = Weapon('Axe','Increase damage by 2',2) # found on path in forest
sword = Weapon("Sword",'Increase damage by 4',4) # found in deeper forest
pitch_fork = Weapon('Pitch fork','Increase damage by 6',6) # found in the village
village_guard_sword = Weapon('Guard sword','Increase damage by 10',10) # buy from a villager for 300 gold
lords_sword = Weapon('Lords sword','Increase damage by 12',12) # found in keep
god_weapon = Weapon('Gods sword','Increase damage by 100',100) # if player uses god_mode func
rusted_sword = Weapon('Rusted sword','Increase damage by 3',3) # drops from bandit
goblin_scimatar = Weapon('Goblin scimatar','Increases damage by 13',13) # drops from goblin brute

# Create armour instances
traveler_armour = Armour('Travelers armour','Reduces damage taken by 2',2) # buy from traveler for 5
village_armour = Armour('Village armour','Reduces damage by 4',6) # buy from villager for 150 gold
troll_armour = Armour('Troll armour','Reduces damage by 6',8) # drops from troll
god_armour = Armour('Gods Armour','Reduces damage taken by 100',100) # if player uses god_mode func

# Create friendly NPC instances
villiger = FriendlyNPC('Villiger',5,"I have heard storys of the horrors out side the village",village_armour,150) # found in village
traveler = FriendlyNPC('Traveler',10,"I just got robbed on the trail i suggest you turn back now",traveler_armour,50) # found along path
hermit = FriendlyNPC('Hermit Samson',15,'Those village folk are always scared of what is out of their village',mega_health_potion,200) # found in hut along path
lord = FriendlyNPC('Lord Joss',20,'Have you heard of the goblins to the north, they send war partys to our lands','','') # found in keep
shepherd = FriendlyNPC('Humble Gabe',10,'I am but a humble shepherd, but i have heard rumors of the goblins to the north','','') # found in meadow
prisoner = FriendlyNPC('Prisoner',2,'','','') # found in cave entrance 2
prisoner_2 = FriendlyNPC('Prisoner',2,'','','') # found in deep cave
village_scout = FriendlyNPC('Zen the scout',10,'','','') # found on path in meadow
satyr = FriendlyNPC('Friendly satyr',10,"My kind has guarded this grove for centuries we don't bother ourselves with the outside world",'','') # found in forest grove
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
excaped_prisoner = Humanoid('Excaped prisoner',3*difficulty,2*difficulty,'',0) # found in dungeon

# Create monsters needed for Boss Battle
dragon = Dragon('Timόtheos',45*difficulty,17*difficulty,'',400) # found in boss room
goblin_brute_2 = Humanoid('Goblin Brute',20*difficulty,9*difficulty,'',100) # summoned during the boss fight

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
hero.inventory.append(health_potion) # Player starts with a health potion

# Main game loop function
def Main_loop():
    # Start Storys
    print('(type help to get a list of actions) \n')
    print(hero.name, 'Your story begins' ,hero.room.description)
    exp_to_next_level = 100

    # Game loop
    while hero.health > 0 and boss.health > 0:
        print('')
        if hero.status == 'Encountered':
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
            input('Press Enter to continue\n>> ')

        elif hero.room == Boss_Room:
            if fight_stage == 1:
                option = input('are you sure you want to enter the boss room this will trigger the boss fight (yes/no)\n>> ')
                # Allows the player to back out of the boss fight 
                if option == 'no':
                    # exits boss room
                    print('you turn back')
                    hero.room = cave_cavern

                else:
                    # starts boss fight
                    print('you enter the room and see a towering figure')
                    hero.status = 'Boss fight'
                    hero.boss_fight(boss)

            else:
                # continues boss fight
                hero.status = 'Boss fight'
                hero.boss_fight(boss)

        else:
            # User inputs
            line = input('What do you want to do \n>> ')
            if hero.rest_cooldown < 0:
                hero.rest_cooldown = 0
            if line in Commands.keys():
                Commands[line](hero, monster)
            else:
                print(hero.name, 'does not understand this suggestion.')

# Run main loop
if __name__ == '__main__':
    Main_loop()

# checks if the player has activated dev mode
if hero.dev == True:
    # Ending options
    if hero.health > 0:
        print('You Win! Game Over')

    else:
        print('Game Over. you lost :(')
    input('Press Enter to continue\n>> ')

    # shows the player their inventory 
    if hero.inventory:
        print('You had:')
        for item in hero.inventory:
            print(f'{item.name}: {item.description}')

    else:
        print('Your inventory was empty.')

    # Shows the player their important stats
    input('Press Enter to continue\n>> ')
    print('You were level',hero.level)
    print('you had',hero.exp,'exp')

else:
    # Ending options
    if hero.health > 0:
        print('You Win! Game Over')
        hero.score += 1000

    else:
        print('Game Over. you lost :(')
    input('Press Enter to continue\n>> ')

    # shows the player their inventory 
    if hero.inventory:
        print('You had:')
        for item in hero.inventory:
            print(f'{item.name}: {item.description}')

    else:
        print('Your inventory was empty.')

    # increses the Players score by their difficulty
    hero.score *= round(difficulty)

    # Shows the player their important stats
    input('Press Enter to continue\n>> ')
    print('You were',hero.level)
    print('you had',hero.exp,'exp')
    print('Your score is',hero.score)

    # Sets a new high score
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
