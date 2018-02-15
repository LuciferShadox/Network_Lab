#  Python implementation

# 	Program    : TCP Emulation
# 	Status     :  Stable
# 	Created by :  Sarath Peter

## Import packages here
import socket
## Write functions here

## Write code here
S_2 = socket.socket()
port = 12345
S_2.connect(('10.1.3.6',port))
msg = S_2.recv(4096)
msg = msg.decode('ASCII')
S_2.send(b'Thank You Server')
print(msg)
S_2.close()
