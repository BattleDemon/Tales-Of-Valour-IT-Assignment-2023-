from LivingThingSubclasses.MonsterClass import Monster

# Create a class for dragons (currently only used by the boss), inheriting from monster
class Dragon(Monster):
    def __init__(self, name, health, maxdamage, drops, gold_drops):
        # Initialize Dragon monsters attributes
        self.name = name
        self.health = health
        self.maxdamage = maxdamage
        self.drops = drops
        self.gold_drops = gold_drops
        self.actions = ['flamebreath','fire-slash']