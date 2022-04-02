# Author: Evan McKenzie
# Class: EE 4272/CS 4461 Computer Networks
# Date Created: February 7, 2022
# Last Edited: February 14, 2022

from socket import *		#import all of the socket library

serverName = 'localhost'
serverPort = 9876
clientSock = socket(AF_INET, SOCK_DGRAM)		#create/link socket
uscomm = input("Press q to get a quote now: ")		#prompt for user input

if uscomm != "q":			#q is the only valid command here
	wrongmess = "wpyf"		#encode obviously incorrect message
	clientSock.sendto(wrongmess.encode(), (serverName, serverPort))		#transmit incorrect message
	print("NOT A VALID COMMAND! The correct string is qotd")		#say something to illustrate error
	clientSock.close();		#close socket
	exit()			#exit client
else:
	sendmess = "qotd"		#send qotd if correct character
	clientSock.sendto(sendmess.encode(), ('localhost', 9876))	#compress and send message to server
	quoteString, serverAddr = clientSock.recvfrom(2048)		#python equivalent of pipe end (blocking for data)
	print("Quote of the Day: ", quoteString.decode())		#print the quote returned from the server
	clientSock.close()		##close connection


