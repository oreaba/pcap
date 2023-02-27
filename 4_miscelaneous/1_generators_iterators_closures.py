# only simple question about clousre came
# generators, iterators, and yield did not come

# -------------------------------------
# Generators - where to find them
# A Python generator is a piece of specialized code able to produce a series of values, and to control the iteration process. 
# This is why generators are very often called iterators, and although some may find a very subtle distinction between these two,
# we'll treat them as one.
for i in range(5):
    print(i)

# A generator returns a series of values, and in general, is (implicitly) invoked more than once.


# -------------------------------------
# Generators - where to find them: continued
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)

# An iterator must provide two methods:

# __iter__() which should return the object itself and which is invoked once 
# (it's needed for Python to successfully start the iteration)
# __next__() which is intended to return the next value (first, second, and so on) of the desired series -
#  it will be invoked by the for/in statements in order to pass through the next iteration; 
# if there are no more values to provide, the method should raise the StopIteration exception
# __init__
# __iter__
# __next__
# 1
# __next__
# 1
# __next__
# 2
# __next__
# 3
# __next__
# 5
# __next__
# 8
# __next__
# 13
# __next__
# 21
# __next__
# 34
# __next__
# 55
# __next__

# the iterator object is instantiated first;
# next, Python invokes the __iter__ method to get access to the actual iterator;
# the __next__ method is invoked eleven times - the first ten times produce useful values, while the eleventh terminates the iteration.

# -------------------------------------
class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter


object = Class(8)

for i in object:
    print(i)

# Class iter
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# -------------------------------------
# The yield statement
# You may think of the yield keyword as a smarter sibling of the return statement, with one essential difference.

def fun(n):
    for i in range(n):
        return i

# It looks strange, doesn't it? It's clear that the for loop has no chance to finish its first execution, 
# as the return will break it irrevocably.

def fun(n):
    for i in range(n):
        yield i

# We've added yield instead of return. This little amendment turns the function into a generator, 
# and executing the yield statement has some very interesting effects.
# First of all, it provides the value of the expression specified after the yield keyword, just like return, 
# but doesn't lose the state of the function.
# All the variables' values are frozen, and wait for the next invocation, 
# when the execution is resumed (not taken from scratch, like after return).

# There is one important limitation: such a function should not be invoked explicitly
# as - in fact - it isn't a function anymore; it's a generator object.
# The invocation will return the object's identifier, not the series we expect from the generator.
# Due to the same reasons, the previous function (the one with the return statement) may only be invoked explicitly, and must not be used as a generator.





# -------------------------------------
# How to build a generator
def fun(n):
    for i in range(n):
        yield i

print(fun(4))       # <generator object fun at 0x10c0764d0>

for v in fun(5):
    print(v)

# 0
# 1
# 2
# 3
# 4
# -------------------------------------
# What if you need a generator to produce the first n powers of 2?
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2  


for v in powers_of_2(8):
    print(v)

# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128

# -------------------------------------
# List comprehensions
# Generators may also be used within list comprehensions, just like here:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = [x for x in powers_of_2(5)]
print(t)

# [1, 2, 4, 8, 16]
# -------------------------------------
# The list() function
# The list() function can transform a series of subsequent generator 
# invocations into a real list:
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = list(powers_of_2(3))
print(t)

# [1, 2, 4]
# -------------------------------------
# The in operator

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for i in range(20):
    if i in powers_of_2(4):
        print(i)

# 1
# 2
# 4
# 8

# -------------------------------------
# The Fibanacci number generator

# Now let's see a Fibonacci number generator, and ensure that it looks much better 
# than the objective version based on the direct iterator protocol implementation.

def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)

# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# -------------------------------------
# More about list comprehensions
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)

# [1, 10, 100, 1000, 10000, 100000]
# [1, 10, 100, 1000, 10000, 100000]

# -------------------------------------
# There is a very interesting syntax we want to show you now. 
# Its usability is not limited to list comprehensions, 
# but we have to admit that comprehensions are the ideal environment for it.

# It's a conditional expression - a way of selecting one of two different values
#  based on the result of a Boolean expression.

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

# [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# -------------------------------------
# More about list comprehensions: continued
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)
# [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

the_list = [1 for x in range(10) if x % 2 == 0] # without else
# [1, 1, 1, 1, 1]

