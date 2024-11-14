#!/usr/bin/env python

import http.server as httpd
import socketserver

PORT = 8000


class GetHandler(httpd.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_head()
        for h in self.headers:
            self.send_header(h, self.headers[h] +"<br>")
        self.end_headers()
        self.send_response(200, "")



Handler = GetHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

httpd.serve_forever()