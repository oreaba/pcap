# came 
# -------------------------------------
from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# We must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))
# -------------------------------------
assert 0
assert ''
assert False
assert None

# all the above raises AssertionError exception
# -------------------------------------
# except:  is the same as  ====>  except BaseException:
# -------------------------------------

# IndexError
# Location: BaseException ← Exception ← LookupError ← IndexError
# -------------------------------------

# LookupError
# Location: BaseException ← Exception ← LookupError
# -------------------------------------

# ArithmeticError
# Location: BaseException ← Exception ← ArithmeticError
# -------------------------------------

# AssertionError
# Location: BaseException ← Exception ← AssertionError

# -------------------------------------
# This code cannot be terminated !!! hahahaha
# by pressing Ctrl-C.

from time import sleep

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")


# -------------------------------------
# KeyboardInterrupt
# Location: BaseException ← KeyboardInterrupt

# Description: a concrete exception raised when the user uses a keyboard shortcut designed to terminate a program's execution (Ctrl-C in most OSs); if handling this exception doesn't lead to program termination, the program continues its execution.

# Note: this exception is not derived from the Exception class. Run the program in IDLE.
# -------------------------------------

# LookupError
# Location: BaseException ← Exception ← LookupError

# Description: an abstract exception including all exceptions caused by errors resulting from invalid references to different collections (lists, dictionaries, tuples, etc.)
# -------------------------------------

# MemoryError
# Location: BaseException ← Exception ← MemoryError

# Description: a concrete exception raised when an operation cannot be completed due to a lack of free memory.
# -------------------------------------


# -------------------------------------

# This code causes the MemoryError exception.
# Warning: executing this code may affect your OS.
# Don't run it in production environments!

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')


# -------------------------------------
# OverflowError
# Location: BaseException ← Exception ← ArithmeticError ← OverflowError

# Description: a concrete exception raised when an operation produces a number too big to be successfully stored
# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...

# from math import exp

# ex = 1

# try:
#     while True:
#         print(exp(ex))
#         ex *= 2
# except OverflowError:
#     print('The number is too big.')


# -------------------------------------
ImportError
# Location: BaseException ← Exception ← StandardError ← ImportError

# Description: a concrete exception raised when an import operation fails

# One of these imports will fail - which one?

# try:
#     import math
#     import time
#     import abracadabra

# except:
#     print('One of your imports has failed.')



# -------------------------------------

# KeyError
# Location: BaseException ← Exception ← LookupError ← KeyError

# Description: a concrete exception raised when you try to access a collection's non-existent element (e.g., a dictionary's element)
# How to abuse the dictionary
# and how to deal with it?

# dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
# ch = 'a'

# try:
#     while True:
#         ch = dictionary[ch]
#         print(ch)
# except KeyError:
#     print('No such key:', ch)

# https://docs.python.org/3.6/library/exceptions.html
# -------------------------------------
# save general exceptions here


# save concrete (special) exceptions here

