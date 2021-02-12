
from random import randint

class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """ this method checks for stealability """
        theftness = (self.price / self.weight) 
        if (theftness >= 0.5 and theftness <= 1):
            return "Kinda stealable..."
        elif theftness < 0.5 :
            return "Not so stealable..."
        else :
            return "Very stealable! Probably already stolen..."
              
    def explode(self):
        """ this method checks for explodability """
        boomness = (self.flammability * self.weight) 
        if boomness < 10:
            return "...fizzle"
        elif (boomness >= 10 and boomness < 50):
            return "...boom"
        else :
            return "...BABOOM!!"     


# subclass of Product - 'Boxing Glove"
class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)
    # second explode method:
    def explode(self):
        """ this method used to check for explodability """
        return "...it's a glove."

    def punch(self):
        """ this method is for punches """
        if self.weight < 5:
            return "That tickles."
        elif (self.weight >=5 and self.weight < 15):
            return "Hey that hurt!" 
        else: 
            return "OUCH!"     