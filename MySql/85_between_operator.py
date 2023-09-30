import pymysql as mq
# server connection or db connection

mysql=mq.connect(host="localhost",user="root",password="",database="school")

mycursor=mysql.cursor()

print("{:<15} {:<20}".format("State Id","state Name"))

try:
    sql="Select state_id,state_name from student where student_id between 2 and 5"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for s in sdata:
        print("{:<15} {:<20}".format(s[0],s[1]))
except:
    print("error...!")