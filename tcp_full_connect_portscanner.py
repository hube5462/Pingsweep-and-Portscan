#Author:	Aaron Huber
#Date:		3/2015

#This python script with port scan a given ip address within the specified range of ports
import socket
import sys

def main():
	ip = sys.argv[1]						#take the ip address from the command line
	for i in range(1, 1025):				#iterate through ports 1 to 1025
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((ip, i))
			print "Port %i is up. " % (i)
			sock.settimeout(3)
		except:
			print "Port %i is down." % (i)
	

main()
