import socket

print("Type 'bye' to close the connection:\n")

# Create a socket object
s = socket.socket()
print("The Socket Created Successfully")

# Reserve a port for your service
port = 1234

# Bind the socket to the port
s.bind(('', port))
print(f'Socket Binded To the Port {port}')

# Put the socket into listening mode
s.listen(5)
print("Socket is listening...")

# Accept a connection
c, addr = s.accept()
print("Got connection from", addr)

# Communication loop
while True:
    data = c.recv(1024).decode()
    if data.lower() == 'bye':
        print("Client has ended the connection.")
        break
    print("Client: ", data)
    
    reply = input("Server: ")
    c.send(reply.encode())
    if reply.lower() == 'bye':
        print("Server has ended the connection.")
        break

# Close the connection gracefully
c.close()
s.close()
