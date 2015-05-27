import _mysql as mikdb
import sys

try:
    mikcon = mikdb.connect('192.168.1.141', 'webuser', 'usepassword', 'miklosnet')

except _mysql.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)


