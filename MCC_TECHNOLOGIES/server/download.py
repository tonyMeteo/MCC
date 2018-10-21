#this program download the file with data colected from the client

import sys
import socket

skClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skClient.connect(("127.0.0.1",2525))

sFileName = "bufferfile.txt"
sData = "Temp"

while True:
    skClient.send(sFileName)
    sData = skClient.recv(1024)
    fDownloadFile = open(sFileName,"wb")
    while sData:
        fDownloadFile.write(sData)
        sData = skClient.recv(1024)
    print ("download complete")
    break
skClient.close()
