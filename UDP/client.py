#  Python implementation

# 	Program    :  UDP Emulation (Client)
# 	Status     :  Developing
# 	Created by :  Sarath Peter

## Import packages here
import socket
## Write functions here

## Write code here
SOCK = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Socket Established \n")
IP = "10.1.3.6"
PORT = 11115

SOCK.bind((IP,PORT))
while True:
    content,client = SOCK.recvfrom(4096)
    print(content.decode())
