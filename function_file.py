# We have seen different types of methods (functions) that are in built methods
# Python developed their own function
# Python has their own classes


# We had checked the classes using which function : type()

'''
string : str
integer : int
float : float
boolean : bool
set : set
complex : complex
dictionary : dict

There are two types of function
1. Inbuilt functions
2. User Defined Functions
User defined functions : Function created by the user
We created the function to define some specific task

'''

'''
# How to create the function
There are some rules to declare the function
1. function defined using def keyword
2. Function could not be start using number
3. Parenthesis is compulsory after defining the function name 
4. ':' are also necessory after the parenthesis

'''
#Type 1
'''
def welcome(): # indentation is most important
    print("Welcome in our Python class")

def funct1():
    print("Function 1")

def funct2():
    print("Function 2")
    print("Welcome in our Python class")
    print("Welcome in our Python class")
    print("Welcome in our Python class")
    print("Welcome in our Python class")


#welcome() # call the function welcome
funct2() # call the funct2
#funct1() # call the funct1
'''

#Type 2 function
#here we are defining the arguments or parameters in the function
'''
def welcome(name): # name is the argument we passed
    print("Welcome",name)

welcome("Sakshi") # defining the argument in the function call

'''

# Type 3 function
# return keyword is added
# return keyword is used to passed the value out of the function
# Create a function to add two values
'''
def add(num1,num2): # declare the variables in parenthesis
    add1=num1+num2 # variables inside the function called as local variables
    return add1

print(add(10,20)) # Define the values of parameters

'''


'''
a=input("Enter first number : ")
b=input("Enter second number : ")
c=input("Enter third number : ")

if a>b and a>c:
    print("Maximum is ",a)
elif b>c:
    print("Maximum is ",b)
else:
    print("Maximum is ",c)

'''

#Write a program to find the factorial of a number
#factorial:  5*4*3*2*1= 120
'''
n=5
fact=1 #we have to store the multilplication

for i in range(1,n+1):
    fact=fact*i    #120=120*5

print("Factorial is ",fact)

'''
'''

#Type 4 function

#we can mention the default values
def add(num1=0,num2=0,num3=0):
    add1=num1+num2+num3
    return add1

print(add()) # without argument                             0+0+3=3
print(add(2)) # with one argument                           2+0+3=5
print(add(2,3)) ## with two arguments           2+3+3=8
print(add(2,3,4)) # with all arguments    2+3+4=9

# If you do not mention the variable value that time it will consider the default values
# But if you give the variable value then it will consider the values declared in function call
'''



# Assignment : 02/03
'''
1. Define a function to find the maximum from the three numbers
2. Define a function to find the maximum from two numbers
3. Define a function to find the factorial of the number given by user'''


#area of a triangle

def cir_areas(r=1):
    cir_area=3.14*r*r
    return  cir_area

def rect_areas(b=1,h=1):
    rect_area = b * h
    return rect_area

def tri_areas(b=1,h=1):
    tri_area=1/2*b*h
    return tri_area

print("Area of Triangle is ",tri_areas(2,6))
print("Area of Reactangle is ",rect_areas(5,3))
print("Area of circle is ",cir_areas(5))





'''
#lambda function
#Anonymous function
#lambda is a single line function

#Syntax:

#function_name : lambda arguments: expression
#write a lambda function to add two numbers

add = lambda a,b : a+b #function declaration

print(add(4,6)) #function call

# write a lambda function to find the square of a number

sq = lambda a : a**2

print(sq(4))




'''






















