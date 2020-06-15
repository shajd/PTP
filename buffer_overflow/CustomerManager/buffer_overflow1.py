#!/usr/bin/python
import socket

ServiceManagerIP = "192.168.150.25"
ServiceManagerPort = 42424

# Array of A's
buff = ["A"]
counter = 100

#Loop to build array
while len(buff) <= 30:
    buff.append("A"*counter)
    counter = counter+200


#Attempt to send message
for string in buff:
    print "Fuzzing PASS with %s bytes" % len(string)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to Win7 machine
    connect = s.connect((ServiceManagerIP, ServiceManagerPort))
    s.send(string + '\r\n')
    s.recv(1024)
    s.close()


