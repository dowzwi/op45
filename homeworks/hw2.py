class Asset:
    pass

class BankAccount(Asset):
    pass

class SavingAccount(BankAccount):
    pass

class CheckingAccount(BankAccount):
    pass

class RealEstate(Asset):
    pass

class InsurableItem(RealEstate):
    pass

class InterestBearingItem(Asset):
    pass

class Security(InterestBearingItem):
    pass

class Stock(Security):
    pass

class Bond(Security):
    pass