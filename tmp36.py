import Adafruit_BBIO.ADC as ADC
import time
import os

class tmp36:
    def __init__(self,props):
        self.name = props["name"]
        self.pin = props["pin"]
        self.log = self.name+".txt"
        dir = os.path.dirname(__file__)
        self.log = os.path.join(dir,self.log)
    def run(self):
        ADC.setup()
        while(True):
            time.sleep(60)
            raw = ADC.read("P9_"+self.pin)
            tempF = rawToF(raw)
            f = open(self.log,"a+")
            #seeks to end of file
            f.seek(0,2)
            #write time stamps with 2 decs of accuracy
            f.write("temp,%.3f,%.2f\n"% (tempF,time.time()))
        print "shouldnt be here"

def rawToF(raw):
    mV = raw * 1800.0 #1.8V reference
    tempC = (mV-500)/10
    tempF = (tempC*9/5)+32
    print("mv:%d C:%.3f F:%.3f" % (mV,tempC,tempF))
    return tempF
