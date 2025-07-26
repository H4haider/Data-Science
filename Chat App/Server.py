import socket


server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(1)
print("Server is Listening on Port 12345")


conn, addr = server_socket.accept()
print("Server is connected by ", addr)

data=server_socket.recv(1024).decode()
print("From Client: ", data)

server_socket.send("Hello Client".encode())
server_socket.close()
