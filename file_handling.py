#To open the file or to create the file
#we are using the open(filename,permission)
#f = open("girls_data.txt","w")  #creating the file


#Properties of file object
'''
1. name : name of opened file
2. mode : mode in which the file is opened
3. closed : it returns the boolean value which indicates whether the file is closed or not
4. readable : it returns the boolean value indicates that file is readable or not
5. writable : it returns the boolean value indicates that file is writable or not
'''

'''f = open("girls_data.txt","w")
print("File Name : ",f.name)
print("File Mode : ",f.mode)
print("Is readable : ",f.readable())
print("Is writable : ",f.writable())
print("Is closed : ",f.closed)

f.close()  # to close the file

print("Is closed : ",f.closed)

f=open("girls_data.txt","r")
'''

'''
Modes of files 

r : Open the existing file for read operation. File pointer is positioned at the beginning. 
    If the file is not existed then you will got a FileNotFoundError is generated
    
w : Open the existing file for write operation. If the file is not existed then it will create the new file.

a : Open the existing file for append operation. If the file is already existed 
    then it will append otherwise it will create new file
    
r+ :to read and write the data into the file. The file pointer(current position of the cursor) 
    is placed at the beginning of the file
    
w+ : To write and read the data. It will override the existing data.

a+ : To append and read the data from the file. It won't override the data

x+ : To open the file in exclusive creating mode foe write operation. 
     If the file already existed then we will get FileExist Error
     
'''

## writing the data on the file
'''
There are two methods to write the data
1. write (str)
2. writelines(list of lines)
'''

#create the file object as f
'''
f=open("girls_data.txt","w")  #opening the file
f.write("Python Programming\n")  #write the data in the file
f.write("Hope Foundation\n")
f.write("Evening Batch\n")
print("Data written in the file successfully") #Printing stmt
f.close() #close the file
'''
# \n is used for the next line


#List of lines
'''f=open("girls_data.txt","w")
list1=["Java\n","C++\n","Python\n","Android\n"]
f.writelines(list1)
print("Data written in the file successfully")
f.close()
'''

#Reading the character data from the file
'''
1. read() : to read all the data
2. read(n) : To read the n characters from the file
3. readline() : To read the single line
4. readlines() : to read all the lines into the list

'''
'''
f=open("girls_data.txt","r")
line1=f.readline()
print(line1,end="")

line2=f.readline()
print(line2,end="")

f.close()
'''


#Alternative method

'''
f=open("girls_data.txt","r")
for line in f:
    print(line,end="")

f.close()


with statemnt
tell() method is used to return the current position of the cursor
seek() is used to move the cursor to specified position
'''
'''
data= "All the girls are good"
f=open("girls_data.txt","w")
f.write(data)

with open("girls_data.txt","r+") as f:
    text=f.read()
    print(text)
    print("The current position: ",f.tell())
    offset=len(text)-3
    f.seek(offset)
    print("The current position: ",f.tell())
    f.write("GEMS!!!!")
    f.seek(0)
    text=f.read()
    print("Data after modification : ")
    print(text)


'''
#os.path.isfile(filename)
#this command is used to get the information from the computer

#WAP to check whether the given file is exist or not. If it is available print the content

'''
import os,sys

fname=input("Enter the file name = ")
if not os.path.isfile(fname):
    print(f"{fname} does not exist")
    sys.exit(0)

f=open(fname,'r')
print("Contents of ",fname)
data=f.read()
print(data)
f.close()


'''
# Assignment
# WAP to print the number of lines, words and characters present in the given file
# Implement the use of these two methods : 1. read(n) 2. readlines()
'''
f= open("girls_data.txt","r")
lines=f.readlines()
for line in lines:
    print(line,end='')

'''
# WAP to print the number of lines, words and characters present in the given file
'''
import os,sys
fname = input("Enter the file name = ")
if not os.path.isfile(fname):
    print(f"{fname} does not exist")
    sys.exit(0)

f=open(fname,"r")
line_count=word_count=char_count=0

for line in f:
    line_count+=1
    char_count+=len(line)
    word_count+=len(line.split())

print("The Number of lines : ",line_count)
print("The Number of words : ",word_count)
print("The Number of Characters : ",char_count)

'''
#handling the binary data

#WAP to read image file and write to a new image file
f1=open("horse1.jpeg","rb")
f2=open("newhorse.jpg","wb")

bytes=f1.read()   # read the f1 and store in bytes
f2.write(bytes)   # writes that bytes in f2 file
f1.close()
f2.close()

#
#The data in the csv files is nothing but the excel data
# We have to know the names of the columns in the table'/file

import csv # importing csv module
# writer object and reader object

with (open("Sample_Superstore.csv","w",newline="") as f):
    w=csv.writer(f)
    w.writerow(["Category","City","Country","Customer Name"])
    while True:
        ecat=input("Enter The category = ")
        ecity=input("Enter the city = ")
        ecountry=input("ENter the country = ")
        ename=input("Enter the name = ")
        w.writerow([ecat,ecity,ecountry,ename])
        choice = input("Add Another (Y/N) ?")
        if choice == 'N':
            break

print("Data entered successfully in CSV file ")






































