# did not come

# Introduction to the calendar module
# In addition to the datetime and time modules, the Python standard library provides a module called calendar which, as the name suggests, offers calendar-related functions.

# Day of the week	Integer value	Constant
# Monday	0	calendar.MONDAY
# Tuesday	1	calendar.TUESDAY
# Wednesday	2	calendar.WEDNESDAY
# Thursday	3	calendar.THURSDAY
# Friday	4	calendar.FRIDAY
# Saturday	5	calendar.SATURDAY
# Sunday	6	calendar.SUNDAY

# -------------------------------------
import calendar
print(calendar.calendar(2020))
calendar.prcal(2023)        # same

# The result displayed is similar to the result of the cal command available in Unix. 
# If you want to change the default calendar formatting, you can use the following parameters:

# w – date column width (default 2)
# l – number of lines per week (default 1)
# c – number of spaces between month columns (default 6)
# m – number of columns (default 3)
#------------------------------------


#------------------------------------
# Calendar for a specific month
# The example displays the calendar for November 2020. As in the calendar function, you can change the default formatting using the following parameters:

# w – date column width (default 2)
# l – number of lines per week (default 1)

import calendar
print(calendar.month(2020, 11))
calendar.prmonth(2023, 2)
#   November 2020
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30
# Note: You can also use the prmonth function, which has the same parameters as the month function, but doesn't require you to use the print function to display the calendar.


#------------------------------------

# The setfirstweekday() function

import calendar

calendar.setfirstweekday(calendar.SATURDAY)
calendar.prmonth(2020, 12)
#    December 2020
# Su Mo Tu We Th Fr Sa
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31

#------------------------------------
# The weekday() function

import calendar
print(calendar.weekday(2020, 12, 24))
# output
# 3

#------------------------------------
# The weekheader() function
# You've probably noticed that the calendar contains weekly headers in a shortened form. 
# If needed, you can get short weekday names using the weekheader method.

# The weekheader method requires you to specify the width in characters for one day of the week. 
# If the width you provide is greater than 3, 
# you'll still get the abbreviated weekday names consisting of three characters.

# So let's look at how to get a smaller header. Run the code in the editor.

# Result:

# Mo Tu We Th Fr Sa Su

import calendar
print(calendar.weekheader(2))   # the width in characters for one day of the week.

# Note: If you change the first day of the week, 
# e.g., using the setfirstweekday function, it'll affect the result of the weekheader function.


#------------------------------------
# How do we check if a year is a leap year?

import calendar

print(calendar.isleap(2024))
print(calendar.leapdays(2010, 2021))  # in the period from 2010 to 2020 there are only three leap years (note: 2021 is not included). They are the years 2012, 2016, and 2020.

# True
# 3

#------------------------------------
# Classes for creating calendars
# The presented functions aren't everything the calendar module offers. In addition to them, we can use the following classes:

# calendar.Calendar – provides methods to prepare calendar data for formatting;
# calendar.TextCalendar – is used to create regular text calendars;
# calendar.HTMLCalendar – is used to create HTML calendars;
# calendar.LocalTextCalendar – is a subclass of the calendar.TextCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.
# calendar.LocalHTMLCalendar – is a subclass of the calendar.HTMLCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.
# During this course, you've already had the opportunity to create text calendars when discussing the functions of the calendar module
#------------------------------------

# Creating a Calendar object

import calendar  

c = calendar.Calendar(calendar.SUNDAY)  # The firstweekday parameter must be an integer between 0-6.

for weekday in c.iterweekdays():
    print(weekday, end=" ")             # 6 0 1 2 3 4 5


#  result:

# 6 0 1 2 3 4 5

#------------------------------------
# The itermonthdates() method

import calendar  

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")

# result
# 2019-10-28 2019-10-29 2019-10-30 2019-10-31 2019-11-01 2019-11-02 2019-11-03 2019-11-04 2019-11-05 2019-11-06 2019-11-07 2019-11-08 2019-11-09 2019-11-10 2019-11-11 2019-11-12 2019-11-13 2019-11-14 2019-11-15 2019-11-16 2019-11-17 2019-11-18 2019-11-19 2019-11-20 2019-11-21 2019-11-22 2019-11-23 2019-11-24 2019-11-25 2019-11-26 2019-11-27 2019-11-28 2019-11-29 2019-11-30 2019-12-01 

#------------------------------------
# Other methods that return iterators

import calendar  

c = calendar.Calendar()

for iter in c.itermonthdays(2023,2):
    print(iter)

# 0 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 0 

#------------------------------------
# https://docs.python.org/3/library/calendar.html

# The monthdays2calendar() method
    
import calendar  

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)

#------------------------------------
# Key takeaways
# 1. In the calendar module, the days of the week are displayed from Monday to Sunday. 
# Each day of the week has its representation in the form of an integer, 
# where the first day of the week (Monday) is represented by the value 0, 
# while the last day of the week (Sunday) is represented by the value 6.
#------------------------------------


# 2. To display a calendar for any year, 
# call the calendar function with the year passed as its argument, 
# e.g.:

import calendar
print(calendar.calendar(2020))


# Note: A good alternative to the above function is the function called prcal, which also takes the same parameters as the calendar function, but doesn't require the use of the print function to display the calendar.

#------------------------------------

# 3. To display a calendar for any month of the year, call the month function, passing year and month to it. For example:

import calendar
print(calendar.month(2020, 9))


# Note: You can also use the prmonth function, which has the same parameters as the month function, but doesn't require the use of the print function to display the calendar.
#------------------------------------


# 4. The setfirstweekday function allows you to change the first day of the week. It takes a value from 0 to 6, where 0 is Sunday and 6 is Saturday.
#------------------------------------


# 5. The result of the weekday function is a day of the week as an integer value for a given year, month, and day:

import calendar
print(calendar.weekday(2020, 9, 29)) # This displays 1, which means Tuesday.

#------------------------------------


# 6. The weekheader function returns the weekday names in a shortened form. The weekheader method requires you to specify the width in characters for one day of the week. If the width you provide is greater than 3, you'll still get the abbreviated weekday names consisting of only three characters. For example:

import calendar
print(calendar.weekheader(2)) # This display: Mo Tu We Th Fr Sa Su

#------------------------------------


# 7. A very useful function available in the calendar module is the function called isleap, which, as the name suggests, allows you to check whether the year is a leap year or not:

import calendar
print(calendar.isleap(2020)) # This displays: True

#------------------------------------


# 8. You can create a calendar object yourself using the Calendar class, 
# which, when creating its object, allows you to change the first day 
# of the week with the optional firstweekday parameter, e.g.:

import calendar  

c = calendar.Calendar(2)

for weekday in c.iterweekdays():
    print(weekday, end=" ")
# Result: 2 3 4 5 6 0 1


# The iterweekdays returns an iterator for weekday numbers. 
# The first value returned is always equal to the value of the firstweekday property.

#------------------------------------

# Exercise 1

# What is the output of the following snippet?

import calendar
print(calendar.weekheader(1))


# Check
# M T W T F S S


# Exercise 2

# What is the output of the following snippet?

import calendar  

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ")


# Check
# 0 1 2 3 4 5 6



