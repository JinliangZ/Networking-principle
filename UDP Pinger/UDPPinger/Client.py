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

    LastPing = 10
    count = 0
    Csocket.settimeout(2)
   

    while count  < LastPing:
        count = count + 1
        startTime = time.time()
        print("ping " , count)
        Csocket.sendto(data.encode(), (serverName, port))

        try:
            newData,severAddress = Csocket.recvfrom(1024)
            RTT = ((time.time()) - startTime)
            print ("RTT=", RTT*1000,'ms')
        except timeout:
            print(" Request timed out ")

    print ("the program is done")
main()