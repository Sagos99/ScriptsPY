from datetime import datetime,timedelta,time

mili = 3440*1000

delta = timedelta(microseconds=mili)

print(str(delta)[:7])