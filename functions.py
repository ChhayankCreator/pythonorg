#A function is a block of code which only runs when it is called.

#You can pass data, known as parameters, into a function.

#A function can return data as a result.
''' In Python a function is defined using the def keyword:   '''

'''3 type of function'''
# In-built Functions  -> int(), str(), bool()
# Module Functions    -> import math
# User-defined Functions 

'''
def function_name (parameters):
    // do something
'''
def addition(num_one,num_two):
    num_one=input("Enter ist num")
    
    num_two=input("Enter Second Number")
    num_one=int(num_one)
    num_two=int(num_two)
    print(num_one+num_two)

addition(2,6)    
