from decimal import Decimal

class Account:
    def __init__(self, name: str):
        self.name = name
        self.balance = Decimal('0')
