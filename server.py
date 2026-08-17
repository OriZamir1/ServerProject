import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 5000))

server_socket.listen(1)

print("listening")

client_socket, client_address = server_socket.accept()
print(f"connected to: {client_address}")

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"received {data.decode()}")

client_socket.close()
server_socket.close()
