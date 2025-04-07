#set
'''
#It is a data structure
#Set can be defined in { } brackets

s1={10,20,30,50,90,70} #It will always change the sequence of the elements
print(s1)'''
'''
#clear()
s1.clear() # it will just simply clear the set
print(s1) # it will print the empty set but do not delete the set
'''

'''s1={10,20,30,50,20,90,30,70,20} #It will not print the duplicate elements
#s1.remove(20) # it will remove the element
print(s1)'''
'''
l1=[10,20,30,50,20,90,30,70,20] # list will print duplicate elements
print(l1)'''
'''
s1={10,20,30,50,20,90,30,70,20}
print("After removing the element")
s1.remove(20)
print(s1)

s1.add(100)
print(s1)'''

'''#copy() : Copy the set as it is in another set
s1={10,20,30,50,20,90,30,70,20}
s2= {101,103,149}
#s3=s1.copy()
s2=s1.copy()
print(s2)
# the elements which are already preset in s2(set2) are removed and it will only stores or copies all
#the values of s1(set1)'''
'''
#intersection() : it will print the common values from both sets
s1={10,20,30,50,20,90,30,70,20}
s2= {10,70,20}

print(s1.intersection(s2))

print(s1.issubset(s2)) # It will give an output in boolean values
print(s2.issubset(s1)) # s2 is a subset of s1

print(s2.issuperset(s1))
print(s1.issuperset(s2))
'''



'''#print(s1.issuperset(s2))

s3=s1.union(s2)
print(s3)

'''
'''s1={10,20,30,50,20,90,30,70,20}
s2= {101,345,754}

#update() : it will update the single set ( update will work like extend() of list
print(s1)
print(s2)
s1.update(s2)

print(s1)
print(s2)
'''


'''
#Dictionary methods

d1={'a':10,'b':20,'c':30,'d':40}
print(d1)

#keys() : to print all the keys of dictionary in list form
print(d1.keys())

#values() :it prints all the values of dictionary in list form
print(d1.values())

d1.clear()
print(d1)

d1={'a':10,'b':20,'c':30,'d':40}
d2=d1.copy()
print(d2)

#pop()
d1.pop('b') # the key we passed that value will be popped from the dictionary
print(d1)

item=d1.popitem()
print(item)
print(d1)

'''
'''#update()
d1={'a':10,'b':20,'c':30,'d':40}
d3={}
d3.update(d1)
print(d3)
print(d1)
'''

'''
def maximum(a, b, c) :
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = input("ENTER 1st NUMBER\n")
b = input("ENTER 2nd NUMBER\n")
c = input("ENTER 3rd NUMBER\n")
print(f"Maximum among three numbers {a},{b},{c} are {maximum(a, b, c)}")


'''
n=5
fact=1
for i in range (1,n+1):
    fact=fact*i

print(fact)











