import sys
import urllib
import pycurl
import os
import time



urlon='http://localhost/arduino/m1on'
urloff='http://localhost/arduino/m1off'

sys.path.insert(0, '/usr/lib/python2.7/bridge/')

urlon='http://localhost/arduino/m1on'
urloff='http://localhost/arduino/m1off'

from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()
phvalue = value.get('PH')

if(phvalue >= 7):
	print phvalue
	print " is high, turning on phpump low for 15 seconds"
        curl = pycurl.Curl()
	curl.setopt(pycurl.URL, urlon)
	curl.perform()	
	time.sleep(15)
	curl.setopt(pycurl.URL, urloff)
	curl.perform()
	curl.close()
        
	

if(phvalue <= 6):
	print phvalue
	print "is low"


