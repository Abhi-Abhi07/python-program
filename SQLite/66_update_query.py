import  sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
        update student set st_name='Anjali',st_email='anjali@gmail.com'  where st_id=4
        ''')
conn.commit()
conn.close()