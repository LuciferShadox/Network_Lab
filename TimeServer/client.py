#  Python implementation

# 	Program    :  UDP Time Server (Client Implementation)
# 	Status     :  Developing
# 	Created by :  Sarath Peter

## Import packages here
import socket
## Write functions here

## Write code here
IP = "127.0.0.1"
PORT = 5005
MSG = "getTime"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MSG, (IP,PORT))

data, address = sock.recvfrom(4096)
print("\n\n")
print("Hello there, today is :" + data[:10] + " and " + data[11:])
print("\n\n")
