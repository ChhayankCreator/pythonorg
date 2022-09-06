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