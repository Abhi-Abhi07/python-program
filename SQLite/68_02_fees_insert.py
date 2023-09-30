import sqlite3
conn=sqlite3.connect("sqlite.db")

ins='''
    insert into fees(fees_id,st_id,fees_amount) values 
    (1,1,2000),
    (2,1,3000),
    (3,2,3000),
    (4,3,3000),
    (5,1,3000),
    (6,2,3000),
    (7,2,5000)
    '''
conn.execute(ins)
conn.commit()
conn.close()