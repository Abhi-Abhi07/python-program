import sqlite3
conn=sqlite3.connect("sqlite.db")

try:
    conn.execute('''
            Create table fees(
                fees_id int AUTO_INCREAMENT PRIMARY KEY,
                st_id int,
                fees_amount int,
                FOREIGN KEY(st_id) REFERENCES st(st_id)
            )
            ''')
    conn.close()
except:
    print("Already executed !")