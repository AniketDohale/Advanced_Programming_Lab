import socket
import threading
import pymongo
from datetime import datetime

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["chat_app_database"]
persons_collection = db["persons"]
chat_collection = db["chat_records"]

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 5555))
server_socket.listen(5)

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')

        if not data:
            break

        # Process the data (assuming a simple protocol for this example)
        if data.startswith("INSERT_PERSON"):
            _, name, age = data.split("|")
            insert_person(name, int(age))
            client_socket.send("Person inserted successfully.".encode('utf-8'))
        elif data.startswith("GET_PERSONS"):
            persons = get_persons()
            client_socket.send(str(persons).encode('utf-8'))
        elif data.startswith("INSERT_CHAT"):
            _, sender, receiver, message = data.split("|")
            insert_chat(sender, receiver, message)
            client_socket.send("Chat inserted successfully.".encode('utf-8'))
        elif data.startswith("GET_CHATS"):
            _, sender, receiver = data.split("|")
            chats = get_chats(sender, receiver)
            client_socket.send(str(chats).encode('utf-8'))
        else:
            client_socket.send("Invalid command.".encode('utf-8'))

    # Close the client socket when the communication ends
    client_socket.close()

def insert_person(name, age):
    person_data = {"name": name, "age": age}
    persons_collection.insert_one(person_data)

def get_persons():
    return list(persons_collection.find())

def insert_chat(sender, receiver, message):
    chat_data = {
        "sender": sender,
        "receiver": receiver,
        "message": message,
        "timestamp": datetime.now()
    }
    chat_collection.insert_one(chat_data)

def get_chats(sender, receiver):
    query = {"$or": [
        {"$and": [{"sender": sender}, {"receiver": receiver}]},
        {"$and": [{"sender": receiver}, {"receiver": sender}]}
    ]}
    return list(chat_collection.find(query).sort("timestamp"))

# Accept and handle incoming connections
while True:
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")
    
    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
