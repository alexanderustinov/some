import socket
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 10000)) # 0.0.0.0 - слушать на
                           # всех адресах этой машины
s.setblocking(False)
s.settimeout(1)

while True:
    try:
        message, (ip, port) = s.recvfrom(500)
    except TimeoutError:
        continue
    logger.info(f"{ip}: {message.decode()}")
