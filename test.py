import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time

print "hello world"

ADC.setup()
while(True):
    time.sleep(1)
    raw = ADC.read("P9_40")
    mV = raw * 1800.0 #1.8V reference
    tempC = (mV-500)/10
    tempF = (tempC*9/5)+32
    print("mv:%d C:%1.3f F:%1.3f" % (mV,tempC,tempF))
print "shouldnt be here"
