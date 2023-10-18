from random import randint
from LivingThingSubclasses.LivingThingClass import LivingThing

#

# Create a class for the player, inheriting from LivingThing
class Player(LivingThing):
    def __init__(self, name,):
        # Initialize player-specific attributes
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
        self.unarmed_attack = ''
        self.first_attack = ''
        self.second_attack = ''

    def punch(self,monster):
        # allows player classes with the unarmed attack punch to use punch, deals 0-3 dmg or +1 if wilder
        dmg = randint(0,3)
        if isinstance(hero, Wilder):
            dmg += 1
        print('you punch the',monster.name,'for',dmg,'damage')
        monster.health -= dmg
        if monster.health < 0:
            monster.health = 0
        print(monster.name,'now has',monster.health,'health')

    def slash(self,monster):
        # allows the traveler to use the slash attack, deals 1-9 dmg
        print(self.name,"slash's at the",monster.name)
        dmg = randint(1,9) + self.equipped_weapon.modifier
        print(self.name,'did',dmg,'damage')
        monster.health -= dmg
        if monster.health < 0:
            monster.health = 0
        print(monster.name,'health is now',monster.health)

    def stab(self,monster):
        # allows player classes with the stab attack, deals 4-6 dmg
        print(self.name,"stab's at the",monster.name)
        dmg = randint(4,6) + self.equipped_weapon.modifier
        print(self.name,'did',dmg,'damage')
        monster.health -= dmg
        if monster.health < 0:
            monster.health = 0
        print(monster.name,'health is now',monster.health)

    def smash(self,monster):
        # allows the wilder to use the smash attack, deals 5-6 dmg
        print(self.name,'smashes into the',monster.name)
        dmg = randint(5,6) + self.equipped_weapon.modifier
        print(self.name,'did',dmg,'damage')
        monster.health -= dmg
        if monster.health < 0:
            monster.health = 0
        print(monster.name,'health is now',monster.health)
    
    def strike(self,monster):
        # allows player classes with the strike attack to use strike, deals 2-5 dmg
        print(self.name,'strikes the',monster.name)
        dmg = randint(2,5) + self.equipped_weapon.modifier
        print(self.name,'did',dmg,'damage')
        monster.health -= dmg
        if monster.health < 0:
            monster.health = 0
        print(monster.name,'health is now',monster.health)

    def fling(self,monster):
        # allows player classes with the unarmed attack fling to use fling, 0-4 dmg chance not to hit
        option = randint(1,3)
        if option == 1:
            print(self.name,'missed the',monster.name)
            print('dealing no damage')

        else:
            print(self.name,'hits the',monster.name)
            dmg = randint(0,4)
            print(self.name,'did',dmg,'damage')
            monster.health -= dmg
            if monster.health < 0:
                monster.health = 0
            print(monster.name,'health is now',monster.health)

    def shoot(self,monster):
        # allows the ranger to use the shoot attack, deals 3-8 dmg
        option = randint(1,10)
        if option == 1:
            print(self.name,'missed the',monster.name)
            print('dealing no damage')

        else:
            print(self.name,'hits the',monster.name)
            dmg = randint(3,8) + self.equipped_weapon.modifier
            print(self.name,'did',dmg,'damage')
            monster.health -= dmg
            if monster.health < 0:
                monster.health = 0
            print(monster.name,'health is now',monster.health)

    def blast(self,monster):
        # allows the shaman to use the blast attack, deals 3-8 dmg
        option = randint(1,10)
        if option == 1:
            print(self.name,'missed the',monster.name)
            print('dealing no damage')

        else:
            print(self.name,'hits the',monster.name)
            dmg = randint(3,8) + self.equipped_weapon.modifier
            print(self.name,'did',dmg,'damage')
            monster.health -= dmg
            if monster.health < 0:
                monster.health = 0
            print(monster.name,'health is now',monster.health)

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
                input('Press Enter to continue\n>> ')
                monster = self.room.monsters
                self.fight(monster) # starts combat

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
                input('Press Enter to continue\n>> ')

            else:
                print("You couldn't find anything")

    def use(self, monster):
        # Allows the player to use item such as health potions
        item_name = input('What item do you want to use?\n>> ')
        item_name = item_name.capitalize()
        for item in self.inventory:
            # checks if the item is in the players inventory 
            if item.name == item_name:
                if isinstance(item, Consumables):
                    # cheaks if the item is a Consumable item
                    if item_name == 'Key':
                        # checks if the item is a key
                        if locket in self.inventory:
                            print('you notice the key matches the lock on the locket')
                            print('you turn the key')
                            print('after you hear the click of the lock the locket disapears')
                            print('you gain 500 xp')
                            self.inventory.remove(locket)
                            self.exp += 500
                            self.score += 500
                            return
                        
                    elif item_name == 'Locket':
                        # checks if the item is a locket
                        if key in self.inventory:
                            print('you notice the lock on the locket matches the shape of the key ')
                            print('you turn the key')
                            print('after you hear the click of the lock the locket disapears')
                            print('you gain 500 xp')
                            self.inventory.remove(locket)
                            self.exp += 500
                            self.score += 500
                            return
                        
                    else:
                        item.attributes()  # Call the item's attributes method
                        self.inventory.remove(item)  # Remove the used item from inventory
                        self.rest_cooldown = self.rest_cooldown - 1
                        self.score += 10
                        self.exp += 10
                    return
                
                else:
                    print('This item is not consumable')
            else:
                print('That is not in your inventory or not an item')

    def fight(self, monster):
        # Engage in combat with a monster
        self.rest_cooldown = self.rest_cooldown - 1
        while self.health > 0 and monster.health > 0:
            # First deals Dmg to the monster then to the hero 
            non_comabat_action = False
            if self.equipped_weapon != '':
                # checks if the player has a weapon
                attack = input(f'What action do you want to do?({self.unarmed_attack}, {self.first_attack}, {self.second_attack},use,inv,stats)\n>> ')
                attack = attack.lower()

                if attack == 'use':
                    # Allows the player to use items during combat
                    self.use(monster)
                    non_comabat_action = True

                elif attack == 'inv':
                    # Allows the player to view their inventory during combat
                    self.show_inventory(monster)
                    non_comabat_action = True

                elif attack == 'stats':
                    # Allows the player to view their stats in combat
                    self.stats(monster)
                    non_comabat_action = True

                elif attack == 'punch':
                    # Allows the player to use the punch action if they are a Traveler or a Wilder
                    if isinstance(hero,Traveler):
                        self.punch(monster)
                    elif isinstance(hero,Wilder):
                        self.punch(monster)
                    else:
                        print("Your class can't use that attack")
                        non_comabat_action = True

                elif attack == 'fling':
                    # Allows the player to use the fling action if they are a Ranger or Wilder
                    if isinstance(hero,Ranger):
                        self.fling(monster)
                    elif isinstance(hero,Shaman):
                        self.fling(monster)
                    else:
                        print("Your class can't use that attack")
                        non_comabat_action = True

                elif attack == 'slash':
                    # Allows the player to use the slash action if they are a Traveler
                    if isinstance(hero,Traveler):
                        self.slash(monster)
                    else:
                        print("Your class can't use that attack")
                        non_comabat_action = True

                elif attack == 'stab':
                    # Allows the player to use the stab action if they are a Traveler or a Shaman
                    if isinstance(hero,Traveler):
                        self.stab(monster)
                    elif isinstance(hero,Shaman):
                        self.stab(monster)
                    else:
                        print("Your class can't use that attack")
                        non_comabat_action = True

                elif attack == 'smash':
                    # Allows the player to use the smash action if they are a Wilder
                    if isinstance(hero,Wilder):
                        self.smash(monster)
                    else:
                        print("Your class can't use that attack")
                        non_comabat_action = True

                elif attack == 'strike':
                    # Allows the player to use the strike action if they are a Wilder or a Ranger
                    if isinstance(hero,Wilder):
                        self.strike(monster)
                    elif isinstance(hero,Ranger):
                        self.strike(monster)
                    else:
                        print("Your class can't use that attack")
                        non_comabat_action = True

                elif attack == 'shoot':
                    # Allows the player to use the shoot action if they are a Ranger
                    if isinstance(hero,Ranger):
                        self.shoot(monster)
                    else:
                        print("Your class can't use that attack")
                        non_comabat_action = True
                
                elif attack == 'blast':
                    # Allows the player to use the blast action if they are a Shaman
                    if isinstance(hero,Shaman):
                        self.blast(monster)
                    else:
                        print("Your class can't use that attack")
                        non_comabat_action = True

                else:
                    print('Please input a real attack')
                    non_comabat_action = True

            else:
                attack = input(f'What action do you want to do?({self.unarmed_attack},use,inv,stats)\n>> ')
                attack = attack.lower()

                if attack == 'use':
                    # Allows the player to use items during combat
                    self.use(monster)
                    non_comabat_action = True

                elif attack == 'inv':
                    # Allows the player to view their inventory during combat
                    self.show_inventory(monster)
                    non_comabat_action = True

                elif attack == 'stats':
                        # Allows the player to view their stats in combat
                        self.stats(monster)
                        non_comabat_action = True

                elif attack == 'punch':
                    # Allows the player to use the punch action if they are a Traveler or a Wilder
                    if isinstance(hero,Traveler):
                        self.punch(monster)
                    elif isinstance(hero,Wilder):
                        self.punch(monster)
                    else:
                        print("Your class can't use that attack")
                        non_comabat_action = True

                elif attack == 'fling':
                    # Allows the player to use the fling action if they are a Ranger or Wilder
                    if isinstance(hero,Ranger):
                        self.fling(monster)
                    elif isinstance(hero,Shaman):
                        self.fling(monster)
                    else:
                        print("Your class can't use that attack")
                        non_comabat_action = True

                else:
                    print('Please input a real attack')
                    non_comabat_action = True

            if monster.health > 0:
                # Monster attack
                if non_comabat_action == True:
                    # checks if the player used: use, inv or didn't input an option
                    pass

                else:
                    mindamage = round(monster.maxdamage/3)
                    dmg = randint(mindamage,monster.maxdamage)
                    if self.equipped_armour != '':
                        dmg -= self.equipped_armour.modifier
                    print('The',monster.name,choice(monster.actions),'you for',dmg,'damage')
                    self.health -= dmg
                    if self.health < 0:
                            self.health = 0
                    print('Your health is now',self.health)
              
        if self.health > 0:
            # checks if the player survived
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
            # if the player died
            print('You were Killed by the', monster.name)
            self.status = 'regular'

    def boss_fight(self,monster):
        # Triggered when entered the boss room
        global fight_stage

        if fight_stage == 1:
            # displays dialog then the player has to fight a monster
            print(boss.name,': Petty mortal')
            print('you have entered my realm ')
            print('Yet you still are not worthy to challenge me')
            print('you need to prove that you are worth my time')
            print(self.name,'you see a gate open behind you and a goblin brute enters')
            monster = goblin_brute_2
            self.fight(monster)
            fight_stage += 1

        elif fight_stage == 2:
            # displays dialog
            print(boss.name,': hmmn')
            print('well done mortal')
            print('NOW YOU CHALLENGE ME')
            print('YOU CANT TURN BACK NOW')
            print('LETS SEE HOW LONG YOU CAN LIVE')
            input('Press Enter to continue\n>> ')
            fight_stage += 1

        elif fight_stage == 3:
            # Triggers a fight with the boss
            first_round = True
            while self.health > 0 and monster.health > 0:
                # the boss attacks first
                non_comabat_action = False
                if first_round == True:
                    first_round = False

                else:
                    if self.equipped_weapon != '':
                        # cheaks if the player has a weapon equiped
                        attack = input(f'What action do you want to do?({self.first_attack},{self.second_attack},use,inv,stats)\n>> ')
                        attack = attack.lower()

                        if attack == 'use':
                            # Allows the player to use items in combat 
                            self.use(boss)
                            non_comabat_action = True

                        elif attack == 'inv':
                            # Allows the player to view their inventory during combat
                            self.show_inventory(boss)
                            non_comabat_action = True

                        elif attack == 'stats':
                            # Allows the player to view their stats in combat
                            self.stats(boss)
                            non_comabat_action = True

                        elif attack == 'punch':
                            # Allows the player to use the punch action if they are a Traveler or a Wilder
                            if isinstance(hero,Traveler):
                                self.punch(boss)
                            elif isinstance(hero,Wilder):
                                self.punch(boss)
                            else:
                                print("Your class can't use that attack")
                                non_comabat_action = True

                        elif attack == 'fling':
                            # Allows the player to use the fling action if they are a Ranger or Wilder
                            if isinstance(hero,Ranger):
                                self.fling(boss)
                            elif isinstance(hero,Shaman):
                                self.fling(boss)
                            else:
                                print("Your class can't use that attack")
                                non_comabat_action = True

                        elif attack == 'slash':
                            # Allows the player to use the slash action if they are a Traveler
                            if isinstance(hero,Traveler):
                                self.slash(boss)
                            else:
                                print("Your class can't use that attack")
                                non_comabat_action = True

                        elif attack == 'stab':
                            # Allows the player to use the stab action if they are a Traveler or a Shaman
                            if isinstance(hero,Traveler):
                                self.stab(boss)
                            elif isinstance(hero,Shaman):
                                self.stab(boss)
                            else:
                                print("Your class can't use that attack")
                                non_comabat_action = True

                        elif attack == 'smash':
                            # Allows the player to use the smash action if they are a Wilder
                            if isinstance(hero,Wilder):
                                self.smash(boss)
                            else:
                                print("Your class can't use that attack")
                                non_comabat_action = True

                        elif attack == 'strike':
                            # Allows the player to use the strike action if they are a Wilder or a Ranger
                            if isinstance(hero,Wilder):
                                self.strike(boss)
                            elif isinstance(hero,Ranger):
                                self.strike(boss)
                            else:
                                print("Your class can't use that attack")
                                non_comabat_action = True

                        elif attack == 'shoot':
                            # Allows the player to use the shoot action if they are a Ranger
                            if isinstance(hero,Ranger):
                                self.shoot(boss)
                            else:
                                print("Your class can't use that attack")
                                non_comabat_action = True
                        
                        elif attack == 'blast':
                            # Allows the player to use the blast action if they are a Shaman
                            if isinstance(hero,Shaman):
                                self.blast(boss)
                            else:
                                print("Your class can't use that attack")
                                non_comabat_action = True

                        else:
                            print('Please input a real attack')
                            non_comabat_action = True

                    else:
                        # Player input
                        attack = input(f'What action do you want to do?({self.unarmed_attack},use,inv,stats)\n>> ')
                        attack = attack.lower()

                        if attack == 'punch':
                            # Allows the player to use the punch action if they are a Traveler or a Wilder
                            if isinstance(hero,Traveler):
                                self.punch(boss)
                            elif isinstance(hero,Wilder):
                                self.punch(boss)
                            else:
                                print("Your class can't use that attack")
                                non_comabat_action = True

                        elif attack == 'fling':
                            # Allows the player to use the fling action if they are a Ranger or Wilder
                            if isinstance(hero,Ranger):
                                self.fling(boss)
                            elif isinstance(hero,Shaman):
                                self.fling(boss)
                            else:
                                print("Your class can't use that attack")
                                non_comabat_action = True

                        elif attack == 'use':
                            # Allows the player to use items in combat 
                            self.use(boss)
                            non_comabat_action = True

                        elif attack == 'inv':
                            # Allows the player to view their inventory during combat
                            self.show_inventory(boss)
                            non_comabat_action = True

                        elif attack == 'stats':
                            # Allows the player to view their stats in combat
                            self.stats(boss)
                            non_comabat_action = True

                        else:
                            print('Please input a real attack')
                            non_comabat_action = True

                if boss.health >= 0:
                    # cheaks if the boss is alive
                    if non_comabat_action == True:
                        # checks if the player used: use, inv or didn't input an option
                        pass

                    else:
                        mindamage = round(boss.maxdamage/3)
                        dmg = randint(mindamage,boss.maxdamage)
                        if self.equipped_armour != '':
                            dmg -= self.equipped_armour.modifier
                        print('The',boss.name,choice(boss.actions),'you for',dmg,'damage')
                        self.health -= dmg
                        if self.health < 0:
                            self.health = 0
                        print('Your health is now',self.health)

            if self.health > 0:
                # checks if you are still alive
                print('Victory!\nYou defeated the', boss.name)
                self.room.monsters = ''
                input('Press Enter to continue\n>> ')
            else:
                # if you died
                print('You were Killed by', boss.name)

    def friendlyencounter(self,monster):
        # Allows the player to encounter friendlyNPC's
        print('Your options are \n>Leave (leave the Npc you encountered')
        print('Buy (allows you to buy items from npc)')
        option = input('Talk (allows the npc to say a line)\n>> ')
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
                    option_2 = input('Do you want to buy this item? (yes/no)\n>> ')
                    if option_2 == 'yes':
                        if self.gold >= self.room.npcs.item_cost:
                            # cheaks if the player has enough gold
                            print('You bought',self.room.npcs.items.name,'for',self.room.npcs.item_cost)
                            self.pick_up_item(self.room.npcs.items)
                            self.gold -= self.room.npcs.item_cost
                            return
                        
                        else:
                            # if the player doesn't have enough gold
                            print("you don't have enough gold to buy", self.room.npcs.items.name)

                    else:
                        return
                    
                else:
                    print("this Npc doesn't have an item to sell")
                    input('Press Enter to continue\n>> ')
                    return
                
            elif option == 'Talk':
                # allows the npc to say a line
                print(self.room.npcs.lines)
                input('Press Enter to continue\n>> ')
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
                if isinstance(item, Weapon):
                    # cheaks if the item is a weapon
                    self.score += 25
                    self.exp += 25

                    if self.equipped_weapon == '':
                        # cheaks if the player all ready has a weapon equiped 
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
                    # cheaks if the item is armour
                    self.score += 25
                    self.exp += 25

                    if self.equipped_armour == '':
                        # cheaks if the player all ready has armour equiped 
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
        global directions
        # Allows the player to move between rooms 
        try:
            self.show_exits(monster)
            print(directions)
            direction = input("Which direction do you want to go? \n>> ")
            if self.room.monsters != '':
                # checks if their is still a monster in a room and if their is has a 1/2 chance of encountering it
                num = randint(1,2)
                if num == 1:
                    print('You have been confronted by',self.room.monsters.name)
                    input('Press Enter to continue\n>> ')
                    self.status = 'Confronted'
                    monster = self.room.monsters
                    self.fight(monster) # start combat

            # checks if the direction that was inputed is an avaliable direction
            if direction in room_connections[self.room]:
                self.room = room_connections[self.room][direction]
                print(f'You went {direction}')
                print(f'you are now in the {self.room.name}')
                self.rest_cooldown = self.rest_cooldown - 1
                self.tire() # chance of dealing 2 dmg
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
        # Shows the exits to a room
        global directions
        directions = 'You can go: '
        for key in room_connections[self.room]:
            directions += key
            directions += ', '

    def dev_mode(self,monster):
        # allows the player to activate dev mode making them overpowered 
        self.health = 1000
        self.equipped_weapon = god_weapon
        self.equipped_armour = god_armour
        self.exp += 100000000
        self.gold += 100000
        Commands.popitem() # makes it so the player can't use this command again
        self.dev = True
