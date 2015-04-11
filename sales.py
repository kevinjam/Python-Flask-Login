import sqlite3 as lite
import sys

sales = (
      ('KevinJanvier',0222222),
      ('Babajide_Adegbenro', 002),
      ('Elly_Yiga', 003),
      ('Muhamed', 004),	
      ('Tousaint Mu', 005)


)

con = lite.connect('sales.db')

with con:
	
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS reps")
	cur.execute("CREATE TABLE reps(rep_name TEXT, amount INT)")
	cur.executemany("INSERT INTO reps VALUES( ?, ?)" , sales)
