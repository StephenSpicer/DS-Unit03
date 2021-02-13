#!/usr/bin/env python
import pytest
from acme import Product
from acme_report import generate_products

#@pytest.fixture
# decorator concepts - pin DONT FORGET
def func(x):
    """ THIS IS A TEST TEST TO TEST PYTEST """
    return x + 1


def test_answer():
    assert func(4) == 5

def test_default_product_price():
    """Test default product price being 10."""   
    prod = Product('test product')
    assert prod.price == 10

def test_default_product_weight():
    """" Test default product weight being 20"""
    prod = Product('Test Product')
    assert prod.weight == 20

def test_stealability():
    """" Test new product having stealability"""
    prod = Product('Test Product', 1000, 2, 1.5)
    assert prod.stealability() == "Very stealable! Probably already stolen..."
    # this should be high stealability
    prod = Product('Test Product', 3, 5, 1.5)
    assert prod.stealability() == "Kinda stealable..."
    #that was medium...
    prod = Product('Test Product', 3, 25, 1.5)
    assert prod.stealability() == "Not so stealable..."

def test_explode():
    """" Test new product exploder potential"""
    prod = Product('Test Product', 10, 50, 2.5)
    #Gonna start with the big exploder
    assert prod.explode() == '...BABOOM!!'

def test_default_num_products():
    #fun fact, this test detected a bug!!!
    """
    tests the default number of products, should be thirty
    make sure however generate products is going that 
    THAT SPECIFIC OUTPUT len is being checked. 
    """
    prods = generate_products()
    assert len(prods) == 30

# man, oh, man, those tests. that was really something. 