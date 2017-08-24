"""
author: Peter Hillyard
email: peterhillyard@gmail.com
"""


import pandas as pd
import matplotlib as mpl
import scipy as sp
import datetime

# This function changes the start, finish, in and out 
# string times (xx:xx:xx) to datetime objects. This
# function assumes that the string 'Start Offset' is
# the first column where the string times begin and that
# there are no other data types after that.
def change_in_out_to_datetime(df,):
    # Get a list of all of the column names
    header_list = list(df.columns.values)

    # Find the index of 'Start Offset'
    time_start_idx = header_list.index('Start Offset')

    # Get all column namess at and after 'Start Offset'
    datetime_str_headers_list = header_list[time_start_idx:]

    # Loop through all datetime strings and make the column type
    # a datetime object
    for datetime_str in datetime_str_headers_list:
        # Some rows do not have entries. These entries will throw an error
        # so 'coerce' will put a NaT object in these entries
        print pd.to_datetime(df[datetime_str], errors='coerce')
        quit()







data = pd.read_csv('data/hardrock-elapsed-2017-08-15.csv')

# Get string times to datetimes
change_in_out_to_datetime(data)
print data["Ouray In"][:5]
quit()

datetime_str = 'Ouray In'# 'Start Offset'
data[datetime_str] = pd.to_datetime(data[datetime_str])
quit()

#Find runners that finished in the bottom half early in the race
data_early = data.sort_values("Maggie In")
print data_early


