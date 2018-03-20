import sys, os
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port   = 8080

os.chdir(webdir)

server_addr = ("", port)

server_obj  = HTTPServer(server_addr, CGIHTTPRequestHandler)

server_obj.serve_forever()
