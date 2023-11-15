import socket


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

file = open("Mettings", "r")

contents = file.readlines()
for line in contents:
   client.send(line.encode('utf-8'))
   msg = client.recv(4000).decode('utf-8')
   print(msg)
