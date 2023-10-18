from NonLivingThingClasses.ItemClass import Item

# Create a class for consumable items, inheriting from item
class Consumables(Item):
    def __init__(self,name,description,attributes):
        # Initialize Consumables
        self.name = name 
        self.description = description
        self.attributes = attributes