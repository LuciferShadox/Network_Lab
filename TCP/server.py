#  Python implementation

# 	Program    :  TCP Emulation (Server)
# 	Status     :  Stable
# 	Created by :  Sarath Peter

## Import packages here
import socket
## Write functions here

## Write code here
S_1 = socket.socket()
port = 10026

S_1.bind(('',port))
print("Socket online at ",port)

S_1.listen(10)
while True:
    Connect,Client = S_1.accept()
    print("Connection from ",Client)
    Connect.send(b'Thank you for using the service')
    Connect.close()
