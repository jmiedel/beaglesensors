import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
import os

LOG = "log.txt"
ADC.setup()
dir = os.path.dirname(__file__)
LOG = os.path.join(dir,LOG)
while(True):
    time.sleep(1)
    raw = ADC.read("P9_40")
    mV = raw * 1800.0 #1.8V reference
    tempC = (mV-500)/10
    tempF = (tempC*9/5)+32
    f = open(LOG,"r+w")
    #seeks to end of file
    f.seek(0,2)
    #write time stamps with 2 decs of accuracy
    f.write("temp,%.3f,%.2f\n"% (tempF,time.time()))
    print("mv:%d C:%.3f F:%.3f" % (mV,tempC,tempF))
print "shouldnt be here"
