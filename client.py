#  Python implementation

# 	Program    :  File Server 2 Implementation
# 	Status     :  Developing
# 	Created by :  Sarath Peter

## Import packages here
import sys
import socket
## Write functions here

## Write code here

CHK = 0
rData = "NULL"

ClientObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = raw_input(" Enter IP Address : ")
PORT = raw_input(" Enter Port : ")
PORT = int(PORT)
##conect using ip and port
ClientObj.connect((IP,PORT))
ClientObj.recv(4096)
com = raw_input("\n FTP -> ")

while True:
    ClientObj.send(com)
    CHK = ClientObj.recv(4096)

    if CHK == 1:
        download_PTR = open(com,"wb")
        rData = ClientObj.recv(4096)
        while rData:
            download_PTR.write(rData)
            rData = ClientObj.recv(4096)
        print("--- Download Completed ---")
        break

    elif CHK == 2:
        ClientObj.send("list")

    else:
        ClientObj.recv(4096)

ClientObj.close()
print("--- Server Closed ---")
