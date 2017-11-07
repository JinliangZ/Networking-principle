from socket import *
import sys 


ip=input("ip address")
port=input("port")
port=int(port)
path=input("path")

clientSocket= socket(AF_INET, SOCK_STREAM)
clientSocket.connect((ip,port))

request= 'GET /' +path+ ' HTTP/1.1\r\nhost: '+ip+':'+str(port)+"\r\n\r\n"
request=request.encode()
print(request)
clientSocket.send(request)

data=b""
tmp=b" "
while tmp:
    tmp=clientSocket.recv(1024)
    data=data+tmp
data=data.decode()

print("content:\n"+data)
clientSocket.close()
    
    