"""BankAcount.py"""

from random import *

accounts = {}


class BankAccount:
    """
    A bank account class with the following properties:
    AccNumber:      A unique identifier for the bank account
    Name:           A string representing owner of bank account
    Balance:        Bank account balance
    Transactions:   List of transaction under the account
    """
    def __init__(self, name, initial_deposit, password):
        self.name = name
        self.accnum = randint(10000,99999)
        self.password = password
        self.balance = int(initial_deposit)
        self.transactions = {}

    def show_balance(self):
        print("Current Balance: ${:.2f}\n".format(self.balance))

    def deposit(self, amount):
        if amount < 1:
            print("Invalid deposit\n")
        else:
            print("Depositing ${:.2f}...".format(amount))
            self.balance += int(amount)
            self.show_balance()
            self.log_transaction('deposit', amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds\n")
        else:
            print("Withdrawing ${:.2f}...".format(amount))
            self.balance -= amount
            self.show_balance()
            self.log_transaction('withdrawal', amount)

    def log_transaction(self, transaction, amount):
        self.transactions[transaction] = amount
        self.show_transactions()

    def show_transactions(self):
        print("Transactions: {}\n".format(self.transactions))

    def validate_password(self, password):
        return True if password == self.password else print("Incorrect password") and False


def create_account(user_name, initial_deposit, password):
    """
    :param user_name: User name to create a Bank Account for
    :param initial_deposit: The initial amount user wants to deposit into account
    :return: None
    """
    bank_acc = BankAccount(user_name, initial_deposit, password)
    accounts[user_name] = bank_acc

    print("\nThank you! Here is your Bank info: ")
    print("Name: {}".format(bank_acc.name.title()))
    print("Acccount Number: {}".format(bank_acc.accnum))
    print("Balance: ${:.2f}\n\n".format(int(bank_acc.balance)))


def request_password():
    password = input("Enter a password for the account: ")
    confirm_password = input("Re-enter password: ")
    if password != confirm_password:
        print("Passwords did not match. Try again")
        request_password()

    return password


def validate_account(name):
    return True if name in accounts.keys() else False


def display_menu():
    return input("What would you like to do? \n"\
            "  Enter 'C' to create an account. \n"\
            "  Enter 'W' to withdraw money \n"\
            "  Enter 'D' to deposit money \n"\
            "  Enter 'B' to show your balance \n"\
            "  Enter 'T' to show your transactions \n"\
            "  Enter 'E' to exit. \n")


def main():
    print("Welcome to Bank of amERICa!")

    while True:
        user_input = display_menu()
        if user_input.lower() == 'c':
            print("Great, lets get some information from you...", end="")
            name = input("What is your full name? ")
            if validate_account(name):
                print("You already has an account with us! \n")
                continue

            initial = input("How much would you like for your initial deposit? ")
            password = request_password()

            create_account(name, initial, password)

        elif user_input.lower() in "wdbt":
            name = input("What is the name under the account? ")
            if validate_account(name):
                password = input("Enter your password: ")
                if accounts[name].validate_password(password):
                    if user_input.lower() == 'w':
                        withdraw_amount = int(input("How much would you like to withdraw? "))
                        accounts[name].withdraw(withdraw_amount)
                    elif user_input.lower() == 'd':
                        deposit_amount = int(input("How much would you like to deposit? "))
                        accounts[name].deposit(deposit_amount)
                    elif user_input.lower() == 'b':
                        accounts[name].show_balance()
                    elif user_input.lower() == 't':
                        accounts[name].show_transactions()
            else:
                print("Sorry, you do not have an account with us. Please create one! \n")

        elif user_input == 'e':
            break
        else:
            print("Invalid input. Please try again. \n")

if __name__ == "__main__":
    main()