# !/usr/bin/env python

import pytest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

def test_default_product_price(self):
    """Test default product price being 10."""
    prod = Product('test product')
    assert prod.price == 10

# def test_default_product_weight(self):
#     """" Test default product weight being 20"""
#     prod = Product('Test Product')
#     assert prod.price == 20

# def test_stealability(self):
#     """" Test new product having stealability"""
#     prod = Product('Test Product', 500, 2, 0)
#     assert prod.stealability >= 1
#     assert prod.stealability == "Very stealable! Probably already stolen..."

# def test_explode(self):
#     """" Test default product weight being 20"""
#     prod = Product('Test Product', 10, 50, 500000)
#     assert prod.explode >= 1