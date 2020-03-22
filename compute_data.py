import pandas as pd
from sqlalchemy import create_engine
import json

#parse DBLoginInfo json file
with open("DBLoginInfo.json", "r") as DBLoginInfoFile:
    userInfo = json.load(DBLoginInfoFile)

#establish connection with database
engine = create_engine('mysql+mysqlconnector://' + userInfo['user'] + ':' + userInfo['passwd'] + '@' + userInfo['host'] + '/c19DB')

#Define stateData datatype
class stateData:
    def __init__(self, stateName = None, data = [], startDate = None, populationDensity = None, pop = None):
        self.stateName = stateName  #name of state
        self.data = data    #array of covid-19 cases in the state each day starting from first confirmed case
        self.startDate = startDate  #date of first confirmed case in the state
        self.populationDensity = populationDensity    #populatioin density of the state
    
    #return format
    def __repr__(self):
        return "%s, %s, %s, %s" % (self.stateName, self.startDate, self.populationDensity, self.data)

#import data from database
confirmedCasesData = pd.read_sql('SELECT * FROM confirmedCasesData', con=engine)
populationData = pd.read_sql('SELECT * FROM populationData', con=engine)

#getStateData formats the data from the database into an array of stateData objects
def getStateData():
    stateArray = [] #array of state objects

    #iterate through each state in the database
    for row,col in confirmedCasesData.iterrows():
        #create new stateData object called stateObj
        stateObj = stateData()

        #assign corresponding stateName to stateObj
        (a, b) = list(col.items())[0]
        stateObj.stateName = b

        #create array for stateData object's data
        stateObj.data = []

        #iterate through number of cases in the state (val) on each day (colidx). Record date of first case and add cases on proceeding days to stateObj data array
        for colidx,val in list(col.items())[2:]:
            if (stateObj.startDate != None):
                stateObj.data.append(val)
            elif (val > 0):
                stateObj.startDate = colidx
                stateObj.data.append(val)

        #get population and population density of the state
        rowidx = populationData.index[populationData['State'] == stateObj.stateName]
        stateObj.populationDensity = populationData.loc[rowidx.values[0],'Density']

        #add state to state array
        stateArray.append(stateObj)

    return stateArray