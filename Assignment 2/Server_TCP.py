# Firas Aboushamalah
#250 920 750
#3357 Assignment 2

# importing the socket and datetime modules
import socket 
from datetime import datetime

# defining the IP and Port #s for TCP to be used in sync with client TCP
TCP_IP = '127.0.0.1'
TCP_PORT = 5005

# establishing the socket objects with correct TCP IP/Port variables
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((TCP_IP, TCP_PORT))
server.listen(1)  #listening for any client requests from Client_TCP.py

#printing the messages to the terminal
print("Server Address: ", TCP_IP)
print("Server is awaiting a call.")

# Waiting for a client to make a connection request to the given IP and Port
while 1: #while true
    conn, addr = server.accept()  #a connection is made, therefore accept it
    print("Connection to client is made.")

	# client request being received
    clientRequest = (conn.recv(1024)).decode('ascii')  #converting the message to ascii

	#check the request for valid input (ex. "What is the current date and time")
    if clientRequest == "What is the current date and time?":
        dateReply = datetime.now()   #if this request is made, get the current date and time
        response = (dateReply.strftime("Current Date and Time - %m/%d/%Y %H:%M:%S"))
        print("Successfully sent response to client.")
    else:  #if the specific request is not as expected
        response = ("ERROR: Invalid Request!")
        print("The server could not send the request.")
        
    #send the correct response whether it was successful or unsuccessful with the appropriate message
    responseCode = response.encode('ascii')  #converting the message back from ascii
    conn.send(responseCode)  #sending the response to the client and closing the connection
    conn.close
