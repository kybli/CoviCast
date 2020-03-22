import numpy as np
from scipy.optimize import curve_fit
from compute_data import getStateData

#exponential takes an x value and three parameters of an exponential function and returns a corresponding y value
def exponential(x, a, b, c):
    return a * np.exp(b * x) + c

#fitData develops the virus transmission model using data from the database and returns the exponential model parameters in an array
def fitData():
    days = []    #holds day index
    means = []   #holds mean number of cases of all states on given day index
    statesOnDay = []    # holds number of states that have data on a given day index

    stateArray = getStateData() #populate stateArray with data from database

    #iterate through all states
    for state in stateArray:

        #eliminate New York. It is an outlier due to its severe lack in testing capacity during the first two weeks.
        if (state.stateName != 'New York'):

            #iterate through days in state data
            for idx in range(len(state.data)):
                
                #if day isnt accounted for in mean array yet, add it to a new index in the array
                if (idx >= len(means)):
                    means.append(0)
                    statesOnDay.append(0)
                    days.append(idx)

                #sum confirmed cases (normalized by state population density) on day idx
                means[idx] = means[idx] + (state.data[idx]/state.populationDensity)
                statesOnDay[idx] = statesOnDay[idx] + 1

    #calculate average confirmed cases on each day      
    for idx in range(len(means)):
        means[idx] = means[idx] / statesOnDay[idx]

    #reformat days list
    days = np.array(days)

    #fit curve
    popt, pcov = curve_fit(exponential, days, means)

    return popt