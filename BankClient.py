import socket
import sys

#Create
try:
    s = socket.socket()
except socket.error as err:
    print("Socket creation failed with error {}...".format(err))

# Connect to server
try:
    s.connect(('127.0.0.1', 12345))
except socket.error as msg:
    print("Couldn't connect to server: {}", msg)
    sys.exit(1)

print("Connected to server...")

data_input = input(">> ")

# Send *encoded* data
while data_input.lower().strip() != 'quit':
    s.sendall(data_input.encode())
    data = s.recv(1024).decode()
    print("Data echoed from server: {}".format(data))
    data_input = input(" --> ")

s.close()