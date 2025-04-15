
#read the data from the sql
import mysql.connector
import pandas as pd
#pandas is  python library to perform operations on the data

db=mysql.connector.connect(host='localhost',user='root', password='Test@123', database='hopegirlss')
cursor=db.cursor()

command='select * from students'
cursor.execute(command)
output=cursor.fetchall()
df=pd.DataFrame(output)

df.to_csv('output1.csv')
print(df)
db.close()

#csv file means comma separated values

