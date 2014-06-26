import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
import os

class tmp36:
    def __init__(props):
        this.log = props["name"]+".txt"
	    dir = os.path.dirname(__file__)
	    this.log = os.path.join(dir,this.log)
	def run():
		ADC.setup()
		while(True):
        	time.sleep(1)
			raw = ADC.read("P9_40")
			mV = raw * 1800.0 #1.8V reference
			tempC = (mV-500)/10
			tempF = (tempC*9/5)+32
			f = open(LOG,"a+")
			#seeks to end of file
			f.seek(0,2)
			#write time stamps with 2 decs of accuracy
			f.write("temp,%.3f,%.2f\n"% (tempF,time.time()))
			print("mv:%d C:%.3f F:%.3f" % (mV,tempC,tempF))
		print "shouldnt be here"
