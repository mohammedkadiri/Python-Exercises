import datetime



d = datetime.date.today()
print(d.weekday())

# Time deltas the difference between dates and time

tdelta = datetime.timedelta(days=7) #Duration of 7 days

print(d + tdelta)

# date2 = date1 + timedelta
#timedelta = date1 + date2

# bday = datetime.date(2019, 7, 5)
#
# till_bday = bday - d
# print(till_bday)


# Working with time
# t = datetime.time(9, 30, 45, 10000)
#  print(t.hour)

# t = datetime.datetime(2016, 7, 26, 12, 30, 45, 10000)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today) # Returns the local current date with a date time of none
print(dt_now)   # Gives us the option to pass the time
print(dt_utcnow)