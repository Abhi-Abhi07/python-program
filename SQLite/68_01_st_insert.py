import sqlite3
conn=sqlite3.connect("sqlite.db")

ins='''
    insert into st(st_id,st_name,st_class,st_email) values 
    (1,'raj','12th','raj@gmail.com'),
    (2,'kanika','12th','kanika@gmail.com'),
    (3,'ram','12th','ram@gmail.com'),
    (4,'ketrina','12th','ketrina@gmail.com')
    '''
conn.execute(ins)
conn.commit()
conn.close()