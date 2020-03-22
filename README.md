C19
======
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
- Area's population density (per square mile).
- The day that the user wants to predict the number of confirmed covid-19 cases in the area for. 
    -  **This input must be given in terms of days since first confirmed covid-19 case in the area.** *For example, if the user wants to make a prediction for March 11 and the first case was recorded on March 1, the user would input 10 as the number of days since the first case.*

**Output:**
- Graph depicting the growth of covid-19 cases in the area over time.
- The point along the projection representing the day specified by user input and the predicted number of confirmed cases on that day.
 
&nbsp;
##### Instructions:
There are two options for using this project. The first is to run it in your terminal and output the visual into a separate file. The second is to run it using Jupyter Notebook. **The second option is recommended because it is more easy to view the output.**

**Option 1:**
After downloading the repository, you will notice that there are several files. **initDB.py** initializes a local SQL database called c19DB. **populateDB.py** converts the csv data for confirmed covid-19 cases in each state and the csv for population density of each state into two tables within the c19DB database. These tables are titled 'confirmed' and 'populationData' respectively. **compute_data.py** processes the data from the database into a format that **reg.py** can use to compute a model for the virus transmission. **predict.py** contains functions required to make predictions using the model and **test.py** uses those functions to allow the user to create a projection with the model.

1. Open the file **init.py** and change the host, user, and password used for establishing a connection with the server so that they match your local server's host, user, and password. This information is located in the first few lines of the file that resemble the code below. After making changes, save the file.

        host = "localhost",
        user = "root",
        passwd = "abcd1234"

2. *In your terminal,* run init. py by executing:

        python init.py

3. *In your terminal,* run test.py by executing:

        python test.py

4. The output will then be saved as a separate file called **output.pdf** in the same directory as the project. This first output is the graph for a population density of 81 people per sq mi 32 days into the virus model 

**To change the input parameters for prediction (day and population density),** open the file test.py and locate the following lines:

    day = 32
    populationDensity = 81

Change the 32 on the line that starts with day to a different day that you wish to predict cases for. Change the 81 to a on the line that starts with populationDensity to a different population density that represents another area you wish to model covid-19 for. After making changes, save the file and follow steps 3 and 4 again to get output.

*Further down in this file, there is a 'Testing' section where you can find population density and covid-19 data for the state of Texas to test the project against*

**Option 2:**
1. After downloading the repository, open your Anaconda-Navigator application.
2. Launch the Jupyter Notebook application from within Anaconda. Next, navigate to the directory where you downloaded the project to and open **test.ipynb**.
3. You'll notice that there are 6 'sections of code' contained in 6 gray rectangles. The first line of each section is:

        #'name of file.py'
        
4. In the first section init.py, change the host, user, and password used for establishing a connection with the server so that they match your local server's host, user, and password. This information is located in the first few lines of the section that resemble the code below.

        host = "localhost",
        user = "root",
        passwd = "abcd1234"

5. After making changes, click the first section so that the section is highlighted (once highlighted there should be a colored bar on the left side of the section that appears). Then click the 'run' button at the top of the screen.
6. Repeat this for the each of the rest of the sections **in the order that they appear**. (make sure you click on each section before you click the run button to make sure that you're running the specific section of code that you intend to run)
7. When you run the last section, you'll notice that a graph appears. This is the output graph for the population density 81 on day 32.

**To change the input parameters for prediction (day and population density),** in the last section of case that starts with #test.py locate the following lines:

    day = 32
    populationDensity = 81

Change the 32 on the line that starts with day to a different day that you wish to predict cases for. Change the 81 to a on the line that starts with populationDensity to a different population density that represents another area you wish to model covid-19 for. After making changes, run the last section again to get your new output.

*Further down in this file, there is a 'Testing' section where you can find population density and covid-19 data for the state of Texas to test the project against*

&nbsp;
#### Testing
Usage: Provided below is the population density of Texas and its recorded number of covid-19 cases per day the first case was detected there. Change the population density in the test file (or the last section of the notebook if you are using option 2) to Texas' population density provided below. Then run the test program several times, incrementing the day variable and comparing the predicted output with the actual data on each day in Texas provided below.

**Texas population density**
population density = 112.8204

**Actual Texas covid-19 data**
| Date (Not used in program) | Day (input for program) | # of cases (Compare with output) |
|----------------------------|-------------------------|----------------------------------|
|           3/10/19          |            0            |                13                |
|           3/11/19          |            1            |                21                |
|           3/12/19          |            2            |                27                |
|           3/13/19          |            3            |                43                |
|           3/14/19          |            4            |                57                |
|           3/15/19          |            5            |                72                |
|           3/16/19          |            6            |                85                |
|           3/17/19          |            7            |                110               |
&nbsp;
### Sources
The model built for this project uses data provided by Johns Hopkins' Center for Systems Science and Engineering and the World Population Review.

**Links:**
- JHU Center for Systems Science and Engineering: https://github.com/CSSEGISandData/COVID-19
- World Population Review: https://worldpopulationreview.com/states/state-densities/