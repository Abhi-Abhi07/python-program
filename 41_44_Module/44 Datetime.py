import datetime

print(datetime.datetime.now())

# print(datetime.datetime(2022,12,22))


now=datetime.datetime.now()
year=now.strftime("%Y")
print("Year : ",year)

print("Year : ",now.strftime("%y"))
print("Month : ",now.strftime("%B"))
print("Month : ",now.strftime("%b"))
print("Month : ",now.strftime("%m"))
print("Minute : ",now.strftime("%M"))
print("Hour(0-23) : ",now.strftime("%H"))
print("Year(0-12) : ",now.strftime("%I"))
print("Am/Pm : ",now.strftime("%p"))


