import mysql.connector

#establish connection with database
c19 = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "abcd1234"
)

#create new database c19DB
cursor = c19.cursor()

#Create Database
cursor.execute("CREATE DATABASE c19DB")