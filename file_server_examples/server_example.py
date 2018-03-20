# Time server program
from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)    # Create a TCP Socket
s.bind(('', 8888))                  # Bind to port 8888
s.listen(5)                         # Listen, but allow no more than
                                    # 5 pending connections.

while True:
    client, addr = s.accept()       # Get a connection
    print("Got a connection from %s" % str(addr))
    timestr = time.ctime(time.time()) + "\r\n"
    client.send(timestr.encode('ascii'))
    client.close()



