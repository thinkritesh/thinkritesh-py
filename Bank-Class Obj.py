class BankAccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_details(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Bank Balance: ₹", self.balance)

account1 = BankAccount("Sango", "1234567890", 5000)
account1.display_details()