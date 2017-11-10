from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver 
clientSocket = socket(AF_INET, SOCK_STREAM)
#use ssl to secure transaction
sslSocket = ssl.wrap_socket(clientSocket)

# Create socket called sslSocket and establish a TCP connection with mailserver 
sslSocket.connect((mailserver, 465))   #587 is another port.
recv = sslSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
sslSocket.send(heloCommand.encode())
recv1 = sslSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# start login and print server response.
sslSocket.send(b"AUTH LOGIN\r\n")
recv2 = sslSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '334':
    print('334 reply not received from server.')

# send username and print server response.
#replace username with your email address
username = '*******@gmail.com'
user64 = base64.b64encode(username.encode())
sslSocket.send(user64+b'\r\n')
recv3 = sslSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '334':
    print('334 reply not received from server.')

# send password and print server response.
#replace password with your email password
password = '*****************'
pass64 = base64.b64encode(password.encode())
sslSocket.send(pass64+b'\r\n')
recv4 = sslSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '235':
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
MAIL_From = 'Mail From: <bylearner@gmail.com> \r\n'
sslSocket.send(MAIL_From.encode())
recv5 = sslSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
RCPT_To = 'RCPT To: <******.ca> \r\n'
sslSocket.send(RCPT_To.encode())
recv6 = sslSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
DATA = 'DATA\r\n'
sslSocket.send(DATA.encode())
recv7 = sslSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
sslSocket.send(b'From: ******@gmail.com\r\n')
sslSocket.send(b'To: ********.ca\r\n')
sslSocket.send(b'Subject: question (a)\r\n')
sslSocket.send(msg.encode())
# Message ends with a single period.
sslSocket.send(endmsg.encode())

# Send QUIT command and get server response.
QUIT = 'QUIT\r\n'
sslSocket.send(QUIT.encode())
recv8 = sslSocket.recv(1024).decode()
print(recv8)
if recv8[:3] != '250':
    print('250 reply not received from server.')

clientSocket.close()
sslSocket.close()
