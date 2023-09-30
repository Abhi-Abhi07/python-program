import pymysql as mq

mysql = mq.connect(host="localhost", user="root", password="", database="school")

mycursor = mysql.cursor()

print("{:<15}".format("Total count "))

try:
    sql = "Select count(*) from orders"
    mycursor.execute(sql)

    sdata=mycursor.fetchall()
    for x in sdata:
        print(x[0])

except:
    print("error...!")