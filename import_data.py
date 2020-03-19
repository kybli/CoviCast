import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

#import data
filePath = "time_series_19-covid-Confirmed.csv"
data = pd.read_csv(filePath)

#init database
c19 = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "abcd1234",
    database = "c19DB"
)

cursor = c19.cursor()

#nested for loop. for each col, create col in sql. then for each row in the col, write data to col
engine = create_engine('mysql+mysqlconnector://root:abcd1234@localhost/c19DB')

data.to_sql(name = 'confirmed', con = engine, if_exists = 'replace', index = False)