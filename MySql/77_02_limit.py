import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")

mycursor=mysql.cursor()

print("{:<15} {:<20} {:<20} {:<10}".format("Student Id","Student Nmae","Student Email","Student Class"))

try:
    sql="Select * from student order by st_id ASC LIMIT 0,3"
    # sql = "Select * from student order by st_id ASC LIMIT 1,2"
    # sql = "Select * from student order by st_id ASC LIMIT 2,2"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for x in sdata:
        print("{:<15} {:<20} {:<20} {:<10}".format(x[0],x[1],x[2],x[3]))

except:
    print("error...!")