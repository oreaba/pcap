# -------------------------------------
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy


sun = Star("Sun", "Milky Way")
print(sun)

# <__main__.Star object at 0x7f1074cc7c50>

# -------------------------------------
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy


sun = Star("Sun", "Milky Way")
print(sun)

# Sun in Milky Way

# -------------------------------------
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

# The Vehicle class is the superclass for both the LandVehicle and TrackedVehicle classes;
# The LandVehicle class is a subclass of Vehicle and a superclass of TrackedVehicle at the same time;
# The TrackedVehicle class is a subclass of both the Vehicle and LandVehicle classes.
# -------------------------------------
# Inheritance: issubclass()

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()

    # issubclass(ClassOne, ClassTwo)
# True	False	False	
# True	True	False	
# True	True	True

# -------------------------------------
# Inheritance: isinstance()
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()

# isinstance(objectName, ClassName)

# True	False	False	
# True	True	False	
# True	True	True	
# -------------------------------------
# Inheritance: the is operator
class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2) # False
print(object_2 is object_3) # False
print(object_3 is object_1) # True
print(object_1.val, object_2.val, object_3.val) # 1 2 1

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2)   # True    - comparing values
print( string_1 is string_2)  # False   - comparing object addresses

# -------------------------------------
# How Python finds properties and methods

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)

# My name is Andy.

# -------------------------------------
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)
#  which accesses the superclass without needing to know its name:

# super().__init__(name)
# The super() function creates a context in which you don't have to (moreover, you mustn't) pass the 
# self argument to the method being invoked - this is why it's possible to activate the superclass constructor using only one argument.
# Note: you can use this mechanism not only to invoke the superclass constructor, 
# but also to get access to any of the resources available inside the superclass.
# COOL AND confront with SOLID

# -------------------------------------
# Testing properties: class variables.
class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()

print(obj.subVar)# 2
print(obj.supVar)# 1
# -------------------------------------

# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12            # we are extending the functionality on the base __init__

obj = Sub()

print(obj.subVar)# 12
print(obj.supVar)# 11
# -------------------------------------
class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102

class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202

class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())   # 100 101 102
print(obj.variable_2, obj.var_2, obj.fun_2())   # 200 201 202
print(obj.variable_3, obj.var_3, obj.fun_3())   # 300 301 302

# -------------------------------------

class SuperA:
    var_a = 10
    def fun_a(self):
        return 11


class SuperB:
    var_b = 20
    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.var_a, obj.fun_a())   # 10 11
print(obj.var_b, obj.fun_b())   # 20 21

# -------------------------------------
class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())# 200 201

# -------------------------------------
class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass

obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())# L LL RR Left

# -------------------------------------
# Do you need anything more? Just make a small amendment in the code - replace: 
# class Sub(Left, Right): with: class Sub(Right, Left):, then run the program again, and see what happens.

# What do you see now? We see:
# R LL RR Right
# -------------------------------------
class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()    # do_it from One
two.doanything()    # do_it from Two

# -------------------------------------

# import time

# class TrackedVehicle:
#     def control_track(left, stop):
#         pass

#     def turn(left):
#         control_track(left, True)
#         time.sleep(0.25)
#         control_track(left, False)


# class WheeledVehicle:
#     def turn_front_wheels(left, on):
#         pass

#     def turn(left):
#         turn_front_wheels(left, True)
#         time.sleep(0.25)
#         turn_front_wheels(left, False)

# Can you see what's wrong with the code?

# The turn() methods look too similar to leave them in this form.

# Let's rebuild the code - we're going to introduce a superclass to gather all the similar aspects of the driving vehicles, moving all the specifics to the subclasses.


# -------------------------------------

import time

class Vehicle:
    def change_direction(self, left, on):
        pass

    def turn(self, left):
        self.change_direction(left, True)
        time.sleep(0.25)
        self.change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(self, left, stop):
        pass

    def change_direction(self, left, on):
        self.control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(self, left, on):
        self.turn_front_wheels(left, on)

# This is how polymorphism helps the developer to keep the code clean and consistent.


