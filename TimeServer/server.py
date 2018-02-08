#  Python implementation

# 	Program    :  UDP Time Server (Server Implementation)
# 	Status     :  Developing
# 	Created by :  Sarath Peter

## Import packages here
import socket
from time import gmtime, strftime
## Write functions here

## Write code here
IP = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

while True:
    data, address = sock.recvfrom(4096)
    if data == "getTime":
        print("\n Connection to time server established from " + address[0] + ":" + str(address[1]))
        time = strftime("%d-%m-%Y %H:%M", gmtime())
        sock.sendto(time, address)
