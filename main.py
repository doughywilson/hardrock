import pandas as pd
df = pd.read_csv('Hardrock 100 2017-elapsed-2017-08-15.csv')

for col in df:
    print col