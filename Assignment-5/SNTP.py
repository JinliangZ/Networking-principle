from socket import *
import struct
import sys
import time

NTP_SERVER = 'europe.pool.ntp.org'  # server domain
TIME1970 = 2208988800      # 1970-01-01 00:00:00

def sntp_client():
    client = socket( AF_INET, SOCK_DGRAM )  #socket object
    data =  bytes('\x1b' + 47 * '\0', encoding = "utf8")  # default sending message
    client.sendto( data, (NTP_SERVER, 123 ))  # send UDP packet
    data, address = client.recvfrom( 1024 )   # response from server
    
    if data:
        print ('Response received from:', address) # print address
        t = struct.unpack( '!12I', data )[10]  # extract timestamp
        t -= TIME1970  #calculate time
        print ('\tTime=%s' % time.ctime(t))

if __name__ == '__main__':
    sntp_client()