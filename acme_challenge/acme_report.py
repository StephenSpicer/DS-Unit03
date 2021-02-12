# module to generate random products and print a report on them.
# !/usr/bin/env python
from random import randint, sample, uniform
from product import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Basket']

# should generate a given number of products (default
def generate_products(num_products=30):
    gen_products = []
    for product in range(num_products):
        gen_products.append(Product(ADJECTIVES[randint(0,4)])) 
    return gen_products

# takes a list of products, and prints a "nice" summary
def inventory_report(products):
    pass  # TODO - your code! Loop over the products to calculate the report.
# - Number of unique product names in the product list
# - Average (mean) price, weight, and flammability of listed products









# if __name__ == '__main__':
#     inventory_report(generate_products())