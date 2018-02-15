#  Python implementation

# 	Program    :  Chat (Client implementation)
# 	Status     :  Stable
# 	Created by :  Sarath Peter

## Import packages here
import socket
import select
import sys
## Write functions here

## Write code here

# Setting socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Error message for no arguements
if len(sys.argv) != 3:
    print("\nUsage : client.py [ip][port]")
    exit()

IP = str(sys.argv[1])   # IP Address of Chat Server
PORT = int(sys.argv[2]) # Port number of Chat Server
server.connect((IP,PORT)) # Connection attempt to Server
print("Connection to server established!!")
while True:

    # Setting Read/Write paths
    socket_list = [sys.stdin, server]
    read_socket,write_socket,error_socket = select.select(socket_list,[],[])

    # Reading Broadcast Messages
    for socks in read_socket:

        if socks == server:

            message = socks.recv(4096) # Recciving Messages
            print(message) # Printing Messages to screen

        else:

            # Writing Messages back
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write(" You -> ")
            sys.stdout.write(message)
            sys.stdout.flush()

#Closing Server
server.close()
