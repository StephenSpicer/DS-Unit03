# Wallet class, unit03 module 4

class wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            print('not enough money, man')
        else:
            self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount