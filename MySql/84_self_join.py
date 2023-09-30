import pymysql as mq
db=mq.connect(host="localhost",user="root",password="",db="ecom")
cur=db.cursor()

try:
    sql="select * from categories as c1,categories as c2 where c1.cat_id=c2.parent_id"
    cur.execute(sql)
    sdata=cur.fetchall()
    for a in sdata:
        print(a)
except:
    pass