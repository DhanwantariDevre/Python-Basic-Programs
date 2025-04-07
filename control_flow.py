#Control flow statements
#Conditional statements
#We are checking the conditions here

#if : if the condition is true then the block of code will be executed

'''age=16

if age>=18:
    print("You are eligible to vote")
else:
    print("You are minor")
'''

#Check whether the number is positive or negative
#else : if the condition is false then the else block will be executed

'''x = 0

if x<0:
    print("Negative")
else:
    print("Positive")


'''

#elif
#The elif statement allows you to check multiple conditions
# It stands for " else if "

# if age is less than 13 then you re a child
#if age is less than 18 then you are a teenager
# if your age is greater than 18 then you are adult
'''
age=21

if age<13:
    print("You are a child")
elif age<18:
    print("You are a teenager")
else:
    print("You are an adult")'''



#nested if
#check the condition within a condition
#write one or more if, elif,else statements inside another if, elif, else statement

#Check whether the number is even, odd, positive, negative


num=int(input("Enter the number = "))

if num>0:
    print("Number is positive")
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")
elif num==0:
    print("Zero")
else:
    print("Number is negative")


#Simple calculator

#Take the input of two numbers
#Take the operator as a input
#write the conditions to check the operation
#If user gives invalid input that time gives an error message to user
#print the result

































