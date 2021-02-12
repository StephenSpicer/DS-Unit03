# module to generate random products and print a report on them.
# !/usr/bin/env python

from random import randint, sample, uniform
from product import Product

ADJECTIVES = [
    'Awesome',
    'Diminished',
    'Outrageous',
    'Shiny',
    'Impressive',
    'Portable',
    'Improved',
    'Dishonorable',
    'Churlish',
    'Eager',
    'Abundant']
NOUNS = [
    'Anvil',
    'Catapult',
    'Disguise',
    'Mousetrap',
    'Basket',
    'Faucet',
    'Collar',
    'Ream',
    'Spade',
    'Tractor',
    'Radiator']

# should generate a given number of products (default
def generate_products(num_products=30):
    gen_products = []
    for product in range(num_products):
        gen_products.append(Product(ADJECTIVES[randint(0,10)]
        + " " + NOUNS[randint(0,10)], randint(5, 100), randint(5, 100), uniform(0.0, 2.5)))
    return gen_products


#our list will change every time but that won't matter. 

# takes a list of products, and prints a "nice" summary
# This took awhile, a few different tweaks and what i understand to be a list comprehension.
# brought back the float format from nicholas lecture - that took way too long

def inventory_report(products):
    """

    """
    print('Unique Product Names: ', len(list(set(product.name for product in products))))
    print('Average Price: {:.1f}'.format(round (sum(product.price for product in products) / len(products), 1)))
    print('Average weight: ', sum( [product.weight for product in products]) / len(products))
    print('Average flammability: ', sum([product.flammability for product in products]) / len(products))
    print(" ____ ")
        

# - Number of unique product names in the product list
# - Average (mean) price, weight, and flammability of listed products









# if __name__ == '__main__':
#     inventory_report(generate_products())