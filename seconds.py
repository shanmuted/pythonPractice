'''from datetime import datetime,timedelta
sec=timedelta(seconds=int(input("enter sec")))
print(sec)'''
time = float(input("Input time in seconds: "))
day = round(time // (24 * 3600))
time =round(time % (24 * 3600))
hour = time // 3600
time =round(time%3600)
minutes = time // 60
time=round(time%60)
seconds = time
print(day ,hour,minutes,seconds)