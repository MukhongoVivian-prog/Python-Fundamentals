"""
create a class BankAccount with two parameters account_holder and balance
set initial values with the  init method


our class should have two methods
withdraw and deposit

withdraw method has two parameter self and amount
withdraw should subtract amount from balance

deposit has 2 parameters self and amount
deposit should add amount to balance

third method
this method should just print the available balance
call it show
def withdraw(self, amount):
self.balance = self.balance - amount
"""

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount):
        self.balance =self.balance - amount

    def deposit(self, amount):
        self.balance =self.balance + amount

    def show(self):
        print("The Account Holder: " + self.account_holder)
        print("Current Balance: "+ str(self.balance))

Account1 = BankAccount("Vivian", 10000)    
Account1.withdraw(5000)
Account1.deposit(2000)


Account1.show()

Account2 = BankAccount("Aisha", 200000)
Account2.withdraw(1000)
Account2.deposit(5000)

print("#########################")
Account2.show()
