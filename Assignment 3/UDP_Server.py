######################
# UDP_Server.py      #
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
unpacker = struct.Struct('I I 8s 32s')

#creating the socket object
sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))
print("Server is created and listening at: ", UDP_IP)

def getCheckSum(ackValue, seqNum, pktData):
    values = (ackValue, seqNum, pktData)
    packer = struct.Struct("I I 8s")
    packed_data = packer.pack(*values)
    chksum = bytes(hashlib.md5(packed_data).hexdigest(), encoding="UTF-8")

    return chksum

while True:
    #Receive Data
    data, addr = sock.recvfrom(1024) 
    UDP_Packet = unpacker.unpack(data) #unpacking the data

    # Prints out received UDP packet
    print('received from:', addr) #printing the address of the sender as well as the message information
    print('received message:', UDP_Packet)

    #getting the checksum value and placing it in the correct variable to compare
    chksum = getCheckSum(UDP_Packet[0],UDP_Packet[1],UDP_Packet[2])

    # creates response ack
    replyAck = 1
    same = UDP_Packet[3] == chksum:
    #Compare Checksums to test for corrupt data
    if same:
        print('Checksums Match!\nPacket data: ', UDP_Packet[2].decode("utf-8"))

        # Creates checksum for response
        response = (replyAck,UDP_Packet[1])
        UDP_Data = struct.Struct('I I')
        resp_data = UDP_Data.pack(*response)
        respChksum =  bytes(hashlib.md5(resp_data).hexdigest(), encoding='UTF-8')

        # placing the response in its own UDP packet to send
        response = (replyAck,UDP_Packet[1],respChksum)
        print("Response sent across network: ", response)
        UDP_Data = struct.Struct('I I 32s')
        UDP_Packet = UDP_Data.pack(*response)

        # Sends same Ack to receiver to show that it is not corrupted
        sock.sendto(UDP_Packet,addr)
    else:
        print('The packet is corrupt: checksum does not match.')

        # Sends previous or different Ack to receiver to show that it is corrupted
        if UDP_Packet[1] == 1:
            UDP_Packet[1] = 0
        else:
            UDP_Packet[1] = 1

        # Creates checksum for response
        response = (replyAck,UDP_Packet[1])
        UDP_Data = struct.Struct('I I')
        resp_data = UDP_Data.pack(*response)
        respChksum =  bytes(hashlib.md5(resp_data).hexdigest(), encoding='UTF-8')

        # Puts response into UDP Packet
        response = (replyAck, UDP_Packet[1],respChksum)
        print("Response sent: ", response)
        UDP_Data = struct.Struct('I I 32s')
        UDP_Packet = UDP_Packet_Data.pack(*response)

        # Sends different ACK to indicate corrupted data
        sock.sendto(UDP_Packet,addr)        