import pandas as pd
from sqlalchemy import create_engine

#establish connection with database
engine = create_engine('mysql+mysqlconnector://root:abcd1234@localhost/c19DB')



#stateData datatype
class stateData:
    def __init__(self, name = None, data = [], startDate = None, popDensity = None, pop = None):
        self.name = name
        self.data = data
        self.startDate = startDate
        self.popDensity = popDensity
        self.pop = pop
    
    def __repr__(self):
        return "%s, %s, %s, %s, %s" % (self.name, self.startDate, self.popDensity, self.pop, self.data)

#import data
confData = pd.read_sql('SELECT * FROM confirmed', con=engine)
popData = pd.read_sql('SELECT * FROM populationData', con=engine)

def getStateData():
    #array of state objects
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
        stateObj.pop = popData.loc[rowidx.values[0],'Pop']
        stateArray.append(stateObj)

    return stateArray