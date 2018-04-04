import socket
import sys
from BankAccount import BankAccount

accounts = {}


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


def validate_password(name, password):
    return accounts[name].validate_password(password)


def withdraw(name, amount):
    accounts[name].withdraw(amount)


def deposit(name, amount):
    accounts[name].deposit(amount)


def show_balance(name):
    accounts[name].show_balance()


def show_transactions(name):
    accounts[name].show_transactions()


def main():
    #Create
    try:
        s = socket.socket()
        print("Socket successfully created...")
    except socket.error as err:
        print("Socket creation failed with error {}...".format(err))


    # Reuse and Bind
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 12345))

    # Listen
    s.listen(5)
    print("Socket is listening for incoming clients...")

    # Accept connections (blocking)
    client, address = s.accept()
    print("Connection accepted with {}\n".format(address))

    # Echo data recieved from clients until 'quit' received
    while True:
        user_input = client.recv(1024).decode()
        if not user_input:
            print("Closing connection...")
            client.close()
            sys.exit(1)
        else:
            print("Data recieved from client: {}".format(user_input))
            #client.sendall(str(data).upper().encode())

if __name__ == "__main__":
    main()