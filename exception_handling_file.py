'''
Types of errors
1. Syntax
2. Runtime '''

'''
x=10
if x==10:
    print("Hello")
'''
#whenever the syntax error occurs programmer has to solve all errors
# only after that your program will be run or successful


#run time errors are also called as 'Exceptions'
# end user : client(the person who used our application)
# while executing a program  if something goes wrong because of
# end user input or
# programming logic
# memory allocation
#if any one of them is satisfied then the program will give us a runtime error

# print(10/0)
# print(10/"ten")

# Exception: An unexpected event occurs and that event disturbs your normal flow of your program then it is an exception
# Exception Handling

#try and except block
'''
try:(keyword)
    print(10/0)
except:(keyword)
    print()
'''
#exception is nothing but the object in python


#Syntax
'''try:
    risky code
except ErrorName:
    HAndling code
    '''

#try-except

'''
print("Hello")
try:
    print(10/0) #zerodivisionerror
    #print("    ")
except ZeroDivisionError:
    print(10/2) #handling statement
'''
# control flow of the statements

'''
try:
    stmt1
    stmt2
    stmt3
    
except ErrorName:
    stmt4
    
stmt5


Case1:  no exception occurs then stmt 1,2,3,5 is executed
Case2 : exception occurs at stmr2 then stmt 1,4,5 and normally terminated
Case3 : if exception occurs at stmt 2 and excep block is not found for stmt2 then stnmt1 is executed, Abnormal termination
'''

#If there are multiple exceptions we have to handle then we can write multiple except blocks

#multiple exceptions

#different error handles using multiple except blocks
'''
try:
    x= int(input("Enter first number "))
    y= int(input("Enter second number "))
    print(x/y)
except ZeroDivisionError:
    print("Can't divide by Zero")
except ValueError:
    print("Please enter any integer value only")

'''
#multiple exceptions handled using single except statement
'''try:
    x= int(input("Enter first number "))
    y= int(input("Enter second number "))
    print(x/y)

except (ZeroDivisionError,ValueError):  #to reduce space complexity
    print("Invalid Input ")
'''

# Default except block
# for unknown error (if we dont knkow about the error that time we define the default except block )

'''
try:
    x = int(input("Enter first number "))
    y= int(input("Enter second number "))
    print(x/y)

except ZeroDivisionError:
    print("Invalid Input ")
except:
    print("DefaultException : Please provide valid input")
'''

#finally block

'''
try:
    risky code
except ErrorName:
    handling code
finally:
    cleanup code(resource deallocation code or resource releasing code)
    
#the main purpose of finally block to maintain the cleanup code
os._exit(0)

'''

# case:1 - If there is no exception

'''try:
    print("try")  #no error
except:
    print("Except")
finally:
    print('finally')'''

# output: try finally

# if exception occurs or may be not occurs the finally block will be executed

#case 2 : If there is an exception rised but handled
'''
try:
    print("try")
    print(10/0) # exception occurs
except ZeroDivisionError:
    print("Except")
finally:
    print('finally')

'''
#case 3 - If there is an exception but not handled
'''try:
    print("try")
    print(10/0) # exception occurs
except NameError:
    print("Except")
finally:
    print('finally')
'''

'''import os #importing the package OS

try:
    print("try")
    os._exit(0)
except NameError:
    print("Except")
finally:
    print('finally')

'''

# nested try except:
'''
try:
    print("Outer try block")
    try:
        print("Inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
        
except:
    print("Outer except block")
finally:
    print("Outer finally block")

'''

# else block in try except finally

'''
try:
    risky code
except:
    will be executed if the exception inside try
else:
    will be executed if there is no exception inside try
finally:
    will be executed whether the exception raised or not raised

'''
'''
try:
    print("try")
    #print(10/0)
except:
    print("except")
else:
    print("else")
finally:
    print("finally")

'''

#Types of exception
'''
1. Predefined exceptions : inbuilt exceptions
#examples of exception
1.ZeroDivisionError
2.ValueError
3.NameError

2.User defined exceptions : customized exceptions

class class_name(parent class name):     # parent class is always exception
    def __init__(self,arg):
        self.msg=msg
'''
'''#Example of user defined exception

class TooYoungException(Exception):
    def __init__(self,msg): #constructor
        self.msg=msg

class TooOldException(Exception):
    def __int__(self,msg):
        self.msg=msg

age = int(input("Enter Age = "))

try:
    if age<18:
        raise TooYoungException("Please wait some more time you will get best match soon!!!")
    elif age>60:
    
    
    
except(TooYoungException, TooOldException) as msg:
    print(msg)

'''






