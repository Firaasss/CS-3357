# Firas Aboushamalah
#250 920 750
#3357 Assignment 2

# importing the socket
import socket 

# defining the IP and Port #s for UDP to be used in sync with server
UDP_IP = '127.0.0.1'
UDP_PORT = 5005
UDP_ADDRESS = (UDP_IP, UDP_PORT)  #address that will be used to send to server

# establishing the socket objects with correct IP and Port variables for a direct connection
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# getting input from the user and sending that directly to the server with given IP and Port
clientReq = input("Please enter your request: ").encode()
s.sendto(clientReq, UDP_ADDRESS)  #sending the input to the server 

# receive the server response in a tuple
data, addr = s.recvfrom(1024)
reply = data.decode()  #decoding the data because above is a tuple

# Display it after decoding
print("Server Response: " + reply)
