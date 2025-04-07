'''
class Dog:              #class declared
    action='bark'       #attribute created

obj1 = Dog()  #creating an object of class Dog as dog1
print(obj1.action)    #Accessing the attribute using object dog1

'''
from multiprocessing.managers import public_methods
from test.test_importlib.resources.test_resource import names

'''
class Employee:
    def putData(self):    # method 1 declared as putData()
        self.id=int(input("Enter employee id = "))
        self.name=input("Enter Employee name = ")
        self.salary= float(input("Enter the salary = "))

    def display(self):    # method 2 declared as display()
        print("Employee ID : ",self.id)
        print("Employee Name :",self.name)
        print("Employee salary : ",self.salary)

emp1= Employee()
emp1.putData()
emp1.display()

emp2= Employee()
emp2.putData()
emp2.display()

emp3= Employee()
emp3.putData()
(emp3.display())

'''


#Inheritance

# Parent class or super class
# child class or sub class
'''
class OTTSubscription:                               # parent class
    def __init__(self,sub_id,plan,total_payment):
        self.id = sub_id                            # we are giving the reference through self keyword
        self.plan = plan
        self.payment = total_payment

    def Subscribe(self):
        print(f"Subscriber with {self.id} id subscribed to {self.plan} plan")

    def Unsubscribe(self):
        print(f"Subscriber with {self.id} id unsubscribed to {self.plan} plan")

class PremiumSubscription(OTTSubscription):           # child class
    def __init__(self,sub_id,plan,total_payment,screen):
        super().__init__(sub_id, plan, total_payment)  # super() is used to access the attributes from the parent class
        self.screen=screen

    def set_max_screens(self,screen):
        self.screen=screen
        print(f"Maximum screen set to {self.screen} in the Premium Plan")


'''

#to implement the data abstraction, the python abc module is used
#Abstract method can not be instantiated directly and serves as a blueprint of other classes
#abstract method can be define using '@abstractmethod' decorator
'''
# from module_name import method_name, classname
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side * self.side

circle1 = Circle(5)
square1 = Square(4)

print(f"Area of Circle = {circle1.area()}")
print(f"Area of Square = {square1.area()}")



'''

#Encapsulation
# we restrict some data to some of the object

#How we can do the encapsulation
#We are using the access modifiers
'''
1. public : Accessible from everywhere

public members have no prefix

2. protected : Accesssible within the class and its subclass

protected members have the prefix with single underscore'_'

3. private : Accessible only within the class

private members have the prefix with double underscore '__'

'''

'''
class BankAccount:
    def __init(self,acc_number, balance):
        self.__acc_number=acc_number   #private
        self._balance = balance     #protected

    def deposit(self,amount):
        if amount > 0:
            self._balance = self.balance + amount #self.balance += amount

    def withdraw(self,amount):
        if 0<amount <= self.balance:
            self._balance -= amount
        else:
            print("Insufficient balance ")

    def get_balance(self):
        return self._balance



'''
'''
#public method
class Public:
    def __init__(self):
        self.name= "Sakshi" #public attribute declaration

    def display(self):
        print(self.name) # public method

obj1 = Public()
obj1.display()
print(obj1.name)

'''
'''#protected members
class Protected:
    def __init__(self):
        self._age=21    #protected attribute

class Prosubclass(Protected):
    def display_age(self):
        print(self.age) #protected attribute called

obj1=Prosubclass()
obj1.display_age()
'''

'''#Private Members

class Private:
    def __init__(self):
        self.__salary=50000      #private attribute

    def salary(self):
        return self.__salary #access from public method

obj = Private()
print(obj.salary())

'''


#Polymorphism
# here we have same function but different behaviour
#Polymorphism in function

'''

#It is also known as operator overloading
def add(a,b):
    return a+b

print(add(3,4))                  # integer addition
print(add("Hello", " World"))    #string concatenation
print(add([1,2], [3,4]))         #list concatenation

'''
# Polymorphism allows methods in different classes to share the same name but different behaviour
# If we have to implement polymorphism then we can acheived it through inheritance and encapsulation
# it acHeives the complexity problem and made the sharing behaviour

'''class Shape:                     #parent class Shape
    def area(self):
        return "None"


class Rectangle(Shape):              #child class rectangle
    def __init__(self, length, breadth):      #constructor __init__ method
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side*self.side


shape1 = Rectangle(2,3)
shape2 = Square(4)

shape=[Rectangle(2,3), Square(4)]
for i in shape:
    print(f"Area = {i.area()}")
'''

