#! python3

import pandas as pd
import matplotlib.pyplot as plt

# columns of interest: Side, Miles, Day of week
# df = pd.read_csv('C:/Users/noona/Downloads/python/projects/aToBeCompleted/street_sweeping/street-sweeping-schedules.csv')

# data_columns = ['Side', 'Miles', 'oneway']

# df.dropna(inplace=True)
# df.set_index('Miles', inplace=True)

# dlf = df.sort_values(by='Miles', ascending=False)

# print(df.head())

# print(dlf.head())

#pd.set_option('display.mpl_style', 'default')
#figsize(15,5)

df = pd.read_csv('C:/Users/noona/Downloads/python/projects/aToBeCompleted/street_sweeping/street-sweeping-schedules.csv')
df.dropna(inplace=True)
#df.set_index('Miles', inplace=True)
df.sort_values(by='Miles', ascending=False)
print(df)

# Line plot of first 50 entries
df[:50].plot()
plt.show()

# Scatter of Miles vs MainID
df[:50].plot.scatter(x='Miles', y='MainID')
plt.show()

# Hexagonal scatter of Miles vs MainID
df[:50].plot.hexbin(x='Miles', y='MainID', gridsize=25)
plt.show()

df[:550].plot.scatter(x='Miles', y='MainID')
plt.show()

df[:550].plot.hexbin(x='Miles', y='MainID', gridsize=25)
plt.show()


# Box plot 
df.plot.box()
plt.show()

# TODO: Add labels and titles to the plots

# TODO: Find other variables of interest to plot and plot them in different ways

