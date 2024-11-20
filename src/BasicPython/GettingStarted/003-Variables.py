import datetime

# Variables are containers for storing data values.

# In Python, variables are created when you assign a value to it
# Python has no command for declaring a variable.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
name = "Your Name"
age = 25
dob = datetime.datetime(1990, 6, 11)

# Output value of variable to console
print(name)
print(age)


# Rules for Python variables:
#   * A variable name must start with a letter or the underscore character
#   * A variable name cannot start with a number
#   * A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#   * Variable names are case-sensitive (age, Age and AGE are three different variables)
#   * A variable name cannot be any of the Python keywords.
myvar = "Python"
my_var = "Python"
_my_var = "Python"
myVar = "Python"
MYVAR = "Python"
myvar2 = "Python"

# For variable names with more than one word, there are several techniques to make them more readable
myVariableName = "Python"           # Camel Case
MyVariableName = "Python"           # Pascal Case
my_variable_name = "Python"         # Snake Case

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)          # x will be '3'
y = int(3)          # y will be 3
z = float(3)        # z will be 3.0

# You can get the data type of a variable with the type() function.
x = 5
y = "Python"

print(type(x))
print(type(y))

# String variables can be declared either by using single or double quotes
x = "Python"
# is the same as
x = 'Python'

# However, variable names are case-sensitive.
# In the following example, A will not overwrite a.
a = 4
A = "Python"


# Python allows you to assign values to multiple variables in one line
# Make sure the number of variables matches the number of values, or else you will get an error.
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

# This syntax is very useful in some cases, for example, swapping two values
x, y = y, x

print(x)
print(y)

# And you can assign the same value to multiple variables in one line
x = y = z = "Orange"

print(x, y, z)

# If you have a collection of values in a list, tuple etc. 
# Python allows you to extract the values into variables.
# This technique is called unpacking or destructuring.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x, y, z)


# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)   # Use global variable x inside function

# Call function myfunc
myfunc()


# If you create a variable with the same name inside a function, this
# variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global 
# and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)       # Output: Python is fantastic

myfunc()

print("Python is " + x)         # Output: Python is awesome


# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

