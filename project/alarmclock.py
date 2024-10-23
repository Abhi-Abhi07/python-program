import os
import datetime
import time

day,month,year=input("Enter date (day/month/year) : ").split("-")
print(datetime.datetime.now())
hours,minn,sec=input("Enter time (hours:minn:sec) : ").split(":")
scheduleDate=datetime.date(int(year),int(month),int(day))

# print(scheduleDate)
# print(datetime.date.today())
# print(time.localtime().tm_hour)
# print(time.localtime().tm_min)
# print(time.localtime().tm_sec)

while(1):
    if(scheduleDate==datetime.date.today() and int(hours)==time.localtime().tm_hour and int(minn)==time.localtime().tm_min and int(sec)==time.localtime().tm_sec):
        os.startfile("D:\\audio.mp3")
        break

print("done")
