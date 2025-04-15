import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password='Test@123',database='Hopegirlss')

cursor=db.cursor()

command='insert into students(stud_ID, Name, Roll_No, Age, Department) values(%s,%s,%s,%s,%s)'

data=[(2,'Ragini',45,21,'BSC'),(3,'Sakshi',41,20,'CSE'),(4,'Aboli',31,20,'BCA'),(5,'Payal',21,20,'ECE')]

#when we have to add one entry we are using execute
#and when we have to insert multiple values that time we have to use executemany()
cursor.executemany(command,data)
db.commit()
db.close()