import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")

mycursor=mysql.cursor()

print("{:<15} {:<20} {:<20}".format("user Id","order id","order amount"))

try:
    sql = "Select user.user_id,orders.order_id,orders.order_amount from state right join orders on user.user_id=orders.user_id"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for x in sdata:
        print("{:<15} {:<20} {:<20}".format(x[0],x[1],x[2]))

except:
    print("error...!")