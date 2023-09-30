import pymysql as mq

mysql=mq.connect(
    host="localhost",
    user="root",
    passwd="",
    database="school"
)

mycursor=mysql.cursor()

try:
    #st_id,st_name,st_class,st_email
    ins="INSERT INTO student (st_name,st_class,st_email) values(%s,%s,%s)"
    
    #single row
    t = ("ravee", "12th", 'ravee@gmail.com')
    mycursor.execute(ins,t)

    #multiple row
    # t=[("anjali","12th",'anjali@gmail.com'),("aarvi","12th",'aarvi@gmail.com')]
    # mycursor.executemany(ins,t)

    mysql.commit()
    print("Insert Data")
except:
    print("Error...1")

