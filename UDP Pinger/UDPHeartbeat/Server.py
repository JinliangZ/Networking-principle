# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
import time
from unittest.util import sorted_list_difference
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
lastsequencenumber=0

while True:
    
    try:
        message, address = serverSocket.recvfrom(1024)
        endTime= time.time()
        
        message= message.decode()
        sequencenumber= int(message.split("+")[0])
        lastsequencenumber= sequencenumber-1 
            
        startTime= float(message.split("+")[1])
        difference= (endTime- startTime)*1000 
        print("sequence number"+ str(sequencenumber)+" time difference value"+ str(difference)+"ms")
       
        
        if lastsequencenumber!=sequencenumber-1:
            print("miss packet"+str(sequencenumber-1))
        
        lastsequencenumber= sequencenumber
    
    except timeout:
        print("client has stopped")
    
   