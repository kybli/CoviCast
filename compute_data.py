import pandas as pd
from sqlalchemy import create_engine

#establish connection with database
engine = create_engine('mysql+mysqlconnector://root:abcd1234@localhost/c19DB')



#Define stateData datatype
class stateData:
    def __init__(self, name = None, data = [], startDate = None, popDensity = None, pop = None):
        self.name = name
        self.data = data    # array of covid-19 cases in the state each day starting from first confirmed case
        self.startDate = startDate
        self.popDensity = popDensity
        self.pop = pop
    
    #return format
    def __repr__(self):
        return "%s, %s, %s, %s, %s" % (self.name, self.startDate, self.popDensity, self.pop, self.data)

#import data from database
confData = pd.read_sql('SELECT * FROM confirmed', con=engine)
popData = pd.read_sql('SELECT * FROM populationData', con=engine)

#getStateData formats the data from the database into an array of stateData objects which is returned to the caller
def getStateData():
    stateArray = [] #array of state objects

    #iterate through each state in the database
    for row,col in confData.iterrows():
        #create new stateData object called stateObj
        stateObj = stateData()

        #assign corresponding name to stateObj
        (a, b) = list(col.items())[0]
        stateObj.name = b

        #create array for stateData object's data
        stateObj.data = []

        #iterate through number of cases in the state (val) on each day (colidx). Record date of first case and add cases on proceeding days to stateObj data array
        for colidx,val in list(col.items())[2:]:
            if (val > 0 and stateObj.startDate == None):
                stateObj.startDate = colidx
                stateObj.data.append(val)
            elif (stateObj.startDate != None):
                stateObj.data.append(val)

        #get population and population density of the state
        rowidx = popData.index[popData['State'] == stateObj.name]
        stateObj.popDensity = popData.loc[rowidx.values[0],'Density']
        stateObj.pop = popData.loc[rowidx.values[0],'Pop']

        #add state to state array
        stateArray.append(stateObj)

    return stateArray