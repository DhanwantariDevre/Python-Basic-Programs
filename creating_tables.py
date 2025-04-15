import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password='Test@123', database= 'hopegirlss')

cursor=db.cursor()

command = "create table Students2 (Stud_ID INT, Name VARCHAR(20), Roll_No INT, Age INT, Department VARCHAR(20))"

cursor.execute(command)

db.close()