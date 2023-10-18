# Imports randint and choice from random so they can be used in the code
from random import randint, choice

hero = ''

# Create a base class representing a living thing
class LivingThing():
    def __init__(self):
        # Initialize LivingThing attributes
        self.name = 'some name'
        self.health = 1
        
    def tire(self):
        # has a 1/3 chance to deal 2 dmg to the livingthing
        diceroll = randint(0,2)
        if diceroll == 0:
            self.health = self.health - 2
            print('You have gotten tired, your health suffered')
            if self.health < 0:
                self.health = 0
            print('Your health is', hero.health)
        else:
            pass

    def heal(self):
        # adds up to 10 health to the livingthing
        heal_amount = randint(0,5) + 5
        self.health += heal_amount
        print('You gained',heal_amount,'health')
        print('Your health is now',self.health)

    def mega_heal(self):
        # adds 20 health to the livingthing
        self.health = self.health + 20
        print('You gained 20 health')
        print('Your health is now',self.health)