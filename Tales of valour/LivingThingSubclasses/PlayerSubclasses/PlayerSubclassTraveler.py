from LivingThingSubclasses.PlayerClass import Player

# Create Player class for the Player, inheriting from player
class Traveler(Player): # like D&D fighter
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
        self.unarmed_attack = 'punch'
        self.first_attack = 'slash'
        self.second_attack = 'stab'