#'hello' is the same as "hello".
print("Hello")
print('Hello')

#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign String to a Variable
a = "Hello"
print(a)

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#Note: in the result, the line breaks are inserted at the same position as in the code.


#Strings are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "banana":
  print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String
"To check if a certain phrase or character is present in a string, we can use the keyword in."
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Slicing
b = "Hello, World!"
print(b[2:5])

#Note: The first character has index 0.


#Slice From the Start
b = "Hello, World!"
print(b[:5]) #Hello

#Slice To the End
b = "Hello, World!"
print(b[2:]) #llo, World!

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2]) #orl

#Modify Strings

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:
a = "   Hello, World!   "
print(a.strip()) # returns "Hello, World!"

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation

#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Format - Strings

#Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)


#Escape Characters

#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

# Code	Result	
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value


#String Methods
#Note: All string methods return new values. They do not change the original string.

# capitalize()    – Converts the first character to upper case
# casefold()      – Converts string into lower case
# center()        – Returns a centered string
# count()         – Returns the number of times a specified value occurs in a string
# encode()        – Returns an encoded version of the string
# endswith()      – Returns True if the string ends with the specified value
# expandtabs()    – Sets the tab size of the string
# find()          – Searches the string for a specified value and returns the position
# format()        – Formats specified values in a string
# format_map()    – Formats specified values in a string
# index()         – Searches the string for a specified value and returns the position
# isalnum()       – Returns True if all characters are alphanumeric
# isalpha()       – Returns True if all characters are alphabet letters
# isascii()       – Returns True if all characters are ASCII characters
# isdecimal()     – Returns True if all characters are decimals
# isdigit()       – Returns True if all characters are digits
# isidentifier()  – Returns True if the string is a valid identifier
# islower()       – Returns True if all characters are lower case
# isnumeric()     – Returns True if all characters are numeric
# isprintable()   – Returns True if all characters are printable
# isspace()       – Returns True if all characters are whitespaces
# istitle()       – Returns True if the string follows title rules
# isupper()       – Returns True if all characters are upper case
# join()          – Joins elements of an iterable to the string
# ljust()         – Returns a left-justified version of the string
# lower()         – Converts a string into lower case
# lstrip()        – Returns a left-trimmed version of the string
# maketrans()     – Returns a translation table for translations
# partition()     – Returns a tuple where the string is split into three parts
# replace()       – Replaces a specified value with another value
# rfind()         – Returns the last position of a specified value
# rindex()        – Returns the last position of a specified value
# rjust()         – Returns a right-justified version of the string
# rpartition()    – Returns a tuple where the string is split into three parts
# rsplit()        – Splits the string and returns a list (from the right)
# rstrip()        – Returns a right-trimmed version of the string
# split()         – Splits the string and returns a list
# splitlines()    – Splits the string at line breaks
# startswith()    – Returns True if the string starts with the specified value
# strip()         – Returns a trimmed version of the string
# swapcase()      – Swaps lower case to upper case and vice versa
# title()         – Converts the first character of each word to upper case
# translate()     – Returns a translated string
# upper()         – Converts a string into upper case
# zfill()         – Fills the string with zeros at the beginning
