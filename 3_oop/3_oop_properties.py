# Instance variables
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val
# -------------------------------------

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

# {'first': 1}
# {'first': 2, 'second': 3}
# {'first': 4, 'third': 5}

# -------------------------------------
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

# {'_ExampleClass__first': 1}
# {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
# {'_ExampleClass__first': 4, '__third': 5}
# -------------------------------------
# Class variables

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        counter += 1
        # or ExampleClass.counter


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

# {'_ExampleClass__first': 1} 3
# {'_ExampleClass__first': 2} 3
# {'_ExampleClass__first': 4} 3
# -------------------------------------
class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val    # or varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)        # {'__module__': '__main__', 'varia': 2, ....}
print(example_object.__dict__)      # {}

# {'__module__': '__main__', 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x7fc8d2a600e0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
# {'__module__': '__main__', 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x7fc8d2a600e0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
# {}

# -------------------------------------
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1              # it will never executed - that's why testing is important since 
                                    # the interpreter will not compile all execution paths on its own.


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)

# 1
# Traceback (most recent call last):
#   File "main.py", line 12, in <module>
#     print(example_object.b)
# AttributeError: 'ExampleClass' object has no attribute 'b'

# -------------------------------------
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    raise

# 1
# AttributeError: 'ExampleClass' object has no attribute 'b'
# -------------------------------------
class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))        # True
print(hasattr(ExampleClass, 'prop'))        # False

# -------------------------------------
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2

example_object = ExampleClass()

print(hasattr(ExampleClass, 'a'))   # True
print(hasattr(ExampleClass, 'b'))   # False

print(hasattr(example_object, 'a')) # True....... yes. True. it can be accessed from both the calss or the object
print(hasattr(example_object, 'b')) # True


# -------------------------------------
class Sample:
    gamma = 0 # Class variable.
    def __init__(self):
        self.alpha = 1 # Instance variable.
        self.__delta = 3 # Private instance variable.


obj = Sample()
obj.beta = 2  # Another instance variable (existing only inside the "obj" instance.)
print(obj.__dict__)    # {'alpha': 1, '_Sample__delta': 3, 'beta': 2}

# -------------------------------------
class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False

# population and victims are class variables, 
# while length and __venomous are instance variables (the latter is also private).
# -------------------------------------
# You're going to negate the __venomous property of the version_2 object, 
# ignoring the fact that the property is private. How will you do this?
version_2 = Python()
version_2._Python__venomous = not version_2._Python__venomous       # Forciebly access the private variable
# -------------------------------------
# Write an expression which checks if the version_2 object 
# contains an instance property named constrictor (yes, constrictor!)
hasattr(version_2, 'constrictor')       # False
