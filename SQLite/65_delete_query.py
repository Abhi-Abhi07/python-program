import sqlite3
conn=sqlite3.connect("sqlite.db")
st_id=input("Enter student id you will remove : ")
conn.execute("DELETE FROM STUDENT where st_id="+st_id)
conn.commit()
conn.close()