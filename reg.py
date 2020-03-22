import numpy as np
from scipy.optimize import curve_fit
from compute_data import getStateData

#func calculates a y value given x and the variables of an exponential function
def func(x, a, b, c):
    return a * np.exp(b * x) + c

#fitData develops the virus transmission model using data from the database and returns the variables for the exponential model equation
def fitData():
    day = []    #holds day index
    mean = []   #holds mean number of cases of all states on given day index
    statesOnDay = []    # holds number of states that have data on a given day index

    stateArray = getStateData() #populate stateArray with data from database

    #iterate through all states
    for state in stateArray:

        #eliminate New York. It is an outlier due to its severe lack in testing capability for the first two weeks.
        if (state.name != 'New York'):

            #iterate through days in state data
            for idx in range(len(state.data)):
                
                #if day isnt accounted for in mean array yet, add it to a new index in the array
                if (idx >= len(mean)):
                    mean.append(0)
                    statesOnDay.append(0)
                    day.append(idx)

                #sum confirmed cases (normalized by state population density) on day idx
                mean[idx] = mean[idx] + (state.data[idx]/state.popDensity)
                statesOnDay[idx] = statesOnDay[idx] + 1

    #calculate average confirmed cases on each day      
    for idx in range(len(mean)):
        mean[idx] = mean[idx] / statesOnDay[idx]

    #reformat day list
    day = np.array(day)

    #fit curve
    popt, pcov = curve_fit(func, day, mean)

    return popt