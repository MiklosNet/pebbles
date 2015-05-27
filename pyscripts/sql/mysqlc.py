import _mysql
import sys

try:
    con = _mysql.connect('192.168.1.141', 'webuser', 'usepassword', 'miklosnet')
        
    con.query("SELECT VERSION()")
    result = con.use_result()
    
    print "MySQL-miklosnet version: %s" % \
        result.fetch_row()[0]
    
except _mysql.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)


