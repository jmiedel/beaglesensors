import time
import os
import threading
import BaseHTTPServer

import tmp36
import hih4000

HOST_NAME = '' #asdf
PORT_NUMBER = 1234 # Maybe set this to 9000.

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    #has a sensors variable taht is a list of all connected sensors
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
        for sensor in s.server.sensors:
            lastLine = readLastLine(sensor.log)
            s.wfile.write("<p>%s: %s</p>" % (sensor.name,lastLine))
        s.wfile.write("</body></html>")

class Sensor:
    #manages polling and logging a single sensor
    def __init__(self):
        print "initting abstract class"
    
    def run():
        print "running abstract class"
        return 

def getAbsPath(relPath):
    dir = os.path.dirname(__file__)
    absPath = os.path.join(dir,relPath)
    return absPath

def initSensor(props):
    type = props["type"]
    if (type == "tmp36"):
        return tmp36.tmp36(props)
    if (type == "hih4000"):
        return hih4000.hih4000(props)
    print "unknown sensor type" + type

#makes a series of sensor objcts based on config file
def readConf():
    f = open(getAbsPath("conf.txt"))
    lines = f.readlines()
    sensors = []
    for line in lines:
        properties = line.split(",")
        propDict = {}
        for p in properties:
            (key,value) = p.split(":")
            propDict[key.strip()] = value.strip()
        #print propDict
        sensors += [initSensor(propDict)]
    #print sensors 
    return sensors

def readLastLine(log):
    logSize = os.path.getsize(log)
    f = open(log)
    #should be adjusted to ensure we are getting last line
    #2 specifies end of file
    if(logSize>1000):
        f.seek(-1000,2)
    lastLine = f.readlines()[-1]
    print log+":"+lastLine
    return lastLine
    
if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    #read in sensor config
    sensors = readConf()
    for s in sensors:
        thread = threading.Thread(target=s.run,args=())
        thread.daemon = True
        thread.start()
    try:
        print time.asctime(),"Server Starts - %s:%s"%(HOST_NAME, PORT_NUMBER)
        httpd.sensors = sensors
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
