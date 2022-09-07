First_Name = "Tony"
Last_Name  = "Stark"
age = 51
is_genius = True
print(First_Name, Last_Name,age,"isgenius",is_genius)


#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# HOW TO COMBINE STRING AND NUMBERS
'''Using Format() Function '''

age = 32
txt = "My NAME IS AMARENDRA SAHA AND MY AGE IS {}" 
print (txt.format(age))
