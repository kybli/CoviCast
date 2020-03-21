import numpy as np
from scipy.optimize import curve_fit
from compute_data import getStateData

def func(x, a, b, c):
    return a * np.exp(b * x) + c

def fitData():
    day = []
    mean = []
    statesOnDay = []

    stateArray = getStateData()

    for state in stateArray:
        if (state.name != 'New York'):
            for idx in range(len(state.data)):
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