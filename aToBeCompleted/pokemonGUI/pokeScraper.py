#! python3

'''Scrape pokemon database and make GUI
	Created Apr 26, 2018
'''

import requests, six
import lxml.html as lh
from itertools import cycle, islice
from matplotlib import colors
import pandas as pd
import matplotlib.pyplot as plt
import csv
from pandas.plotting import scatter_matrix 

url='http://pokemondb.net/pokedex/all'

# Create handle, page, to handle contents of website
page = requests.get(url)

# Store contents of website under doc
doc = lh.fromstring(page.content)

# Parse data stored between <tr>...</tr> of site HTML code
tr_elements = doc.xpath('//tr')

# Create empty list
col = []
i=0

# For each row, store each first element (header) and empty list
for t in tr_elements[0]:
	i += 1
	name = t.text_content()
	print('%d:"%s"'%(i,name))
	col.append((name,[]))

	
# data stored on second row 
for j in range(1,len(tr_elements)):
	# T is j'th row
	T = tr_elements[j]
	
	# If row not size 10, //tr data not from our table
	if len(T) != 10:
		break
		
	# index of column
	i=0
	
	# Iterate through each element of row
	for t in T.iterchildren():
		data = t.text_content()
		# Check if row empty
		if i>0:
		# Convert numerical to integers
			try:
				data = int(data)
			except:
				pass
		# Append data to list of i'th column
		col[i][1].append(data)
		# Increment i for next column
		i+=1
		
[len(C) for (title,C) in col]

Dict = {title:column for (title, column) in col}
df = pd.DataFrame(Dict)

def str_bracket(word):
	'''Add brackets around second term'''
	list = [x for x in word]
	for char_ind in range(1, len(list)):
		if list[char_ind].isupper():
			list[char_ind] = ' ' + list[char_ind]
	fin_list = ''.join(list).split(' ')
	length = len(fin_list)
	if length > 1:
		fin_list.insert(1, '(')
		fin_list.append(')')
	return ' '.join(fin_list)
	
def str_break(word):
	'''Break strings at upper case'''
	list = [x for x in word]
	for char_ind in range(1, len(list)):
		if list[char_ind].isupper():
			list[char_ind] = ' ' + list[char_ind]
	fin_list = ''.join(list).split(' ')
	return fin_list
	
word = 'ILovePokemon'
print(str_bracket(word))
print(str_break(word))

df['Name']=df['Name'].apply(str_bracket)
df['Type']=df['Type'].apply(str_break)
df.head()
print(df)

df.to_json('C:/Users/noona/Downloads/python/projects/aToBeCompleted/pokemonGUI/PokemonData.json')

df = pd.read_json('C:/Users/noona/Downloads/python/projects/aToBeCompleted/pokemonGUI/PokemonData.json')
df = df.set_index(['#'])
df.head()

def max_stats(df, col_list):
	'''Get pokemon highest value column in dataframe'''
	message = ''
	for col in col_list:
		stat = df[col].max()
		name = df[df[col]==df[col].max()]['Name'].values[0]
		message += name +' has the greatest '+col+' of '+str(stat)+' .\n'
	return message

def min_stats(df, col_list):
	'''Get pokemon lowest value of column in dataframe'''
	message = ''
	for col in col_list:
		stat =df[col].min()
		name =df[df[col]==df[col].min()]['Name'].values[0]
		message += name+' has the worst '+col+' of '+str(stat)+'.\n'
	return message
	
stats = ['Attack', 'Defense', 'HP', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total']

print(max_stats(df, stats))

print(min_stats(df, stats))

# Total is last element so taken out from scatter matrix
scatter_matrix(df[stats[:-1]], alpha=0.2, figsize=(10,10), diagonal='kde')	
plt.show()
	
# new dataframe where type values separate from list
newDict = {}
stats_col = ['#', 'Name', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

# collecting list of type for each pokemon
Dict['Type']=df['Type'].values

# creating empty list for each key (column)
for col in stats_col:
	newDict[col]=[]
	newDict['Type']=[]
	
# populating each dictionary value (empty list) with data
for row in range(len(Dict['#'])):
	for t in Dict['Type'][row]:
		for col in stats_col:
			# append all columns except type to new dictionary
			newDict[col].append(Dict[col][row])
		# appending type separately for each pokemon in new dictionary
		newDict['Type'].append(t)

# convert dictionary to dataframe
new_df = pd.DataFrame(newDict)
new_df.head()
print(new_df[:10])

types = new_df['Type'].unique()
print(types)


# Colors to cycle through when plotting hbar graph
my_colors = list(six.iteritems(colors.cnames))
my_colors = list(islice(cycle(my_colors), None, len(new_df)))

def barh_stats():
	'''Plot hbar mean and std. dev of eadh attribute of pokemon type'''
	i=0
	plt.figure(figsize=(15,5))
	plt.suptitle('Statistics', fontsize=15)
	
	# cycle through each pokemon type
	for t in types:
	
		# iterate i value to change color to my_colors[i]
		i+=1
		
		# Plotting mean
		plt.subplot(121)
		plt.title('Mean')
		new_df[new_df['Type']==t].mean().plot(kind='barh', color=my_colors[i])
		
		# plotting std dev
		plt.subplot(122)
		plt.title('Standard Deviation')
		new_df[new_df['Type']==t].std().plot(kind='barh', color=my_colors[i])
	
	# add list of pokemon type to legend
	plt.legend(types, bbox_to_anchor=(1.3,1.1))

barh_stats()
plt.show()


	
	

	
	
# Check length first 12 rows
#[len(T) for T in tr_elements[:12]]
