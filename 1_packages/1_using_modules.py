# came 
import math
print(math.sin(math.pi/2))
# -------------------------------------
# Now we're going to show you how the two namespaces (yours and the module's one) can coexist.


import math


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

# -------------------------------------
from math import sin, pi

print(sin(pi/2))
# -------------------------------------
# Here, we've reversed the sequence of the code's operations:


pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))
# -------------------------------------

# from module import *
#
# -------------------------------------
# import module as alias
# -------------------------------------
# from module import n as a, m as b, o as c

# -------------------------------------
# from math import pi as PI, sin as sine
# -------------------------------------
# print(sine(PI/2))
# -------------------------------------
# from mint import make_money
# make_money()
# -------------------------------------
# sample solution
# from mint import make_money as make_more_money


# -------------------------------------