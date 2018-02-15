#  Python implementation

# 	Program    :  File Server Implementation (Client)
# 	Status     :  Stable
# 	Created by :  Sarath Peter

## Import packages here
import socket
## Write functions here

## Write code here

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 10101                    # Reserve a port for your service.

s.connect((host, port))
s.send("You have connected to "+host)

with open('received_file', 'wb') as f:
    print('file opened')
    print('receiving data...\n')
    while True:

        data = s.recv(1024)
        print(data)
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('===== File Reccived from '+host+' =====')
s.close()
print('connection closed')
