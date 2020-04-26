######################
# UDP_Client.py      #
# FIRAS ABOUSHAMALAH #
# 250-920-750        #
######################
####
import binascii
import socket
import struct
import sys
import hashlib

UDP_IP = '127.0.0.1'
UDP_PORT = 5005
ackValue = 0
seqNum = 0

print('UDP target IP:', UDP_IP)
print('UDP target port:', UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
unpacker = struct.Struct("I I 8s 32s")

# This is the data of the 3 packets we are trying to send
allPacketData = ['NCC-1701','NCC-1422','NCC-1017']

# Loops through list of all packet data and sends each raw_data
for data in allPacketData:

	# Converts each packet data into bytes
	raw_data_as_bytes = data.encode("utf-8")

	#Creating the checksum bit
	values = (ackValue, seqNum, raw_data_as_bytes)
	packer = struct.Struct('I I 8s')
	packed_data = packer.pack(*values)
	chksum =  bytes(hashlib.md5(packed_data).hexdigest(), encoding='UTF-8')

	#Build the UDP Packet
	values = (ackValue,seqNumNum,raw_data_as_bytes,chksum)
	UDP_Packet_Data = struct.Struct('I I 8s 32s')
	UDP_Packet = UDP_Packet_Data.pack(*values)

	#Send the UDP Packet
	sock.sendto(UDP_Packet, (UDP_IP, UDP_PORT))
	print("The packet is being sent: ", values)
	print("UDP Packet has officially been sent.")

	# Listening and receiving the packet
	reply, server_addr = sock.recvfrom(1024) #making the buffer size 1024 bytes

	# struct object to see time

	REPLY_Packet = unpacker.unpack(reply)
	print("The packet is returned in response from the receiver: ", REPLY_Packet)

	# Assigns ack to variable currAck for comparison
	currseqNum = seqNum
	respseqNum = REPLY_Packet[1]

	# Check for new ack response and send the packet using this info
	while respseqNum != currseqNum: 
		print("Ack is different")
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
		print("Resent packet: ", UDP_Packet)
		sock.sendto(UDP_Packet, (UDP_IP, UDP_PORT))
		print("UDP Packet has been resent.") # sends packet again if previous packet was corrupted
		reply, server_addr = sock.recvfrom(1024) # receives new check
		print("Packet received from receiver ", reply)

		# Unpacks response to see values contained
		REPLY_Packet = unpacker.unpack(reply)
		replyAck = REPLY_Packet[0]

	# Switches up seqNum for next packet
	if seqNum == 1:
		seqNum = 0
	else:
		seqNum = 1

# Close connection at the end
sock.close()