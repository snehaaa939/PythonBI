class Account:
    def __init__(self, account_holder, account_number, amount=500):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__amount = amount

    def get_balance(self):
        return self.__amount

    def deposit(self, deposit_amount):
        if deposit_amount <= 10:
            raise ValueError("Deposit amount can't be less than 10.")
        self.__amount = self.__amount + deposit_amount

    # Implement method name withdraw that takes amount and deducts that from account balance
    # Validation: Withdraw amount can't be less than 100 and more than 1 lakh
    # Withdraw amount cannot be more than account balance

    def withdraw(self, withdraw_amount):
        if withdraw_amount < 100:
            raise ValueError("Withdraw amount must be at least 100")
        elif withdraw_amount > 100000:
            raise ValueError("Withdraw amount cannot exceed 1 lakh")
        elif withdraw_amount > self.__amount:
            raise ValueError("Insufficient balance")
        else:
            self.__amount = self.__amount - withdraw_amount
            print("Remaining balance:", self.__amount)

    # Create a method named transfer balance that takes argument as other account and transfer amount
    # Deduct given amount from first account using withdraw function
    # Deposit into other account using deposit function

    def transfer_balance(self, other_account, transfer_amount):
        self.other_account = other_account
        print(f"Transferring {transfer_amount}.....")

        self.withdraw(transfer_amount)
        other_account.deposit(transfer_amount)


acc_1 = Account("Ram", "12345")
acc_2 = Account("Shyam", "1234567", 10000)
acc_2.transfer_balance(acc_1, 3500)
print("Account1:", acc_1.get_balance())
print("Account2:", acc_2.get_balance())
print("Transfer successful")

# Name Mangling:- Technique to access private attributes of object from outside of class.
acc_1._Account__amount = 504
print("Account1:", acc_1.get_balance())
