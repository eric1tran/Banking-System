"""BankAcount.py"""

from random import *

accounts = {}

class BankAccount:
    """
    A bank account class with the following properties:
    AccNumber:  A unique identifier for the bank account
    Name:       A string representing owner of bank account
    Balance:    Bank account balance
    """
    def __init__(self, name, initial_deposit):
        self.name = name
        self.accnum = randint(10000,99999)
        self.balance = int(initial_deposit)

    def print_balance(self):
        print ("Current Balance: ${:.2f}\n\n".format(self.balance))

    def deposit(self, amount):
        print ("Depositing ${:.2f}...".format(amount))
        self.balance += int(amount)
        self.print_balance()

    def withdraw(self, amount):
        print ("Withdrawing ${:.2f}...".format(amount))
        if amount > self.balance:
            print ("Insufficient funds\n")
        else:
            self.balance -= amount
            self.print_balance()


def CreateAccount(user_name, initial_deposit):
    """
    :param user_name: User name to create a Bank Account for
    :param initial_deposit: The initial amount user wants to deposit into account
    :return: None
    """
    bank_acc = BankAccount(user_name, initial_deposit)
    accounts[user_name] = bank_acc

    print ("\nThank you! Here is your Bank info: ")
    print ("Name: {}".format(bank_acc.name.title()))
    print ("Acccount Number: {}".format(bank_acc.accnum))
    print ("Balance: ${:.2f}\n\n".format(int(bank_acc.balance)))

def account_valid(name):
    return True if name in accounts.keys() else False

def user_menu():
    return input("What would you like to do? \n"\
            "  Enter '1' to create an account. \n"\
            "  Enter '2' to withdraw money \n"\
            "  Enter '3' to deposit money \n"\
            "  Enter '4' to check your balance \n"\
            "  Enter '5' to exit. \n")

print ("Welcome to Bank of amERICa!")

while True:
    user_input = user_menu()
    if user_input.lower() == '1':
        print ("Great, lets get some information from you...", end="")
        name = input("What is your full name? ")
        if account_valid(name):
            print("You already has an account with us! \n")
            continue

        initial = input("How much would you like for your initial deposit? ")
        CreateAccount(name, initial)

    elif user_input in "234":
        name = input("What is the name under the account? ")
        if account_valid(name):
            if user_input.lower() == '2':
                withdraw_amount = int(input("How much would you like to withdraw? "))
                accounts[name].withdraw(withdraw_amount)
            elif user_input.lower() == '3':
                deposit_amount = int(input("How much would you like to deposit? "))
                accounts[name].deposit(deposit_amount)
            elif user_input.lower() == '4':
                accounts[name].print_balance()
        else:
            print ("Sorry, you do not have an account with us. Please create one! \n")
    elif user_input == '5':
        break
    else:
        print ("Invalid input. Please try again. \n")