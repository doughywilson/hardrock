"""Joey Wilson - messing around with hardrock 100 data to hopefully learn from it."""


import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import df_funcs as dff
import glob

filenames = glob.glob('data/2*')

for fn in filenames:

    data = pd.read_csv(fn)

    # Get all timestamps into timedeltas
    dff.change_in_out_to_timedelta(data)

    #Plot first half duration vs last half duration for each runner
    firstHalf = data["Engineer In"]
    secondHalf = data["Finish"] - firstHalf
    place = data["Overall rank"]


    plt.plot(firstHalf, secondHalf, '.')
    # for k in range(firstHalf.size):
    #     if firstHalf[k] < 100 and secondHalf[k] < 100:
    #         plt.text(firstHalf[k], secondHalf[k], place[k])

plt.axis([10, 30, 10, 30])
plt.plot([0,100],[0,100],":")
plt.xlabel('1st Half time (h)')
plt.ylabel('2nd Half time (h)')
plt.grid("on")
plt.show()

