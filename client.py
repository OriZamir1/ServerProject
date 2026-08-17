import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1', 5000))

while True:
    msg = input("you: ")
    if msg.lower() == "quit":
        break
    client_socket.send(msg.encode())

client_socket.close()