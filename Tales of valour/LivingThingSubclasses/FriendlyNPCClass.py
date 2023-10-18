from LivingThingSubclasses.LivingThingClass import LivingThing

# Create a class for friendly NPC's, also inheriting from LivingThing
class FriendlyNPC(LivingThing):
    def __init__(self,name,health,lines,items,item_cost):
        # Initialize friendly NPC attributes
        self.name = name
        self.health = health
        self.lines = lines
        self.items = items
        self.item_cost = item_cost
