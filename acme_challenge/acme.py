
# DS23 02/12/2021


from numpy.core.fromnumeric import prod
from product import Product 
from acme_report import generate_products

class AcmeCorp:
    # defining the constructor function:
    def __init__(self):
        self.products = []
        
    # this should create products eventually
    def create_product(self, name, price=10, weight=20, flammability=0.5):
        prod = Product(name, price, weight, flammability)
        return prod

    # this for loop should populate the acme store i think    
    def load_acme_prods(self, num_items = []):
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

ac = AcmeCorp()

# here we go with raw data to feed our new class
num_items = [
    ['A Cool Toy', 10, 20, 0.5],
    ['calculator', 50, 0.5, 1],
    ['beanbag', 65, 25, 35],
    ['popsicle sticks', 1, 0.5, 6],
    ['hammer', 30, 6, 0],
    ['gold iphone', 900, 2, 15],
    ['candy', 1, 0.1, 0],
    ['fertilizer', 35, 45, 650],
    ['expensive matches', 100, 0.1, 100]]

ac.load_acme_prods(num_items)

ac.check_explodability()
ac.check_stealability()
gen_list = generate_products()
print(gen_list)
