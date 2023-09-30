import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")

mycursor=mysql.cursor()

print("{:<15}".format("order amount"))

try:
    sql = "Select sum(order_amount) from orders"
    mycursor.execute(sql)

    sdata=mycursor.fetchone()
    print("{:<15}".format(sdata))

    # sdata=mycursor.fetchall()
    # for x in sdata:
    #     print("{:<15}".format(x[0]))

except:
    print("error...!")