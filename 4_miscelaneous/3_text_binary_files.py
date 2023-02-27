# came

# -------------------------------------
# Processing text files
# Opening tzop.txt in read mode, returning it as a file object:
stream = open("tzop.txt", "rt", encoding = "utf-8")

print(stream.read()) # printing the content of the file

# -------------------------------------
# For example, if you're using a Unix/Linux OS configured to 
# use UTF-8 as a system-wide setting, the open() function may look as follows:

stream = open('file.txt', 'rt', encoding='utf-8')

# note:
# For the purposes of our experiments with file processing carried out in this section, 
# we're going to use a pre-uploaded set of files 
# (i.e., tzop.txt, or text.txt files) which you'll be able to work with. 
# If you'd like to work with your own files locally on your machine, 
# we strongly encourage you to do so, and to use IDLE 
# (or any other IDE that you may prefer) to carry out your own tests.

# -------------------------------------
from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# If applied to a text file, the function is able to:

# read a desired number of characters (including just one) from the file, 
# and return them as a string;
# read all the file contents, and return them as a string;
# if there is nothing more to read (the virtual reading head reaches the end of the file), 
# the function returns an empty string.

# output:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# -------------------------------------
# use the try-except mechanism and open the file of the predetermined name (text.txt in our case)
# try to read the very first character from the file (ch = s.read(1))

# -------------------------------------

# If you're absolutely sure that the file's length is safe and you can read the whole file to the memory at once, you can do it - the read() function, invoked without any arguments or with an argument that evaluates to None, will do the job for you.

from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# open the file as previously;
# read its contents by one read() function invocation;
# next, process the text, iterating through it with a regular for loop, 
# and updating the counter value at each turn of the loop;

# -------------------------------------
# Processing text files: readline()

# If you want to treat the file's contents as a set of lines, 
# not a bunch of characters, the readline() method will help you with that.

# The method tries to read a complete line of text from the file, 
# and returns it as a string in the case of success. Otherwise, it returns an empty string.

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# -------------------------------------
# Processing text files: readlines()
# Another method, which treats text file as a set of lines, not characters, is readlines().

# The readlines() method, when invoked without arguments, tries to read all the file contents, and returns a list of strings, one element per file line.

# If you're not sure if the file size is small enough and don't want to test the OS, you can convince the readlines() method to read not more than a specified number of bytes at once (the returning value remains the same - it's a list of a string).

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# -------------------------------------
# Processing text files: continued

# The last example we want to present shows a very interesting trait 
# of the object returned by the open() function in text mode.

# We think it may surprise you - the object is an instance of the iterable class.
# Strange? Not at all. Usable? Yes, absolutely.

# The iteration protocol defined for the file object is 
# very simple - its __next__ method just returns the next line read in from the file.

# Moreover, you can expect that the object automatically 
# invokes close() when any of the file reads reaches the end of the file.

from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):         # like readline()
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))

# -------------------------------------
# Dealing with text files: write()
# Writing text files seems to be simpler, as in fact there is one method that can be used to perform such a task.

# The method is named write() and it expects just one argument - a string that will be transferred to an open file (don't forget - the open mode should reflect the way in which the data is transferred - writing a file opened in read mode won't succeed).

# No newline character is added to the write()'s argument, so you have to add it yourself if you want the file to be filled with a number of lines.

# The example in the editor shows a very simple code that creates a file named newtext.txt (note: the open mode w ensures that the file will be created from scratch, even if it exists and contains data) and then puts ten lines into it.

from os import strerror

try:
	fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))

# line #1
# line #2
# line #3
# line #4
# line #5
# line #6
# line #7
# line #8
# line #9
# line #10

# -------------------------------------

# Dealing with text files: continued

# Look at the example in the editor. We've modified the previous code to 
# write whole lines to the text file.

# The contents of the newly created file are the same.

# Note: you can use the same method to write to the stderr stream, 
# but don't try to open it, as it's always open implicitly.

from os import strerror

try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# -------------------------------------
# What is a bytearray?
# Before we start talking about binary files, 
# we have to tell you about one of the specialized classes Python uses to store amorphous data.

# Amorphous data is data which have no specific shape or form - they are just a series of bytes.
# Python has more than one such container - one of them is a specialized class name bytearray - 
# as the name suggests, it's an array containing (amorphous) bytes.

data = bytearray(10)

