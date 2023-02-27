# came 
# -------------------------------------
1/0
# Traceback (most recent call last):
# File "div.py", line 2, in 
# value /= 0
# ZeroDivisionError: division by zero
# -------------------------------------

my_list = []
x = my_list[0]

# Traceback (most recent call last):
# File "lst.py", line 2, in 
# x = list[0]
# IndexError: list index out of range

# -------------------------------------

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if second_number != 0:
    print(first_number / second_number)
else:
    print("This operation cannot be done.")

print("THE END.")

# -------------------------------------

try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")


# 1
# Oh dear, something went wrong...
# 3
# -------------------------------------
try:
    x = int(input("Enter a number: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")

print("THE END.")

# -------------------------------------

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")


# -------------------------------------

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")


# -------------------------------------

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")

print("THE END.")

# Traceback (most recent call last):
# File "exc.py", line 3, in 
# y = 1 / x
# ZeroDivisionError: division by zero
# -------------------------------------

