#!/usr/bin/python
# -*- coding: utf-8 -*

import pyinotify
import socket
import time
    
UDP_IP="192.168.0.7"
UDP_PORT=6005
LOG_FILE="/home/bhervy/Documents/nantes1900.log" #pathname is for test. Change it on demo machine

#Define function that send message to networked machine through UDP
def UDPSend(msg,IP,port):
	#sock = socket.socket( socket.AF_INET, # Internet
                        #socket.SOCK_DGRAM ) # UDP
	#sock.sendto( MESSAGE, (UDP_IP, UDP_PORT) )

#Define function that handles change in the log file
def onChange(event):
	f=open(LOG_FILE, 'rw')
	f.close()
	time.sleep(.05)
	f=open(LOG_FILE, 'rw')
	message = f.read()
	print("Envoi de la nouvelle valeur:", message)
	UDPSend(message, UDP_IP, UDP_PORT)

def main():
    # watch manager
	wm = pyinotify.WatchManager()

    # notifier
	notifier = pyinotify.Notifier(wm)
	wm.add_watch(LOG_FILE, pyinotify.IN_CLOSE_WRITE, onChange)
	notifier.loop()

if __name__ == '__main__':
    main()
