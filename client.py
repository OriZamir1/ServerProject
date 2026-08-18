import socket
import threading


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1', 5000))

user_name = input("enter username: ")

def receive_message():
    while True:
        data = client_socket.recv(1024)
        if not data:
            print("closed connection")
            break
        print()
        print(data.decode())

receive_thread = threading.Thread(target=receive_message)
receive_thread.daemon = True
receive_thread.start()


while True:
    msg = input("you: ")
    if msg.lower() == "quit":
        break
    full_message = f"{user_name}:  {msg}"
    client_socket.send(full_message.encode())

client_socket.close()
