"""Joey Wilson - messing around with hardrock 100 data to hopefully learn from it."""


import pandas as pd
import matplotlib as mpl
import scipy as sp

data = pd.read_csv('data/hardrock-elapsed-2017-08-15.csv')

#Find runners that finished in the bottom half early in the race
data_early = data.sort_values("Maggie In")
print data_early


