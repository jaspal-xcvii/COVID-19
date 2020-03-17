#Libraries
import pandas as pd
from pandas import DataFrame

import matplotlib.pyplot as plt
import numpy as np
import os
import os.path
import shutil
import time

#Name of program
name = "Covid-19 analysis"

#define the start time of the program
start_time = time.time()

#Code to read in the csv files obtained from John Hopkins University 
current_directory = os.getcwd()
os.chdir("..") #change working directory to one up
#creates tuple of all the directories
one_directory_up = [os.path.join(current_directory,one_directory_up) for one_directory_up in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory,one_directory_up))] # Gets all directories in the folder as a tuple

#looks through the directories and finds the location of the folder/files
found = False
for directory in one_directory_up:
    if os.path.exists(directory + "/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"):
        file_confirmed = directory + "/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
        file_recovered = directory + "/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
        file_deaths = directory + "/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
        found = True

#If all three are found, print message
if found == True:
    print("All files have been found")
else:
    print("ERROR - files cannot be found")

#reads in the csv from found directory locations
covid_19_confirmed = pd.read_csv(file_confirmed)
covid_19_recovered = pd.read_csv(file_recovered)
covid_19_deaths = pd.read_csv(file_deaths)


#Make an array to hold all the headers. These should be the same in all 3 files, so just take 1.
columns = covid_19_confirmed.columns.tolist()

#Used to seperate country/region information from the data
location_columns = ['Province/State', 'Country/Region', 'Lat', 'Long']
location_long_lat_columns = ['Lat', 'Long']
location_name_columns = ['Country/Region', 'Province/State']

#Finds all the columnds with data
data_columns = [title for title in columns if title not in location_columns]

#Last day, one before last
last_day = columns[-1]
new_columns = location_name_columns + [last_day]

#covid_19_confirmed.info() #Gives information about each column. e.g name, number of entries and type
#covid_19_confirmed.sort_values(["Country/Region", "Province/State"], inplace=True)
#covid_19_confirmed.fillna("NA", inplace=True)


#removes provinces, leaves only countries behind
remove_provinces = covid_19_confirmed[pd.notna(covid_19_confirmed['Province/State'])].index #indexes provinces to remove
covid_19_confirmed.drop(remove_provinces , inplace=True)
covid_19_deaths.drop(remove_provinces , inplace=True)
covid_19_recovered.drop(remove_provinces , inplace=True)

covid_19_confirmed.drop(['Province/State','Lat','Long'], inplace=True, axis=1)
covid_19_deaths.drop(['Province/State','Lat','Long'], inplace=True, axis=1)
covid_19_recovered.drop(['Province/State','Lat','Long'], inplace=True, axis=1)
#df = DataFrame(covid_19_confirmed,columns=data_columns)
#df.plot(x ='Year', y='Unemployment_Rate', kind = 'line')

print(covid_19_confirmed)


print(name + " execution time --- %s seconds ---" % (time.time() - start_time)) #execution time