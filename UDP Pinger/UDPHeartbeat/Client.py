from socket import *
import datetime
import time
#coding= utf-8

def main():
    serverName = 'localhost'
    port = 12000
    Csocket = socket(AF_INET, SOCK_DGRAM)
    data = ' ping'
    #data = input("Enter a message in lowercase")


    count = 0
    Csocket.settimeout(2)
    sequence=1
   

    while True:
        time.sleep(2)
        count = count + 1
        startTime = time.time()
        message=str(sequence)+'\n'+ str(startTime)
        print("ping " , count)
        print(message)
        Csocket.sendto(message.encode(), (serverName, port))
        sequence=sequence+1
        time.sleep(1)
        

main()