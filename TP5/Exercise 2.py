class BankAccount:
    """Create a class named BankAccount."""

    """ Define a class attribute bank_name = "ITC Bank"."""
    bank_name = "ITC Bank"


    def __init__(self, owner, account_number, balance):
        
        """ Define a constructor with owner, account_number, and balance."""
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):

        """Create a method named deposit(amount)."""
        if amount > 0:

            print("\nDepoit :", amount)
            self.balance += amount

        else:
            print("Invalid number ")

    def withdraw(self,amount):

        """Create a method named withdraw(amount)."""
        if amount <=0:
            print("Invalid number ")
        elif self.balance<amount:

            print("withdrawal amount must be positivel")
        else:
            print("\nWithdraw:", amount)
            self.balance -= amount
        

    def display_balance(self):

        """ Create a method named display_balance()"""
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Account Owner: {self.owner}")
        print(f"Initial Balance: ${self.balance}")


""" Create two bank account objects"""
""" Test deposit and withdrawal operations"""
account1 = BankAccount("Me", 1 ,1000)

print("Account 1")

account1.display_balance()
account1.deposit(500)
print("Invitial Balance:", account1.balance)

account1.withdraw(200)
print("Wihtdraw Balance:", account1.balance)

print("\nFinal Balacne :", account1.balance)

print("\n=====================================")
account2 = BankAccount("you", 2 ,2000)
print("\nAccount 2")

account2.display_balance()
account2.deposit(500)
print("Invitial Balance:", account2.balance)

account2.withdraw(200)
print("Wihtdraw Balance:", account2.balance)

print("\nFinal Balacne :", account2.balance)



    
        

