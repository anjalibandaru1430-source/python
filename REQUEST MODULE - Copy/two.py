class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient funds")
    def show_balance(self):
        print("balance:",self.__balance)

acc=BankAccount(1000)

acc.deposit(500)
acc.withdraw(300)
acc.show_balance()
