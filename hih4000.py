import Adafruit_BBIO.ADC as ADC
import time
import os

class hih4000:
    def __init__(self,props):
        self.name = props["name"]
        self.pin = props["pin"]
        self.log = self.name+".txt"
        dir = os.path.dirname(__file__)
        self.log = os.path.join(dir,self.log)
    def run(self):
        ADC.setup()
        while(True):
            time.sleep(1)
            pin = "P9_"+str(self.pin)
            raw = ADC.read(pin)
            mV = raw * 1800.0 #1.8V reference
            rh = (mV*4.3-.826)/(0.0315*1000)
            f = open(self.log,"a+")
            #seeks to end of file
            f.seek(0,2)
            #write time stamps with 2 decs of accuracy
            f.write("humid,%.3f,%2f\n"% (rh,time.time()))
            print("mv:%d rh:%.3f" % (mV,rh))
        print "shouldnt be here hih4000"
