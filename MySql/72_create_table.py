import pymysql as mq

conn=mq.connect(
    host="localhost",
    user="root",
    passwd="",
    database="school"
)

mysqlc=conn.cursor()
#Table student (st_id,st_name,st_class,st_email)
tc="""create table student(
   st_id INT primary key auto_increment,
   st_name varchar(25),
   st_class varchar(20),
   st_email varchar(30)
   )"""
mysqlc.execute(tc)