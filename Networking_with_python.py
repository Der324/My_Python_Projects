# Sockets in Python

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ("data.pr4e.org", 80) )
print(mysock)

# Networking Protocol
# Internet Standards

# Writing a Web Browser using Python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n".encode()
mysock.send(cmd)

while True:
   data = mysock.recv(512)
   if ( len(data) < 1 ):
       break
   print(data.decode())
mysock.close()

# Exercise!

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end=" ")
mysock.close()