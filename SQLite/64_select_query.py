import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM student limit 2,2")
#limit me 2,1 yani second row ke baad se ek row show
#limit me 1,3 yani first row ke baad se two roww show

for a in data:
    print(a[0],a[1],a[2])
