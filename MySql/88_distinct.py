import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")

mycursor=mysql.cursor()

print("{:<15}".format("Emp Department Name"))

try:
    sql = "Select distinct(dname) from emp"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for x in sdata:
        print("{:<15}".format(x[0]))
except:
    print("error...!")