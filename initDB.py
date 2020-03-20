import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

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

#import data
filePath1 = "time_series_19-covid-Confirmed.csv"
confData = pd.read_csv(filePath1)

filePath2 = "population_data.csv"
popData = pd.read_csv(filePath2)

engine = create_engine('mysql+mysqlconnector://root:abcd1234@localhost/c19DB')

confData.to_sql(name = 'confirmed', con = engine, if_exists = 'replace', index = False)
popData.to_sql(name = 'populationData', con = engine, if_exists = 'replace', index = False)