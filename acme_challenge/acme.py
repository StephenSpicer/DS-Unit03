# DS23 02/12/2021
from random import randint


class AcmeCorp:
    # defining the constructor function:
    def __init__(self):
        self.products = []
    # this should create products eventually

    def create_product(self, name, price=10, weight=20, flammability=0.5):
        prod = Product(name, price, weight, flammability)
        return prod

    def load_acme_prods(self, num_items=[]):
        list_of_products = []
        for item in num_items:
            list_of_products.append(self.create_product(item))
        self.products = list_of_products
        return list_of_products
    # checking both of those last methods

    def check_stealability(self):
        if self.products:
            for product in self.products:
                print(product.stealability())

    def check_explodability(self):
        if self.products:
            for product in self.products:
                print(product.explode())


class Product:
    # constructor with the defaults
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = randint(1000000, 9999999)
    #stealability
    def stealability(self):
        """ this method checks for stealability """
        theftness = (self.price / self.weight) 
        if (theftness >= 0.5 and theftness <= 1):
            return "Kinda stealable..."
        elif theftness < 0.5 :
            return "Not so stealable..."
        else :
            return "Very stealable!"

    #explode              
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


#ac = AcmeCorp()

# here we go with raw data to feed our new class
# num_items = [
#     ['A Cool Toy', 10, 20, 0.5],
#     ['calculator', 50, 0.5, 1],
#     ['beanbag', 65, 25, 2],
#     ['popsicle sticks', 1, 0.5, 1.2],
#     ['hammer', 30, 6, 0],
#     ['gold iphone', 900, 2, 2],
#     ['candy', 1, 0.1, 0],
#     ['fertilizer', 35, 45, 2.3],
#     ['expensive matches', 100, 0.1, 2.5]]

# ac.load_acme_prods(num_items)

# ac.check_explodability()
# ac.check_stealability()


#to check that our generate_products() function is working... 
# gen_list = generate_products()

# for object in gen_list:
#     print(object.name)
#     print(object.price)
#     print(object.weight)
#     print(object.flammability)
#     print(" ____ ")

# print(len(gen_list))

# to check that our inventory_report() function is working. 

# ir = inventory_report(gen_list)
# print(ir)