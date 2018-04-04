import socket
import sys
import BankServer

def display_menu():
    print ("What would you like to do? \n"\
            "  Enter 'C' to create an account. \n"\
            "  Enter 'W' to withdraw money \n"\
            "  Enter 'D' to deposit money \n"\
            "  Enter 'B' to show your balance \n"\
            "  Enter 'T' to show your transactions \n"\
            "  Enter 'E' to exit. \n")
#Create
try:
    s = socket.socket()
except socket.error as err:
    print("Socket creation failed with error {}...".format(err))

# Connect to Bank server
try:
    s.connect(('127.0.0.1', 12345))
except socket.error as msg:
    print("Couldn't connect to amERICa Bank server: {}", msg)
    sys.exit(1)

print("Connected to server...\n\n")

print("Welcome to Bank of amERICa!...\n")

# Send *encoded* data
while True:
    display_menu()
    user_input = input(">> ")

    # TODO: Arg parse?
    if user_input.lower() == 'c':
        print("Great, lets get some information from you...", end="")
        name = input("What is your full name? ")
        if BankServer.validate_account(name):
            print("You already has an account with us! \n")
            continue

        initial = input("How much would you like for your initial deposit? ")
        password = BankServer.request_password()

        BankServer.create_account(name, initial, password)

    elif user_input.lower() in "wdbt":
        name = input("What is the name under the account? ")
        if BankServer.validate_account(name):
            password = input("Enter your password: ")
            if BankServer.validate_password(name, password):
                if user_input.lower() == 'w':
                    withdraw_amount = int(input("How much would you like to withdraw? "))
                    BankServer.withdraw(name, withdraw_amount)
                elif user_input.lower() == 'd':
                    deposit_amount = int(input("How much would you like to deposit? "))
                    BankServer.deposit(name, deposit_amount)
                elif user_input.lower() == 'b':
                    BankServer.show_balance(name)
                elif user_input.lower() == 't':
                    BankServer.show_transactions(name)
        else:
            print("Sorry, you do not have an account with us. Please create one! \n")

    elif user_input.lower() == 'e':
        break
    else:
        print("Invalid input. Please try again. \n")

    #s.send(user_input.encode())
    #data_received = s.recv(1024).decode()
    #print("Data echoed from server: {}".format(data_received))

s.close()