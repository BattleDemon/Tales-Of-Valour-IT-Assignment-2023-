from LivingThingSubclasses.MonsterClass import Monster

# Create a class for beast monsters, inheriting from Monster
class Beast(Monster):
    def __init__(self, name, health, maxdamage, drops, gold_drops):
        # Initialize Beast monsters attributes
        self.name = name
        self.health = health
        self.maxdamage = maxdamage
        self.drops = drops
        self.gold_drops = gold_drops
        self.actions = ['slash','maul']