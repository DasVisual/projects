import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import quandl
style.use('ggplot')

# Retrieve stock data-uses own date format 
#quandl.ApiConfig.api_key = '46GypMeHJtrn8Dheqmmk' # commented to avoid re-running
#ef = quandl.get_table("WIKI/PRICES")

#print(ef.head())


# Makes csv file out of the stock data
#ef.to_csv('C:/Users/Admin/Desktop/non-essential/TSLA.csv')

db = pd.read_csv('C:/Users/Admin/Desktop/non-essential/TSLA - Copy.csv', parse_dates=True, index_col=2)
db['100ma'] = db['adj_close'].rolling(window=100, min_periods=0).mean()
print(db.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(db.index, db['adj_close'])
ax1.plot(db.index, db['100ma'])
ax2.bar(db.index, db['volume'])


plt.show()
