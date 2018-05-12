import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import quandl

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2018, 2, 27)

# Retrieve stock data-uses own date format 
#quandl.ApiConfig.api_key = '46GypMeHJtrn8Dheqmmk' # commented to avoid re-running
#ef = quandl.get_table("WIKI/PRICES")

#print(ef.head())


# Makes csv file out of the stock data
#ef.to_csv('C:/Users/Admin/Desktop/non-essential/TSLA.csv')

db = pd.read_csv('C:/Users/Admin/Desktop/non-essential/TSLA.csv', parse_dates=True, index_col=2)
db[['high', 'low']].plot()
plt.show()

db['adj_close'].plot()
plt.show()

