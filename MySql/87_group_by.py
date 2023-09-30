import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")

mycursor=mysql.cursor()

print("{:<15} {:<15}".format("Emp count","Emp Department Name"))

try:
    sql = "Select count(*),dname from emp group by dname"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for x in sdata:
        print("{:<15} {:<15}".format(x[0],x[1]))
except:
    print("error...!")