import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")

mycursor=mysql.cursor()

print("{:<15} {:<20} {:<20} {:<10}".format("Student Id","Student Nmae","Student Email","Student Class"))

try:
    name=input("enter the student name:- ")
    classname = input("enter the student class name:- ")
    # sql="Select * from student where st_name='"+name+"'"
    # sql = "Select * from student where st_name like '%" + name + "%'"
    # sql = "Select * from student where st_name like '%" + name + "%' and st_class='"+classname+"'"
    sql = "Select * from student where st_name like '%" + name + "%' or st_class='" + classname + "'"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for x in sdata:
        print("{:<15} {:<20} {:<20} {:<10}".format(x[0],x[1],x[2],x[3]))

except:
    print("error...!")