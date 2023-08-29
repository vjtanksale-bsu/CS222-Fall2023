class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} dollars. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount} dollars. Current balance: {self.balance}"
        else:
            return "Insufficient funds."

    def get_balance(self):
        return self.balance


# Create an instance of the BankAccount class
my_account = BankAccount("12345", 1000)

# Perform actions using methods
print("Initial balance:", my_account.get_balance())

print(my_account.deposit(500))
print(my_account.withdraw(200))
print(my_account.withdraw(1500))  # Attempt to withdraw more than balance

print("Final balance:", my_account.get_balance())
