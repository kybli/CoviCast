from reg_v1 import fitData, func
from matplotlib import pyplot as plt

modelVars = fitData()

def predict(inputDay, popDensity):
    print(func(inputDay, modelVars[0], modelVars[1], modelVars[2]) * popDensity)

def plot(inputDay, popDensity):
    days = []
    predY = []

    dayRange = inputDay * 2
    if (dayRange < 20):
        dayRange = 20

    for day in range(dayRange):
        days.append(day)

    for day in days:
        predY.append(predict(day,popDensity))
        
    plt.plot(days, predY, 'r-')
    plt.plot([inputDay], predY[inputDay], 'bo')

    plt.show()