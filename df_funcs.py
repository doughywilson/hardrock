"""
author: Peter Hillyard
email: peterhillyard@gmail.com
"""


import pandas as pd
import scipy as sp

# This function changes the start, finish, in and out 
# string times (xx:xx:xx) to datetime objects. This
# function assumes that the string 'Start Offset' is
# the first column where the string times begin and that
# there are no other data types after that.
#
# Input:
#    df - pandas dataframe
#
# Output:
#    no output since df is an object that is changed in
#    the function
def change_in_out_to_timedelta(df,):
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
        df[datetime_str] = pd.to_timedelta(df[datetime_str], errors='coerce', unit='h') / sp.timedelta64(1, 'h')


