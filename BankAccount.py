"""BankAcount.py"""

def CreateAccount():
    user_name = raw_input("What's your name? ")

user_input = raw_input("Hello, do you have a Bank Account with us? ")
if user_input.lower() == 'no':
    CreateAccount()
else:
    user_name = input("Great, whats your name? ")
