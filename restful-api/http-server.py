#!/usr/bin/python3

import http.server
import json


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        



port = 8000
address = ("", port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)


print(f"Serveur démarré sur le PORT {port}")

httpd.serve_forever()