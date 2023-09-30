import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")

mycursor=mysql.cursor()

print("{:<15} {:<20} {:<20}".format("Order Id","Order Date","Order Amount"))

try:
    sql="Select order_id,order_date,order_amount from orders where order_id in(1,6)"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for x in sdata:
        print("{:<15} {:<20} {:<20}".format(x[0],x[1],x[2]))

except:
    print("error...!")