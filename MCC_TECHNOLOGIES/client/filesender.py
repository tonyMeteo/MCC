#this app send the bufferfile over to the server

import sys
import socket
import os

host = ''

skServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

skServer.bind((host,2525))

skServer.listen(10)
print "Server Active"

bFileFound = 0

while True:
    Content,Adress = skServer.accept()
    print Adress
    sFileName = Content.recv(1024)
    for file in os.listdir("./"):
        if file == sFileName:
            bFileFound = 1
            break
    if bFileFound == 0:
        print sFileName+ "Not found on server"
    else:
        print sFileName+" File found"
        fUploadFile = open("./"+sFileName,"rb")
        sRead = fUploadFile.read(1024)
        while sRead:
            Content.send(sRead)
            sRead = fUploadFile.read(1024)
        print "Sending Completed"
    break
Content.close()
skServer.close()
