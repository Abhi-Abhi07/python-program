import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")

mycursor=mysql.cursor()

print("{:<15}".format("Oreder Total"))

try:
    # sql="Select min(order_amount) from orders"
    sql = "Select max(order_amount) from orders"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for x in sdata:
        print("{:<15}".format(x[0]))
except:
    print("error...!")