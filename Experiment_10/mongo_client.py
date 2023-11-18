import socket


def send_data(sock, data):
    sock.send(data.encode('utf-8'))
    response = sock.recv(1024).decode('utf-8')
    print(response)


# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5555))

while True:
    # Simple command-line interface for the client
    print("\nMenu:")
    print("1. Insert Person")
    print("2. Get Persons")
    print("3. Insert Chat")
    print("4. Get Chats")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        send_data(client_socket, f"INSERT_PERSON|{name}|{age}")
    elif choice == "2":
        send_data(client_socket, "GET_PERSONS")
    elif choice == "3":
        sender = input("Enter sender: ")
        receiver = input("Enter receiver: ")
        message = input("Enter message: ")
        send_data(client_socket, f"INSERT_CHAT|{sender}|{receiver}|{message}")
    elif choice == "4":
        sender = input("Enter sender: ")
        receiver = input("Enter receiver: ")
        send_data(client_socket, f"GET_CHATS|{sender}|{receiver}")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the client socket when done
client_socket.close()
