import socket
from  common import addr
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(addr)
print(s.recv(500))