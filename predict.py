from reg import fitData, func
from matplotlib import pyplot as plt

#save variables for virus model to modelVars
modelVars = fitData()

#predict function returns a predicted number of covid-19 cases for a population density of 'popDensity' on day 'inputDay'
#inputs: inputDay, popDensity
def predict(inputDay, popDensity):
    return func(inputDay, modelVars[0], modelVars[1], modelVars[2]) * popDensity

#plots projected covid-19 transmission over time. Output plot is saved as output.pdf
#inputs: inputDay, popDensity
def plot(inputDay, popDensity):
    days = []   #day index
    predY = []  #predicted number of covid-19 cases on each day represented by index

    #create a domain for the graph that spans double the input Day and atleast 20 days
    dayRange = inputDay * 2
    if (dayRange < 20):
        dayRange = 20

    #populate day array
    for day in range(dayRange):
        days.append(day)

    #populate predY array with predicted values
    for day in days:
        predY.append(predict(day,popDensity))

    #plot configuration
    plt.plot(days, predY, color='lightblue', linewidth=3)
    plt.plot([inputDay], predY[inputDay], color='darkblue', marker='o')
    plt.xlim(0, dayRange - 1)
    plt.title("Covid-19 Transmission Projection for Population Density of " + str(popDensity) + " people/sqmi")
    plt.xlabel("Days Since First Case")
    plt.ylabel("Number of Confirmed Cases")
    
    #label the data point representing the day specified by the user
    label = "    Day: " + str(inputDay) + ", Cases: " + str(int(predY[inputDay]))
    plt.annotate(label, xy =(inputDay, predY[inputDay]) )
    
    #export output
    plt.savefig('output.pdf')