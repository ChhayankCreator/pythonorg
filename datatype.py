'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
#complex
x = 1j
print(type(x))

#range
x = range(6)
print(type(x))

# Python does not have a random() function to make a random number, but Python has a built-in module called random

#Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1,10))

#Slicing
#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

#Negative Indexing
'''Use negative indexes to start the slice from the end of the string:
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):'''

b = "Hello, World!"
print(b[-5:-2])
