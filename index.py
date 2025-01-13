def is_even(num):
    """
    This fucntion returns if a given number is even or odd
    Input - any valid integer
    output - odd/even
    """
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
# integer = int(input("Enter a input: "))
# print(is_even(integer))

# How to access documentation
print(is_even.__doc__)
print(print.__doc__)

# ------------------------------------------
# Parameter VS Arguments
# 1. Default Argument
# 3. Positional Argument
# 2. Keyword Argument

# 1. Default Argument
# If the parameters did not get any value, it will take the default value. a = 1 amd b = 1
def power(a = 1, b= 1):
    return a**b
print(power(3,4))
print(power(5))
print(power())

# 2. Posiitonal Argument
# First Argument is passed to first parameter and so on
print(power(2,3))

# 3. Keyword Argument
# First Argument(b) is passed to 2nd parameter and Second Argument(a) is passed to 1st parameter
print(power(b = 3, a = 2))

# -----------------------------------
# *args and **kwargs
# *args - Positional Arguments
# **kwargs - Keyword Arguments

# *args/ or any other word can be used
# Allows us to pass a variable number of non-keyword arguments to a function
def mul(*args):
    product = 1
    for i in args:
        product = product * i
    return product

print(mul(1,2,3,4,5))


# **kwargs/ or any other word can be used
# Allows us to pass a variable number of keyword arguments to a function
# It sends a Key-valus pair
def add(**kwargs):
    sum = 0
    for i in kwargs.values():
        sum = sum + i
    return sum

print(add(a = 1, b = 2, c = 3, d = 4, e = 5))

def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display(india = "delhi", sirilanka = "colombo", nepal = "kathmandu", pakistan = "Islamabad")

# Points to remenber
# Order of arguments matter(normal -> *args -> **kwargs)
# The words *args and **kwargs are conventional, you can use any name of your choice


# --------------------------------------------

# How Functions are executed in memory
# Without Return statement
def iseven(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

print(iseven(5))

L = [1,2,3]
print(L.append(4))
print(L)


# -------------------------------
# Valriable Scope

def g(y):
    """Since we donot have x in local scope(function), the interperator 
    will search for it at global level"""
    print("Function g() called")
    print(x)
    print(x + 1)
x = 5
g(x)
print(x)

def f(y):
    print("Function f() called")
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)

def h(y):
    # It will throw an error since h() can access the x but not change it
    # x += 1
    print("Error")
x = 5
h(x)
print(x)


# Global keyword can be used to change that variable
def j(y):
    global x 
    x += 1
x = 5
j(x)
print(x)


def k(x):
    x = x + 1
    print("in k(x): x =", x)
    return x

x = 3
z = k(x)
print("in main pregram scope: z = ", z)
print("in main pregram scope: x = ", x)


# ----------------------------------

# Nested Functions
def f():
    def g():
        print("Inside g()")
    g()
    print("Inside f()")

f() # First, Inside g(), then Inside f()


def g(x):
    def h():
        x = "abc"
    x = x + 1
    print("Inside g(): x = ", x)
    h()
    return x

x = 3
z = g(x)



# ------------------------------------

# Functions are First Class Citizens
# In Easy words, functions in Python are data types

def square(num):
    return num**2

print(square(2))
print(type(square))

x = square
print(x(3))