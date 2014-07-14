#!/usr/bin/env python
 
import logging
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
 
class HttpServerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.getheader("Content-Length"))
        request = self.rfile.read(content_length)
        logging.info("Request: %s" % request)
        # BaseHTTPRequestHandler has a property called server and because
        # we create MyHTTPServer, it has a handler property
        response = self.server.handler(request)
        logging.info("Response: %s" % response)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response)
     
class MyHTTPServer(HTTPServer):
    """this class is necessary to allow passing custom request handler into
       the RequestHandlerClass"""
    def __init__(self, server_address, RequestHandlerClass, handler):
        HTTPServer.__init__(self, server_address, RequestHandlerClass)
        self.handler = handler
             
class HttpServer:
    def __init__(self, name, host, port, handler):
        self.name = name
        self.host = host
        self.port = port
        self.handler = handler
        self.server = None
         
    def start(self):
        logging.info('Starting %s at %s:%d' % (self.name, self.host, self.port))
        # we need use MyHttpServer here
        self.server = MyHTTPServer((self.host, self.port), HttpServerHandler,
                                   self.handler)
        self.server.serve_forever()
     
    def stop(self):
        if self.server:
            logging.info('Stopping %s at %s:%d' % (self.name, self.host,
                                                   self.port))
            self.server.shutdown()
 
def server_handler(request):
    if request == "foo":
        return "bar"
    elif request == "bar":
        return "foo"
    else:
        return "foobar"
 
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', 
                        level=logging.INFO)
    server = HttpServer("test server", "localhost", 9999, server_handler)
    server.start()