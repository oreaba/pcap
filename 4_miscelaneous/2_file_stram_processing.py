
# -------------------------------------
# File names
# Windows
# C: \directory\file

# Windows
# /directory/files
# -------------------------------------
# The main and most striking difference is that you have to use two different separators for the directory names: \ in Windows, and / in Unix/Linux.
# In Unix/Linux systems, it may look as follows:


name = "/dir/file"
# But if you try to code it for the Windows system:
name = "\dir\file"
# you'll get an unpleasant surprise: either Python will generate an error, or the execution of the program will behave strangely, as if the file name has been distorted in some way.

# In fact, it's not strange at all, but quite obvious and natural. Python uses the \ as an escape character (like \n).
# This means that Windows file names must be written as follows:

name = "\\dir\\file"

# The operation of connecting the stream with a file is called opening the file, while disconnecting this link is named closing the file.


# -------------------------------------
# If the opening is successful, the program will be allowed to perform only the operations which are consistent with the declared open mode.

# There are two basic operations performed on the stream:

# read from the stream: the portions of the data are retrieved from the file and placed in a memory area managed by the program (e.g., a variable);
# write to the stream: the portions of the data from the memory (e.g., a variable) are transferred to the file.

# -------------------------------------
# There are three basic modes used to open the stream:

# read mode: a stream opened in this mode allows read operations only; trying to write to the stream will cause an exception (the exception is named UnsupportedOperation, which inherits OSError and ValueError, and comes from the io module);
# write mode: a stream opened in this mode allows write operations only; attempting to read the stream will cause the exception mentioned above;
# update mode: a stream opened in this mode allows both writes and reads.

# -------------------------------------
# For our purposes, we'll concern ourselves only with streams represented by BufferIOBase and TextIOBase objects. You'll understand why soon.


# -------------------------------------
# File handles: continued
# Similarly, the trait of the program allowing execution in different environments is called portability. A program endowed with such a trait is called a portable program.

# during reading/writing of lines from/to the associated file, nothing special occurs in the Unix environment, but when the same operations are performed in the Windows environment, a process called a translation of newline characters occurs: when you read a line from the file, every pair of \r\n characters is replaced with a single \n character, and vice versa; during write operations, every \n character is replaced with a pair of \r\n characters;

# -------------------------------------
# Opening the streams
file = 'path'
stream = open(file, mode = 'r', encoding = None)

# -------------------------------------

# Opening the streams: modes
# r open mode: read
# the stream will be opened in read mode;
# the file associated with the stream must exist and has to be readable, otherwise the open() function raises an exception.

# w open mode: write
# the stream will be opened in write mode;
# the file associated with the stream doesn't need to exist; if it doesn't exist it will be created; if it exists, it will be truncated to the length of zero (erased); if the creation isn't possible (e.g., due to system permissions) the open() function raises an exception.

# a open mode: append
# the stream will be opened in append mode;
# the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; if it exists the virtual recording head will be set at the end of the file (the previous content of the file remains untouched.)

# r+ open mode: read and update
# the stream will be opened in read and update mode;
# the file associated with the stream must exist and has to be writeable, otherwise the open() function raises an exception;
# both read and write operations are allowed for the stream.

# w+ open mode: write and update
# the stream will be opened in write and update mode;
# the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; the previous content of the file remains untouched;
# both read and write operations are allowed for the stream.
# -------------------------------------

# Selecting text and binary modes

# Text mode	Binary mode	    Description
# rt	            rb	        read
# wt	            wb	        write
# at	            ab	        append
# r+t	            r+b	        read and update
# w+t	            w+b	        write and update


# extra:
# You can also open a file for its exclusive creation. 
# You can do this using the x open mode. 
# If the file already exists, the open() function will raise an exception.


# -------------------------------------
# Opening the stream for the first time

