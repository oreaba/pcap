
# -------------------------------------
class Classy:
    def method(self):
        print("method")


obj = Classy()
obj.method()

# -------------------------------------
class Classy:
    def method(self, par):
        print("method:", par)


obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)


# method: 1
# method: 2
# method: 3
# -------------------------------------
# Test examples here.
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()

# 2 3

# -------------------------------------
class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy()
obj.method()

# method
# other
# -------------------------------------
class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("object")

print(obj_1.var)

# object
# -------------------------------------
class Classy:
    def __init__(self, value = None):
        self.var = value


obj_1 = Classy("object")
obj_2 = Classy()

print(obj_1.var)
print(obj_2.var)

# object
# None
# -------------------------------------

class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()      # AttributeError: 'Classy' object has no attribute '__hidden'
except:
    print("failed")

obj._Classy__hidden()


# visible
# failed
# hidden
# -------------------------------------
class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)


# {'var': 2}
# {'__module__': '__main__', 'varia': 1, '__init__': <function Classy.__init__ at 0x7f6d59a39320>, 'method': <function Classy.method at 0x7f6d59a393b0>, '_Classy__hidden': <function Classy.__hidden at 0x7f6d59a39440>, '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objects>, '__doc__': None}

# -------------------------------------

class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

# Classy
# Classy

print(obj.__name__)     # __name__ is attribute of the class not the object - an object has no name
# will cause an error
# -------------------------------------
# __module__ is a string, too - it stores the name of the module which contains the definition of the class.
class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)


# __main__
# __main__

# As you know, any module named __main__ is actually not a module, but the file currently being run.
# -------------------------------------

class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

# ( object )
# ( object )
# ( SuperOne SuperTwo )
# -------------------------------------
# introspection, which is the ability of a program to examine the type or properties of an object at runtime;
# reflection, which goes a step further, and is the ability of a program to manipulate the 
# values, properties and/or functions of an object at runtime.

# -------------------------------------
# Investigating classes

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

# {'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}
# {'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}

# -------------------------------------
class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("My name is " + self.name + " living in a " + Sample.__module__)

obj = Sample()
obj.myself()


# My name is Sample living in a __main__

# -------------------------------------
# The declaration of the Snake class is given below. Enrich the class with a method named increment(), adding 1 to the __victims property.

class Snake:
    def __init__(self):
        self.victims = 0

# solution
class Snake:
    def __init__(self):
        self.victims = 0

    def increment(self):
        self.victims += 1
# -------------------------------------
class Snake:
    pass


class Python(Snake):
    pass


print(Python.__name__, 'is a', Snake.__name__)
print(Python.__bases__[0].__name__, 'can be', Python.__name__)

# Python is a Snake
# Snake can be Python
