import pymysql as mq
# server connection or db connection

mysql=mq.connect(host="localhost",user="root",password="",database="school")

mycursor=mysql.cursor()

print("{:<15} {:<20} {:<20} {:<10}".format("Student Id","Student Nmae","Student Email","Student Class"))

try:
    sql="Select * from student"
    mycursor.execute(sql)
    # sdata=mycursor.fetchall()
    # for x in sdata:
    #     # print(x)
    #     print("{:^15} {:^20} {:<20} {:<10}".format(x[0],x[1],x[2],x[3]))

    sdata=mycursor.fetchone()
    print("{:^15} {:^20} {:<20} {:<10}".format(sdata[0],sdata[1],sdata[2],sdata[3]))
except:
    print("error...!")