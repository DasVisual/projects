#! python3

'''Script scrapes CNN news article for title and author, etc 
	and saves in CSV file
	Created April 24, 2018
'''

from bs4 import BeautifulSoup
import csv
import urllib.request
from datetime import datetime

# URL
article_page = ['https://www.cnn.com/2018/04/24/us/toronto-suspect-what-we-know/index.html', 
'https://www.cnn.com/2018/04/23/politics/ronny-jackson-veterans-affairs-nomination/index.html']

data = []

# for loop
for pg in article_page:
	# query to page
	page = urllib.request.urlopen(pg)
	
	# parse html
	soup = BeautifulSoup(page, 'html.parser')
	
	# take out div and get title
	title_box = soup.find('h1', attrs={'class':'pg-headline'})
	title = title_box.text.strip()
	print(title)
	
	# take out div get author 
	# make sure HTML code is pasted correctly
	author_box = soup.find('span', attrs={'class':'metadata__byline__author'})
	author = author_box.text.strip()
	print(author)
	
	# time and date
	time_box = soup.find('p', attrs={'class':'update-time'}) 
	time = time_box.text.strip()
	print(time)

	data.append((title, author, time))
try:
	with open('C:/Users/noona/Downloads/python/projects/aToBeCompleted/scrapeNewsArticles/index.csv', 'a') as csv_file:
		# Writes headers for csv
		writer = csv.writer(csv_file)
		writer.writerow(['Title', 'Author', 'Time'])
	
	with open('C:/Users/noona/Downloads/python/projects/aToBeCompleted/scrapeNewsArticles/index.csv', 'a') as csv_file:
		# Writes data from list/tuple into csv
		writer = csv.writer(csv_file) # This might be unnecessary already have
		for title, author, time in data:
			writer.writerow([title, author, time])
except IOError as e:
	print('Could not make csv' % e)
	
	# Tried solution from: https://stackoverflow.com/questions/38133759/how-to-get-text-from-span-tag-in-beautifulsoup 
	# did not work for now
		# # take out div and get author 
		# #author_box = soup.find('span', attrs={'class':'metadata_byline'})
		# #author = author_box.text.strip()
		# #print(author_box)
	# try: 
		# soup = BeautifulSoup("""<div class="metadata "><div class="metadata__info 
		# js-byline-images" data-bundle="byline"><p class="metadata__byline"><span 
		# class="metadata__byline__author">By Michelle Krupa, CNN</span>""", "xml")

		# print(soup.select_one("span[title*=By]").text)
	# except IOError as e:
		# print("Could not find author" % e)