# -------------------------------------
# List comprehensions vs. generators
# Just one change can turn any list comprehension into a generator.
# Now look at the code below and see if you can find the detail that 
# turns a list comprehension into a generator:
the_list        = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator   = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

# 1 0 1 0 1 0 1 0 1 0 
# 1 0 1 0 1 0 1 0 1 0 


# It's the parentheses. The brackets make a comprehension, the parentheses make a generator.


# len(the_list) will evaluate to 10. Clear and predictable. 
# len(the_generator) will raise an exception, and you will see the following message:
# TypeError: object of type 'generator' has no len()
# -------------------------------------
# Of course, saving either the list or the generator is not necessary 
# - you can create them exactly in the place where you need them - just like here:
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:    # LIST
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):   # GENERATOR
    print(v, end=" ")
print()

# Note: the same appearance of the output doesn't mean that both loops work in the same way. 
# In the first loop, the list is created (and iterated through) as a whole - 
# it actually exists when the loop is being executed.
# In the second loop, there is no list at all - 
# there are only subsequent values produced by the generator, one by one.


# -------------------------------------

# The lambda function

# A lambda function is a function without a name 
# (you can also call it an anonymous function). 
# Of course, such a statement immediately raises the question: 
# how do you use anything that cannot be identified?
# Fortunately, it's not a problem, as you can name such a function if you really need, 
# but, in fact, in many cases the lambda function can exist and work while remaining fully incognito.
# lambda parameters: expression
# Such a clause returns the value of the expression when taking into account the current value of the current lambda argument.


two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

# the first lambda is an anonymous parameterless function that always returns 2. 
# As we've assigned it to a variable named two, we can say that the function is not anonymous anymore, 
# and we can use the name to invoke it.

# the second one is a one-parameter anonymous function that returns the value of its squared argument. 
# We've named it as such, too.

# the third lambda takes two parameters and returns the value of the first one raised to the power of the second one. 
# The name of the variable which carries the lambda speaks for itself. We don't use pow to avoid confusion with the built-in function of the same name and the same purpose.

# 4 4
# 1 1
# 0 0
# 1 1
# 4 4

# -------------------------------------
def print_function(fun, args):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function(poly, [x for x in range(-2, 3)])

# f(-2)=18
# f(-1)=8
# f(0)=2
# f(1)=0
# f(2)=2

# -------------------------------------
def print_function(fun, args):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function(lambda x: 2 * x**2 - 4 * x + 2, [x for x in range(-2, 3)])


# f(-2)=18
# f(-1)=8
# f(0)=2
# f(1)=0
# f(2)=2

# -------------------------------------
lambda x: 2 * x**2 - 4 * x + 2
# The code has become shorter, clearer, and more legible.


# -------------------------------------
# Lambdas and the map() function
# In the simplest of all possible cases, the map() function:

map(function, list)

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

# [1, 2, 4, 8, 16]
# 1 4 16 64 256 

# -------------------------------------
# the second map() argument may be any entity that can be iterated (e.g., a tuple, or just a generator)
# map() can accept more than two arguments.

#  The map() function applies the function passed by its first argument to all its second argument's elements,
#  and returns an iterator delivering all subsequent function results.


# -------------------------------------
# Lambdas and the filter() function

# It expects the same kind of arguments as map(), but does something different - 
# it filters its second argument while being guided by directions flowing from the function 
# specified as the first argument (the function is invoked for each list element, just like in map()).
# The elements which return True from the function pass the filter - the others are rejected.

# Note: we've made use of the random module to initialize the random number generator 
# (not to be confused with the generators we've just talked about) with the seed() function, 
# and to produce five random integer values from -10 to 10 using the randint() function.

from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

# [8, -5, 5, -2, 8]
# [8, 8]


# -------------------------------------
# A brief look at closures

# Let's start with a definition: 
# closure is a technique which allows the storing of values in spite of the fact that the context 
# in which they have been created does not exist anymore. Intricate? A bit.

def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

# The last two lines will cause a NameError exception - neither par nor loc is accessible outside the function. Both the variables exist when and only when the outer() function is being executed.

# Look carefully:

