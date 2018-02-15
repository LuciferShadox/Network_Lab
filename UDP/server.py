#  Python implementation

# 	Program    :  UDP Emulation (Server)
# 	Status     :  Developing
# 	Created by :  Sarath Peter

## Import packages here
import socket
## Write functions here

## Write code here

IP = '127.0.0.1'
PORT = 10392

MESSAGE = b"You've have connected to Sarath Peter's Computer"

print("Address online : ",IP,':',PORT)

SOCK = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SOCK.sendto(MESSAGE, (IP,PORT))
