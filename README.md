# CoviCast
By: Kyle Li

-----

### Project Goal
Recently, the novel coronavirus strain covid-19 has rapidly spread around the world, overwhelming the governments and helthcare systems of countries on every continent. The goal of C19 is to help prepare hospitals and governments by providing them with a projection of how many people will be infected in the state/province in the coming days. Using this information, hospitals and authorities can allocate funds and make public safety desicions accordingly.

### Model Description
The predictive analysis model used by the program is trained on the timeseries data of confirmed covid-19 cases and population densities of the states in the US. The training data is computed by first normalizing each state's daily count of confirmed covid-19 cases by their population density. The normalized number of confirmed cases in each state per day are then averaged and used to train a statistically significant model for predicting the growth of confirmed covid-19 cases over time.

*As of right now, the data of confirmed covid-19 cases in the US that used to train this model is becoming more complete each day as the US increases its covid-19 testing capacity. Over time, as the US tests more people and finds more covid-19 cases that were previously unconfirmed, the model will become increasingly accurate.*

### Usage
**Reminder: This project was designed to map the transmission of covid-19 in a specific area such as a state or province.**
*Anaconda and MySQL Connector are required to run this project. Project can either be downloaded directly from Github page or the project repository can be clonned into a local directory*

**Inputs:**
- Date of first confirmed covid-19 case in the area
- Target date that user wants to predict covid-19 cases for
- Area's population density (per square mile).

**Output:**
- Approximate number of covid-19 cases on user inputted target date.
- Graph depicting the growth of covid-19 cases in the area over time.
- The point along the projection representing the day specified by user input and the predicted number of confirmed cases on that day.
 
&nbsp;

After downloading the repository, you will notice that there are several files.
- **initDB.py** initializes a local SQL database called c19DB.
- **populateDB.py** converts the csv data for confirmed covid-19 cases in each state and the csv for population density of each state into two tables within the c19DB database. These tables are titled 'confirmed' and 'populationData' respectively.
- **compute_data.py** processes the data from the database into a format that **reg.py** can use to compute a model for the virus transmission.
- **predict.py** contains functions required to make predictions using the model
- **runPredict.py** uses those functions to allow the user to create a projection with the model.

&nbsp;
##### Instructions:
1. Open the file **DBLoginInfo.json**. It should look like the code below. Change the host, user, and password used for establishing a connection with the server so that they match your local server's host, user, and password. If you don't know your host or user, they are usually 'localhost' and 'root' respectively when you first download mysql. After making changes, save the file.

        {
        "host": "input your host here",
        "user": "input your user here",
        "passwd": "input your password here"
        }

2. *In your terminal, first navigate to the project directory.* Then run initDB.py by executing:

        python initDB.py

3. *In your terminal,* run populateDB.py by executing:

        python populateDB.py

4. Lastly, *in your terminal* start the main program by executing:

        python runPredict.py

5. Follow the instructions provided by the program in your terminal to compute your output

6. The output will then be saved as a separate file called **output.pdf** in the same directory as the project in your file system.

    *Further down in this file, there is a 'Testing' section where you can find population density and covid-19 data for the state of Texas to test the project against*

&nbsp;
#### Testing
Usage: Provided below is the population density of Texas and its recorded number of covid-19 cases per day the first case was detected there. Change the population density in the test file (or the last section of the notebook if you are using option 2) to Texas' population density provided below. Then run the test program several times, incrementing the day variable and comparing the predicted output with the actual data on each day in Texas provided below.


**Texas population density:**

Population Density = **112.8204**


**Actual Texas covid-19 data**
| Date  |  # of cases (Compare with output) |
|----------------------------|----------------------------------|
|           3/10/19 (Start Date)          |                13                |
|           3/11/19          |                21                |
|           3/12/19          |                27                |
|           3/13/19          |                43                |
|           3/14/19          |                57                |
|           3/15/19          |                72                |
|           3/16/19          |                85                |
|           3/17/19          |                110               |
### Sources
The model built for this project uses data provided by Johns Hopkins' Center for Systems Science and Engineering and the World Population Review.

**Links:**
- JHU Center for Systems Science and Engineering: https://github.com/CSSEGISandData/COVID-19
- World Population Review: https://worldpopulationreview.com/states/state-densities/
