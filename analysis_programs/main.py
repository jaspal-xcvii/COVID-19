#Libraries
import pandas as pd
import os
import os.path
import shutil


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


input_directory = "../csse_covid_19_data/csse_covid_19_time_series/"

covid_19_confirmed = pd.read_csv(file_confirmed)
covid_19_recovered = pd.read_csv(file_recovered)
covid_19_deaths = pd.read_csv(file_deaths)

columns = covid_19_confirmed.columns.tolist()
location_columns = ['Province/State', 'Country/Region', 'Lat', 'Long']
location_long_lat_columns = ['Lat', 'Long']
location_name_cols = ['Country/Region', 'Province/State']

data_cols = [c for c in columns if c not in location_columns]
last_day = columns[-1]
new_cols = location_name_cols + [last_day]

# time_series_covid_19_confirmed.info()
covid_19_confirmed.sort_values(["Country/Region", "Province/State"], inplace=True)
# time_series_covid_19_confirmed.fillna("NA", inplace=True)
covid_19_confirmed.head()