# Note: such a constructor fills the whole array with zeros.


# -------------------------------------
# Bytearrays: continued
# Bytearrays resemble lists in many respects. For example, they are mutable, they're a subject of the len() function, and you can access any of their elements using conventional indexing.

# There is one important limitation - you mustn't set any byte array elements with a value which is not an integer (violating this rule will cause a TypeError exception) and you're not allowed to assign a value that doesn't come from the range 0 to 255 inclusive (unless you want to provoke a ValueError exception).

# You can treat any byte array elements as integer values - just like in the example in the editor.

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

# 0xa
# 0x9
# 0x8
# 0x7
# 0x6
# 0x5
# 0x4
# 0x3
# 0x2
# 0x1

# -------------------------------------

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# -------------------------------------
# How to read bytes from a stream
# Reading from a binary file requires use of a specialized method name readinto(), 
# as the method doesn't create a new byte array object, 
# but fills a previously created one with the values taken from the binary file.

# the method returns the number of successfully read bytes;
# the method tries to fill the whole space available inside its argument; 
# if there are more data in the file than space in the argument, 
# the read operation will stop before the end of the file; 
# otherwise, the method's result may indicate that the byte array 
# has only been filled fragmentarily (the result will show you that, too, 
# and the part of the array not being used by the newly read contents remains untouched)
# Look at the complete code below:

# Your code that reads bytes from the stream should go here.
from os import strerror

data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# first, we open the file (the one you created using the previous code) 
# with the mode described as rb;
# then, we read its contents into the byte array named data, of size ten bytes;
# finally, we print the byte array contents - are they the same as you expected?

# -------------------------------------
# How to read bytes from a stream
# An alternative way of reading the contents of a binary file is offered 
# by the method named read().

# Invoked without arguments, it tries to read all the contents of the file into the memory, 
# making them a part of a newly created object of the bytes class.

# This class has some similarities to bytearray, 
# with the exception of one significant difference - it's immutable.
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Fortunately, there are no obstacles to creating a byte array by taking 
# its initial value directly from the bytes object, just like here:
# Be careful - don't use this kind of read if you're not sure that the 
# file's contents will fit the available memory.

from os import strerror

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# -------------------------------------

# How to read bytes from a stream: continued

# If the read() method is invoked with an argument, 
# it specifies the maximum number of bytes to be read.

# The method tries to read the desired number of bytes from the file, 
# and the length of the returned object can be used to determine the number of bytes actually read.

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))



# -------------------------------------
# Your code that reads bytes from the stream should go here.
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Note: the first five bytes of the file have been read by the code - 
# the next five are still waiting to be processed.


# -------------------------------------
# Copying files - a simple and functional tool


from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()

# -------------------------------------
# 1. To read a file’s contents, the following stream methods can be used:

# read() is able to read the whole file at once;
# read(number) – reads the number characters/bytes from the file and returns them as a string; 
# readline() – reads a single line from the text file;
# readlines() – is able to read all lines at once;
# readlines(number) – reads the number lines from the text file;
# readinto(bytearray) – reads the bytes from the file and fills the bytearray with them;

# -------------------------------------

# 2. To write new content into a file, the following stream methods can be used:

# write(string) – writes a string to a text file;
# write(bytearray) – writes all the bytes of bytearray to a file;

# -------------------------------------

# 3. The open() method returns an iterable object which can be used to iterate through all the file's lines inside a for loop. For example:

for line in open("file", "rt"):
    print(line, end='')


# The code copies the file's contents to the console, line by line. Note: the stream closes itself automatically when it reaches the end of the file.

# -------------------------------------

# Exercise 1

# What do we expect from the readlines() method when the stream is associated with an empty file?

# Check
# An empty list (a zero-length list).


# -------------------------------------

# Exercise 2

# What is the following code intended to do?

for line in open("file", "rt"):
    for char in line:
        if char.lower() not in "aeiouy ":
            print(char, end='')


# Check
# It copies the file's contents to the console, ignoring all vowels.


# -------------------------------------

# Exercise 3

# You're going to process a bitmap stored in a file named image.png, and you want to read its contents as a whole into a bytearray variable named image. Add a line to the following code to achieve this goal.

try:
    stream = open("image.png", "rb")
    # Insert a line here.
    stream.close()
except IOError:
    print("failed")
else:
    print("success")


# Check
image = bytearray(stream.read())
