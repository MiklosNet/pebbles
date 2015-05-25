import sys
import urllib
import pycurl
import os
import time

urlon='http://192.168.1.111/arduino/m1on'
urloff='http://192.168.1.111/arduino/m1off'
urlon='http://192.168.1.111/arduino/m1on'
urloff='http://192.168.1.111/arduino/m1off'

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


