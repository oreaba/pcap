# came 

# Demonstrating the capitalize() method:
# capitalizes the first character only, and make the rest lower case.
print('aBcD'.capitalize())      # Abcd
print("Alpha".capitalize())     # Alpha
print('ALPHA'.capitalize())     # Alpha
print(' Alpha'.capitalize())    # [space]alpha
print('123'.capitalize())       # 123
print("αβγδ".capitalize())      # Αβγδ

# -------------------------------------

# Demonstrating the center(n) method:
# put this string in the center of n white spaces
print('[' + 'alpha'.center(10) + ']')   # [  alpha   ]
print('[' + 'alpha'.center(50) + ']')   # [                      alpha                       ]


print('[' + 'Beta'.center(2) + ']')     # [Beta]
print('[' + 'Beta'.center(4) + ']')     # [Beta]
print('[' + 'Beta'.center(6) + ']')     # [ Beta ]

# put this string in the center of n astrisks (not white spacs)
print('[' + 'gamma'.center(20, '*') + ']')  # [*******gamma********]


# -------------------------------------
# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")                # yes
else:
    print("no")

t = "zeta"
print(t.endswith("a"))          # True
print(t.endswith("A"))          # False
print(t.endswith("et"))         # False
print(t.endswith("eta"))        # True




# letters only
# Example 1: Demonstrating the isapha() method:
# interested in letters only
print("Moooo".isalpha())    # True
print('Mu40'.isalpha())     # False

# Example 2: Demonstrating the isdigit() method:
# looks at digits only
print('2018'.isdigit())     # True
print("Year2019".isdigit()) # False

# -------------------------------------

# Demonstrating the isalnum() method:
# must be either: character or digit (or combinations) ONLY
print('lambda30'.isalnum()) # True
print('lambda'.isalnum())   # True          # tricky
print('30'.isalnum())       # True
print('@'.isalnum())        # False         # special keys are not characters
print('lambda_30'.isalnum())# False         # special keys are not characters
print(''.isalnum())         # False         # empty is not characters

t = 'Six lambdas'           
print(t.isalnum())              # False     # white space is not a character

t = 'ΑβΓδ'
print(t.isalnum())              # True

t = '20E1'
print(t.isalnum())              # True
# -------------------------------------

# Example 1: Demonstrating the islower() method:
# accepts lower-case letters only
print("Moooo".islower())    # False
print('moooo'.islower())    # True

# Example 2: Demonstrating the isupper() method:
#  it concentrates on upper-case letters only.
print("Moooo".isupper())    # False
print('moooo'.isupper())    # False
print('MOOOO'.isupper())    # True

# Example 3: Demonstrating the isspace() method:
# identifies whitespaces only
print(' \n '.isspace())     # True
print(" ".isspace())        # True
print("mooo mooo mooo".isspace())   # False
# -------------------------------------
# Demonstrating the upper() method:
# Last but not least, the upper() method makes a copy of the source string,
# replaces all lower-case letters with their upper-case counterparts, 
# and returns the string as the result.
print("I know that I know nothing. Part 2.".upper()) # I KNOW THAT I KNOW NOTHING. PART 2.
# -------------------------------------
# Demonstrating the lower() method:
# makes a copy of a source string, replaces all upper-case letters with their lower-case counterparts
print("SiGmA=60".lower())       # sigma=60
# -------------------------------------
# 1. Some of the methods offered by strings are:
# Demonstrating the title() method:
# The title() method performs a somewhat similar function -
#it changes every word's first letter to upper-case, 
# turning ALL OTHER ONES to lower-case. -------> IMPORTANT
print("I know that I know nothing. Part 1.".title())    # I Know That I Know Nothing. Part 1.
# -------------------------------------

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))   #omicron,pi,rho


print("".join(["my", "name", "is", "mohammad"]))    # mynameismohammad
print(" ".join(["my", "name", "is", "mohammad"]))   # my name is mohammad

print("-".join(["my", "name", "is", "mohammad"]))   # my-name-is-mohammad
print("*.*".join(["my", "name", "is", "mohammad"])) # my*.*name*.*is*.*mohammad
print("-".join('aaaaa'))    # a-a-a-a-a

print(" ".join(["my", "name", "is", 12])) #TypeError: sequence item 3: expected str instance, int found

# -------------------------------------

# Demonstrating the replace() method:
# returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument.

print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))  # www.pythoninstitute.org
print("This is it!".replace("is", "are"))       # Thare are it!
print("Apple juice".replace("juice", ""))       # "Apple "
print(len("Apple juice".replace("juice", "")))  # prints 6 not 5

print("Apple juice".replace("", ".")) # magic! puts this substring at the start, and after each characher - .A.p.p.l.e. .j.u.i.c.e.

# 3rd arg: is the number of replacements
print("This is it!".replace("is", "are", 1))    # Thare is it!      # replace one time only
print("This is it!".replace("is", "are", 2))    # Thare are it!     # replcae two times only

# -------------------------------------


# -------------------------------------
# Demonstrating the find() method:
print("Eta".find("ta"))     # 1
print("Eta".find("mma"))    # -1        does not crash the program - ''.index('notfound') does

# it's safer than index() - 
# it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
# -------------------------------------

