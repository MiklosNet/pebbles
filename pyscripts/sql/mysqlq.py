import mysqlc as dahouse
import sys

with mikcon:
    
    cur = mikcon.cursor()
    cur.execute("INSERT INTO reading(volt,val,descr,date,sid) VALUES('Jack London','','','','','')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
