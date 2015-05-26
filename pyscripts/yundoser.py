import sys
import urllib
import pycurl
import os
import time
sys.path.insert(0, '/usr/lib/python2.7/bridge/')
from bridgeclient import BridgeClient as bridgeclient

urlon='/arduino/m1on'
urloff='http://localhost/arduino/m1off'
urlph='http://localhost/arduino/getph'

def checkph():
	curl = pycurl.Curl()
	curl.setopt(pycurl.URL, urlph)
	curl.perform()
	curl.close()
	value = bridgeclient()
	phvalue = value.get('PH')
	if(phvalue > "7"):
	   duration = offsetph(phvalue)
	   adjustph(duration)
	print("ph")
	print phvalue
	return phvalue;

def adjustph(duration):
	curl = pycurl.Curl()
	curl.setopt(pycurl.URL, urlon)
	curl.perform()
        print("adjusting ph")	
	time.sleep(duration)
	curl.setopt(pycurl.URL, urloff)
	curl.perform()
	curl.close()

def offsetph(ph):
	phtop = 6.8
	if(ph > phtop):
	   magicnum = ph - phtop
	   if(magicnum >= 3):
	    pumpduration = 35
           if(magicnum <= 2):
	    pumpduration = 15   
        return pump_duration;
	    
results = checkph()


        
	




