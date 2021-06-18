import smtplib, ssl
import os

path = '/home/pi/ip.txt'
printlist = []
with open(path, 'r') as f:
 for line in f:
  trim = line.strip()
  if trim.startswith('inet'):
   printlist.append(trim)

list2str = ' |........| '.join(map(str, printlist))
#print(list2str)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "unstoppablepirate@gmail.com"  # Enter your address
receiver_email = "mehmood97ashiq@gmail.com"  # Enter receiver address
password = "iamapirate1234"
message = """\
Subject: Hi from Raspberry Pi

Ip Address:

{printlist}
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.format(printlist=list2str))

