# came

# Example 1

word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 3

i_am = 'I\'m'
print(len(i_am))

# -------------------------------------
multiline = '''Line #1
Line #2'''

print(len(multiline))

# -------------------------------------
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# -------------------------------------
# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))  # 97
print(ord(char_2))  # 32


print(ord('B'))  # 66

# -------------------------------------
# Demonstrating the chr() function.

# Demonstrating the chr() function.

print(chr(97))
print(chr(945))

x='a'
print(chr(ord(x)) == x)

x=97
print(ord(chr(x)) == x)



# -------------------------------------
# Indexing strings.

the_string = 'silly walking'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

print(the_string[-2])

# -------------------------------------
# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()


# -------------------------------------
# Slices

alpha = "abcdefg"

# second index is not included.
print(alpha[1:3])   # bc 
print(alpha[3:])    # defg
print(alpha[:3])    # abc
print(alpha[3:-2])  # de
print(alpha[-3:4])  #  ''   both indeices refer to the same number
print(alpha[4:-3])  #  ''   both indeices refer to the same number
print(alpha[-3:])   # efg
print(alpha[:-5])   # ab
print(alpha[-5:])   # cdefg
print(alpha[:2])    # ab
print(alpha[::2])   # aceg
print(alpha[::3])   # adg
print(alpha[1:5:2]) # bd
print(alpha[0:-1:1])# abcdef
print(alpha[0:6:1]) # abcdef
print(alpha[0:7:1]) # abcdefg
print(alpha[1::2])  # bdf
print(alpha[::-1])  # gfedcba

# -------------------------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)


# -------------------------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)


# -------------------------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"

del alphabet[0] # TypeError: 'str' object doesn't support item deletion
# -------------------------------------
# Python strings don't have the append() method - you cannot expand them in any way.

# The example below is erroneous:
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.append("A")    # AttributeError: 'str' object has no attribute 'append'

# with the absence of the append() method, the insert() method is illegal, too:

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.insert(0, "A")     # AttributeError: 'str' object has no attribute 'insert'
# -------------------------------------
alphabet = "bcdefghijklmnopqrstuvwxy"
print(id(alphabet))     # address of the object
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet)
print(id(alphabet))     # address of the object
# You may want to ask if creating a new copy of a string each time you modify its contents worsens the effectiveness of the code.
# Yes, it does. A bit. It's not a problem at all, though.
# -------------------------------------

# Demonstrating min() - Example 1:
# min('') # ValueError
print(min("aAbByYzZ"))          # A  which is 65

print(min('Aa'))                # A  which is 65
print(min('aA'))                # A  which is 65
print(min('aZ'))                # Z which is 90
print(min('zkjdfhjdksfb'))      # b


# # Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')       # [ ]       space which is 32

t = [0, 1, 2]
print(min(t))           # 0

# -------------------------------------
# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))          # z which is 122


# Demonstrating max() - Examples 2 & 3:
print(max('aboewfbX'))          # w which is 119

t = 'The Knights Who Say "Ni!"' 
print('[' + max(t) + ']')       # y which is 121

t = [0, 1, 2]
print(max(t))       # 2

# -------------------------------------
# The index() method (it's a method, not a function)
# searches the sequence from the beginning, in order to find the first element of the value specified in its argument.
# its absence will cause a ValueError exception.
# Demonstrating the index() method:
print("aAbByYzZaA".index("y"))      # 4
print("aAbByYzZaA".index("Z"))      # 7
print("aAbByYzZaA".index("A"))      # 1
print("aAbByYzZaA".index("!"))      # ValueError: substring not found

print("aAbByYzZaA".rindex("A"))    # 9  scans from right to left


# -------------------------------------
# Demonstrating the list() function:
print(list("abcabc"))       # ['a', 'b', 'c', 'a', 'b', 'c']

# Demonstrating the count() method:
print("abcabc".count("b"))      # 2
print('abcabc'.count("d"))      # 0

# -------------------------------------
print(len("\n\n"))              # 2
# -------------------------------------
asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)
# -------------------------------------

# note
# chr(ord(character)) == character
# ord(chr(codepoint)) == codepoint

# -------------------------------------
s = 'yesteryears'
print (s[3:6])              # ter
the_list = list(s)
print(the_list[3:6])        # ['t', 'e', 'r']
# -------------------------------------
for ch in "abc":
    print(chr(ord(ch) + 1), end='')     # bcd
# -------------------------------------

