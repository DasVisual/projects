import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
style.use('ggplot')


db = pd.read_csv('C:/Users/Admin/Desktop/non-essential/TSLA.csv', parse_dates=True, index_col=2)

db_ohlc = db['adj_close'].resample('10D').ohlc()
db_volume = db['volume'].resample('10D').sum()

db_ohlc = db_ohlc.reset_index()
db_ohlc['date'] = db_ohlc['date'].map(mdates.date2num)

fig = plt.figure()
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, db_ohlc.values, width=2, colorup='g')
ax2.fill_between(db_volume.index.map(mdates.date2num),db_volume.values,0)

print(db_ohlc.head())

plt.show()
