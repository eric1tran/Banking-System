import socket
import sys

print("BankServer")

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
    data = client.recv(1024).decode()
    if data.strip() == 'quit':
        print("Closing connection...")
        client.close()
        sys.exit(1)
    elif data:
        print("Data recieved from client: {}".format(data))
        client.sendall(data.encode())

