import pymysql

#Server Name -> localhost
#username -> root
#Password -> ''
myobj=pymysql.connect(
    host="localhost",
    user="root",
    passwd="")
cursorobj=myobj.cursor()
try:
    db="create database school"
    cursorobj.execute(db)
    print("database created")

except:
    print("database error !")