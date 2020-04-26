# Firas Aboushamalah
#250 920 750
#3357 Assignment 2

# importing the socket and datetime modules
import socket
from datetime import datetime

# defining the IP and Port #s for UDP to be used in sync with client UDP
UDP_IP = '127.0.0.1'
UDP_PORT = 5005
UDP_ADDRESS = (UDP_IP, UDP_PORT)  # Creating a variable that will hold the UDP IP and Port adress

# establishing the socket objects with correct TCP IP/Port variables
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(UDP_ADDRESS)  #using the Ip and Ports to bind the socket object

#printing the messages to the terminal
print("Server Address: ", UDP_IP)
print("Server is awaiting a call.")

while 1:  #while true
	# client request being received
    clientRequest, addr = s.recvfrom(1024)
	
	#check the request for valid input (ex. "What is the current date and time")
    if clientRequest.decode('ascii') == "What is the current date and time?":
        dateReply = datetime.now()  #get the date and put it in the response variable
        response = dateReply.strftime("Current Date and Time - %m/%d/%Y %H:%M:%S")
        print("Successfully sent response to client.")
		
	# If it's invalid; then we send back an error message
    else:
        response = "ERROR: Invalid input"
    responseCode = response.encode('ascii')  #encode the response back from ascii
    s.sendto(responseCode, addr) #sending the response to the client
