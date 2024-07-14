class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def deposit(self, balance):
        self.balance += balance

    def __withdraw(self, balance):
        self.balance -= balance

    def __show_balance(self):
        print("Balance is ", self.balance)

    def if_you_are_auth(self, key):
        if key:
            print(self.__show_balance())
        else:
            print("Not allowed")

    def if_you_are_auth_user(self, key, balance):
        if key:
            self.__withdraw(balance=balance)
            self.__show_balance()
        else:
            print("Not allowed")


ambani = BankAccount()
ambani.deposit(100)

secret_pass = input("Enter secret pass")
if secret_pass == "1234":
    ambani.if_you_are_auth(True)
else:
    ambani.if_you_are_auth(False)

password = input("Enter password to withdraw amount")
amount = int(input("Enter amount to withdraw "))
if secret_pass == "1234":
    ambani.if_you_are_auth_user(True, balance=amount)
else:
    ambani.if_you_are_auth_user(False, balance=amount)