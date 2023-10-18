from NonLivingThingClasses.ItemClass import Item

# Create a class for armour, inheriting from item
class Armour(Item):
    def __init__(self,name,description,modifier):
        # initialize Armour
        self.name = name
        self.description = description
        self.modifier = modifier