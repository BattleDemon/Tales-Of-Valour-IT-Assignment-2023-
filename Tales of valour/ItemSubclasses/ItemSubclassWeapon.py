from NonLivingThingClasses.ItemClass import Item

# Create a class for Weapons, inheriting from Item
class Weapon(Item):
    def __init__(self,name,description,modifier):
        # Initialize Weapons
        self.name = name
        self.description = description
        self.modifier = modifier