
import pytest 
from pydataset import data

from lambdata.Wallet import wallet

@pytest.fixture
# decorator concepts - pin DONT FORGET
def empty_wallet():
    """ returns a wallet instance with a zero balance"""
    return wallet()

@pytest.fixture
def Wallet01():
    """returns balance of 20"""
    return wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount():
    Wallet = wallet(100)
    assert Wallet.balance == 100

def test_wallet_add_cash():
    Wallet = wallet(20)
    Wallet.add_cash(100)
    assert Wallet.balance == 120

def test_wallet_spend_cash():
    Wallet = wallet(20)
    Wallet.spend_cash(10)
    assert Wallet.balance == 10