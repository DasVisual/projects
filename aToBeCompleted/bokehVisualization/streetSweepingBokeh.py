#! python3

'''Bokeh visualization of street_sweeping'''

import numpy as np
import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin

# df = pd.read_csv('C:/Users/noona/Downloads/python/projects/aToBeCompleted/street_sweeping/street-sweeping-schedules.csv')
# df.dropna(inplace=True)
# print(df[:10])


# # FIX: Tried to plot a hex scatter plot but didnt work
# x = df['Miles']
# y = df['MainID']

# bins = hexbin(x, y, 0.1)

# p = figure(tools="wheel_zoom,reset", match_aspect=True, background_fill_color='#440154')
# p.grid.visible = True

# p.hex_tile(q="q", r="r", size=0.1, line_color=None, source=bins,
           # fill_color=linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))

# output_file("C:/Users/noona/Downloads/python/projects/aToBeCompleted/bokehVisualization/hex_tile.html")

# show(p)

import pandas as pd
from bokeh.plotting import figure, output_file, show

# pandas
df = pd.read_csv('C:/Users/noona/Downloads/python/projects/aToBeCompleted/street_sweeping/street-sweeping-schedules.csv')
# read in name, x , y
# print df.x, df,y

# bokeh
plot =  figure()
plot.scatter(x=df['Miles'], y=df['MainID'])

output_file('C:/Users/noona/Downloads/python/projects/aToBeCompleted/bokehVisualization/test.html')
show(plot)