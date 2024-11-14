#!/usr/bin/env python

import http.server as httpd
import socketserver

PORT = 8000


class GetHandler(httpd.BaseHTTPRequestHandler):

    def do_GET(self):
        rList = []
        for h in self.headers:
            rList.append("{}: {}".format(h, self.headers[h]))
        rList.sort()
        RESPONSE = "HEADERS RECEIVED:\n\n" + "\n".join(rList)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-length", len(RESPONSE))
        self.end_headers()
        self.wfile.write(str.encode(RESPONSE))

Handler = GetHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

httpd.serve_forever()

