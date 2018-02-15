#  Python implementation

# 	Program    :  Chat (Server implementation)
# 	Status     :  Stable
# 	Created by :  Sarath Peter

## Import packages here

import socket
import select
import sys
from thread import *

## Write functions here

list_clients = [] # List of clients

def client_thread(conn, addr):
    # Greeting message
    conn.send("Welcome to FriendZone")
    while True:
        try:
            # getting message
            message = conn.recv(4096)
            if message:
                print(addr[0]+" -> "+message)
                msg_send = addr[0]+" -> "+message
                broadcast(msg_send, conn)
            else:
                remove(conn)
        except:
            continue

def broadcast(message, connection):
    for clients in list_clients:
        if clients != connection:
            try:
                # Sending message to clients
                clients.send(message)
            except:
                clients.close()
                remove(clients)

def remove(connection):
    # if Connections lost
    if clients != list_clients:
        list_clients.remove(connection)

## Write code here

# Setting socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Error message for no arguements
if len(sys.argv) != 3:
    print("Usage : server.py [ip][port]")

IP = str(sys.argv[1])     # IP Address of server running
PORT = int(sys.argv[2])   # Port number coresponding to IP Address
server.bind((IP, PORT))   # Socket Binding
server.listen(100)        # Socket Listening to 100 conections

print("-- FriendZone Server is online --")
print("ADDRESS : "+IP+":"+str(PORT))

# Waiting for Connections
while True:

    conn,addr = server.accept() # Getting Clients
    list_clients.append(conn)   # Adding clients to lists
    print(addr[0]+" is online") # Client is Online

    # Starting Message thread
    start_new_thread(client_thread,(conn, addr))

# Closing Server
print("Closing Connections")
conn.close()
server.close()
