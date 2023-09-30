import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")

mycursor=mysql.cursor()

print("{:<15} {:<20} {:<20}".format("State Id","State Name","Country Name"))

try:
    sql = "Select state.state_id,state.state_name,country.country_name from state inner join country on state.country_id=county.country_id"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for x in sdata:
        print("{:<15} {:<20} {:<20}".format(x[0],x[1],x[2]))

except:
    print("error...!")