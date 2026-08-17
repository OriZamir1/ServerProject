import socket
import threading


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 5000))

server_socket.listen(1)

print("listening")

def send_message():
    while True:
        msg = input("server: ")
        if(msg.lower() == "quit"):
            break
        client_socket.send(msg.encode())

client_socket, client_address = server_socket.accept()
print(f"connected to: {client_address}")

receive_thread = threading.Thread(target=send_message)
receive_thread.daemon = True
receive_thread.start()


while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"received {data.decode()}")

client_socket.close()
server_socket.close()
