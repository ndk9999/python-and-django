# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:
#   * Text Type:	    str
#   * Numeric Types:	int, float, complex
#   * Sequence Types:	list, tuple, range
#   * Mapping Type:	    dict
#   * Set Types:	    set, frozenset
#   * Boolean Type:	    bool
#   * Binary Types:	    bytes, bytearray, memoryview
#   * None Type:	    NoneType

x = "Hello World"	                # str
x = 20	                            # int
x = 20.5	                        # float
x = 1j	                            # complex
x = ["apple", "banana", "cherry"]	# list
x = ("apple", "banana", "cherry")	# tuple
x = range(6)	                    # range
x = {"name" : "John", "age" : 36}	# dict
x = {"apple", "banana", "cherry"}	# set
x = frozenset({"apple", "banana", "cherry"})	#frozenset
x = True	                        # bool
x = b"Hello"	                    # bytes
x = bytearray(5)	                # bytearray
x = memoryview(bytes(5))	        # memoryview
x = None	                        # NoneType

y = b"Hello"
print(y)

# In Python, the data type is set when you assign a value to a variable
# You can get the data type of any object by using the type() function
x = 5
print(type(x), type(y))


# ==================================================================================
# Numbers
# There are three numeric types in Python:
#   * int       : or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#   * float     : or "floating point number", is a number, positive or negative, containing one or more decimals.
#   * complex   : Complex numbers are written with a "j" as the imaginary part

p = 1    # int
q = 2.8  # float
r = 1j   # complex

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100

# Complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j

# You can convert from one type to another with the int(), float(), and complex() methods
# Note: You cannot convert complex numbers into another number type.
a = float(p)        #convert from int to float
b = int(q)          #convert from float to int
c = complex(x)      #convert from int to complex

# To make random numbers, use built-in module random
import random
print(random.randrange(1, 10))


# ==================================================================================
# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# You can display a string literal with the print() function:
print("Hello")
print('Hello')

# You can assign a multiline string to a variable by using three quotes or three single quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

# Note: In the result, the line breaks are inserted at the same position as in the code.

# Strings in Python are arrays of bytes representing unicode characters.
# Square brackets can be used to access elements of the string. 
# The first character has index 0.
# A single character is simply a string with a length of 1.
a = "Hello, World!"
print(a[1])

# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
  print("Yes, 'free' is present.")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
print("expensive" not in txt)

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# You can return a range of characters by using the slice syntax.
b = "Hello, World!"
print(b[2:5])           # Output: llo

# Get the characters from the start to position 5 (not included)
print(b[:5])            # Hello

# Get the characters from position 2, and all the way to the end
print(b[2:])            # llo, World!

# Use negative indexes to start the slice from the end of the string
print(b[-5:-2])         # orl

a = " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip())        # returns "Hello, World!"
print(a.replace("H", "J"))
print(a.split(","))     # returns ['Hello', ' World!']

# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

# We can combine strings and numbers by using the format() method
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# We can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Method	    Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	    Returns a centered string
# count()	    Returns the number of times a specified value occurs in a string
# encode()	    Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	    Searches the string for a specified value and returns the position of where it was found
# format()	    Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	    Searches the string for a specified value and returns the position of where it was found
# isalnum()	    Returns True if all characters in the string are alphanumeric
# isalpha()	    Returns True if all characters in the string are in the alphabet
# isascii()	    Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	    Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	    Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	    Returns True if all characters in the string are whitespaces
# istitle()	    Returns True if the string follows the rules of a title
# isupper()	    Returns True if all characters in the string are upper case
# join()	    Joins the elements of an iterable to the end of the string
# ljust()	    Returns a left justified version of the string
# lower()	    Converts a string into lower case
# lstrip()	    Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	    Returns a string where a specified value is replaced with a specified value
# rfind()	    Searches the string for a specified value and returns the last position of where it was found
# rindex()	    Searches the string for a specified value and returns the last position of where it was found
# rjust()	    Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	    Splits the string at the specified separator, and returns a list
# rstrip()	    Returns a right trim version of the string
# split()	    Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	    Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	    Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	    Converts a string into upper case
# zfill()	    Fills the string with a specified number of 0 values at the beginning

# ==================================================================================
# Boolean
# Booleans represent one of two values: True or False.

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# The bool() function allows you to evaluate any value, and give you True or False in return
#   * Almost any value is evaluated to True if it has some sort of content.
#   * Any string is True, except empty strings.
#   * Any number is True, except 0.
#   * Any list, tuple, set, and dictionary are True, except empty ones.

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Python also has many built-in functions that return a boolean value, 
# like the isinstance() function, which can be used to determine if an 
# object is of a certain data type
x = 200
print(isinstance(x, int))


# ==================================================================================
# Lists
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:
fruits = ["apple", "banana", "cherry"]
print(fruits)

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# If you add new items to a list, the new items will be placed at the end of the list.

# To determine how many items a list has, use the len() function
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List items can be of any data type. A list can contain different data types.
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

# List items are indexed and you can access them by referring to the index number
# The first item has index 0.
thislist = ["apple", "banana", "cherry"]
print(thislist[1])          # banana

# Negative indexing means start from the end,
# -1 refers to the last item, -2 refers to the second last item etc.
print(thislist[-1])         # cherry

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])        # ["cherry", "orange", "kiwi"]
print(thislist[:4])         # ["apple", "banana", "cherry", "orange"]
print(thislist[2:])         # ["cherry", "orange", "kiwi", "melon", "mango"]

# Specify negative indexes if you want to start the search from the end of the list
print(thislist[-4:-1])      # ["orange", "kiwi", "melon"]

