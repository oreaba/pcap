# came 
# -------------------------------------
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("THE END.")
# -------------------------------------
try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")

print("THE END.")
# -------------------------------------
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")
# Zero division!
# THE END.

# -------------------------------------
try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")
# Arithmetic problem!
# THE END.


# -------------------------------------
def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")

# Arithmetic problem!
# THE END.
# -------------------------------------

def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")

# What happened? An exception was raised!
# THE END.
# -------------------------------------
# The raise instruction raises the specified exception named exc as if it was raised in a normal (natural) way:

# -------------------------------------

def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")

# What happened? An error?
# THE END
# In this way, you can test your exception handling routine without forcing the code to do stupid things.

# -------------------------------------


def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        # raise

try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

# output:
# I did it again!
# ArithmeticError will not be caught


# 
# -------------------------------------
def bad_fun(n):
    try:
        #raise           # RuntimeError: No active exception to reraise
        return n / 0
        
    except:
        print("I did it again!")
        raise       # raise whatever the exception that has occurred - so this will raise division by zero exception

try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

# output:
# I did it again!
# I see!
# ArithmeticError will be caught
# -------------------------------------
import math

x = float(input("Enter a number: "))
assert x >= 0.0             # assert = all is good if

x = math.sqrt(x)

print(x)

# -1
# Traceback (most recent call last):
#   File "main.py", line 4, in <module>
#     assert x >= 0.0
# AssertionError

# -------------------------------------
try:
    pass
    # Risky code.
except IndexError:
    pass
    # Taking care of mistreated lists
except LookupError:
    pass
    # Dealing with other erroneous lookups
# -------------------------------------
try:
    pass
    # Risky code.
except LookupError:
    pass
    # Dealing with erroneous lookups
except IndexError:
    pass
    # You'll never get here 
# -------------------------------------
# 4. The Python statement assert expression evaluates the expression and raises the AssertError exception 
# when the expression is equal to zero, an empty string, or None. 

# assert raises exception when the expression is evaluated to 
False
0
''
None
# You can use it to protect some critical parts of your code from devastating data.
# -------------------------------------


# all the above raises AssertionError exception
# -------------------------------------
def foo(x):
    assert x        # make sure x is not 0 or false, or '' or none
    return 1/x


try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")

# some
# -------------------------------------
# try:
#     raise Exception
# except:
#     print('c')
# except BaseException:       # A named except clause cannot appear after catch-all except clausePylance
#     print('a')
# except Exception:
#     print('b')

    # output:
    # SyntaxError: default 'except:' must be last
# -------------------------------------
