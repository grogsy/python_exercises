# Asynchronous HTTP server using only asyncore

import asyncore, socket
import os
import mimetypes
import collections

try:
    from http.client import responses
except:
    from httplib import responses

# This class merely handles accept events
class async_http(asyncore.dispatcher):

    def __init__(self, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind(('', port))
        self.listen(5)

    def handle_accept(self):
        client, addr = self.accept()
        print("Connected: %s" % str(addr))
        return async_http_handler(client)

# Handle clients
class async_http_handler(asyncore.dispatcher):
    def __init__(self, sock=None):
        asyncore.dispatcher.__init__(self, sock)
        self.got_request  = False
        self.request_data = b""
        self.write_queue  = collections.deque()
        self.responding   = False

    # Only readable if request header not read
    def readable(self):
        return not self.got_request

    # Read incoming request data
    def handle_read(self):
        chunk = self.recv(8192)
        self.request_data += chunk
        if b'\r\n\r\n' in self.request_data:
            self.handle_request()

    # Handle incoming request
    def handle_request(self):
        self.got_request = True
        header_data  = self.request_data[:self.request_data.find(b'\r\n\r\n')]
        header_text  = header_data.decode('latin-1')
        header_lines = header_text.splitlines()
        request      = header_lines[0].split()
        op  = request[0]
        url = request[1][1:]
        self.process_request(op, url)

    # Process the request
    def process_request(self, op, url):
        self.responding = True
        if op == 'GET':
            if not os.path.exists(url):
                self.send_error(404, "File %s not found\r\n" % url)
            else:
                type, encoding = mimetypes.guess_type(url)
                size = os.path.getsize(url)
                self.push_text('HTTP/1.0 200 OK\r\n')
                self.push_text('Context-length: %d\r\n' % size)
                self.push_text('Content-type: %s\r\n' % type)
                self.push_text('\r\n')
                self.push(open(url, "rb").read())
        else:
            self.send_error(501, "%s method not implemented" % op)

    # Error handling
    def send_error(self, code, message):
        self.push_text('HTTP/1.0 %s %s\r\n' % (code, responses[code]))
        self.push_text('Content-type: text/plain\r\n')
        self.push_text('\r\n')
        self.push_text(message)

    # Add binary data to the output queue
    def push(self, data):
        self.write_queue.append(data)

    # Add encoded text data to the output queue
    def push_text(self, text):
        self.push(text.encode('latin-1'))

    # Only writable if a response is ready
    def writable(self):
        return self.responding and self.write_queue



    # Write response data
    def handle_write(self):
        chunk = self.write_queue.popleft()
        bytes_sent = self.send(chunk)
        if bytes_sent != len(chunk):
            self.write_queue.appendleft(chunk[bytes_sent:])
        if not self.write_queue:
            self.close()

# Create the server
a = async_http(8080)
# Poll forever
asyncore.loop()