# the inner() function returns the value of the variable accessible inside its scope, 
# as inner() can use any of the entities at the disposal of outer()
# the outer() function returns the inner() function itself; more precisely, 
# it returns a copy of the inner() function, the one which was frozen at the moment 
# of outer()'s invocation; the frozen function contains its full environment, 
# including the state of all local variables, which also means that the value of 
# loc is successfully retained, although outer() ceased to exist a long time ago.
def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

# 1
# The function returned during the outer() invocation is a closure.


# -------------------------------------
# A closure has to be invoked in exactly the same way in which it has been declared.


def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64

# -------------------------------------
def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

# the inner() function is parameterless, so we have to invoke it without arguments.
# Now look at the code in the editor. 
# It is fully possible to declare a closure equipped with an arbitrary number of parameters, 
# e.g., one, just like the power() function.

# This means that the closure not only makes use of the frozen environment, 
# but it can also modify its behavior by using values taken from the outside.

# This example shows one more interesting circumstance - 
# you can create as many closures as you want using one and the same piece of code. 
# This is done with a function named make_closure(). Note:
# the first closure obtained from make_closure() defines a tool squaring its argument;
# the second one is designed to cube the argument.
# This is why the code produces the following output:

# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64



# -------------------------------------
# 1. An iterator is an object of a class providing at least two methods 
# (not counting the constructor!):

# __iter__() is invoked once when the iterator is created and returns the iterator's object itself;
# __next__() is invoked to provide the next iteration's value and raises 
# the StopIteration exception when the iteration comes to and end.

# -------------------------------------
# 2. The yield statement can be used only inside functions. 
# The yield statement suspends function execution and causes the function 
# to return the yield's argument as a result. 
# Such a function cannot be invoked in a regular way – 
# its only purpose is to be used as a generator 
# (i.e. in a context that requires a series of values, like a for loop.)

# -------------------------------------
# 3. A conditional expression is an expression built using the if-else operator. For example:

print(True if 0 >=0 else False)
# outputs True.

# -------------------------------------
# 4. A list comprehension becomes a generator when used inside parentheses 
# (used inside brackets, it produces a regular list). For example:

for x in (el * 2 for el in range(5)):
    print(x)

# outputs 02468.
# -------------------------------------
# 4. A lambda function is a tool for creating anonymous functions. For example:

def foo(f, x):
    return f(x)

print(foo(lambda x: x ** 0.5), 9)


# outputs 3.0.


# -------------------------------------
# 5. The map(fun, list) function creates a copy of a list argument, 
# and applies the fun function to all of its elements, 
# returning a generator that provides the new list content element by element. For example:

short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)

# outputs ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor'].
# -------------------------------------
# 6. The filter(fun, list) function creates a copy of those list elements, 
# which cause the fun function to return True. 
# The function's result is a generator providing the new list content element by element. 
# For example:

short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)


# outputs ['Python', 'Monty'].


# -------------------------------------
# 7. A closure is a technique which allows the storing of values 
# in spite of the fact that the context in which they have been 
# created does not exist anymore. For example:

def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    return inner


b_tag = tag('<b>')
print(b_tag('Monty Python'))


# outputs <b>Monty Python</b>
# -------------------------------------
# Exercise 1

# What is the expected output of the following code?

class Vowels:
    def __init__(self):
        self.vow = "aeiouy "  
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]


vowels = Vowels()
for v in vowels:
    print(v, end=' ')

# a e i o u y


# -------------------------------------
# Write a lambda function, setting the least significant bit of its integer argument, 
# and apply it to the map() function to produce the string 1 3 3 5 on the console.

any_list = [1, 2, 3, 4]
# even_list = # Complete the line here.
even_list = list(map(lambda n: n | 1, any_list))

print(even_list)


# -------------------------------------
# Exercise 3

# What is the expected output of the following code?

def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement


stars = replace_spaces()
print(stars("And Now for Something Completely Different"))

# And*Now*for*Something*Completely*Different

# -------------------------------------
# note: PEP 8, the Style Guide for Python Code, recommends that lambdas should not be assigned to variables, but rather they should be defined as functions.

# This means that it is better to use a def statement, and avoid using an assignment statement that binds a lambda expression to an identifer. For example:

# Recommended:
def f(x): return 3*x

# Not recommended:
f = lambda x: 3*x
# Binding lambdas to identifiers generally duplicates the functionality of the def statement. Using def statements, on the other hand, generates more lines of code.