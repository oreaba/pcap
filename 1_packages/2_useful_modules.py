# came 
# -------------------------------------
#returns an alphabetically sorted list
# dir(module)

import math

for name in dir(math):
    print(name, end="\t")



# -------------------------------------
import math
dir(math)
# -------------------------------------


from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

# -------------------------------------
from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))


# -------------------------------------
from math import ceil, floor, trunc

x = 1.4
y = 2.6

# floor = nearest smallest integer
print(floor(x), floor(y))       # 1 2   
print(floor(-x), floor(-y))     # -2 -3

# ceil = nearest greatest integer
print(ceil(x), ceil(y))         # 2 3
print(ceil(-x), ceil(-y))       # -1 -2

# trunc = remove the fraction
print(trunc(x), trunc(y))       # 1 2
print(trunc(-x), trunc(-y))     # -1 -2

# -------------------------------------
import math
result = math.e == math.exp(1)
# True
# -------------------------------------
# Selected functions from the random module
from random import random

for i in range(5):
    print(random())

# 0.8104270250232664
# 0.5161690521192961
# 0.3632855709777154
# 0.5104138715226607
# 0.9459960590667644

# -------------------------------------
# seed() - sets the seed with the current time;
# seed(int_value) - sets the seed with the integer value int_value.


# -------------------------------------
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

# 0 0 0 0

# -------------------------------------

from random import randint

for i in range(10):
    print(randint(1, 10), end=',')      # print 10 random numbers - from 1 (included) to 10 (included)

# 4,7,4,4,9,3,7,10,1,9,
for i in range(10):
    print(randrange(1, 10), end=' ')    # print 10 random numbers - from 1 (included) to 9 only (included) 
# 6 9 5 1 5 6 6 3 6 5

for i in range(10):
    print(randrange(1, 10, 1), end=' ') # print 10 random numbers - from 1 (included) to 9 only (included) 
# 3 2 4 5 9 1 8 1 6 3

for i in range(10):
    print(randrange(1, 10, 2), end=' ') # print 10 random numbers - from 1 (included) to 9 only (included) - odd numbers only [1,3,5,7,9]
# 1 3 5 5 3 7 5 3 3 9

for i in range(10):
    print(randrange(0, 10, 2), end=' ') # print 10 random numbers - from 1 (included) to 9 only (included) - even numbers only [2,4,6,8]
# 6 8 6 8 6 8 8 4 2 0
# -------------------------------------
# The choice and sample functions

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# choice = Choose a random element from a non-empty sequence.
print(choice(my_list))

# sample(list, k)
# sample = Chooses k unique random elements from a population sequence (if possible) - if not, give me 5 anyways
print(sample(my_list, 5))       # [1, 2, 8, 2, 9]
print(sample(my_list, 10))      # [4, 10, 5, 6, 2, 2, 3, 8, 7, 9]

print(sample(my_list, 20))      # ValueError: Sample larger than population or is negative
print(sample(my_list, -5))      # ValueError: Sample larger than population or is negative

# 2
# [2, 3, 7, 8, 6]
# [5, 8, 10, 7, 1, 9, 6, 3, 4, 2]

# -------------------------------------
# platform module

# -------------------------------------
from platform import platform

# human readable
print(platform())           # macOS-13.2.1-x86_64-i386-64bit
print(platform(1))          # If "aliased" is true, the function will use aliases for various platforms that report system names which differ from their common names, e.g. SunOS will be reported as Solaris.
print(platform(0, 1))       # macOS-13.2.1
print(platform(0, True))    # macOS-13.2.1

# Intel x86 + Windows ® Vista (32 bit):
# Windows-Vista-6.0.6002-SP2
# Windows-Vista-6.0.6002-SP2
# Windows-Vista

# Intel x86 + Gentoo Linux (64 bit):
# Linux-4.4.0-210-generic-x86_64-with
# Linux-4.4.0-210-generic-x86_64-with
# Linux-4.4.0-210-generic-x86_64-with

# Raspberry PI2 + Raspbian Linux (32 bit):
# inux-4.4.0-1-rpi2-armv7l-with-debian-9.0
# Linux-4.4.0-1-rpi2-armv7l-with-debian-9.0
# Linux-4.4.0-1-rpi2-armv7l-with-glibc2.9
# -------------------------------------
from platform import machine

print(machine())        # x86_64

# Intel x86 + Windows ® Vista (32 bit):

# x86
# output

# Intel x86 + Gentoo Linux (64 bit):

# x86_64
# output

# Raspberry PI2 + Raspbian Linux (32 bit):

# armv7l
# output


# -------------------------------------
from platform import processor

print(processor())      # i386
# Intel x86 + Windows ® Vista (32 bit):

# x86
# output

# Intel x86 + Gentoo Linux (64 bit):

# Intel(R) Core(TM) i3-2330M CPU @ 2.20GHz
# output

# Raspberry PI2 + Raspbian Linux (32 bit):

# armv7l
# -------------------------------------

from platform import system

print(system())     # Darwin

# Intel x86 + Windows ® Vista (32 bit):

# Windows
# output

# Intel x86 + Gentoo Linux (64 bit):

# Linux
# output

# Raspberry PI2 + Raspbian Linux (32 bit):

# Linux

# -------------------------------------

from platform import version

print(version())

# Intel x86 + Windows ® Vista (32 bit):

# 6.0.6002
# output

# Intel x86 + Gentoo Linux (64 bit):

# #1 SMP PREEMPT Fri Jul 21 22:44:37 CEST 2017
# output

# Raspberry PI2 + Raspbian Linux (32 bit):

# #1 SMP Debian 4.4.6-1+rpi14 (2016-05-05)

# -------------------------------------

from platform import python_implementation, python_version_tuple

print(python_implementation())      # CPython
print(python_version_tuple())       # ('3', '11', '0')

for atr in python_version_tuple():
    print(atr, end='')              # 3110

# python_version_tuple() → returns a three-element tuple filled with:
# the major part of Python's version;
# the minor part;
# the patch level number.
# CPython
# 3
# 7
# 7
# -------------------------------------

# All the modules:
#  https://docs.python.org/3/py-modindex.html
# -------------------------------------
# -------------------------------------
# -------------------------------------
# -------------------------------------
# -------------------------------------
# -------------------------------------
