import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")

cursorobj=mysql.cursor()
name=input("Enter the name ")
class_name=input("Enter the class Name ")
st_id=input("Enter the student id ")
st_email=input("Enter the email ")

sql="update student set st_name=%s,st_class=%s,st_email=%s where st_id=%s"
data=(name,class_name,st_email,st_id)
try:
    cursorobj.execute(sql,data)
    mysql.commit()
    print("Data Updated")
except:
    print("error......!")