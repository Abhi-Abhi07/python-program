import sqlite3
conn=sqlite3.connect("sqlite.db")

try:
    conn.execute('''
            Create table student(
                st_id int AUTO_INCREMENT PRIMARY KEY,
                st_name VARCHAR(25),
                st_class VARCHAR(25),
                st_email VARCHAR(50)
            )
            ''')
    conn.close()
except:
    print("Already executed !")