import sqlite3
conn=sqlite3.connect("sqlite.db")

try:
    conn.execute('''
            Create table st(
                st_id int AUTO_INCREAMENT PRIMARY KEY,
                st_name VARCHAR(25),
                st_class VARCHAR(25),
                st_email VARCHAR(50)
            )
            ''')
    conn.close()
except:
    print("Already executed !")