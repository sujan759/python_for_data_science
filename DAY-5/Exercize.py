# time zone stamp
import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp1= time.strftime('%H')
print(timestamp1)
timestamp2=time.strftime('%M')
print(timestamp2)
timestamp3=time.strftime('%S')
print(timestamp3)
if timestamp>="12:00:00" and  timestamp<"16:00:00" :
    print("AfterNon")
if timestamp>"16:00:00" and  timestamp<"19:00:00" :
    print("evening")
if timestamp1>"19" and  timestamp1<"23" and timestamp2<'' :
    print("good night")
    