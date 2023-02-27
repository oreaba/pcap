# did not come

# Introduction to the datetime module

# Getting the current local date and creating date objects

# -------------------------------------
from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# The today method returns a date object representing the current local date. 
# Note that the date object has three attributes: year, month, and day.


#------------------------------------

from datetime import date

my_date = date(2019, 11, 4)
print(my_date)
# 2019-11-04

#------------------------------------
# When creating a date object, keep the following restrictions in mind:

# Parameter	Restrictions
# year	
# The year parameter must be greater than or equal to 1 (MINYEAR constant) 
# nd less than or equal to 9999 (MAXYEAR constant).

# month	
# The month parameter must be greater than or equal to 1 and less than or equal to 12.

# day	
# The day parameter must be greater than or equal to 1 and less than or equal 
# to the last day of the given month and year.
#------------------------------------

# Creating a date object from a timestamp

# The date class gives us the ability to create a date object from a timestamp.

# In Unix, the timestamp expresses the number of seconds since January 1, 1970, 00:00:00 (UTC).
#  This date is called the Unix epoch, because this is when the counting of time began on Unix systems.

# The timestamp is actually the difference between a particular date 
# (including time) and January 1, 1970, 00:00:00 (UTC), expressed in seconds.


from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

# Timestamp: 1677394690.9115312
# Date: 2023-02-26

# If you run the sample code several times, you'll be able to see how the timestamp increments itself. 
# It's worth adding that the result of the time function depends on the platform, 
# because in Unix and Windows systems, leap seconds aren't counted.
#------------------------------------

# Creating a date object using the ISO format

# The datetime module provides several methods to create a date object. One of them is the fromisoformat method, which takes a date in the YYYY-MM-DD format compliant with the ISO 8601 standard.


from datetime import date

d = date.fromisoformat('2019-11-04')
print(d)

# 2019-11-04
# In our example, YYYY is 2019, MM is 11 (November), and DD is 04 (fourth day of November).
# Note: The fromisoformat method has been available in Python since version 3.7.



#------------------------------------
# The replace() method

from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

# Result:

# 1991-02-05
# 1992-01-16

#------------------------------------
# What day of the week is it?

from datetime import date

d = date(2019, 11, 4)
print(d.weekday())          # from 0 to 6

# Result:
# 0

# 0 is Monday and 6 is Sunday

#------------------------------------
# The date class has a similar method called isoweekday, 
# which also returns the day of the week as an integer, but 1 is Monday, and 7 is Sunday:
from datetime import date

d = date(2019, 11, 4)
print(d.isoweekday())           # from 1 to 7

# Result:
# 1
# 1 is Monday, and 7 is Sunday:


#------------------------------------
# Creating time objects
# time(hour, minute, second, microsecond, tzinfo, fold)


from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)

# Time: 14:53:20.000001
# Hour: 14
# Minute: 53
# Second: 20
# Microsecond: 1

# The time class constructor accepts the following optional parameters:
# Parameter	Restrictions
# hour	
# The hour parameter must be greater than or equal to 0 and less than 23.

# minute	
# The minute parameter must be greater than or equal to 0 and less than 59.

# second	
# The second parameter must be greater than or equal to 0 and less than 59.

# microsecond	
# The microsecond parameter must be greater than or equal to 0 and less than 1000000.

# tzinfo	
# The tzinfo parameter must be a tzinfo subclass object or None (default).

# fold	
# The fold parameter must be 0 or 1 (default 0).



#------------------------------------
# The time module

import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(.5)

# Extend the student's sleep by changing the number of seconds. Note that the sleep function accepts only an integer or a floating point number.


#------------------------------------
# The ctime() function

# The time module provides a function called ctime, which converts the time in seconds since January 1, 1970 (Unix epoch) to a string.


import time

timestamp = 1572879180
print(time.ctime(timestamp))    
# Mon Nov  4 14:53:00 2019


print(time.ctime())             
print(time.ctime(time.time()))  

# Tue Feb 21 18:54:18 2023 # the same as print(time.ctime(time.time())) 
# Tue Feb 21 18:54:18 2023

# The example shows two functions that convert the elapsed time from the Unix epoch 
# to the struct_time object. The difference between them is that the gmtime function 
# returns the struct_time object in UTC, while the localtime function returns local time. 
# For the gmtime function, the tm_isdst attribute is always 0.


#------------------------------------
# The gmtime() and localtime() functions

import time

timestamp = time.time()
print(time.gmtime(timestamp))
print(time.localtime(timestamp))


# time.struct_time:
#     tm_year   # specifies the year
#     tm_mon    # specifies the month (value from 1 to 12)
#     tm_mday   # specifies the day of the month (value from 1 to 31)
#     tm_hour   # specifies the hour (value from 0 to 23)
#     tm_min    # specifies the minute (value from 0 to 59)
#     tm_sec    # specifies the second (value from 0 to 61 )
#     tm_wday   # specifies the weekday (value from 0 to 6)
#     tm_yday   # specifies the year day (value from 1 to 366)
#     tm_isdst  # specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
#     tm_zone   # specifies the timezone name (value in an abbreviated form)
#     tm_gmtoff # specifies the offset east of UTC (value in seconds)

