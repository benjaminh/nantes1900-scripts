#!/usr/bin/python
# -*- coding: utf-8 -*

import socket

#Define socket for UDP communication   
UDP_IP="0.0.0.0"
UDP_PORT=6005
sock = socket.socket( socket.AF_INET, # Internet
                         socket.SOCK_DGRAM ) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind( (UDP_IP,UDP_PORT) )

#Loop for listening UDP data
while True:
	data, addr = sock.recvfrom( 1024 ) # buffer size is 1024 bytes
	print "received message:", data
