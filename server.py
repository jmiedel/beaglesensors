import time
import os
import BaseHTTPServer

HOST_NAME = '' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 1234 # Maybe set this to 9000.
LOG = "log.txt"
dir = os.path.dirname(__file__)
LOG = os.path.join(dir,LOG)

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body><p>This is a test.</p>")
        logSize = os.path.getsize(LOG)
        f = open(LOG)
        #should be adjusted to ensure we are getting last line
        #2 specifies end of file
        if(logSize>1000):
            f.seek(-1000,2)
        lastLine = f.readlines()[-1]
        print lastLine
        s.wfile.write("<p>lastLine: %s</p>" % lastLine)
        s.wfile.write("</body></html>")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
