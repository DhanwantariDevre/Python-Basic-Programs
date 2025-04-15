import mysql.connector # class is mysql.connector

db = mysql.connector.connect(host='localhost',user='root', password='Test@123')
#create an instance of mysql.connector to check the connectivity

print(db)



#This is the output(Successfully built the connection)
# <mysql.connector.connection_cext.CMySQLConnection object at 0x000002C324C663C0>

# We store all the data tables in database