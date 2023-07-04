import datetime as mydate
#import datetime as datetimepython

date = mydate.date(2023,6,21)
print(date)
print(date.day)
#############################
time = mydate.time(21,27,36)
print(time.second)
###############################

now  = mydate.datetime.today()
print(now.hour)