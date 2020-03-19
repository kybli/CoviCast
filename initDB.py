import mysql.connector

c19 = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "abcd1234"
)

#create new database c19DB
cursor = c19.cursor()
cursor.execute("CREATE DATABASE c19DB")

#return all databases
cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)