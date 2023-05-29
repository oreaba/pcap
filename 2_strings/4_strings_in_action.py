# came 
# -------------------------------------
# Python's strings can be compared using the same set of operators which are in use in relation to numbers.
# it just compares code point values

# Test examples here.
print('alpha' == 'alpha')
print('alpha' != 'Alpha')

# The final relation between strings is determined 
# by comparing the first different character in both strings


#compares code point values 
print('A'>'a')  # False.  65>97? NO
print('b'>'B')  # True      98 > 66? YES

# When you compare two strings of different lengths and the shorter one is identical to the longer one's beginning, the longer string is considered greater.
print('alpha' < 'alphabet')     # True 
print('beta' > 'Beta')          # True 
print('ali ibrahim' > 'ali')    # True 


# compares code point values of first different character in both strings
print('blpha' < 'alphabet') # False     98 (b) < 97 (a) ?? No
# 
print('mohamed' > 'mohmed')  # False is a (97) (4th character) > m (109) (4th character) ? no
# -------------------------------------
# Comparing strings
# Test examples here.
print('10' == '010')        # False     strings do not match
print('10' > '010')         # True      1 (49) is greater that 0 (48)
print('10' > '8')           # False     1 (49) is not greater than 8 (56)
print('20' < '8')           # True      2 (50) is less than 8 (56)
print('20' < '80')          # True      2 (50) is less than 8 (56)


# string == number is always False;
# string != number  is always True;
# string >= number always raises an exception

print('10' == 10)       # False
print('10' != 10)       # True
print('10' == 1)        # False
print('10' != 1)        # True
print('10' > 10)        # TypeError: '>' not supported between instances of 'str' and 'int'

# -------------------------------------
# Sorting
# Demonstrating the sorted() function:
# a function named sorted(), creating a new, sorted list;
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek) # The original list - first_greek- remains untouched

print(first_greek)
print(first_greek_2)

print()

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

# a method named sort(), which sorts the list in situ
second_greek.sort() # updates the current list
print(second_greek)


# -------------------------------------

itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)    # 13 1.3


si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)        # 14.3


ord('u')      # 117  
int('u')      # ValueError: invalid literal for int() with base 10: 'u'
float('a')    # ValueError

# -------------------------------------

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)         # sorts the words based on the code point of the first character [ascending order]
print(s3)               # ['Where', 'are', 'of', 'snows', 'the', 'yesteryear?']
print(s3[1])            # are  because 'W' is 65 and 'a' 97 - sorting numbers in ascending order

print(s2)
print(s3)
print('a' > 'W')        # True ... so all upper case come first before lower cases
# -------------------------------------
# s1 = '12.5'
s1 = '12'
i = int(s1)     # ValueError for s1=12.5 --- expects int 
s2 = str(i)
f = float(s2)
print(s1 == s2)
print(f)
# -------------------------------------
# extra:
my_string = 'datadrivenscience'
for i in range(my_string):      # TypeError: 'str' object cannot be interpreted as an integer
     print(i)