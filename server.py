import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 5000))

server_socket.listen(5)

print("listening")

clients = []




def handle_client(client_socket, client_address):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        for client in clients:
            if client != client_socket:
                client.send(data) #we do not encode/decode because we treat the data like a black box we just get data and forward it
    client_socket.close()
    clients.remove(client_socket)
    print(f"disconnected: {client_address}")

#stage 3 left over - single client only, not compatible with multiple clients
# def send_message():
#     while True:
#         msg = input("server: ")
#         if(msg.lower() == "quit"):
#             break
#         client_socket.send(msg.encode())

while True:
    client_socket, client_address = server_socket.accept()
    print(f"connected to: {client_address}")
    clients.append(client_socket)
    receive_thread = threading.Thread(target=handle_client , args=(client_socket, client_address))
    receive_thread.daemon = True
    receive_thread.start()

