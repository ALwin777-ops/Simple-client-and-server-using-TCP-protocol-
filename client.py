import socket

print("Type 'bye' to close the connection:\n")

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 1234

# Connect to the server on local computer
s.connect(('127.0.0.1', port))

# Start communication loop
while True:
    message = input("Client: ")
    s.send(message.encode())
    if message.lower() == 'bye':
        print("You ended the connection.")
        break

    reply = s.recv(1024).decode()
    print("Server: ", reply)
    if reply.lower() == 'bye':
        print("Server ended the chat.")
        break

# Close the connection gracefully (outside the loop)
s.close()
