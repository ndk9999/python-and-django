# Use import statement to import a module
import datetime

# This is one-line comment. Below is an example of multiline comments using a multiline string.
"""
This multiline string can be considered as multiline comments because
Python will ignore string literals that are not assigned to a variable
"""

# Use print function to write content directly to console
print('Whatever you want to show to your users')

# Indentation refers to the spaces at the beginning of a code line.
# Python uses indentation to indicate a block of code.
# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error
if 5 > 2:
  print("Five is greater than two!")
  print("5 + 2 = ", 5 + 2)

# In Python, variables are created when you assign a value to it
# Python has no command for declaring a variable.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
name = "Your Name"
age = 25
dob = datetime.datetime(1990, 6, 11)

print(name)
print(age)