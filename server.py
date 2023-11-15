import socket
import datetime as dt
from datetime import timedelta

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen(5)
print("Server Starting...........")

file = open("timezones", 'r')


while True:
        communication_socket, address = server.accept()
        print("Connected")

        contents = file.readlines()   #
        for line in contents:
                msg = communication_socket.recv(1024).decode('utf-8')
                print(msg)
                msg_list = msg.split(',')
                datetime = msg_list[0] + "" + msg_list[2]

                time = dt.datetime.strptime(datetime, '%y/%m/%d %H:%M:%S')


                cityTimeZone = line.split(',')
                if int(cityTimeZone[1]) < 0:
                                SouthAfricanTime = time - dt.timedelta(hours=(float(int(cityTimeZone[1]) * -1)))
                elif int(cityTimeZone[1]) > 0:
                        SouthAfricanTime = time + dt.timedelta(hours=int(cityTimeZone[1]))
                else:
                        SouthAfricanTime = time
                communication_socket.send(f"{SouthAfricanTime.date()} , {msg_list[1]} , {SouthAfricanTime.time()} , {msg_list[3]} ,{msg_list[4]}".encode('utf-8'))