try:
    stream = open("C:\Users\User\Desktop\file.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)

# the open mode is defined as text to read (as text is the default setting, we can skip the t in mode string)
# if open() fails, we handle the exception printing full error information (it's definitely good to know what exactly happened)


# -------------------------------------

# Pre-opened streams
# We said earlier that any stream operation must be preceded by the open() function invocation. There are three well-defined exceptions to the rule.
import sys

sys.stdin
# stdin (as standard input)
# the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs;
# the well-known input() function reads data from stdin by default.

sys.stdout
# stdout (as standard output)
# the stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program;
# the well-known print() function outputs the data to the stdout stream.

sys.stderr
# stderr (as standard error output)
# the stderr stream is normally associated with the screen, pre-open for writing, regarded as the primary place where the running program should send information on the errors encountered during its work;
# we haven't presented any method to send the data to this stream (we will do it soon, we promise)
# the separation of stdout (useful results produced by the program) from the stderr (error messages, undeniably useful but does not provide results) gives the possibility of redirecting these two types of information to the different targets. More extensive discussion of this issue is beyond the scope of our course. The operation system handbook will provide more information on these issues.



# -------------------------------------
# Closing streams
# The last operation performed on a stream (this doesn't include the stdin, stdout, and stderr streams which don't require it) should be closing.

stream.close()
# -------------------------------------
# Diagnosing stream problems
# The IOError object is equipped with a property named errno (the name comes from the phrase error number) and you can access it as follows:


try:
    pass
    # Some stream operations.
except IOError as exc:
    print(exc.errno)

# errno.EACCES → Permission denied 
# The error occurs when you try, for example, to open a file with the read only attribute for writing.

# errno.EBADF → Bad file number 
# The error occurs when you try, for example, to operate with an unopened stream.

# errno.EEXIST → File exists 
# The error occurs when you try, for example, to rename a file with its previous name.

# errno.EFBIG → File too large 
# The error occurs when you try to create a file that is larger than the maximum allowed by the operating system.

# errno.EISDIR → Is a directory 
# The error occurs when you try to treat a directory name as the name of an ordinary file.

# errno.EMFILE → Too many open files 
# The error occurs when you try to simultaneously open more streams than acceptable for your operating system.

# errno.ENOENT → No such file or directory 
# The error occurs when you try to access a non-existent file/directory.

# errno.ENOSPC → No space left on device 
# The error occurs when there is no free space on the media.



# -------------------------------------
# Diagnosing stream problems: continued
# Its name is strerror(), and it comes from the os module and expects just one argument - an error number.
# Note: if you pass a non-existent error code (a number which is not bound to any actual error), the function will raise ValueError exception.


from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))


# -------------------------------------
from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))

# -------------------------------------
# 1. A file needs to be open before it can be processed by a program, 
# and it should be closed when the processing is finished.

# Opening the file associates it with the stream, 
# which is an abstract representation of the physical data stored on the media. 
# The way in which the stream is processed is called open mode. Three open modes exist:

# read mode – only read operations are allowed;
# write mode – only write operations are allowed;
# update mode – both writes and reads are allowed.

# -------------------------------------
# 2. Depending on the physical file content, different Python classes can be 
# used to process files. In general, the BufferedIOBase is able to process any file, 
# while TextIOBase is a specialized class dedicated to processing text files 
# (i.e. files containing human-visible texts divided into lines using new-line markers). 
# Thus, the streams can be divided into binary and text ones.


# -------------------------------------
# 3. The following open() function syntax is used to open a file: 

# open(file_name, mode=open_mode, encoding=text_encoding)

# The invocation creates a stream object and associates it with the file named file_name, using the specified open_mode and setting the specified text_encoding, or it raises an exception in the case of an error.


# -------------------------------------
# 4. Three predefined streams are already open when the program starts:

# sys.stdin – standard input;
# sys.stdout – standard output;
# sys.stderr – standard error output.

# -------------------------------------
# 4. The IOError exception object, created when any file operations fails (including open operations), contains a property named errno, which contains the completion code of the failed action. Use this value to diagnose the problem.

# Exercise 1

# How do you encode an open() function’s mode argument value 
# if you're going to create a new text file to only fill it with an article?

# Check
# "wt" or "w"


# -------------------------------------
# Exercise 2

# What is the meaning of the value represented by errno.EACESS?

# Check
# Permission denied: you're not allowed to access the file's content.
# -------------------------------------
# Exercise 3

# What is the expected output of the following code, assuming that the file named file does not exist?

# import errno

# try:
#     stream = open("file", "rb")
#     print("exists")
#     stream.close()
# except IOError as error:
#     if error.errno == errno.ENOENT:
#         print("absent")
#     else:
#         print("unknown")


# Check
# absent