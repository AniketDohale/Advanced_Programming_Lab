from socket import *
import sqlite3

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('chat_history.db')
cursor = conn.cursor()

# Create a table to store chat history if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        message TEXT
    )
''')
conn.commit()

# Server details
server_port = 5000

# Socket setup
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print("Welcome: The server is now ready to receive")

try:
    connection_socket, address = server_socket.accept()
    while True:
        # Receive client's message
        sentence = connection_socket.recv(2048).decode()

        # Save the chat history in the database
        cursor.execute(
            'INSERT INTO chat_history (sender, message) VALUES (?, ?)', ('Client', sentence))
        conn.commit()

        # Display client's message
        print('Client >> ', sentence)

        # Get server's response
        message = input("Server >> ")
        cursor.execute(
            'INSERT INTO chat_history (sender, message) VALUES (?, ?)', ('Server', message))

        # Send response to the client
        connection_socket.send(message.encode())

        # Check for exit condition
        if message.lower() == 'q':
            break

finally:
    # Close the database connection and the socket
    conn.close()
    server_socket.close()
