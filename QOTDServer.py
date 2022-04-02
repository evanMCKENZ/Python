# Author: Evan McKenzie
# Class: EE 4272/CS 4461 Computer Networks
# Date Created: February 7, 2022
# Last Edited: February 14, 2022

import random           #import random number library
from socket import *		#import all of the socket library

serverSock = socket(AF_INET, SOCK_DGRAM)	#create UDP socket
print("SOCKET CREATED")

serverSock.bind(('', 9876))		#bind socket to port number 9876
print("SOCKET BOUND, READY TO TRANSMIT")

while True:		#loop while receiving q

	incmess, clientAddr = serverSock.recvfrom(2048)		#block for input from client
	print("---------------------------------------------------------")
	print("MESSSAGE RECEIVED")

	clientString = incmess.decode()		#decode the client side message
	print("DECODING MESSAGE", clientString)

	if clientString != 'qotd':		#quality check client side string (needs to be qotd)
		print("ERROR: INCORRECT MESSAGE STRING. The correct string is qotd")		#output if incorrect message received
		print("---------------------------------------------------------")
	else:
		print("CORRECT MESSAGE RECEIVED: 'QOTD' ")		#correct message received output

		rand = random.randrange(1, 10)			#get random number
		print("RANDOM NUMBER FOR QUOTE: ", rand)

		if rand == 1:			#array of quotes to pick from (star wars only)
			quote = "Do or do not, there is no try - Master Yoda"
		elif rand == 2:
			quote = "I find your lack of faith disturbing - Darth Vader"
		elif rand == 3:
			quote = "May the Force be with you. Always - Obi-Wan Kenobi"
		elif rand == 4:
			quote = "Never tell me the odds - Han Solo"
		elif rand == 5:
			quote = "Now, young Skywalker, you will die - Emperor Palpatine"
		elif rand == 6:
			quote = "There's always a bigger fish - Qui-Gon Jinn"
		elif rand == 7:
			quote = "I'm just a simple man trying to make my way in the universe - Jango Fett"
		elif rand == 8:
			quote = "This is the way - Din Djarin"
		elif rand == 9:
			quote = "I am one with the Force and the Force is with me - Chirrut Imwe"
		elif rand == 10:
			quote = "Rebellions are built on hope - Jyn Erso"
		else:		#default
			quote = "ERROR: INVALID RANDOM NUMBER"

		print("QUOTE SELECTED: ", quote)
		print("SENDING QUOTE...")
		print("---------------------------------------------------------")
		serverSock.sendto(quote.encode(), clientAddr)	#send quote back to client and restart loop
