from LivingThingSubclasses.PlayerClass import Player

# Create a Player class for the Player, inheriting from player
class Ranger(Player): # like D&D ranger
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
        self.unarmed_attack = 'flign'
        self.first_attack = 'shoot'
        self.second_attack = 'strike'