import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header 
from email.mime.image import MIMEImage

fromaddr = '********@gmail.com'
toaddrs  = '**********.ca'
username = '********@gmail.com'
password = '*****************'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.set_debuglevel(True) # show communication with the server

#get mail content
f = open('picture1.png', 'rb')
pic = MIMEImage(f.read())
pic.add_header('Content-ID', '<image1>')
f.close()
msg_html = MIMEText('<b>I love computer networks!</b><br><img src="cid:image1"><br>', 'html')
multi = MIMEMultipart('related')
multi['Subject'] = 'question (c)'
multi['From'] = '*********@gmail.com'
multi['To'] = '*********.ca'
mul_alt = MIMEMultipart('alternative')
multi.attach(mul_alt)
mul_alt.attach(msg_html)
multi.attach(pic)

server.sendmail(fromaddr, [toaddrs], multi.as_string())

server.quit()
