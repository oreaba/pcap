# did not come
# -------------------------------------
# In this section, you'll learn about a module called os, which lets you interact with the operating system using Python.

# A good example of this is the mkdir function, which allows you to create a directory just like the mkdir command in Unix and Windows. If you don't know this command, don't worry.

# get information about the operating system;
# manage processes;
# operate on I/O streams using file descriptors.

# -------------------------------------
import os
print(os.uname())

# posix.uname_result(sysname='Darwin', nodename='mhamdy.local', release='22.3.0', version='Darwin Kernel Version 22.3.0: Mon Jan 30 20:42:11 PST 2023; root:xnu-8792.81.3~2/RELEASE_X86_64', machine='x86_64')
# -------------------------------------
# systemname — stores the name of the operating system;
# nodename — stores the machine name on the network;
# release — stores the operating system release;
# version — stores the operating system version;
# machine — stores the hardware identifier, e.g., x86_64.

# -------------------------------------
# Unfortunately, the uname function only works on some Unix systems. If you use Windows, you can use the uname function in the platform module, which returns a similar result.

# The os module allows you to quickly distinguish the operating system using the name attribute, which supports one of the following names:

# posix — you'll get this name if you use Unix;
# nt — you'll get this name if you use Windows;
# java — you'll get this name if your code is written in Jython.

import os
print(os.name)
# posix
# -------------------------------------
# Creating directories in Python
import os

os.mkdir("my_first_directory")
print(os.listdir())

# my_first_directory — this is a relative path which will create the my_first_directory directory in the current working directory;
# ./my_first_directory — this is a relative path that explicitly points to the current working directory. It has the same effect as the path above;
# ../my_first_directory — this is a relative path that will create the my_first_directory directory in the parent directory of the current working directory;
# /python/my_first_directory — this is the absolute path that will create the my_first_directory directory, which in turn is in the python directory in the root directory.

# To change the directory permissions, we recommend the chmod function, which works similarly to the chmod command on Unix systems. You can find more information about it in the documentation.


# -------------------------------------
# Recursive directory creation

import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())

# The mkdir function is very useful, but what if you need to create another directory 
# in the directory you've just created. Of course, you can go to the created directory 
# and create another directory inside it, but fortunately the os module provides 
# a function called makedirs, which makes this task easier.

# The makedirs function enables recursive directory creation, which means that 
# all directories in the path will be created. Let's look at the code in the 
# editor and see how it is in practice.
# -------------------------------------

# Where am I now?
# As you’ve probably guessed, the os module provides a function that returns 
# information about the current working directory. It's called getcwd. 
# Look at the code in the editor to see how to use it in practice.

import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())

# .../my_first_directory
# .../my_first_directory/my_second_directory

# NOTE: On Unix-like systems, the equivalent of the getcwd function is the pwd command, which prints the name of the current working directory.


# -------------------------------------
# Deleting directories in Python
import os

os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory")
print(os.listdir())

# The os module also allows you to delete directories. It gives you the option of deleting a single directory or a directory with its subdirectories. To delete a single directory, you can use a function called rmdir, which takes the path as its argument. Look at the code in the editor.

# -------------------------------------

# To remove a directory and its subdirectories, you can use the removedirs function, which requires you to specify a path containing all directories that should be removed:

import os

os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())
# -------------------------------------

# The system() function

import os

returned_value = os.system("mkdir my_first_directory")
print(returned_value)

# Result:
# 0
# The system function is available in both Windows and Unix. 
# Depending on the system, it returns a different result.
# In Windows, it returns the value returned by the shell after 
# running the command given, while in Unix, it returns the exit status of the process.


# -------------------------------------
# 1. The uname function returns an object that contains information 
# about the current operating system. The object has the following attributes:

# systemname (stores the name of the operating system)
# nodename (stores the machine name on the network)
# release (stores the operating system release)
# version (stores the operating system version)
# machine (stores the hardware identifier, e.g. x86_64.)
# -------------------------------------

# 2. The name attribute available in the os module allows 
# you to distinguish the operating system. 
# It returns one of the following three values:

# posix (you'll get this name if you use Unix)
# nt (you'll get this name if you use Windows)
# java (you'll get this name if your code is written in something like Jython)

# -------------------------------------
# 3. The mkdir function creates a directory in the path passed as its argument. 
# The path can be either relative or absolute, e.g:

import os

os.mkdir("hello")             # the relative path
os.mkdir("/home/python/hello") # the absolute path

# -------------------------------------
# Note: If the directory exists, a FileExistsError exception will be thrown. 
# In addition to the mkdir function, the os module provides the makedirs function, 
# which allows you to recursively create all directories in a path.
# -------------------------------------
# 4. The result of the listdir() function is a list containing 
# the names of the files and directories that are in the path passed as its argument.

# It's important to remember that the listdir function omits the 
# entries '.' and '..', which are displayed, 
# for example, when using the ls -a command on Unix systems. 
# If the path isn't passed, the result will be returned for the current working directory.

# -------------------------------------
# 5. To move between directories, you can use a function called chdir(), 
# which changes the current working directory to the specified path. 
# As its argument, it takes any relative or absolute path.

# -------------------------------------
# If you want to find out what the current working directory is, 
# you can use the getcwd() function, which returns the path to it.

# -------------------------------------
# 6. To remove a directory, you can use the rmdir() function, 
# but to remove a directory and its subdirectories, use the removedirs() function.

# -------------------------------------
# 7. On both Unix and Windows, you can use the system function, 
# which executes a command passed to it as a string, e.g.:

import os

returned_value = os.system("mkdir hello")
# The system function on Windows returns the value returned 
# by shell after running the command given, 
# while on Unix it returns the exit status of the process.


# -------------------------------------
# Exercise 1

# What is the output of the following snippet if you run it on Unix?

import os
print(os.name)

# posix
# -------------------------------------
# Exercise 2

# What is the output of the following snippet?

import os

os.mkdir("hello")
print(os.listdir())


['hello']