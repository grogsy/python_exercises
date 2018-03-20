# An asynchronous HTTP server using asynchat
# How it works:
#               - While the server is listening
#                 clients can request sessions to the server
#                 via webbrowser in order to access files
#                 To test on a local machine type into browser:
#                    http://localhost:8080/<file_name>/
#
#                 To test from a local network:
#                    http://<private_network_ip>:8080/<file_name>/
#
# Of course you can change the port number to suit your use case.
# script is from the example provided by David Beazley's "Python Essentials" book


import asynchat, asyncore, socket
import os
import mimetypes

try:
    from http.client import responses                       # Python 3
except ImportError:
    from httplib import responses                           # Python 2

# This class plugs into the asyncore module and merely handles accept events
class async_http(asyncore.dispatcher):

    def __init__(self, port):
        # initialize the server to listen in for clients
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind(('', port))
        self.listen(5)

    def handle_accept(self):
        # send incoming connections to the custom handler
        client, addr = self.accept()
        print("Connected: %s " % str(addr))
        return async_http_handler(client)

# Class that handles asyncrhonous HTTP requests.
class async_http_handler(asynchat.async_chat):
    def __init__(self, conn=None):
        asynchat.async_chat.__init__(self, conn)
        self.data = []
        self.got_header = False
        self.set_terminator(b"\r\n\r\n")

    # Get incoming data from the client and append to data buffer
    def collect_incoming_data(self, data):
        if not self.got_header:
            self.data.append(data)

    # Got a terminator(the blank line)
    def found_terminator(self):
        self.got_header = True
        header_data         = b"".join(self.data)
        # Decode header data (binary) into text for further processing
        header_text         = header_data.decode('latin-1')
        header_lines        = header_text.splitlines()
        request             = header_lines[0].split()
        op                  = request[0]
        url                 = request[1][1:]
        self.process_request(op, url)

    # Push text onto the outgoing stream, but encode it first
    def push_text(self, text):
        self.push(text.encode('latin-1'))

    # Process the request
    def process_request(self, op, url):
        if op == "GET":
            if not os.path.exists(url):
                self.send_error(404, "File %s not found\r\n" % url)
            else:
                # get metadata about the file(file extension and size)
                type, encoding = mimetypes.guess_type(url)
                size = os.path.getsize(url)
                
                # build the HTTP response to send back to the client
                self.push_text("HTTP/1.0 200 OK\r\n")
                self.push_text("Content-length: %s\r\n" % size)
                self.push_text("Content-type: %s\r\n" % type)
                self.push_text("\r\n")
                
                # the method responsible for building the requested file,
                # push_with_producer is a built-in method
                # inherited from the async_chat class that requires
                # a file producing method or class to work with
                # we use a class in this case
                self.push_with_producer(file_producer(url))
        else:
            self.send_error(501, "%s method not implemented" % op)
        self.close_when_done()

    # Error handling
    def send_error(self, code, message):
        self.push_text("HTTP/1.0 %s %s\r\n" % (code, responses[code]))
        self.push_text("Content-type: text/plain\r\n")
        self.push_text("\r\n")
        self.push_text(message)

# class responsible for building the file requested from the client
class file_producer(object):
    def __init__(self, filename, buffer_size=512):
        self.f = open(filename, "rb")
        self.buffer_size = buffer_size

    def more(self):
        # using asynchat's push_with_producer method requires 
        # the file producing object to define a 'more' method
        # in order to build the file properly
        
        data = self.f.read(self.buffer_size)
        
        if not data:
            self.f.close()
        return data

a = async_http(8080)
asyncore.loop()

