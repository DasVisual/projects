#! python3

'''Take airport location data and plot it on a map'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
import bokeh as bk
from decimal import Decimal


# you can use input() to allow columns to be named whatever for general script!!
u_cols =['Airport','Latitude','Longitude']

df = pd.read_csv(
	'C:/Users/noona/Downloads/python/projects/aToBeCompleted/airportLocationMap/Locations.csv', 
	sep=',', names=u_cols)

# Look at data type and see if needs changes
describe = df.describe()
print(describe)

type = df.dtypes	
print('\n',type)

info = df.info()
print(info)

# dropped first column and labels-updated dataframe
df2 = df.drop(df.index[0])
print(df2[:10])



# Reset index to use 0
df3 = df2.reset_index(drop=True) 

'''
l = []
for df3 in range(0,1000):
	l.append(Decimal(i).quantize(Decimal('0.01')))
print(l[:10])
'''
# Putting columns into lists
lat_list = df3['Latitude'].tolist()
long_list = df3['Longitude'].tolist()
print('\n','Latitude',lat_list[:5])
print('\n','Longitude',long_list[:5], '\n')

# Here I tried to make lat and long integers to plot but they have too many decimal points
# pd.to_numeric(df3, downcast='signed')
# df3['Latitude'].astype('int')
# df3['Longitude'].astype('int')

print(df3[:10], sep='\t')


# Tried plotting
#df3.plot(x='Latitude', y='Longitude')
#plt.show()


# Plotting map data: https://bokeh.pydata.org/en/latest/docs/user_guide/geo.html

##output_file('C:/Users/noona/Downloads/python/projects/aToBeCompleted/airportLocationMap/gmap.html')

##map_options = GMapOptions(lat=70.01, lng=-143.72, map_type='roadmap', zoom=5)


'''Moved away from using Google Maps API, now trying to use geopandas

NEXT STEP: Properly install geopandas and navigate docs to map lat and long
	
'''






