import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password='Test@123',database='hopegirlss')

cursor=db.cursor()

command= "insert into Students (stud_ID, Name, Roll_No, Age, Department) values(%s,%s,%s,%s,%s)"

data=(1,"Vaishnavi",23,19,'CSE')  # to add the data in a table

cursor.execute(command,data)

db.commit()  # to commit(save) the changes

db.close()



