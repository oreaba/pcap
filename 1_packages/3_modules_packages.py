# came 
# -------------------------------------
# -------------------------------------
# -------------------------------------
# -------------------------------------
# -------------------------------------
# -------------------------------------
print("I like to be a module.")
print(__name__)

# I like to be a module
# __main__
# when you run a file directly, its __name__ variable is set to __main__;
# when a file is imported as a module, its __name__ variable is set to the file's name (excluding .py)
# -------------------------------------
# Imagine the following context:

# there is a module named mod1;
# there is a module named mod2 which contains the import mod1 instruction;
# there is a main file containing the import mod1 and import mod2 instructions.
# At first glance, you may think that mod1 will be imported twice - fortunately, only the first import occurs. 
# Python remembers the imported modules and silently omits all subsequent imports.
# -------------------------------------

#    #!  For Unix and Unix-like OSs (including MacOS) such a line instructs the OS how to execute the contents of the file

# -------------------------------------

from sys import path
print(path)                     # prints the PATH environment variable
path.append('..\\modules')      # add a directory to the PATH env var.
print(path)

# import module

# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(module.suml(zeroes))
# print(module.prodl(ones))

# -------------------------------------

# You need to use a different trick instead - 
# Python expects that there is a file with a very unique name inside the package's folder: __init__.py
# -------------------------------------
# The content of the file is executed when any of the package's modules is imported. 
# If you don't want any special initializations, you can leave the file empty, but you mustn't omit it.
# -------------------------------------
# 1. While a module is designed to couple together some related entities (functions, variables, constants, etc.), 
# a package is a container which enables the coupling of several related modules under one common name. 
# Such a container can be distributed as-is (as a batch of files deployed in a directory sub-tree)
#  or it can be packed inside a zip file.

# # -------------------------------------

# 2. During the very first import of the actual module, 
# Python translates its source code into the semi-compiled format stored inside the pyc files, 
# and deploys these files into the __pycache__ directory located in the module's home directory.

# # -------------------------------------

# 3. If you want to instruct your module's user that a particular entity should be treated as private 
# (i.e. not to be explicitly used outside the module) you can mark its name with either the _ or __ prefix. 
# Don't forget that this is only a recommendation, not an order.

# # -------------------------------------

# 4. The names shabang, shebang, hasbang, poundbang, and hashpling describe the digraph written as #!,  (hasbang)
# used to instruct Unix-like OSs how the Python source file should be launched. 
# This convention has no effect under MS Windows.

# # -------------------------------------

# 5. If you want convince Python that it should take into account a non-standard package's directory, 
# its name needs to be inserted/appended into/to the import directory list 
# stored in the path variable contained in the sys module.

# # -------------------------------------

# 6. A Python file named __init__.py is implicitly run when a package containing it is subject to import, 
# and is used to initialize a package and/or its sub-packages (if any). The file may be empty, but must not be absent.

# -------------------------------------

# You want to prevent your module's user from running your code as an ordinary script. 
# How will you achieve such an effect?

import sys

if __name__ == "__main__":
    print("Don't do that!")
    sys.exit()

# -------------------------------------
import sys

# note the double backslashes! because the first backslash is the escape sequence character in python
sys.path.append("D:\\Python\\Project\\Modules")
