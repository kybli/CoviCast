import mysql.connector
import json

#parse DBLoginInfo json file
with open("DBLoginInfo.json", "r") as DBLoginInfoFile:
    userInfo = json.load(DBLoginInfoFile)

#establish connection with database
c19DBConnector = mysql.connector.connect(
    host = userInfo['host'],
    user = userInfo['user'],
    passwd = userInfo['passwd']
)

#create cursor
cursor = c19DBConnector.cursor()

#Create Database
cursor.execute("CREATE DATABASE c19DB")