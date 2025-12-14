#EJECUTAR MI APLICACION

from bank_account import BankAccount

def main():

    account = BankAccount(initial_balance=0, interest_rate=0.05)

    account.deposit(1000)
    account.withdraw(500)
    account.calculate_interest()
    print("Balance Final (POO)", account.balance)

if __name__=="__main__";
    main()