# -------------------------------------
# How to build a hierarchy of classes: continued
import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)

# wheels:  True True
# wheels:  True False
# tracks:  False True
# tracks:  False False
# -------------------------------------
# Don't forget that:

# a single inheritance class is always simpler, safer, and easier to understand and maintain;

# multiple inheritance is always risky, as you have many more opportunities to make a mistake in identifying these parts of the superclasses which will effectively influence the new class;

# multiple inheritance may make overriding extremely tricky; moreover, using the super() function becomes ambiguous
# -------------------------------------
# multiple inheritance violates the single responsibility principle (more details here: https://en.wikipedia.org/wiki/Single_responsibility_principle) as it makes a new class of two (or more) classes that know nothing about each other;
# we strongly suggest multiple inheritance as the last of all possible solutions - if you really need the many different functionalities offered by different classes, composition may be a better alternative.

# -------------------------------------
# What is Method Resolution Order (MRO) and why is it that not all inheritances make sense?

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# bottom
# middle
# top

# -------------------------------------
class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle, Top):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# class Bottom(Middle, Top):

# -------------------------------------
class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")

# un comment the block below
# class Bottom(Top, Middle):
#     def m_bottom(self):
#         print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle
# We think that the message speaks for itself. Python's MRO cannot be bent or violated, 
# not just because that's the way Python works, but also because it’s a rule you have to obey.


# -------------------------------------

# The diamond problem

class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()

# -------------------------------------
# Let's rebuild our example from the previous page to make it more diamond-like, just like below:

class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


# Note: both Middle classes define a method of the same name: m_middle().


# -------------------------------------
# 1. A method named __str__() is responsible for converting an object's contents into a (more or less) readable string. 
# You can redefine it if you want your object to be able to present itself in a more elegant form. 
# For example:


class Mouse:
    def __init__(self, name):
        self.my_name = name


    def __str__(self):
        return self.my_name


the_mouse = Mouse('mickey')
print(the_mouse)  # Prints "mickey". 


# -------------------------------------
# 2. A function named issubclass(Class_1, Class_2) is able to determine if Class_1 is a subclass of Class_2. For example:
class Mouse:
    pass


class LabMouse(Mouse):
    pass


print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse))  # Prints "False True"



# -------------------------------------
# 3. A function named isinstance(Object, Class) checks if an object comes from an indicated class. For example:
class Mouse:
    pass


class LabMouse(Mouse):
    pass


mickey = Mouse()
lmickey = LabMouse()
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))  # Prints "True False".
print(isinstance(lmickey, Mouse))  # Prints "True".



# -------------------------------------
# 4. A operator called is checks if two variables refer to the same object. For example:
class Mouse:
    pass


mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey)  # Prints "False True".



# -------------------------------------
# 5. A parameterless function named super() returns a reference to the nearest superclass of the class. For example:

class Mouse:
    def __str__(self):
        return "Mouse"


class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()


doctor_mouse = LabMouse()
print(doctor_mouse)  # Prints "Laboratory Mouse".


# -------------------------------------
# 6. Methods as well as instance and class variables defined in a superclass are automatically inherited by their subclasses. For example:

class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name

    def __str__(self):
        return "Hi, my name is " + self.name

class LabMouse(Mouse):
    pass

professor_mouse = LabMouse("Professor Mouser")
print(professor_mouse, Mouse.Population)  # Prints "Hi, my name is Professor Mouser 1"


# -------------------------------------
# 7. In order to find any object/class property, Python looks for it inside:

# the object itself;
# all classes involved in the object's inheritance line from bottom to top;
# if there is more than one class on a particular inheritance path, Python scans them from left to right;
# if both of the above fail, the AttributeError exception is raised.

# -------------------------------------
# 8. If any of the subclasses defines a method/class variable/instance variable of 
# the same name as existing in the superclass, the new name overrides any of the
# previous instances of the name. For example:

class Mouse:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name

class AncientMouse(Mouse):
    def __str__(self):
        return "Meum nomen est " + self.name

mus = AncientMouse("Caesar")  # Prints "Meum nomen est Caesar"
print(mus)
