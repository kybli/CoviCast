from reg import fitData, exponential
from matplotlib import pyplot as plt
from datetime import date, datetime, timedelta
import matplotlib.ticker as ticker

#save parameters for virus model to modelVars
modelVars = fitData()

#predict function returns a predicted number of covid-19 cases for a population density of 'popDensity' on day 'inputDay'
#inputs: inputDay, popDensity
def predict(inputDay, popDensity):
    return exponential(inputDay, modelVars[0], modelVars[1], modelVars[2]) * popDensity

#plots projected covid-19 transmission over time. Output plot is saved as output.pdf
#inputs: inputDay, popDensity
def plot(inputDay, popDensity, startDateObj, targetDateObj):
    days = []   #day index
    predY = []  #predicted number of covid-19 cases on each day represented by index

    #create a domain for the graph that spans double the input Day and atleast 20 days
    dayRangeEnd = inputDay + 11
    dayRangeStart = inputDay - 10
    if (inputDay < 10):
        dayRangeEnd = 20
        dayRangeStart = 0

    
    for day in range(dayRangeStart,dayRangeEnd):
        #populate day array
        days.append((startDateObj + timedelta(days = day)).strftime("%m/%d/%Y"))
        
        #populate predY array with predicted values
        predY.append(predict(day,popDensity))

    #plot configuration
    plt.plot(days, predY, color='lightblue', linewidth=3)
    plt.xlim(0, dayRangeEnd - dayRangeStart - 1)
    plt.title("Covid-19 Transmission Projection\nfor Population Density of " + str(popDensity) + " people/square mile")
    plt.xlabel("Dates")
    plt.ylabel("Number of Confirmed Cases")
    plt.xticks(rotation=90)
    # Pad margins so that markers don't get clipped by the axes
    plt.margins(0.2)
    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom=0.25)
    
    #label the data point representing the day specified by the user
    if (inputDay < 10):
        plt.plot([inputDay], predY[inputDay], color='darkblue', marker='o')
        caseOutput = predY[inputDay]
        dayLabelX = inputDay

    else:
        plt.plot([10], predY[10], color='darkblue', marker='o')
        caseOutput = predY[10]
        dayLabelX = 10

    label = "    Day: " + targetDateObj.strftime("%m/%d/%Y") + ", Cases: " + str(int(caseOutput))
    plt.annotate(label, xy =(dayLabelX, caseOutput) )

    #export output
    plt.savefig('output.pdf')