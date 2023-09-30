import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM student")

for n in data:
    print(n)

print()
print()

st_name=input("Enter the student name : ")
st_class=input("Enter the student class : ")
# data=conn.execute("SELECT * FROM student where st_name='"+st_name+"'")
# data=conn.execute("SELECT *FROM student where st_name like'%"+st_name+"%'")

# data=conn.execute("SELECT *FROM student where st_name='"+st_name+"' and st_class='"+st_class+"'")

data=conn.execute("SELECT *FROM student where st_name='"+st_name+"' or st_class='"+st_class+"'")
for a in data:
    print(a)
conn.close()