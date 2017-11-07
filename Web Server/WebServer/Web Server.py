#!/usr/bin/env python
# coding= utf-8

#import socket module
from socket import *
import sys # In order to terminate the program
from fileinput import filename


serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('', 666))
serverSocket.listen(1)
print ('Web server is on port: 666')
while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print (message, '::', message.split()[0], ':', message.split()[1])
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        connectionSocket.send(outputdata.encode())
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        print ('404 Not Found')
        #Close client socket
        connectionSocket.send('\HTTP/1.1 404 Not Found\n\n'.encode())
        connectionSocket.close()
            
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data

