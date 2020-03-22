import pandas as pd
from sqlalchemy import create_engine
import json

#parse DBLoginInfo json file
with open("DBLoginInfo.json", "r") as DBLoginInfoFile:
    userInfo = json.load(DBLoginInfoFile)

#import csv data
confirmedCasesFilePath = "time_series_19-covid-Confirmed.csv"
confirmedCasesData = pd.read_csv(confirmedCasesFilePath)

populationDataFilePath = "population_data.csv"
populationData = pd.read_csv(populationDataFilePath)


#create engine and use it to upload csv files to database
engine = create_engine('mysql+mysqlconnector://' + userInfo['user'] + ':' + userInfo['passwd'] + '@' + userInfo['host'] + '/c19DB')

confirmedCasesData.to_sql(name = 'confirmedCasesData', con = engine, if_exists = 'replace', index = False)
populationData.to_sql(name = 'populationData', con = engine, if_exists = 'replace', index = False)