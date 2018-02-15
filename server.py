#  Python implementation

# 	Program    :  File Server 2 Implementation (Server)
# 	Status     :  Developing
# 	Created by :  Sarath Peter

## Import packages here

import sys
import socket
import os

## Write functions here

## Write code here

host = "10.1.3.36"
port = 10201
FND_FLAG = 0
default_path = "/home/student"

skServer = socket.socket()
skServer.bind((host, port))
skServer.listen(20)
print("====== File Server is online ======")
while True:

    Content, Address = skServer.accept()
    IP_ADDR = Address[0]+':'+str(Address[1])
    print(IP_ADDR+" is online")
    Content.send("\nServer directory : "+default_path+"\n")
    Serverfile = Content.recv(4096)

    if Serverfile == 'list':
        for files in os.listdir(default_path):
            Content.send(" -> "+files)

    if ServerFile == 'help':
            print("-- DOCS here --")

    if ServerFile == 'exit':
            break

    if Serverfile[:4] == 'goto':
            FND_FLAG = 2
            for files in os.listdir(default_path):
                if os.path.isdir(Serverfile):
                    default_path = default_path + Serverfile[5:]
                    Content.send(FND_FLAG)
                else:
                    Content.send("\n==(!)== Error 004 : Path not found !! ==(!)==")

    if Serverfile[:3] == 'get':
        FND_FLAG = 1
        Content.send(FND_FLAG)
        for files in os.listdir(default_path):
            if os.path.isfile(files) and files == Serverfile[4:]:
                upload_PTR = open(default_path+Serverfile[4:],"rb")
                read_PTR = upload_PTR.read(4096)
                while read_PTR:
                    Content.send(read_PTR)
                    read_PTR = upload_PTR.read(4096)
                print("====== Upload success!! ======")
                print("File uploaded to "+IP_ADDR)

            else:
                Content.send("\n==(!)== Error 404 : File not found !! ==(!)==")
                FND_FLAG = 0

    else:
        Content.send("--> Invalid Code <--")

Content.close()
skServer.close()
print("\n====== Server down ======")
