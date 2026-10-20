class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.__owner = owner          
        self.__balance = float(balance) 

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposite: {amount}. Current balance: {self.__balance}")
        else:
            print("Deposite ammount should be more than 0")

    def withdraw(self, amount):
        # BUG: Does not check for negative amounts!
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        self.__balance -= amount

    def getBalance(self):
        return self.__balance
