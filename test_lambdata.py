"""
Basic Unit Tests for lambdata package.

"""

from pydataset import data
import lambdata as ld
from lambdata import OOP_examples

user1 = ld.OOP_examples.SocialMediaUser(name= 'nick', location = 'arizona')
user2 = ld.OOP_examples.SocialMediaUser(name= 'carl', location = 'costa rica', upvotes = 250)

def inc(x):
    return x + 1

def test_inc():
    ans = inc(3)
    assert ans == 4

def test_increment_int():
    """Making sure increment works for integers"""
    x0 = 0
    y0 = ld.increment(x0) # should be 1, allegedly
    assert y0 == 1

    x1 = 100
    y1 = ld.increment(x1) #101
    assert y1 == 101

def test_increment_float():
    """Making sure increment works for floats"""
    x0 = 10.5
    y0 = ld.increment(x0) # should be 11.5
    assert y0 == 11.5

def test_increment_neg_int():
    """Making sure increment works for negative integers"""
    x0 = -1
    y0 = ld.increment(x0) # 0 
    assert y0 == 0 

def test_increment_neg_float():
    """Making sure increment works for negative floats"""
    x0 = -1.5 
    y0 = ld.increment(x0) # -0.5
    assert y0 == -0.5


def test_colors():
    assert 'cyan' in ld.COLORS
    assert 'mauve' in ld.COLORS
    assert 'brown' not in ld.COLORS
    assert 'ANY OTHER COLOR' not in ld.COLORS

def test_number_colors():
    """ Testing number of elements in colors"""
    assert len(ld.COLORS) == 4
    assert not len(ld.COLORS) > 4

# Testing OOP_Examples

def test_SMU_name():
    """ testing that SMU constructor works properly"""
    # testing name
    assert user1.name.lower() == 'nick'
    assert user2.name.lower() == 'carl'
    #testing location
    assert user1.location.lower() == 'arizona'
    assert user2.location.lower() == 'costa rica'
    assert user1.upvotes == 0 #checking default upvote value at 0
    assert user2.upvotes == 250

def test_popular():
    """testing that 0 upvotes is unpopular"""
    assert not user1.is_popular()


def test_unpopular():
    """testing to make sure 250 upvotes is popular"""
    assert user2.is_popular()
    assert isinstance(user1.is_popular(), bool)


def test_SMU_constructor_types():
    """ Testing types"""
    assert isinstance(user1.name, str)
    assert isinstance(user1.location, str)
    assert isinstance(user1.upvotes, int)
