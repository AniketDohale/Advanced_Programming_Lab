# Server Side Script

from socket import *
server_port = 5000
server_socket = socket(AF_INET, SOCK_STREAM)
# binds address (hostname, port number pair)
server_socket.bind(('', server_port))
server_socket.listen(1)  # sets up and start TCP listener
print("Welcome: The server is now ready to receive")
connection_socket, address = server_socket.accept()
while True:
    sentence = connection_socket.recv(2048).decode()
    print('Client >> ', sentence)
    message = input("Server >> ")
    connection_socket.send(message.encode())
    if (message == 'q'):
        connection_Socket.close()
