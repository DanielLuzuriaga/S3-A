#EJEMPLO POO
#CLASES Y METODOS
#MODULARIDAD

class BankAccount:
    def __init__(self, initial_balance=0, interest_rate=0.05):
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Fondos insuficientes")

    def calculate_interest(self):
        self.balance += self.balance * self.interest_rate
