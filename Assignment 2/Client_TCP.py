# Firas Aboushamalah
#250 920 750
#3357 Assignment 2

# importing the socket
import socket 

# defining the IP and Port #s for TCP to be used in sync with server
TCP_IP = '127.0.0.1'
TCP_PORT = 5005

# establishing the socket objects with correct TCP IP/Port variables
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((TCP_IP, TCP_PORT))  #connecting to the server via TCP
print("Connection to the Server is Established.")
# The successful request will be read from server as "What is the current date and time?"
requestInput = input("Please enter your request: ").encode()
s.sendall(requestInput)  #sending the request

# Recieve the server response and decoding it
response = (s.recv(1024)).decode()

# Printing the result to terminal
print("Server Response: " + response)
print("CONNECTION CLOSED") #closing the connection from client after completing the exchange, while server remains open
s.close #closed
