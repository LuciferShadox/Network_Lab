#  Python implementation

# 	Program    :  File Server Implementation (Server)
# 	Status     :  Stable
# 	Created by :  Sarath Peter

## Import packages here
import socket
## Write functions here

## Write code here

port = 10101                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('------- File Server is online ------')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print(addr[0]+':'+str(addr[1])+" is online")
    data = conn.recv(1024)
    print(repr(data))

    filename='test_message.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent :\n')
       print(l)
       l = f.read(1024)
    f.close()

    print('\nFile Sent to '+addr[0]+':'+str(addr[1]))
    conn.send('Thank you for connecting Sarath\'s File Server ')
    conn.close()
