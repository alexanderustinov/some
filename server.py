import socket
import logging

logger = logging.getLogger(__name__)
logging.basicConfig()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c = s.bind(('127.0.0.1', 8080))
s.listen(5)

s.setblocking(False)
s.settimeout(1)

while True:
    try:
        client_socket = s.accept()
    except TimeoutError:
        continue
    client, (addr, port) = client_socket
    logger.warning(f"{addr} connected from port {port}")

    incoming = client.recv(500)
    # print(incoming)
    content = """<!doctype html>
<html lang=en>
<head>
<meta charset=utf-8>
<title>blah</title>
</head>
<body>
<p>Съешь этих мягких французских булок, да выпей чаю</p>
</body>
</html>
"""
    client.send(f"""HTTP/1.1 200 OK
Content-Length: {len(content.encode())}
Content-Type: text/html; charset=utf-8\r\n\r\n{content}
""".encode())
    client.close()
    
    



