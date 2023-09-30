import sqlite3
conn=sqlite3.connect("sqlite.db")
print("Student Id","Student Name","Student Fees")
# data=conn.execute("SELECT * FROM fees as f inner join st as s on f.st_id=s.st_id")
data=conn.execute("SELECT f.st_id,s.st_name,f.fees_amount FROM fees as f inner join st as s on f.st_id=s.st_id")
for a in data:
    # print(a[0])
    # print(a[0],a[1])
    # print(a[0],a[1],a[2])
    print(a)
conn.close()