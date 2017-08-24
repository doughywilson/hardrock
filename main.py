"""Joey Wilson - messing around with hardrock 100 data to hopefully learn from it."""


import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

data = pd.read_csv('data/2017.csv')

#Plot first half duration vs last half duration for each runner

firstHalf = pd.to_timedelta(data["Engineer In"]) / sp.timedelta64(1,'h')
secondHalf = pd.to_timedelta(data["Finish"]) / sp.timedelta64(1,'h') - firstHalf
place = data["Overall rank"]


plt.plot(firstHalf, secondHalf, '.')
for k in range(firstHalf.size):
    if firstHalf[k] < 100 and secondHalf[k] < 100:
        plt.text(firstHalf[k], secondHalf[k], place[k])
plt.axis([10, 30, 10, 30])
plt.plot([0,100],[0,100],":")
plt.show()

