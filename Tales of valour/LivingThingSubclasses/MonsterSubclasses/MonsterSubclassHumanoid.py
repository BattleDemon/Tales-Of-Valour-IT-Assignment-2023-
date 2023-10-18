from LivingThingSubclasses.MonsterClass import Monster

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