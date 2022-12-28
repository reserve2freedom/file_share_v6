import http.server
import socket
import sys

class HTTPServer6(http.server.HTTPServer):
	address_family = socket.AF_INET6

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
handler = http.server.SimpleHTTPRequestHandler
server = HTTPServer6(('::', port), handler)
server.serve_forever()
