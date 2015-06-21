import sys
import urllib
import pycurl
import os
import time
import MySQLdb as mdb
import datetime

sys.path.insert(0, '/usr/lib/python2.7/bridge/')
from bridgeclient import BridgeClient as bridgeclient

urlon='/arduino/m1on'
urloff='http://localhost/arduino/m1off'
urlph='http://localhost/arduino/getph'

def checkph():
	value = bridgeclient()
	phvalue = value.get('PH')
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

con = mdb.connect('192.168.1.141', 'webuser', 'usepassword', 'miklosnet');
with con:

    cur = con.cursor()

    phresult = checkph()
    setime = datetime.datetime.now()
    idis = 1
    
    loggit = "INSERT INTO reading (val,date,sid) VALUES (%s, %s, %s)"

    cur.execute(loggit, (phresult,setime,idis))
    con.commit()

    print phresult
    print setime
    print idis



        
	




