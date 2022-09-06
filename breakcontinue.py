'''
student = ["ram", "shyam", "amarendra", "chhayank", "Asusvivobook"]
i = 0
while i < len(student):
    if i == 3:
        break
    print(student[i])
    i=i+1
    '''
student = ["ram", "shyam", "amarendra", "chhayank", "Asusvivobook"]

for name in student:
    if name  == "chhayank":
       ''' break/continue'''
    print(name)
    
#Escape Character
'''
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.
'''
#EXAMPLE ->
txt = "Hello, Everyone this is \"Chhayank Sharma\" , Good Morning"
print (txt)    

txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

# \n	New Line

txt = "Hello\nWorld!"
print(txt)

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)


#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 