t = 'theta'
print(t.find('eta'))        # 2
print(t.find('et'))         # 2
print(t.find('the'))        # 0
print(t.find('ha'))         # -1 -------> because this substring is not found


# -------------------------------------
# start searching from a specific index

print('kappa'.find('a', 2))     # 4  -----> it ignores a at 1 because we start at 2
# The second argument specifies the index at which the search will be started 
# (it doesn't have to fit inside the string).
# -------------------------------------
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')          # might be used in Motadaber in Python (with highlighting found text)
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
    # The code prints the indices of all occurrences of the article the,
# 15
# 80
# 198
# 221
# 238
# -------------------------------------
# 1st arg = substring
# 2nd arg = start index (included)
# 3rd arg = end index (not-included)

print('kappa'.find('a', 1, 1))      # -1
print('kappa'.find('a', 1, 2))      # 1
print('kappa'.find('a', 2, 4))      # -1

print('kappa'.find('a', 3, 40))     # 4
# -------------------------------------

# Demonstrating the rfind() method: (search from the back - right) - find - from bottom to up
# The one-, two-, and three-parameter methods named rfind() do nearly the same things as their counterparts 
# (the ones devoid of the r prefix), but start their searches from the end of the string, not the beginning
# (hence the prefix r, for right).

print("tau tau tau".rfind("ta"))            # 8
print("tau tau tau".rfind("ta", 9))         # -1
print("tau tau tau".rfind("ta", 3, 9))      # 4


# -------------------------------------
# Demonstrating the strip() method:
# The strip() method combines the effects caused by rstrip() and lstrip() - 
# it makes a new string lacking all the leading and trailing whitespaces.
print("[" + "   aleph   ".strip() + "]")    # [aleph] # string must not start or end with space
print("alhephhhh".strip('h'))    # [alhep] # string must not start or end with h
print("mohamedhamdy".strip('mdoy')) # hamedha string must not start or end with characters 'm' 'd' 'o' 'y'
# -------------------------------------
# -------------------------------------
# Demonstrating the lstrip() method: - the input is characters not substring
# returns a newly created string formed from the original one by removing all leading whitespaces.
print("[" + " tau ".lstrip() + "]")     # [tau ] removes leading white space character from the beginning

print("www.cisco.com".lstrip("w.")) # cisco.com. #removes w or . from the leading
print("pythoninstitute.org".lstrip(".org"))  # pythoninstitute.org      because p is not . or o or r or g
# -------------------------------------

# Demonstrating the rstrip() method:
# Two variants of the rstrip() method do nearly the same as lstrips, but affect the opposite side of the string.

print("[" + " upsilon ".rstrip() + "]") # [ upsilon]
print("cisco.com".rstrip(".com"))       # cis - removes '.' or 'c' or 'o' or 'm' from the end  -- so tricky
# a string must not end with any of those characters specified in the string .com#


# Demonstrating the split() method:
#  it splits the string and builds a list of all detected substrings.
#  The method assumes that the substrings are delimited by whitespaces
#  the spaces don't take part in the operation, and aren't copied into the resulting list.
print("phi       chi\npsi".split())     # ['phi', 'chi', 'psi']         endline is considered a white space
print("mohammad".split())               # ['mohammad']                  because there are no spaces
print("ali,ahmed".split(','))           # ['ali', 'ahmed']              use , instead of space

# -------------------------------------

# Demonstrating the startswith() method:
print("omega".startswith("meg"))    # False
print("omega".startswith("om"))     # True

print("oreaba.com".endswith(".com")) # True
print("oreaba".endswith(".com"))     # False
print()

# -------------------------------------
# Demonstrating the swapcase() method:
# The swapcase() method makes a new string by swapping the case of all letters within the source string: lower-case characters become upper-case, and vice versa.
print("I know that I know nothing.".swapcase())
# i KNOW THAT i KNOW NOTHING.


# -------------------------------------
# center() – centers the string inside the field of a known length;
# count() – counts the occurrences of a given character;

# capitalize()  – changes all string letters to capitals;
# lower()       – converts all the string's letters into lower-case letters;
# upper()       – converts all the string's letter into upper-case letters.
# title()       – makes the first letter in each word upper-case;
# swapcase()    – swaps the letters' cases (lower to upper and vice versa)

# find()    – finds a substring starting from the start of the string;
# rfind()   – finds a substring starting from the end of the string;
# split()   – splits the string into a substring using a given delimiter;
# join()    – joins all items of a tuple/list into one string;
# replace() – replaces a given substring with another;
# lstrip()  – removes the white characters from the beginning of the string;
# rstrip()  – removes the trailing white spaces from the end of the string;
# strip()   – removes the leading and trailing white spaces;
# -------------------------------------
# 2. String content can be determined using the following methods (all of them return Boolean values):
# isupper() – does the string consists only of upper-case letters?
# islower() – does the string consists only of lower-case letters?
# isalnum() – does the string consist only of letters and digits?
# isalpha() – does the string consist only of letters?
# isspace() – does the string consists only of white spaces?
# startswith() – does the string begin with a given substring?
# endswith() – does the string end with a given substring?



# -------------------------------------
sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"

# Could aliasing cause potential confusion in this problem?

# no

# ✔️ Since a string is immutable, aliasing won't be as confusing. Beware of using something like item = item + new_item with mutable objects though because it creates a new object. However, when we use += then that doesn't happen.