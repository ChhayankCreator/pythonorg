
'''Python allows you to assign values to multiple variables in one line:

Example
x, y, z = "Orange", "Banana", "Cherry"'''


'''And you can assign the same value to multiple variables in one line:

Example
x = y = z = "Orange"

'''
'''from re import X


a = input('Enter Your Name: ')
a = str(a) 

print (type(a))'''

# Global Variables
'''Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

Example
Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()'''

# Local Variable
'''If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

Example
Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)'''

# The global Keyword
'''   To create a global variable inside a function, you can use the global keyword.
  '''
'''def quality():
    global x
    x = "fantastic"  
quality()
print('python is' +x)'''
# Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))