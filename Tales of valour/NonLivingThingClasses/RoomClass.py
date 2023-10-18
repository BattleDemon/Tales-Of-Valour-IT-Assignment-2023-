# Create a class for Rooms
class Room():
    def __init__(self,name ,description, monsters, npcs, items):
        # Initialize Rooms
        self.name = name
        self.description = description
        self.monsters = monsters
        self.npcs = npcs
        self.items = items