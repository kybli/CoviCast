from predict import plot, predict
from datetime import date, datetime
from os import system, name, get_terminal_size

#clear terminal screen function
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   # for mac and linux(here, os.name is 'posix')
   else:
      _ = system('clear')

screen_clear()

#welcome page
print("\n\n" + "Welcome to the C19 Project".center(get_terminal_size().columns))
print("By: Kyle Li".center(get_terminal_size().columns))
print("\n\n\n" + "Recently, the novel coronavirus strain covid-19 has rapidly spread around the world, overwhelming the governments and helthcare systems of countries on every continent. The goal of C19 is to help prepare hospitals and governments by providing them with a projection of how many people will be infected in the state/province in the coming days. Using this information, hospitals and authorities can allocate funds and make public safety desicions accordingly.".center(get_terminal_size().columns - 20))

#get start and target date for area
while True:
    inputStartDate = input("\n\n\n\n\n\n\n\n\nEnter the date of the first confirmed covid-19 case in your area [in the format mm/dd/yy]: ")
    startDateObj = datetime.strptime(inputStartDate, '%m/%d/%y')

    inputTargetDate = input("Enter the target date for which you are predicting the number of covid-19 cases [in the format mm/dd/yy]: ")
    targetDateObj = datetime.strptime(inputTargetDate, '%m/%d/%y')

    datesDifference = targetDateObj - startDateObj

    if (datesDifference.days < 0):
        print("Your start date cannot occur after your target date. Please retry.\n\n")
    
    else:
        break

#get population density
while True:
    inputPopulationDensity = float(input("Enter the population density of your area (people/square mile): "))
    if (inputPopulationDensity < 0):
        print("You cannot have a negative population density. Please retry.\n\n")
    else:
        break

#create plot
plot(datesDifference.days, inputPopulationDensity, startDateObj, targetDateObj)

#return results
print("\n\n\n\n\n")
print("There will be approximately "  + str(int(predict(datesDifference.days, inputPopulationDensity))) + " covid-19 cases on " + targetDateObj.strftime("%m/%d/%Y"))
print("\nCovid-19 projection successfully saved as a pdf in your project directory")
