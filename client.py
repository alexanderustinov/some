import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    text = input()
    s.sendto(text.encode(), ('192.168.202.255', 10000))