# result
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)

#------------------------------------
import time

timestamp = 1572879180
st = time.gmtime(timestamp)     
# return time struct

print(time.asctime(st))

print(time.asctime())
print(time.ctime())

print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

# Result:

# Mon Nov  4 14:53:00 2019
# 1572879180.0

#------------------------------------

# Creating datetime objects

from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())

# Datetime: 2019-11-04 14:53:00
# Date: 2019-11-04
# Time: 14:53:00
#------------------------------------
# Methods that return the current date and time

# today() — returns the current local date and time with the tzinfo attribute set to None;
# now() — returns the current local date and time the same as the today method, unless we pass the optional argument tz to it. The argument of this method must be an object of the tzinfo subclass;
# utcnow() — returns the current UTC date and time with the tzinfo attribute set to None.

from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())

# today: 2023-02-26 07:23:49.236598
# now: 2023-02-26 07:23:49.236893
# utcnow: 2023-02-26 07:23:49.237082

# today() — returns the current local date and time with the tzinfo attribute set to None;
# now() — returns the current local date and time the same as the today method, unless we pass the optional argument tz to it. The argument of this method must be an object of the tzinfo subclass;
# utcnow() — returns the current UTC date and time with the tzinfo attribute set to None
#------------------------------------
# Getting a timestamp
# The timestamp method returns a float value expressing the number of seconds elapsed between the date and time indicated by the datetime object and January 1, 1970, 00:00:00 (UTC).

from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())
print(datetime.now().timestamp())
# Result:

# Timestamp: 1601823300.0

#------------------------------------
# Date and time formatting (part 1)

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

# All datetime module classes presented so far have a method called strftime. This is a very important method, because it allows us to return the date and time in the format we specify.

# The strftime method takes only one argument in the form of a string specifying the format that can consist of directives.

# A directive is a string consisting of the character % (percent) and a lowercase or uppercase letter, e.g., the directive %Y means the year with the century as a decimal number. Let's see it in an example. Run the code in the editor.


from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

# Result:

# 2020/01/04

# %Y – returns the year with the century as a decimal number. In our example, this is 2020.
# %m – returns the month as a zero-padded decimal number. In our example, it's 01.
# %d – returns the day as a zero-padded decimal number. In our example, it's 04.

#------------------------------------

# Date and time formatting (part 2)

from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%Y/%B/%d %H:%M:%S"))

# Result:

# 14:53:00
# 20/November/04 14:53:00

#------------------------------------

# The strftime() function in the time module
# You probably won't be surprised to learn that the strftime function is available in the time module. 
# It differs slightly from the strftime methods in the classes provided by the datetime module because, 
# in addition to the format argument, it can also take (optionally) a tuple or struct_time object.


# If you don't pass a tuple or struct_time object, the formatting will be done using the current local time. 
# Take a look at the example in the editor.
# https://docs.python.org/3/library/time.html#time.strftime
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# 2019/11/04 14:53:00
# 2020/10/12 12:19:40

#------------------------------------
# The strptime() method

# strptime creates a datetime object from a string representing a date and time.
# The strptime method requires you to specify the format in which you saved the date and time. 
# Let's see it in an example. Take a look at the code in the editor.


from datetime import datetime
dt = datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")
print(dt)
print(type(dt))
# output
# 2019-11-04 14:53:00

#------------------------------------
import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

# Result:
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)
#------------------------------------
# Date and time operations

# Sooner or later you'll have to perform some calculations on the date and time. 
# Fortunately, there's a class called timedelta in the datetime module that was created 
# for just such a purpose.
# To create a timedelta object, just do subtraction on the date or datetime objects, 
# just like we did in the example in the editor. Run it.


from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

# Result:

# 366 days, 0:00:00
# 365 days, 9:07:00

#------------------------------------
# Creating timedelta objects

# You've already learned that a timedelta object can be returned as a result of subtracting two date or datetime objects.
# Of course, you can also create an object yourself. For this purpose, let's get acquainted with the arguments accepted by the class constructor, which are: days, seconds, microseconds, milliseconds, minutes, hours, and weeks. Each of them is optional and defaults to 0.

from datetime import timedelta
delta = timedelta(weeks=2, days=2, hours=3)
print(delta)

# Result:

# 16 days, 3:00:00

from datetime import timedelta
delta = timedelta(weeks=0, days=0, hours=3)
print(delta)
#------------------------------------
# The result of 10800 is obtained by converting 3 hours into seconds. In this way the timedelta object stores the arguments passed during its creation. Weeks are converted to days, hours and minutes to seconds, and milliseconds to microseconds.


from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

