#FUNCTIONS AD FIRST CLASS OBJECTS:
 # ASSIGN A FUNCTION TO A VARIABLE

'''
def display(str):
    return 'Hi'+ str
x= display('Vijay')
print(x)
'''


# Function Inside a Function:
'''
def display(str):
    def message():
        return 'How are you?'
    result= message()+str
    return result
print(display("Vijay"))
'''

# Function as a Parameter to Other Function:

#Wrong Syntax: 

'''def display(fun):
    return 'Hi'+ Fun
def message():
    return 'How are You?'
print(display(message)) # call display function and pass message() function.
'''
# In above print stmt instead of defining message function i.e message() we wrote it as string 'message
#Corrected Syntax:
'''
def display(fun):
    return 'Hi'+ Fun
def message():
    return 'How are You?'
print(display(message())) # call display function and pass message() function.
'''

# Function returning other function
def display():
    def message():
        return 'How are you?'
    return message()
# call display() function and it returns message() fuction, fun refers to name:message.
print(fun)

