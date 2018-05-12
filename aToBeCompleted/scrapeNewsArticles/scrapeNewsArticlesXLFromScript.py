#! python3

'''Script scrapes CNN news articles--in HTML--for title and author, etc 
	and saves in EXCEL FILE---Gathers URLs from other script
	Created April 25, 2018
'''

'''TODO: Still working on properly gathering URLs from other script'''

from bs4 import BeautifulSoup
#import csv
import urllib.request
from datetime import datetime

import xlsxwriter
import re

 
article_page = ['https://www.cnn.com/2018/04/24/us/toronto-suspect-what-we-know/index.html', 
'https://www.cnn.com/2018/04/23/politics/ronny-jackson-veterans-affairs-nomination/index.html', 
'https://www.cnn.com/2018/04/24/us/toronto-suspect-what-we-know/index.html', 
'https://www.cnn.com/2018/04/23/politics/ronny-jackson-veterans-affairs-nomination/index.html', 
'https://www.cnn.com/2018/04/25/health/fda-nuplazid-safety-evaluation-invs/index.html', 
'https://www.cnn.com/2018/04/25/politics/supreme-court-travel-ban/index.html', 
'https://www.cnn.com/2018/04/24/opinions/venezuela-maduro-regime-needs-regional-solution-rubio-opinion/index.html', 
'https://www.cnn.com/2018/04/24/opinions/school-house-rock-opinion-seymour/index.html', 
'https://www.cnn.com/2018/04/24/opinions/trumps-worst-sin-against-ronny-jackson-lizza/index.html']

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
	
	# URL 
	#url_box = soup.find('a', href=True)
	#url_box = soup.find('meta', attrs={'itemprop': 'url'})
	#url_box = soup.find('meta', attrs={'property': 'vr:canonical'})
	# PArtial solution (I imported urllib.request vs answer given in only urllib):
	# ^^https://stackoverflow.com/questions/1752317/how-to-get-the-true-url-of-a-file-on-the-web-python
	url = urllib.request.urlopen(pg).geturl()
	#url = url_box.text.strip()
	print(url)
	
	data.append((title, author, time, url))

try: 
	workbook = xlsxwriter.Workbook('C:/Users/noona/Downloads/python/projects/aToBeCompleted/scrapeNewsArticles/indexXLFrom.xlsx')
	worksheet = workbook.add_worksheet()
	
	# support: http://xlsxwriter.readthedocs.io/tutorial03.html
	worksheet.set_column('A:A', 67)
	worksheet.set_column('B:B', 66)
	worksheet.set_column('C:C', 33)
	worksheet.set_column('D:D', 81)
	
	bold = workbook.add_format({'bold': True})
	
	worksheet.write('A1', 'Title', bold)
	worksheet.write('B1', 'Author', bold)
	worksheet.write('C1', 'Time Updated', bold)
	worksheet.write('D1', 'URL/Link', bold)
	
	row = 1
	col = 0
	
	for title, author, time, url in data:
		worksheet.write(row, col, title)
		worksheet.write(row, col + 1, author)
		worksheet.write(row, col + 2, time)
		worksheet.write(row, col + 3, url)
		row += 1
	workbook.close()
except IOError as e:
	print('Could not make Excel file' % e)
	
# # try:
	# # with open('C:/Users/noona/Downloads/python/projects/aToBeCompleted/scrapeNewsArticles/index.csv', 'a') as csv_file:
		# # # Writes headers for csv
		# # writer = csv.writer(csv_file)
		# # writer.writerow(['Title', 'Author', 'Time'])
	
	# # with open('C:/Users/noona/Downloads/python/projects/aToBeCompleted/scrapeNewsArticles/index.csv', 'a') as csv_file:
		# # # Writes data from list/tuple into csv
		# # writer = csv.writer(csv_file) # This might be unnecessary already have
		# # for title, author, time in data:
			# # writer.writerow([title, author, time])
# # except IOError as e:
	# # print('Could not make csv' % e)
	
	
	
	
	
	
	
	# # Tried solution from: https://stackoverflow.com/questions/38133759/how-to-get-text-from-span-tag-in-beautifulsoup 
	# # did not work for now
		# # # take out div and get author 
		# # #author_box = soup.find('span', attrs={'class':'metadata_byline'})
		# # #author = author_box.text.strip()
		# # #print(author_box)
	# # try: 
		# # soup = BeautifulSoup("""<div class="metadata "><div class="metadata__info 
		# # js-byline-images" data-bundle="byline"><p class="metadata__byline"><span 
		# # class="metadata__byline__author">By Michelle Krupa, CNN</span>""", "xml")

		# # print(soup.select_one("span[title*=By]").text)
	# # except IOError as e:
		# # print("Could not find author" % e)