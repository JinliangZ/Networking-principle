from socket import *
from matplotlib import pyplot as plt
import datetime
import time
import numpy
#coding= utf-8

def main():
    serverName = 'localhost'
    port = 12000
    Csocket = socket(AF_INET, SOCK_DGRAM)
    data = ' ping'
    #data = input("Enter a message in lowercase")

    LastPing = 200
    count = 0
    Csocket.settimeout(2)
    rtts=[]

    while count  < LastPing:
        count = count + 1
        startTime = time.time()
        print("ping " , count)
        Csocket.sendto(data.encode(), (serverName, port))

        try:
            newData,severAddress = Csocket.recvfrom(1024)
            RTT = ((time.time()) - startTime)
            rtts.append(RTT)
            print ("RTT=", RTT*1000,'ms')
        except timeout:
            print(" Request timed out ")
    print('minimum RTT=',min(rtts))
    print('maximum RTT=',max(rtts))  
    print('average RTT=',numpy.mean(rtts)) 
    print('standard deviation RTT=',numpy.std(rtts))
    l=len(rtts)
    print('packet loss rate=',(LastPing-l)/LastPing*100,'%') 
    print ("the program is done")
    plt.hist(rtts, bins = 100) 
    plt.title("histogram") 
    plt.show()   
main()