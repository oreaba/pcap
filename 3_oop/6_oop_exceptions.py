# -------------------------------------
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n


print(reciprocal(2))
print(reciprocal(0))

# Everything went fine
# 0.5
# Division failed
# None
# -------------------------------------
try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())

# Note: the identifier's scope covers its except branch, and doesn't go any further.

# As you can see, the except statement is extended, and contains an additional phrase starting with the as keyword, followed by an identifier. The identifier is designed to catch the exception object so you can analyze its nature and draw proper conclusions.

# The example presents a very simple way of utilizing the received object - just print it out (as you can see, the output is produced by the object's __str__() method) and it contains a brief message describing the reason.

# The same message will be printed if there is no fitting except block in the code, and Python is forced to handle it alone.



# -------------------------------------

def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print(e.args)
    print_args(e.args)

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    # print(e, e.__str__(), sep=' : ', end=' : ')
    print(e.args)
    print_args(e.args)

# Detailed anatomy of exceptions
# Let's take a closer look at the exception's object, as there are some really interesting elements here (we'll return to the issue soon when we consider Python's input/output base techniques, as their exception subsystem extends these objects a bit).

# The BaseException class introduces a property named args. It's a tuple designed to gather all arguments passed to the class constructor. It is empty if the construct has been invoked without any arguments, or contains just one element when the constructor gets one argument (we don't count the self argument here), and so on.

# We've prepared a simple function to print the args property in an elegant way. You can see the function in the editor.


# We've used the function to print the contents of the args property in three different cases, where the exception of the Exception class is raised in three different ways. To make it more spectacular, we've also printed the object itself, along with the result of the __str__() invocation.

# The first case looks routine - there is just the name Exception after the raise keyword. This means that the object of this class has been created in a most routine way.

# The second and third cases may look a bit weird at first glance, but there's nothing odd here - these are just the constructor invocations. In the second raise statement, the constructor is invoked with one argument, and in the third, with two.

# As you can see, the program output reflects this, showing the appropriate contents of the args property:


# :  :
# my exception : my exception : my exception
# ('my', 'exception') : ('my', 'exception') : ('my', 'exception')

# -------------------------------------

# How to create your own exception

class MyZeroDivisionError(ZeroDivisionError):	
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:		
        raise ZeroDivisionError("some bad news")

for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

# Division by zero
# Division by zero
# -------------------------------------

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')

# Original division by zero
# My division by zero
# -------------------------------------
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese

# -------------------------------------

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese

# Note: we're going to collect more specific information here than a regular Exception does, so our constructor will take two arguments:

# one specifying a pizza as a subject of the process,
# and one containing a more or less precise description of the problem.

# -------------------------------------
class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese

# The TooMuchCheeseError exception needs more information than the regular PizzaError exception, so we add it to the constructor - the name cheese is then stored for further processing.
# -------------------------------------

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

# Note:

# removing the branch starting with except TooMuchCheeseError will cause all appearing exceptions to be classified as PizzaError;
# removing the branch starting with except PizzaErrorwill cause the TooMuchCheeseError exceptions to remain unhandled, and will cause the program to terminate.

# We'll remove this weakness by setting the default values for all constructor parameters. Take a look:

class PizzaError(Exception):
    def __init__(self, pizza='uknown', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uknown', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if cheese > 100:
        raise TooMuchCheeseError
    print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

# Now, if the circumstances permit, it is possible to use the class names alone.

# -------------------------------------
# 1. The else: branch of the try statement is executed when there has been no exception during the execution of the try: block.

# -------------------------------------
# 2. The finally: branch of the try statement is always executed.

# -------------------------------------
# 3. The syntax except Exception_Name as an exception_object: lets you intercept an object carrying information 
# about a pending exception. The object's property named args (a tuple) stores all arguments passed to the object's constructor.


# -------------------------------------
# 4. The exception classes can be extended to enrich them with new capabilities, or to adopt their traits to newly defined exceptions.

# For example:

try:
    assert __name__ == "__main__"
except:
    print("fail", end=' ')
else:
    print("success", end=' ')
finally:
    print("done")


# The code outputs: success done.

# -------------------------------------
# What is the expected output of the following code?

import math

try:
    print(math.sqrt(9))
except ValueError:
    print("inf")
else:
    print("fine")

# 3.0
# fine

# -------------------------------------
# What is the expected output of the following code?

import math

try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("fine")
finally:
    print("the end")

#     inf
# the end
# -------------------------------------

# What is the expected output of the following code?

import math

class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)

