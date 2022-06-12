import socket
s = socket.socket()
host = "127.0.0.1"
port = 1560
s.connect((host,port))
print("Connected Successfully")

filename = input(str("Enter ?"))
file = open(filename,"wb")
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("Success ...")
d = input()