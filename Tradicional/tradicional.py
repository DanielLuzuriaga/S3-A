#EJEMPLO DE PROGRAMACION TRADICIONAL
#SOLO ARCHIVO
#VARIABLES GLOBALES

balance = 0
interest_rate = 0.05 #%5

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Fondos insuficientes")

def calculate_interest():
    global balance, interest_rate
    balance += balance * interest_rate

def main():
    deposit(1000)
    withdraw(500)
    calculate_interest()
    print("Balance Final (Tradicional)", balance)

if __name__== "__main__":
    main()      