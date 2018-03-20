# Time client program
from socket import *

s = socket(AF_INET, SOCK_STREAM)        # Create a TCP Socket
s.connect(('localhost', 8888))          # Connect to the server
tm = s.recv(1024)                       # Receive no more than 1024 bytes
s.close()

print("The time is %s" % tm.decode('ascii'))
