import pandas as pd
from sqlalchemy import create_engine

#import csv data
filePath1 = "time_series_19-covid-Confirmed.csv"
confData = pd.read_csv(filePath1)

filePath2 = "population_data.csv"
popData = pd.read_csv(filePath2)


#create engine and use it to upload csv files to database
engine = create_engine('mysql+mysqlconnector://root:abcd1234@localhost/c19DB')

confData.to_sql(name = 'confirmed', con = engine, if_exists = 'replace', index = False)
popData.to_sql(name = 'populationData', con = engine, if_exists = 'replace', index = False)