#! python3

'''Scrape html websites stocks and visualize'''

import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

# specify url
quote_page = ['https://www.bloomberg.com/quote/SPX:IND',
'https://www.bloomberg.com/quote/CCMP:IND']

# for loop
data = []
for pg in quote_page:
	# query website and return html to variable 'page'
	page = urllib.request.urlopen(pg)

	# parse html using BS and store in variable soup
	soup = BeautifulSoup(page, 'html.parser')

	# Take out <div> from name and get its values
	name_box = soup.find('h1', attrs={'class': 'name'})
	name = name_box.text.strip()
	print(name)
	
	# get index price
	price_box = soup.find('div', attrs={'class': 'price'})
	price = price_box.text
	print(price)

	data.append((name,price))
	
# open csv and checks for error
try:
	with open('C:/Users/noona/Downloads/python/projects/aToBeCompleted/scraperStocks/index.csv', 'a') as csv_file:
		writer = csv.writer(csv_file)
		for name, price in data:
			writer.writerow([name, price, datetime.now()])
except IOError as e:
	print('Could not make csv' % e)

df = pd.read_csv('C:/Users/noona/Downloads/python/projects/aToBeCompleted/scraperStocks/index.csv')
print(df)