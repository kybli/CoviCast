from reg_v1 import fitData, func
from matplotlib import pyplot as plt

modelVars = fitData()

def predict(inputDay, popDensity):
    return func(inputDay, modelVars[0], modelVars[1], modelVars[2]) * popDensity

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

    plt.plot(days, predY, color='lightblue', linewidth=3)
    plt.plot([inputDay], predY[inputDay], color='darkblue', marker='o')
    plt.xlim(0, dayRange - 1)
    plt.title("Covid-19 Transmission Projection")
    plt.xlabel("Days Since First Case")
    plt.ylabel("Number of Confirmed Cases")
    
    
    label = "    Day: " + str(inputDay) + ", Cases: " + str(int(predY[inputDay]))
    
    plt.annotate(label, xy =(inputDay, predY[inputDay]) )
    
    plt.show()