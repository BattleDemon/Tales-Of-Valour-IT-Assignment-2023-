from LivingThingSubclasses.LivingThingClass import LivingThing

# Create a class for monsters, also inheriting from LivingThing
class Monster(LivingThing):
    def __init__(self, name, health, maxdamage,drops,gold_drops):
        # Initialize monster attributes
        self.name = name
        self.health = health
        self.maxdamage = maxdamage
        self.drops = drops
        self.gold_drops = gold_drops