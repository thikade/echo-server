#!/usr/bin/env python

import http.server as httpd
import socketserver

PORT = 8000


class GetHandler(httpd.BaseHTTPRequestHandler):

    def do_GET(self):
        RESPONSE = "HEADERS RECEIVED:\n\n"
        for h in self.headers:
            RESPONSE += "{}: {}\n".format(h, self.headers[h])

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-length", len(RESPONSE))
        self.end_headers()
        self.wfile.write(str.encode(RESPONSE))

Handler = GetHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

httpd.serve_forever()