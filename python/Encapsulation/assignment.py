# Create a class BankAccount that has:
# 	attributes: owner, __balance (private attribute with default value 0).
# 	methods: deposit, withdraw, get_balance, transfer.
# 		deposit to add amount to balance if it's is +ve.
# 		withdraw to subtract amount from balance if it's +ve and less than balance.
# 		get_balance to display current balance.
# 		transfer to transfer amount from one account to another.
# Create two bank accounts account_1 with owner Rabindra and account_2 with owner John.
# 	Deposit 1000 to account_1 and 500 to account_2.
# 	Withdraw 200 from account_1 and 100 from account_2.
# 	Transfer 200 from account_1 to account_2.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    # deposit to add amount to balance if it's is +ve.
    def deposit(self, deposit_amount):
        if deposit_amount < 0:
            raise ValueError("Deposit amount can't be negative.")
        self.__balance = self.__balance + deposit_amount

    # withdraw to subtract amount from balance if it's +ve and less than balance.
    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if withdraw_amount < 0:
            raise ValueError("Withdraw amount must be positive.")
        elif withdraw_amount > self.__balance:
            raise ValueError("Insufficient balance.")
        else:
            self.__balance = self.__balance - withdraw_amount

    # get_balance to display current balance.
    def get_balance(self):
        return self.__balance
        
    # transfer to transfer amount from one account to another.
    def transfer(self, other_account, transfer_amount):
        self.withdraw(transfer_amount)
        other_account.deposit(transfer_amount)

# Create two bank accounts account_1 with owner Rabindra and account_2 with owner John.

account_1 = BankAccount("Rabindra", 50000)
account_2 = BankAccount("John", 500)

# 	Deposit 1000 to account_1 and 500 to account_2.
print("After deposit:")
account_1.deposit(1000)
account_2.deposit(500)
print("Account1:", account_1.get_balance())
print("Account2:", account_2.get_balance())
# 	Withdraw 200 from account_1 and 100 from account_2.
print("\n")
print("After Withdraw:")
account_1.withdraw(200)
account_2.withdraw(100)
print("Account1:", account_1.get_balance())
print("Account2:", account_2.get_balance())
# 	Transfer 200 from account_1 to account_2.
print("\n")
print("After Transfer:")
account_1.transfer(account_2, 200)
print("Account1:", account_1.get_balance())
print("Account2:", account_2.get_balance())