import socket

s = socket.socket()
host = "127.0.0.1"
port = 1560
s. bind((host,port))
s.listen(1)
print("Waiting for Connections...")
conn, addr = s.accept()
print(addr, "Has Connected to the server")

filename = input(str("name ?"))
file = open(filename,"rb")
file_data = file.read(1024)
conn.send(file_data)
print("Sented Success")