#Result:
# Days: 16
# Seconds: 10800
# Microseconds: 0
# The result of 10800 is obtained by converting 3 hours into seconds. In this way the timedelta object stores the arguments passed during its creation. Weeks are converted to days, hours and minutes to seconds, and milliseconds to microseconds.
#------------------------------------

# Creating timedelta objects: continued

from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)

# Result:

# 16 days, 2:00:00
# 32 days, 4:00:00
# 2019-11-05
# 2019-11-05 18:53:00

# The timedelta object can be multiplied by an integer. In our example, we multiply the object representing 16 days and 2 hours by 2. As a result, we receive a timedelta object representing 32 days and 4 hours.

# Note that both days and hours have been multiplied by 2. Another interesting operation using the timedelta object is adding. In the example, we've added the timedelta object to the date and datetime objects.

# As a result of these operations, we receive date and datetime objects increased by days and hours stored in the timedelta object.

# The presented multiplication operation allows you to quickly increase the value of the timedelta object, while multiplication can also help you get a date from the future.

# Of course, the timedelta, date, and datetime classes support many more operations. We encourage you to familiarize yourself with them in the documentation.


#------------------------------------
# 1. To create a date object, you must pass the year, month, and day arguments as follows:

# from datetime import date

# my_date = date(2020, 9, 29)
# print("Year:", my_date.year) # Year: 2020
# print("Month:", my_date.month) # Month: 9
# print("Day:", my_date.day) # Day: 29

# The date object has three (read-only) attributes: year, month, and day.

# 2. The today method returns a date object representing the current local date:

# from datetime import date
# print("Today:", date.today()) # Displays: Today: 2020-09-29

#------------------------------------
# 3. In Unix, the timestamp expresses the number of seconds 
# since January 1, 1970, 00:00:00 (UTC). This date is called the "Unix epoch", 
# because it began the counting of time on Unix systems. 
# The timestamp is actually the difference between a particular 
# date (including time) and January 1, 1970, 00:00:00 (UTC), expressed in seconds. 
# To create a date object from a timestamp, we must pass a Unix timestamp to the fromtimestamp method:

# from datetime import date
# import time

# timestamp = time.time()
# d = date.fromtimestamp(timestamp)


# Note: The time function returns the number of seconds 
# from January 1, 1970 to the current moment in the form of a float number.


#------------------------------------

# 4. The constructor of the time class accepts six arguments 
# (hour, minute, second, microsecond, tzinfo, and fold). 
# Each of these arguments is optional.

# from datetime import time

# t = time(13, 22, 20)

# print("Hour:", t.hour) # Hour: 13
# print("Minute:", t.minute) # Minute: 22
# print("Second:", t.second) # Second: 20

#------------------------------------
# 5. The time module contains the sleep function, which suspends program execution for a given number of seconds, e.g.:

# import time

# time.sleep(10)
# print("Hello world!") # This text will be displayed after 10 seconds.

#------------------------------------
# 6. In the datetime module, date and time can be represented either as separate objects, or as one object. The class that combines date and time is called datetime. All arguments passed to the constructor go to read-only class attributes. They are year, month, day, hour, minute, second, microsecond, tzinfo, and fold:

# from datetime import datetime

# dt = datetime(2020, 9, 29, 13, 51)
# print("Datetime:", dt) # Displays: Datetime: 2020-09-29 13:51:00


#------------------------------------
# 7. The strftime method takes only one argument in the form of a string specifying a format that can consist of directives. A directive is a string consisting of the character % (percent) and a lower-case or upper-case letter. Below are some useful directives:

# %Y – returns the year with the century as a decimal number;
# %m – returns the month as a zero-padded decimal number;
# %d – returns the day as a zero-padded decimal number;
# %H – returns the hour as a zero-padded decimal number;
# %M – returns the minute as a zero-padded decimal number;
# %S – returns the second as a zero-padded decimal number.

from datetime import date

d = date(2020, 9, 29)
print(d.strftime('%Y/%m/%d')) # Displays: 2020/09/29

#------------------------------------

#------------------------------------
# 8. It's possible to perform calculations on date and datetime objects, e.g.:

from datetime import date

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

d = d1 - d2
print(d) # Displays: 366 days, 0:00:00.
print(d * 2) # Displays: 732 days, 0:00:00.


# The result of the subtraction is returned as a timedelta object that expresses the difference in days between the two dates in the example above.

# Note that the difference in hours, minutes, and seconds is also displayed. The timedelta object can be used for further calculations (e.g. you can multiply it by 2).


# -------------------------------------
# Exercise 1

# What is the output of the following snippet?

from datetime import time

t = time(14, 53)
print(t.strftime("%H:%M:%S"))


# Check
# 14:53:00
# -------------------------------------
# Exercise 2

# What is the output of the following snippet?

from datetime import datetime

dt1 = datetime(2020, 9, 29, 14, 41, 0)
dt2 = datetime(2020, 9, 28, 14, 41, 0)

print(dt1 - dt2)


# Check
# 1 day, 0:00:00