try:
    raise NewValueError("Enemy warning", "Red alert", "High readiness")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')

# Enemy warning! Red alert! High readiness! 

# Exceptions are classes
# All the built-in Python exceptions form a hierarchy of classes. There is no obstacle to extending it if you find it reasonable.

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)

# -------------------------------------
# BaseException
#    +---Exception
#    |   +---TypeError
#    |   +---StopAsyncIteration
#    |   +---StopIteration
#    |   +---ImportError
#    |   |   +---ModuleNotFoundError
#    |   |   +---ZipImportError
#    |   +---OSError
#    |   |   +---ConnectionError
#    |   |   |   +---BrokenPipeError
#    |   |   |   +---ConnectionAbortedError
#    |   |   |   +---ConnectionRefusedError
#    |   |   |   +---ConnectionResetError
#    |   |   +---BlockingIOError
#    |   |   +---ChildProcessError
#    |   |   +---FileExistsError
#    |   |   +---FileNotFoundError
#    |   |   +---IsADirectoryError
#    |   |   +---NotADirectoryError
#    |   |   +---InterruptedError
#    |   |   +---PermissionError
#    |   |   +---ProcessLookupError
#    |   |   +---TimeoutError
#    |   |   +---UnsupportedOperation
#    |   |   +---herror
#    |   |   +---gaierror
#    |   |   +---timeout
#    |   |   +---Error
#    |   |   |   +---SameFileError
#    |   |   +---SpecialFileError
#    |   |   +---ExecError
#    |   |   +---ReadError
#    |   +---EOFError
#    |   +---RuntimeError
#    |   |   +---RecursionError
#    |   |   +---NotImplementedError
#    |   |   +---_DeadlockError
#    |   |   +---BrokenBarrierError
#    |   +---NameError
#    |   |   +---UnboundLocalError
#    |   +---AttributeError
#    |   +---SyntaxError
#    |   |   +---IndentationError
#    |   |   |   +---TabError
#    |   +---LookupError
#    |   |   +---IndexError
#    |   |   +---KeyError
#    |   |   +---CodecRegistryError
#    |   +---ValueError
#    |   |   +---UnicodeError
#    |   |   |   +---UnicodeEncodeError
#    |   |   |   +---UnicodeDecodeError
#    |   |   |   +---UnicodeTranslateError
#    |   |   +---UnsupportedOperation
#    |   +---AssertionError
#    |   +---ArithmeticError
#    |   |   +---FloatingPointError
#    |   |   +---OverflowError
#    |   |   +---ZeroDivisionError
#    |   +---SystemError
#    |   |   +---CodecRegistryError
#    |   +---ReferenceError
#    |   +---BufferError
#    |   +---MemoryError
#    |   +---Warning
#    |   |   +---UserWarning
#    |   |   +---DeprecationWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---SyntaxWarning
#    |   |   +---RuntimeWarning
#    |   |   +---FutureWarning
#    |   |   +---ImportWarning
#    |   |   +---UnicodeWarning
#    |   |   +---BytesWarning
#    |   |   +---ResourceWarning
#    |   +---error
#    |   +---Verbose
#    |   +---Error
#    |   +---TokenError
#    |   +---StopTokenizing
#    |   +---Empty
#    |   +---Full
#    |   +---_OptionError
#    |   +---TclError
#    |   +---SubprocessError
#    |   |   +---CalledProcessError
#    |   |   +---TimeoutExpired
#    |   +---Error
#    |   |   +---NoSectionError
#    |   |   +---DuplicateSectionError
#    |   |   +---DuplicateOptionError
#    |   |   +---NoOptionError
#    |   |   +---InterpolationError
#    |   |   |   +---InterpolationMissingOptionError
#    |   |   |   +---InterpolationSyntaxError
#    |   |   |   +---InterpolationDepthError
#    |   |   +---ParsingError
#    |   |   |   +---MissingSectionHeaderError
#    |   +---InvalidConfigType
#    |   +---InvalidConfigSet
#    |   +---InvalidFgBg
#    |   +---InvalidTheme
#    |   +---EndOfBlock
#    |   +---BdbQuit
#    |   +---error
#    |   +---_Stop
#    |   +---PickleError
#    |   |   +---PicklingError
#    |   |   +---UnpicklingError
#    |   +---_GiveupOnSendfile
#    |   +---error
#    |   +---LZMAError
#    |   +---RegistryError
#    |   +---ErrorDuringImport
#    +---GeneratorExit
#    +---SystemExit
#    +---KeyboardInterrupt

# -------------------------------------