# To determine if a specified item is present in a list use the in keyword
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# To change the value of a specific item, refer to the index number
thislist[1] = "blackcurrant"
thislist[1:3] = ["blackcurrant", "watermelon"]

# If you insert more items than you replace, the new items will be inserted 
# where you specified, and the remaining items will move accordingly
thislist[1:2] = ["blackcurrant", "watermelon"]      # watermelon is inserted at index 2

# If you insert less items than you replace, the ole items will be removed 
# where you specified, and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]                      # cherry is removed

# To insert a new list item, without replacing any of the existing values, 
# we can use the insert() method.
thislist.insert(2, "watermelon")

# To add an item to the end of the list, use the append() method
thislist.append("orange")

# To append elements from another list to the current list, use the extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

# The extend() method does not have to append lists, you can add any iterable object 
# such as tuples, sets, dictionaries etc.
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)

# The remove() method removes the specified item (removes the first occurance).
thislist.remove("banana")

# The pop() method removes the specified index.
# If you do not specify the index, the pop() method removes the last item.
thislist.pop(1)
thislist.pop()        # removes the last item

# The del keyword also removes the specified index
del thislist[0]

# The clear() method empties the list.
thislist.clear()

# You can loop through the list items by using a for loop
for x in thislist:
  print(x)

# Use the range() and len() functions to create a suitable iterable and
# loop through the list items by referring to their index number
for i in range(len(thislist)):
  print(thislist[i])

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# List Comprehension offers the shortest syntax for looping through lists
# Syntax: newlist = [expression for item in iterable if condition == True]
[print(x) for x in thislist]
newlist = [x for x in fruits if "a" in x]
newlist = [x.upper() for x in fruits if "a" in x]
newlist = [x if x != "banana" else "orange" for x in fruits]

# List objects have a sort() method that will sort the list alphanumerically
# By default the sort() method is case sensitive
thislist.sort()                   # ascending
thislist.sort(reverse = True)     # descending

# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)

# if you want a case-insensitive sort function, use str.lower as a key function
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)

# The reverse() method reverses the current sorting order of the elements
thislist.reverse()

# Copy a list
mylist = thislist.copy()
list(thislist)

# Join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2         # Use operator +

for x in list2:               # Use for loop
  list1.append(x)

list1.extend(list2)           # Use extend method


# ==================================================================================
# Tuples
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc

print(thistuple[1])         # prints the second item in the tuple
print(thistuple[-1])        # prints the last item in the tuple
print(len(thistuple))       # determines how many items a tuple has
print(type(thistuple))      # gets the data type of a tuple
print(thistuple[2:5])       # returns the third, fourth, and fifth item
print(thistuple[:4])        # returns the items from the beginning to fourth item
print(thistuple[2:])        # returns the items from index 2nd and to the end
print(thistuple[-4:-1])     # searches from the end of the tuple

# To create a tuple with only one item, you have to add a comma after the item, 
# otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)

#NOT a tuple
thistuple = ("apple")

# Tuple items can be of any data type and a tuple can contain different data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple1 = ("abc", 34, True, 40, "male")

# Using the tuple() method to make a tuple
thistuple = tuple(("apple", "banana", "cherry"))    # note the double round-brackets

# To determine if a specified item is present in a tuple use the in keyword
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Tuples are unchangeable, meaning that you cannot change its values, add, or remove 
# items once the tuple is created. But you can convert the tuple into a list, change 
# the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
y.append("orange")
y.remove("apple")
x = tuple(y)

# Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
  
# The del keyword can delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple

# Unpacking a tuple: extract the values back into variables
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits      # red will be a list
(green, *tropic, red) = fruits      # tropic will be a list

# You can loop through the tuple items by using a for loop or while loop.
for x in thistuple:
  print(x)

for i in range(len(thistuple)):
  print(thistuple[i])

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# To join two or more tuples you can use the + operator
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

# If you want to multiply the content of a tuple a given number of times, 
# you can use the * operator
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2


# ==================================================================================
# Sets
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets are unordered, so you cannot be sure in which order the items will appear.
# Sets cannot have two items with the same value. Duplicate values will be ignored.
thisset = {"apple", "banana", "cherry", "apple"}      # apple, banana, cherry

# The values True and 1 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", True, 1, 2}   # banana, cherry, True, apple, 2

# The values False and 0 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", False, True, 0}   # 0 will be removed

# Get the number of items in a set
print(len(thisset))

# Set items can be of any data type and a set can contain different data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

# Using the set() constructor to make a set
thisset = set(("apple", "banana", "cherry"))    # note the double round-brackets

# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop
# or ask if a specified value is present in a set, by using the in keyword
for x in thisset:
  print(x)

print("banana" in thisset)

# Add an item to a set, using the add() method
thisset.add("orange")

# To add items from another set into the current set, use the update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

# The object in the update() method does not have to be a set, it can be any 
# iterable object (tuples, lists, dictionaries etc.)
mylist = ["kiwi", "orange"]
thisset.update(mylist)

# To remove an item in a set, use the remove(), or the discard() method.
# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.
thisset.remove("banana")
thisset.discard("banana")

# You can also use the pop() method to remove a random item
x = thisset.pop()       # x is the removed item

# The clear() method empties the set
thisset.clear()

# The del keyword will delete the set completely
del thisset

# Join Two Sets
set3 = set1.union(set2)
set1.update(set2)

#  get the items that exist in both set x, and set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
z = x.intersection(y)

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
z = x.symmetric_difference(y)


# ==================================================================================
# Dictionaries





# ==================================================================================






# ==================================================================================






# ==================================================================================






# ==================================================================================