import sys
import pycurl
import time
import MySQLdb
import subprocess
import re
import sys
import time
import datetime

sys.path.insert(0, '/usr/lib/python2.7/bridge/')
from bridgeclient import BridgeClient as bridgeclient

urlon='http://localhost/arduino/m1on'
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

def mysqlmiklo():
    conn = MySQLdb.connect("localhost","root","tash415","miklosnet")
    while(True):
    date = time.strftime("%d/%m/%Y")
    clock = time.strftime("%H:%M")
    c = conn.cursor()
    c.execute("INSERT INTO data_th (date, clock, temp, hum) VALUES (%s, %s, %s, %s)",
    (date, clock, temp, humidity))

results = checkph()


        
	

#!/usr/bin/python


