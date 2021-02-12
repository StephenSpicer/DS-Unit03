!/usr/bin/env python

import pytest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

def test_default_product_price(self):
    """Test default product price being 10."""
    prod = Product('Test Product')
    assert prod.price == 10