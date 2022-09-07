# basic list 
# list data type - Collection of items
'''
marks = [22, 34, 21]
print(marks) #  Print All List
print(marks[2]) # Print element at 2 index
print(marks[0:2])# Print from 0 , 1 not count 2
print(marks[-1]) #Start Counting From Last
'''

#For Loop In The List
'''
marks = [21, 24, 80, 49, 40, 39]
for score in marks:
    print(score)
'''  
marks = [20, 46, 63, 353, 2425, 5336, 24242]
marks.append(69) # add the element at the last of the list
print(marks)

marks = [33, 23, 556, 142, 1246, 4646, 5454]
marks.insert(0,21) # Index number -> 0 , Element ->21 
# can add the element at any index number in the list
print(marks)

# Check The Number is Exist In the List or Not
print(21 in marks)# give Output as True / False

print(len(marks)) # Will Print the Length of List Marks
  
# Printing Marks Using While Loop
marks = [33, 23, 556, 142, 1246, 4646, 5454]
i = 0
while i < len(marks):
    print(marks[i])
    i = i+1  
marks.clear() # Will clear the all list
print(marks)


#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
marks = ['apple', 'banana', 'cherry']
marks.insert(2,'straberry')

# To add an item to the end of the list, use the append() method:
marks = ['12', '24', '37']
marks.append('286')
print(marks)
