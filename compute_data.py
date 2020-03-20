import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

#establish connection with database
engine = create_engine('mysql+mysqlconnector://root:abcd1234@localhost/c19DB')



#stateData datatype
class stateData:
    def __init__(self, name = None, data = [], startDate = None, popDensity = None):
        self.name = name
        self.data = data
        self.startDate = startDate
        self.popDensity = popDensity
    
    def __repr__(self):
        return "%s, %s, %s, %s" % (self.name, self.startDate, self.popDensity, self.data)

#import data
confData = pd.read_sql('SELECT * FROM confirmed', con=engine)
popData = pd.read_sql('SELECT * FROM populationData', con=engine)
'''
filePath1 = "time_series_19-covid-Confirmed.csv"
confData = pd.read_csv(filePath1)

filePath2 = "population_data.csv"
popData = pd.read_csv(filePath2)
'''
#start date array
stateArray = []

for row,col in confData.iterrows():
    stateObj = stateData()
    (a, b) = list(col.items())[0]
    stateObj.name = b
    stateObj.data = []

    for colidx,val in list(col.items())[2:]:
        if (val > 0 and stateObj.startDate == None):
            stateObj.startDate = colidx
            stateObj.data.append(val)
        elif (stateObj.startDate != None):
            stateObj.data.append(val)

    rowidx = popData.index[popData['State'] == stateObj.name]
    stateObj.popDensity = popData.loc[rowidx.values[0],'Density']
    stateArray.append(stateObj)

for x in stateArray:
    print(x)

#export data. Right now no changes are made so no need
confData.to_sql(name = 'confirmed', con = engine, if_exists = 'replace', index = False)