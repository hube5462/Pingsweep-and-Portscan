#Author:	Aaron Huber
#Date:		3/2015

#This python script will perform a pingsweep of a given network, notifying the user what addresses are up

import subprocess
import socket
import sys

def main():
	submask = sys.argv[1]
	for i in range(1, 255):
		ip = submask + "." + str(i)
		
		try:
			pingresult = subprocess.check_output("ping -c 1 %s" % ip, shell=True)
			print ip + " is up!"
		except:
			pass						#subprocess will throw an exception if ping doesn't return
										#an exit code of 0; nothing necessary to do with a ping that has no response
main()
