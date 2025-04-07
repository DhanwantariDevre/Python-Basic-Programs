#List Methods

'''l1=[10,20,40,30.8,"Hello",True]
# It stores values of different data types
print(l1)

#append() : It appends the string at last of the list
l1.append("Pycharm")
print(l1)

#insert() It will insert the value in a list
l1.insert(4,"Python")
print(l1)

#remove() : It removes the value from the list
l1.remove(30.8)
print(l1)
'''

'''l1=[10,20,40,30.8,"Hello",True]
#copy() method
l2=l1.copy()
print(l2)
print(l1)
'''
'''#reverse() : it reverse the string but store it in itself
l1.reverse()
print(l1)

#pop() it will remove the elements from the last
l1.pop()
print(l1)
'''
'''#sort() : It will sort the list and it requires same data type values
l3=[34,56,23,68,13,78,90]
l3.sort()
print(l3)

l4=["Python","Hello","World"]
l4.sort()
print(l4)

l5=[True,False]
l5.sort()
print(l5)'''

'''
#extend() : it will extend the list with other list which we passed as a parameter
l3=[34,56,23,68,13,78,90]
l4=["Python","Hello","World"]

l3.extend(l4)
print(l3)
print(l4)

#count() : It will count the number of times the string occurs
#count is starts from 1 and indexing is stsrts from 0
c=l3.count(23)
print(c)'''

# set methods

'''
s1= {10,20,40,20,30,70,20} # it will not print the duplicate values
print(s1)
s1.remove(20) # it will remove all the occurrences of that element
print(s1)

print("Popped element = ",s1.pop())
print(s1)
s1.add(50)
print(s1)

s2={60,90}
print(s2)
s3=s1.copy()
print(s1)
print(s2)
print(s3)

s3=s1.intersection(s2)
print(s3)

print(s1.issubset(s2))

print(s2.issuperset(s1))

print(s1.pop())

s3=s1.union(s2) # union stores the union in third set
print(s3)

s1.update(s2) #stores the values in s1 means union in s1
print(s1)

'''
# Dictionary Methods

d1={'a':1,'b':2,'c':3,'d':4}
print(d1)

print(d1.keys()) #output  in strings
print(d1.values())
d1.clear() #not delete but clear the dictionary
print(d1)

d1={'a':1,'b':2,'c':3,'d':4}
d2=d1.copy()
print(d2)

element=d1.get('b') #get the values from the key
print(element)

d1.pop('b')
print(d1)

item=d1.popitem()
print(item)
print(d1)

d2={'h':12,'j':78,'k':45}
d1.update(d2)
print(d1)


'''
l1=[10,20,40,30,70,20] # it will print the duplicate values
print(l1)
l1.remove(20) #It will remove the first occurrence
print(l1)'''

























