import mysql.connector

db= mysql.connector.connect(host='localhost',user='root',password='Test@123')

cursor=db.cursor()  # when we write any command or do some changes for that we have to write this cursor()

#command = "create database HopeGirlss"
command = "create database CollegeData"

cursor.execute(command)
#to execute the queries or statements

db.close()