#Polymorphism in Python using None keyword
'''
class Example:
    def add(self,a=None,b=None,c=None):
        x=0
        if a!=None and b!=None and c!=None:
            x=a+b+c
        elif a!=None and b!=None and c==None:
            x=a+b
        return x

obj=Example()

print(obj.add(10,20,30))
print(obj.add(10,20))

'''
'''
# when we are declaring method with same name in same class but having different behaviour
#same name : different behaviour
#Method Overloading

class Example:
    def add(self,a,b):
        x=a+b
        return x

    def add(self, a, b, c):
        x=a+b+c
        return x

obj = Example()

print(obj.add(10, 20))
print(obj.add(10, 20, 30))

'''


#Method Overrriding
#the specific implementation of the method is already provided by the parent class by child class
#It is used to change the behaviour of the method
#Condition: there is a need for atleast two classes to implement method overriding
#Inheritance always required as we need child class and parent class
'''
class A:
    def funct1(self):
        print("WE are in Function1 of CLass A")

    def funct2(self):
        print("We are in function2 of class A")


class B:
    def funct1(self):
        print("We are in function1 of class B")

    def funct3(self):
        print("We are in function3 of class B")

#create an instance
obj = B()

#call the overrided function
obj.funct1()'''


#single inheritance

'''
#parent class
class Parent:
    def fun1(self):
        print("We are in Parent class")

#child class
class Child(Parent):
    def fun2(self):
        print("We are in Child class")

obj=Child()
obj.fun1()
obj.fun2()
'''

#Multiple Inheritance
#More than one parent class and one child class
'''
#first parent claass
class Mother:
    mothername=""

    def mother(self):
        print(self.mothername)

#second parent class
class Father:
    fathername=""

    def father(self):
        print(self.fathername)


#child class
class  Daughter(Mother,Father):
    def parents(self):
        print("Father = ",self.fathername)
        print("Mother = ",self.mothername)

d1=Daughter()
d1.fathername = "Ram"
d1.mothername = "Sita"
d1.parents()

d2=Daughter()
d2.fathername = "Arun"
d2.mothername = "Suvarna"
d2.parents()

'''

#Multilevel Inheritance
#parent class and intermediary class both inherited into child class
'''
class Grandfather():
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername

#intermediary class
class Father(Grandfather):
    def __init__(self,fathername, grandfathername):
        self.fathername=fathername

        #invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)

#child class
class Daughter(Father):
    def __init__(self,daughtername, fathername, grandfathername):
        self.daughtername=daughtername

        #invoking constructor of father class
        Father.__init__(self, fathername, grandfathername)

    def printinfo(self):
        print("Grandfather's name : ",self.grandfathername)
        print("Father's name : ",self.fathername)
        print("Daughter's name : ", self.daughtername)

d1=Daughter('Vaishnavi','Arun','Duttatray')
#print(d1.grandfathername)
d1.printinfo()
'''

''''
#Hierarchical Inheritance
# There is one parent class and more than one child classes

#Parent class
class Parent:
    def func1(self):
        print("WE are in Parent class")

#child class
class Child1(Parent):
    def func2(self):
        print("We are in Child1 class")

class Child2(Parent):
    def func3(self):
        print("We are in Child2 Class")

# creating objects and function call
obj1 = Child1()
obj2 = Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()
'''
'''
#Hybrid Inheritance
#Where we used multiple types of inheritance

#Implement the hybrid inheritance

class School:                                         #parent class
    def func1(self):
        print("This function is in School class")

class Student1(School):                               #child class (school is the parent class)
    def func2(self):
        print("This function is in Student 1 class")

class Student2(School):                               #child class (school is the parent class)
    def func3(self):
        print("This function is in Student 2 class")

class Student3(Student1,School):                      #child class (student1 and school are parent clases)
    def func4(self):
        print("This function is is in student3 class")

obj = Student3()
obj.func1()
obj.func2()

'''

'''print("Hello World")      #Simple write the sytring in double or single quotes

# Output is Hello Ram
name = input("Enter your name = ")
age = int(input("Enter your age = "))

print("I am",name,"I am ",age,"years old")      # using variable name
'''



'''#using format function
name = input("Enter your name = ")
age = int(input("Enter your age = "))

#where you have to print the variable name write the curly braces there
# and put the variable_name in the format function as an arguments

print("I am {} and I am {} years old".format(name,age))'''


'''
#using short format
name = input("Enter your name = ")
age = int(input("Enter your age = "))

print(f"I am {name} and I am {age} years old")


'''
#end keyword to print the next statement on the same line
print("Hello", end=' ')
print("World", end=' ')
print("Python")










